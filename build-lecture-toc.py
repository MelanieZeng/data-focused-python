import glob, os

if __name__ == "__main__":

    md = []
    md.append('# Lectures\n')
    
    for dir in next(os.walk('lectures'))[1]:
        if dir.lower().startswith('week'):
            md.append(f"* {dir}")
            path = os.path.join('lectures', dir)
            files = os.listdir(path)
            for file in [file for file in files if file.endswith('.md')]:
                print(path, file)
                md.append(f"  * [{file}]({os.path.join(dir,file)})")
    print('\n'.join(md))

    with open('lectures/lectures.md', 'w') as f:
        f.write('\n'.join(md))

        # for filename in filenames: 
        #     print(os.path.join(root, filename) )


        # if dir not in toc:
        #     toc[dir] = []

        # for file in files:
        #     if file.endswith('.ipynb'):
        #         # run nbconvert
        #         toc[dir].append({ file)

    
    
