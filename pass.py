# pass by value 會產生一個分身
# pass by reference 直接使用本尊 (y 就是 x)
# pass by object reference (Python) (y 對應到 x 的 value) (pass by sharing)
# dynamic binding
# 有設質指令 (=)，會創造新物件 (pass by value)
# 使用 object attribute (pass by reference)

def f(y):
    y.append(1)

x= [0]
f(x)
print(x)    # pass by value => [0] or pass by reference => [0,1]


def ff(y):
    y += 1

x = 0
ff(x)
print(x)    # pass by value => 0 // pass by reference => 1