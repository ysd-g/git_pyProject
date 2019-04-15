# 文字列の連結
account = "hoge"
domain = "docomo.ne.jp"
email = account + "@" + domain
print(email) # hoge@docomo.ne.jp
print(account*3) # hogehogehoge
print("\n") # 改行


# 数値計算
x = 10
print(x/7) # 1.428571...
print(x//7) # 1 (除算)
print(x%7) # 3
print(x**2) # 100


#文字列フォーマット指定
name1 = "Endo" #文字型は、%s
age1 = 21 #数値型は、%d
weight1 = 58.9 #浮動小数点型は、%f

name2 = "Yoshida"
age2 = 24
weight2 = 57.9

print("name: %10s, age: %10d, weight: %10.2f" %(name1, age1, weight1))
print("name: %10s, age: %10d, weight: %10.2f \n" %(name2, age2, weight2))

#左揃え(こっちのほうが見やすい)
print("name: %-10s, age: %-10d, weight: %-10.2f" %(name1, age1, weight1))
print("name: %-10s, age: %-10d, weight: %-10.2f \n" %(name2, age2, weight2))

#{}を使っても表示できる
print("name: {0}, age: {1}, weight: {2}".format(name1, age1, weight1))
print("name: {0:10s}, age: {1:10d}, weight: {2:10.2f}".format(name1, age1, weight1))
print("name: {0:<10s}, age: {1:<10d}, weight: {2:<10.2f}".format(name1, age1, weight1))



