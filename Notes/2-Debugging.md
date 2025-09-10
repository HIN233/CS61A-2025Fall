# Debugging

## Understanding the `Traceback Messages` & `Error Messages`

```python
File "<file name>", line <number>, in <function>
```

```python
<error type>: <error message>
```

## Debugging Techniques

### Running doctests

在`dockets`中有类似交互式calling的信息:

```python
def foo(x):
    """A random function.

    >>> foo(4)
    4
    >>> foo(5)
    5
    """
```

```bash
python3 -m doctest file.py
```

这实际上将您的文件加载到Python解释器中，并检查每个doctest输入（例如foo(4)）是否与指定的输出（例如4）相同。如果不同，将有一条消息告诉您哪些doctests失败了。

```bash
python3 -m doctest file.py -v
```

命令行工具有一个-v选项，代表详细模式。除了告诉您哪些doctests失败了，它还会告诉您哪些doctests通过了。

### Printing

建议：

- 不要只是打印出一个变量 —— 添加一些信息以便于你阅读：
```python
print(x)   # harder to interpret
print('DEBUG: x =', x)  # easier
```

- 使用print调用查看函数调用的结果（即在函数调用之后）。

- 在while循环的末尾使用`print`调用查看计数器变量在每次迭代后的状态：
```python
i = 0
while i < n:
    i += func(i)
    print('DEBUG: i is', i)
```

- 类似地，可以在例如 VsCode 和 PyCharm 的 Debug 模式下直接查看变量的值等信息。

### Interactive Debugging

一种很多程序员喜欢用来调查他们代码的方法是通过使用交互式Python：

```bash
python3 -i file.py
```

在执行file.py的内容后启动一个交互式Python会话。

## Error Types

- SyntaxError
- IndentationError
- TypeError
- NameError