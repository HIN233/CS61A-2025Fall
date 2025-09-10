# Icebreaker I: What have you been up to this summer?

# Icebreaker II: Why are you taking CS 61A? What do you hope to get out of it?

# Numeric expressions
2025
2000 + 25
2 * 5
2 ** 5
1 + 2 ** 3 + 4 * ((5 // 6) + 7 * 8 * 9)

# Functions
abs(-2)
max(1, 2, -3)
pow(2, 5)
pow(5, 2)

from operator import add, mul
add(2, 3)
mul(2, 3)
2 + 3
2 * 3
1 + 2 * 3
add(1, mul(2, 3))
mul(add(1, 2), 3)
mul(add(2, mul(4, 6)), add(3, 5))


# Values
"Go Bears"

# Objects
# Note: Download from http://composingprograms.com/shakespeare.txt
shakes = open('shakespeare.txt')
text = shakes.read().split()
len(text)
text[:25]
text.count('our')
text.count('thou')
text.count('you')
text.count('forsooth')
text.count('the')
text.count('.')
text.count(':')
text.count(',')
text.count(',') / len(text)

# Sets
words = set(text)
len(words)

# Combinations and Data 
{w for w in words if len(w) == 4}
'draw'
'draw'[0]
'draw'[::-1]

{w for w in words if len(w) == 4 and w == w[::-1]}
{w for w in words if len(w) == 5 and w == w[::-1]}
{w for w in words if len(w) == 4 and w[::-1] in words}
{w for w in words if len(w) == 5 and w[::-1] in words}
{w for w in words if len(w) == 6 and w[::-1] in words}
{w for w in words if len(w) > 6 and w[::-1] in words}

