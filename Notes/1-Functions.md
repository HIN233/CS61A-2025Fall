# Python & Functions

## Environment

Frame: Holds name-value bindings; looks like a box; no repeated names allowed!
Global frame: The frame with built-in names (min, pow, etc.)
Environment: A sequence of frames that always **ends with** the global frame. An environment is **a sequence of frames.**
Lookup: Find the value for a name by looking in each frame of an environment
A name (which is a type of expression) such as x is evaluated by looking it up

## Designing Functions

### Docstring & 参数默认值

文档字符串的第一行应该包含函数的单行描述，接着是一个空行，下面可能是参数和函数意图的详细描述。此外，文档字符串可能包含调用该函数的交互式会话示例。

```python
 def complex(real=0.0, imag=0.0):
    """Form a complex number.

    Keyword arguments:
    real -- the real part (default 0.0)
    imag -- the imaginary part (default 0.0)
    """
    if imag == 0.0 and real == 0.0:
        return complex_zero
    ...
```

实践指南：缩进句体时，所有行必须以相同的方式缩进相同的量（使用空格，而不是制表符）。缩进的任何变化都会导致错误。

断言（Assertions）：程序员使用 assert 语句来验证是否符合预期，例如验证被测试函数的输出。assert 语句在布尔上下文中有一个表达式，后面是一个带引号的文本行（单引号或双引号都可以，但要保持一致），如果表达式的计算结果为假值，则显示该行。

```py
assert fib(8) == 13, '第八个斐波那契数应该是 13'
```

当被断言的表达式的计算结果为真值时，执行断言语句无效。而当它是假值时，assert 会导致错误，使程序停止执行，并输出后面的提示语句。

### Higher-Order Function

一种“可以接收其他函数作为参数”或“可以把函数当作返回值”的函数。这种可以操作函数的函数就叫做高阶函数（higher-order functions）。以下是一个例子：

```python
def make_fair_dice(sides):
    """Return a die that returns 1 to SIDES with equal chance."""
    assert type(sides) == int and sides >= 1, 'Illegal value for sides'
    def dice():
        return randint(1,sides)
    return dice
```

#### Curring

我们可以使用高阶函数把一个接受多个参数的函数转化成一个函数链，每个函数接受一个参数。更具体的说，给顶一个函数`f(x, y)`，我们可以定义一个高阶函数`g`使得`g(x)(y)`等价于`f(x, y)`。这种转化成为柯里化。

例如：
```python

>>> def curried_pow(x):
        def h(y):
            return pow(x, y)
        return h

>>> curried_pow(2)(3)
8
```

### Lambda 表达式

在python中可以使用lambda表达式创建临时函数，可以通过构造相应的英文句子来理解其结构。

```
lambda          x       :           f(g(x))
A function that takes x and returns f(g(x))
```

```python
>>> def compose(f, g)
        return lambda x:f(g(x))
```

### 函数装饰器

python提供了一种特殊的语法来使用高阶函数作为执行`def`语句的**一部分**，成为装饰器。举例`trace`：

```python
>>> def trace(f):
        def wrapped(x):
            print(f"-> {f} ({x})")
            return f(x)
        return wrapped

>>> @trace
    def triple(x):
        return 3 * x

>>> triple(12)
-> <function triple at 0x102a39848> (12)
36
```

在这里，`triple`的`def`语句有一个注解（annotation）`@trace`相当于：
```python
>>> def triple(x):
        return 3 * x
>>> triple = trace(triple)
```
