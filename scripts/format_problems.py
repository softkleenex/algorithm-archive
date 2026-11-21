import os
import glob
import re
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

def get_language_from_ext(ext):
    ext_map = {
        ".py": "python",
        ".c": "c",
        ".cc": "cpp",
        ".cpp": "cpp",
        ".java": "java",
        ".js": "javascript",
        ".ts": "typescript",
        ".go": "go",
        ".rs": "rust",
        ".kt": "kotlin",
        ".swift": "swift",
    }
    return ext_map.get(ext.lower(), "")

def read_file_content(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except OSError as e:
        if e.errno == 11: # Resource deadlock avoided
            print(f"File locked by iCloud, attempting to read using cat: {filepath}")
            # Try to force download, but don't wait for it
            force_icloud_download(filepath)
            try:
                # Use cat to bypass the python open() restriction
                result = subprocess.run(['cat', filepath], check=True, capture_output=True, text=True)
                return result.stdout
            except Exception as e2:
                print(f"Warning: Could not read {filepath} even with cat: {e2}")
                return None
        else:
            print(f"Warning: Could not read {filepath} due to error: {e}")
            return None

def format_readme(readme_path):
    dir_path = os.path.dirname(readme_path)
    
    content = read_file_content(readme_path)
    if content is None:
        return False
        
    code_files = [f for f in os.listdir(dir_path) if f != "README.md" and not f.endswith(".md") and os.path.isfile(os.path.join(dir_path, f))]
    
    code_content = ""
    language = ""
    if code_files:
        code_file = code_files[0]
        ext = os.path.splitext(code_file)[1]
        language = get_language_from_ext(ext)
        
        try:
            with open(os.path.join(dir_path, code_file), 'r', encoding='utf-8') as cf:
                code_content = cf.read()
        except Exception:
            pass

    # Check if already formatted
    if "---" in content[:10] or "## 💡" in content:
        if code_content and "## 💻 코드" in content:
            parts = content.split("## 💻 코드")
            new_content = parts[0] + f"## 💻 코드\n\n```{language}\n{code_content}\n```\n"
            if content.strip() != new_content.strip():
                with open(readme_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                return True
        return False
        
    title_match = re.search(r'^#\s+\[(.*?)\]\s+(.*)', content, re.MULTILINE)
    difficulty = "Unrated"
    problem_title = "Unknown Problem"
    
    if title_match:
        difficulty = title_match.group(1).strip()
        problem_title = title_match.group(2).strip()

    platform = "백준" if "백준" in dir_path else "AtCoder" if "atcoder" in dir_path.lower() else "Algorithm"
    frontmatter = f"""---
title: "[{difficulty}] {problem_title}"
tags: ["{platform}", "{difficulty}"]
---

"""
    
    custom_sections = f"""

---

## 💡 해결 방법
<!-- 이 문제에 대한 접근 방식과 풀이를 작성하세요 -->

## 💻 코드

```{language}
{code_content}
```
"""
    
    new_content = frontmatter + content + custom_sections
    
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    return True

def create_md_for_standalone_code(code_path):
    dir_path = os.path.dirname(code_path)
    filename = os.path.basename(code_path)
    name, ext = os.path.splitext(filename)
    
    language = get_language_from_ext(ext)
    if not language:
        return False
        
    # If README.md exists, it's handled by format_readme
    if os.path.exists(os.path.join(dir_path, "README.md")):
        return False
        
    md_path = os.path.join(dir_path, f"{name}.md")
    
    code_content = read_file_content(code_path)
    if code_content is None:
        return False

    # If a markdown file with the same name already exists, update it
    if os.path.exists(md_path):
        content = read_file_content(md_path)
        if content is None:
            return False
            
        if "## 💻 코드" in content:
            parts = content.split("## 💻 코드")
            new_content = parts[0] + f"## 💻 코드\n\n```{language}\n{code_content}\n```\n"
            if content.strip() != new_content.strip():
                with open(md_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                return True
        return False

    platform = "백준" if "백준" in dir_path else "AtCoder" if "atcoder" in dir_path.lower() else "Algorithm"
    difficulty = "Unrated"

    # For AtCoder, extract contest ID from parent folder
    contest_info = ""
    if platform == "AtCoder":
        parent_dir = os.path.basename(dir_path)
        contest_id = ""
        if parent_dir.isdigit():
            contest_id = f"abc{parent_dir}" # Default to abc assumption for numeric folders
            difficulty = f"ABC{parent_dir}"
        elif parent_dir != "atcoder":
            contest_id = parent_dir.lower()
            difficulty = parent_dir
            
        if contest_id:
            # Try to guess task ID from the filename (e.g., 'a', 'A', 'B_Spiral_Galaxy')
            task_id = ""
            parts = name.split('_')
            if len(parts) > 1 and len(parts[0]) == 1:
                task_id = parts[0].lower()
            elif len(name) == 1:
                task_id = name.lower()
                
            if task_id:
                url = f"https://atcoder.jp/contests/{contest_id}/tasks/{contest_id}_{task_id}"
                contest_info = f"\n이 문제는 **{difficulty}** 콘테스트 문제입니다. \n\n🔗 [문제 바로가기]({url})\n"
            else:
                url = f"https://atcoder.jp/contests/{contest_id}/tasks"
                contest_info = f"\n이 문제는 **{difficulty}** 콘테스트 문제입니다. \n\n🔗 [콘테스트 문제 목록]({url})\n"

    content = f"""---
title: "[{platform}] {name}"
tags: ["{platform}", "{difficulty}"]
---

# {name}

이 문제는 {platform}에서 푼 문제입니다. {contest_info}

---

## 💡 해결 방법
<!-- 이 문제에 대한 접근 방식과 풀이를 작성하세요 -->

## 💻 코드

```{language}
{code_content}
```
"""
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    return True

def main():
    updated_count = 0
    
    # 1. Process README.md files
    readmes = glob.glob("problems/백준/**/README.md", recursive=True) + glob.glob("problems/atcoder/**/README.md", recursive=True)
    for readme in readmes:
        if format_readme(readme):
            updated_count += 1
            print(f"Formatted README: {readme}")
            
    # 2. Process standalone code files (like AtCoder files without README)
    code_files = []
    for ext in [".py", ".cc", ".cpp", ".java", ".c"]:
        code_files.extend(glob.glob(f"problems/백준/**/*{ext}", recursive=True))
        code_files.extend(glob.glob(f"problems/atcoder/**/*{ext}", recursive=True))
        
    for code_file in code_files:
        if create_md_for_standalone_code(code_file):
            updated_count += 1
            print(f"Created MD for code: {code_file}")
            
    print(f"Total {updated_count} files formatted/created.")

if __name__ == "__main__":
    main()
