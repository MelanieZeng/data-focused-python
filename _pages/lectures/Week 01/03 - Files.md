---
toc: true
toc_sticky: true
toc_label: "Page Contents"
toc_icon: "cog"
---
# Files

Read and write files
open and close files


```python
f = open('file.txt')
```


    ---------------------------------------------------------------------------

    FileNotFoundError                         Traceback (most recent call last)

    <ipython-input-1-bbe9c83e51d2> in <module>()
    ----> 1 f = open('file.txt')
    

    FileNotFoundError: [Errno 2] No such file or directory: 'file.txt'


## creating a  file


```python
f = open('file.txt', 'w')
f.write('hello world')
f.close()
```

## using with


```python
with open('file.txt') as f:
    text = f.read()
    print(text)
```

    hello world

