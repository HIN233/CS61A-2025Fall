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

### HW02 - `make_repeater`

返回一个函数，该函数对输入值应用 `f` 共 `n` 次（即 `f` 的 `n` 次复合函数）。

```python
def make_repeater(f, n):
    """Returns the function that computes the nth application of f.

    >>> add_three = make_repeater(increment, 3)
    >>> add_three(5)
    8
    >>> make_repeater(triple, 5)(1) # 3 * (3 * (3 * (3 * (3 * 1))))
    243
    >>> make_repeater(square, 2)(5) # square(square(5))
    625
    >>> make_repeater(square, 3)(5) # square(square(square(5)))
    390625
    """
```

#### 代码实现
```python
def make_repeater(f, n):
    if n == 1:
        return f
    else:
        return lambda x: f(make_repeater(f, n-1)(x))
```

#### 替代实现（迭代版本）
```python
def make_repeater(f, n):
    def g(x):
        for i in range(n):
            x = f(x)
        return x
    return g
```

#### 核心原理

##### 1.作用域
在`make_repeater`内定义的函数`g` / `lambda x: f(make_repeater(f, n-1)(x))`是一个闭包，能够访问`make_repeater`的参数`f`和`n`。通过这种方式把`f`和`n`“记住”下来，从而去被`(5)`调用。

##### 2. 递归思想
- **基准情况**：`n=1` 时，直接返回 `f`
- **递归情况**：`n>1` 时，返回 `f` 与 `make_repeater(f, n-1)` 的组合

##### 3. Lambda函数的作用
```python
lambda x: f(make_repeater(f, n-1)(x))
```
- 创建一个匿名函数，接受参数 `x`
- 先递归计算内层 `make_repeater(f, n-1)(x)`
- 再将结果传递给外层函数 `f`

##### 执行顺序
**从内到外执行**，不是从右到左读取：
```
f( make_repeater(f, n-1)(x) )
    ↑    先执行(内部)      ↑
```

##### 执行过程示例（n=3）
```python
make_repeater(square, 3)(5)
= lambda x: square(make_repeater(square, 2)(x)) (5)
= square(make_repeater(square, 2)(5))

# 展开内层：
make_repeater(square, 2)(5)
= lambda x: square(make_repeater(square, 1)(x)) (5)
= square(make_repeater(square, 1)(5))
= square(square(5))  # 因为 make_repeater(square, 1) = square
= square(25)
= 625

# 代回外层：
= square(625)
= 390625
```

## 环境作用域要点
1. **闭包机制**：内部lambda函数通过闭包捕获外部函数的参数 `f` 和 `n`
2. **递归调用**：每次递归调用都会创建新的作用域，但都引用相同的 `f`
3. **参数传递**：外层的 `x` 被传递给内层的函数调用

## 注意事项
1. **递归深度**：递归版本在 `n` 很大时可能达到最大递归深度
2. **n=0的情况**：当前代码未处理 `n=0`（应返回恒等函数）
3. **性能考虑**：迭代版本通常更高效，避免递归开销
