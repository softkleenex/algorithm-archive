import os
import glob
import re
import unicodedata
import urllib.parse
import subprocess
import time

def force_icloud_download(filepath):
    try:
        # macOS specific command to force download from iCloud
        subprocess.run(['brctl', 'download', filepath], check=True, capture_output=True)
        time.sleep(0.5) # Give it a moment to download
        return True
    except Exception as e:
        print(f"Failed to force download: {e}")
        return False

def get_problem_info(filepath):
    # macOS 는 한글 파일명을 자모 분해형으로 돌려주고 git 은
    # core.precomposeunicode 로 NFC 로 저장한다. 정규화하지 않으면
    # 로컬에서 만든 링크와 CI(Linux 체크아웃)에서 만든 링크의
    # 퍼센트 인코딩이 달라져 README 가 매번 서로를 덮어쓴다.
    filepath = unicodedata.normalize("NFC", filepath)

    platform = "Unknown"
    pid = "-"
    title = os.path.basename(filepath).replace(".md", "")
    difficulty = "-"
    
    # Path example: problems/백준/Bronze/1000. A＋B/README.md
    parts = filepath.split('/')
    if "백준" in parts:
        platform = "Baekjoon"
        if len(parts) >= 5:
            difficulty = parts[2]
            folder_name = parts[3]
            # Replace unicode spaces with standard space for matching
            clean_name = folder_name.replace(' ', ' ').strip()
            match = re.match(r'^(\d+)\.\s*(.*)', clean_name)
            if match:
                pid = match.group(1)
                title = match.group(2)
            else:
                title = clean_name
    elif "atcoder" in parts:
        platform = "AtCoder"
        if len(parts) >= 4:
            pid = parts[2]
            title = parts[-1].replace(".md", "")
            if title == "README":
                title = parts[-2]
    
    # URL encode the filepath for valid markdown links in GitHub
    # We replace spaces with %20 so it's a valid relative path in GitHub markdown
    link = f"./{urllib.parse.quote(filepath)}"
    return {
        "platform": platform,
        "pid": pid,
        "title": title,
        "difficulty": difficulty,
        "link": link,
        "sort_key": int(pid) if pid.isdigit() else 999999
    }

def update_readme():
    files = glob.glob("problems/백준/**/*.md", recursive=True) + glob.glob("problems/atcoder/**/*.md", recursive=True)
    files = [f for f in files if not f.endswith("index.md")]
    
    problems = []
    for f in files:
        info = get_problem_info(f)
        problems.append(info)
        
    # Sort problems: Baekjoon first, then by Problem ID
    problems.sort(key=lambda x: (0 if x["platform"] == "Baekjoon" else 1, x["sort_key"], x["title"]))
    
    total_baekjoon = sum(1 for p in problems if p["platform"] == "Baekjoon")
    total_atcoder = sum(1 for p in problems if p["platform"] == "AtCoder")
    total = len(problems)
    
    stats_md = f"""<!-- problems:start -->
### 🏆 Algorithm Solving Status

**Total Solved: {total} Problems** (Baekjoon: {total_baekjoon}, AtCoder: {total_atcoder})

<details>
<summary>💡 <b>전체 풀이 문제 목록 (클릭하여 펼치기)</b></summary>
<br>

| 플랫폼 | 번호 | 문제 이름 | 난이도 | 풀이 링크 |
| :--- | :--- | :--- | :--- | :--- |
"""
    
    for p in problems:
        stats_md += f"| {p['platform']} | {p['pid']} | {p['title']} | {p['difficulty']} | [풀이 보기]({p['link']}) |\n"
        
    stats_md += "\n</details>\n<!-- problems:end -->"

    try:
        with open("README.md", "r", encoding="utf-8") as f:
            readme_content = f.read()
    except OSError as e:
        if e.errno == 11:
            print(f"README.md locked by iCloud, attempting to download and read with cat...")
            force_icloud_download("README.md")
            try:
                result = subprocess.run(['cat', "README.md"], check=True, capture_output=True, text=True)
                readme_content = result.stdout
            except Exception as e2:
                print(f"Warning: Could not read README.md even with cat: {e2}")
                return
        else:
            print(f"Warning: Could not read README.md due to error: {e}")
            return

    if "<!-- problems:start -->" in readme_content:
        new_content = re.sub(
            r"<!-- problems:start -->.*?<!-- problems:end -->",
            stats_md,
            readme_content,
            flags=re.DOTALL
        )
    else:
        new_content = readme_content + "\n\n" + stats_md

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_content)

def main():
    update_readme()
    print("Successfully updated README.md with detailed problem list.")

if __name__ == "__main__":
    main()
