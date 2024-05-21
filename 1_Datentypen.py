# Integer und ein bisschen binär

int_a=10
int_b=int_a
print(int_a, int_b)
int_a=11
print(int_a, int_b)
print(int_a & int_b)
int_a=1
int_b=2
print(bin(int_a) +'\n'+bin(int_b))
print(bin(int_a | int_b))
print(bin((int_a | int_b) <<2))

# Float und Runden

float_a=1043.791854
print(round(float_a, 3))

float_b=1.9999999999999999
float_b=1.9999777777777777
print(int(float_b))

from math import ceil
from math import floor

print(floor(float_b))
print(round(float_b,5))

# Listen
# Listen Methoden: append, extend, copy, count, index, insert, pop, remove, reverse, sort
# builtin: all()/any()

list_a=[1,2,3,4,5,6,7,8,9,10]
print(list_a[0:5])
print(list_a[0:int((len(list_a)/2))])
list_a.reverse()
print((list_a))
print((list_a[::-1]))
list_b=list_a
list_b=[20,19,18]
list_c=[17,16,15]
list_b.append(list_a)
print((list_b))
list_b.extend(list_c)
print((list_b))
list_c.sort(reverse=1)
print((list_c))
list_d=list_c.copy()
#list_d=list_c
print(list_d)
list_d[0]=100
print(id(list_c), id(list_d))
print(list_d.index(16))
list_e=[1,2,3,1,5,2,4,1,0]
print(list_e.count(1))
list_f=list_a+list_e
print(set(list_f))
#all/any


# String

str_a="Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam"
print(str_a.rfind("sit"))

print("dolor" in str_a)

# Dictionary

dict_a={"Red":"#ff0000", "Green":"#00ff00", "Blue":"#0000ff"}
print(dict_a.keys(),
      dict_a.values(),
      dict_a.items(),
      dict_a.get("Red"))









