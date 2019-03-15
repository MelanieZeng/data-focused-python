import glob, os
from pathlib import Path

if __name__ == "__main__":

    md = []
    md.append('# Lectures\n')
    lecture_root = "_pages/lectures"
    for week in [week for week in os.listdir(lecture_root) if week.lower().startswith('week')]:
        md.append(f"* {week}")
        week_path = os.path.join(lecture_root, week)
        files = os.listdir(week_path)
        for file in [file for file in files if file.endswith('.md')]:
            file_path = os.path.join(week_path, file)
            print(file_path)
            md.append(f"  * [{Path(file).resolve().stem.title()}]({file_path})")
    print('\n'.join(md))

    with open(os.path.join(lecture_root, 'lectures.md'), 'w') as f:
        f.write('\n'.join(md))    
