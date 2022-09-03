# namespace 命名空間
# name

# Build-in Namespace e.g. print(), int()
# Module: Global Name Space 全域 (檔案層級的)
# Function: Local Namespace 區域 (function內的)

x = 5
def f():
    # enclosed namespace
    def ff():
        # local namespace
        x = 5

# LEGB
# L: local         e.g. x = 5, q = 1
# E: enclosed      e.g. x = 1
# G: global        e.g. y = 10, x = 5, f(), fff()
# B: build-in

y = 10
x = 5
def f():
    x = 1
    def ff():
        x = 5

def fff():
    q = 1