#for文
for i in range(0, 10):
    if i % 2 == 0:
        continue
    print(i)
print("Finish\n")

#----------------------------------------------------------------


#pass
def test():
    #関数の中身を今書かずに、あとで記述したいときに、passを入れる
    pass

msg = test() # Noneが返ってくる
print(msg)
print("\n")

#----------------------------------------------------------------




#コンストラクタ     "def __init__():"
class User:
    count = 0

    def __init__(self, name, age):
        User.count += 1 #クラス変数
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, %10s" %self.name)



usr1 = User("Yoshida", 24)
usr2 = User("Tanaka", 27)

print("count: {0:<5d}".format(User.count))
print("name: {0:<10s} age: {1:5d}".format(usr1.name, usr1.age))
print("name: {0:<10s} age: {1:5d}".format(usr2.name, usr2.age))
print("\n")

usr1.greet()
usr2.greet()
print("\n")



#----------------------------------------------------------------


#継承

class AdminUser(User):
    def __init__(self, name, age):
        super().__init__(name, age)
        
    def say_hello(self):
        print("Hello. AdminUser, {}さん".format(self.name))

usr3 = AdminUser("Kensuke", 25)
usr3.say_hello()
print("\n")




#----------------------------------------------------------------


#例外処理
def div(a, b):
    try:
        print("{0}/{1} の計算を始めます".format(a, b))
        print("計算結果：{}".format(a/b))

    except ZeroDivisionError: #例外処理
        print("not by Zero")

    else:                     #例外がないときに出力
        print("no exception")

    finally:
        print("---end--- 処理が終わりました")
        print("\n")

div(20, 7)
div(20, 0)



#----------------------------------------------------------------








