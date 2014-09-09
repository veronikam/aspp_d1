# 'break' works on the innermost loop. If we want to break out
# of the outer loop, we often have to resort to flag variable.
# Rewrite the following example to use .close() to stop the
# outer loop.

from __future__ import print_function

def counter(n):
    i = 1
    while i <= n:
        yield i
        i += 1

def print_table():
    outer = counter(10)
    total, limit = 0, 100
    for i in outer:
        inner = counter(i)
        print(i, end=': ')
        for j in inner:
            print(i * j, end=' ')
            total += i * j
            if total >= limit: 
                outer.close()
                break
        print()
    print('total:', total)

if __name__ == '__main__':
    print_table()
