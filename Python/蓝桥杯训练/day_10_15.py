"""a = int(input())
a = list(str(bin(a)[2:]))
num = 0
#print(a)
for i in range(len(a)+1):
    if a[i-1] == '1':
        num += 1
print(num)"""
"""
def fin(x):
    num = 0
    while x:
        num += x & 1
        #print(bin(x))
        x >>= 1
    return num

num = int(input())
a = fin(num)
print(a)


def fin(x):
    num = 0
    while x:
        num ^= x & 1
        #print(bin(x))
        x >>= 1
    return num

num = int(input())
a = fin(num)
print(a)
"""
"""
x &= x-1
x           = (00101100)
x-1         = (00101011)  
x & (x-1)   = (00101000)
...
x & (x-1)   = (00100000)
...
x & (x-1)   = (00000000)


x & ~(x-1)
"""

"""def fin(x):
    result = 0
    while x:
        result ^= 1
        x &= x-1    #擦去最小的一位
        #print(bin(x))
    return result

num = int(input())
a = fin(num)
print(a)"""


"""
#查表法
def fin(x):
    a = [0, 1, 1, 0]
    SIZE = 2
    BIT_MASK = 0x03 #用来屏蔽前面的元素
    print(bin(x))
    return (a[x >> (3*SIZE)]^
            a[(x >> (2*SIZE)) & BIT_MASK]^
            a[(x >> (1*SIZE)) & BIT_MASK]^
            a[x & BIT_MASK])

num = int(input())
a = fin(num)
print(a)

print(bin(num))

print(bin(0x03))
print(bin(num & 0x03))"""

#并行运算
"""

x           = (11010111)
>>4         = (00001101)
^=(x>>4)    = (11011010) 第一轮
>>2         = (00110110)
^=(x>>2)    = (00101100) 第二轮
>>1         = (00010110)
^=(x>>1)    = (00111010) 第三轮
x&(00000001)= (00000000)

"""

## 整数的逆序问题

"""def reverse(x):
    if x < 0:
        return -reverse(-x)

    y = 0
    while x:
        y *= 10         #原本数字*10
        y += x % 10     #加上现在x的个位数
        x //= 10        #将x向右移动一位

    return y

num = int(input())
a = reverse(num)
print(a)
"""
"""
def reverse(x):
    if x < 0:
        return -reverse(-x)

    y = 0
    while x:
        y <<= 1         #原本数字*10
        print(bin(y))
        y |= (x & 1)     #加上现在x的个位数
        print(bin(x))
        print(bin(x & 1))
        x >>= 1        #将x向右移动一位
        print(bin(x))

    return y

num = int(input())
a = reverse(num)
print(a)

a = [0,1,1,0]

def reverse(x):
    SIZE = 2
    BIT_MASK = 0x03
    return (a[x >> (3 * SIZE)] ^
            a[(x >> (2 * SIZE)) & BIT_MASK] ^
            a[(x >> (1 * SIZE)) & BIT_MASK] ^
            a[x & BIT_MASK])

print(reverse(10))
"""

A = [1,2,3,4,5,6,7,8,9,10]
"""
a = []
for i in range(len(A)):
    if i % 2 == 0:
        a = [i] + a
    else:
        a = a + [i]
"""
def fun(A):
    l = 0
    r = len(A) - 1
    while l < r:
        if A[l] % 2 == 0:
            l += 1
        else:
            A[l], A[r] = A[r], A[l]
            r -= 1
    return print(A)
print(fun(A))


print(

)
