# _
# _name
# name_
# __name
# __name__

# 功能跟 i 一樣，可拿來代表沒意義的但又需要用的變數
for _ in range(10):
    print(_, 'hi')

# 把切割開來的age存進_，因為不重要不需要，臨時創作用
name, _ = 'name$age'.split('$')

# public     # 別的地方也能用
# private    # 只能在同區域用(同個檔案?)
# naming convention 命名公約

class Qwe():
    def public_function(self):
        print('abcdef')

# helper function
    def _private_function(self):    # 理論上private只能在這個class內呼叫
        print('abcdef')

q = Qwe()
q.public_function()
q._private_function()

class Person:
    def __init__(self):
        self.x = 1
        self._y = 1
        self.__z = 1    # 雙底線是為了避免在繼承時撞名(Python的直譯器會去重新命名)

# 雙底線開頭雙底線結尾的 function 為 Python 先地譯好的一些功能
# 叫做 dunder methods / magic methods