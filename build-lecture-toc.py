import glob, os

if __name__ == "__main__":
    os.chdir('lectures')
    
    with open('lectures.md', 'w') as f:
        f.write('# Lectures\n\n')
        for file in glob.glob("*.md"):
            if file == 'lectures.md':
                continue
            print(file)
            f.writelines(f'* [{file}]({file})\n')

