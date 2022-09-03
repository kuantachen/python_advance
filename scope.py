# scope 範圍
# LEGB rule
# 低層可以讀取不能寫入高層

# x = 1

def f():
    x = 1    # enclosed scope
    # global x
    def ff():
        nonlocal x    # 使用 enclosed 的 x
        x = 10  # local scope
    ff()
    print(x)

f()
# print(x)