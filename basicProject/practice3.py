#リスト

scores = [40, 50, 300, 49, 59]
print(scores[0])


scores.append(100)
scores.append(56)

print(scores[len(scores)-1])

print("リストの中身一覧.{}".format(scores))

print("リストの大きさは、{}です".format(len(scores)))

print("\n")


#----------------------------------------------------------------


#for文とenumerate()
#enumerateは、値とそのID番号を取得するときに便利

print("値だけ出力する")

for score in scores:
    print("値: {}".format(score))
print("\n")

print("IDと値を出力する")


for i, score in enumerate(scores):
    print("ID: {0}, 値: {1}".format(i, score))
print("\n")



print("要素の始点、終点[0:7]")
print(scores[0:7])  #出力結果：[40, 50, 300, 49, 59, 100, 56]
print(scores[1:6])  #出力結果：[50, 300, 49, 59, 100]
print("\n")

print("終点のみ")
print(scores[:len(scores)])  #出力結果：[40, 50, 300, 49, 59, 100, 56]

print(scores[:2])   #出力結果：[40, 50]

print(scores[2:])   #出力結果：[300, 49, 59, 100, 56]

print(scores[-3:])  #出力結果：[59, 100, 56]

print("\n")


#----------------------------------------------------------------
#remove: 削除したい"値"を()の中に書く
#pop: 削除したい"位置"を()の中に書く



rng = list(range(1, 11))
print(rng)          #出力結果：[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("\n")


rng = list(range(11))
print(rng)          #出力結果：[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("\n")


#-----------remove-----------

Rng = [1, 1, 4, 5, 1, 4]

Rng.remove(4)       #値4を削除する
print(Rng)          #出力結果：[1, 1, 5, 1, 4]


Rng.remove(4)       #値4を削除する
print(Rng)          #出力結果：[1, 1, 5, 1]
print("\n")



#-----------pop-----------

Rng = [1, 1, 4, 5, 1, 4]

Rng.pop(4)       #位置4を削除する
print(Rng)          #出力結果：[1, 1, 4, 5, 4]


Rng.pop(4)       #位置4を削除する
print(Rng)          #出力結果：[1, 1, 4, 5]
print("\n")



#-----------del-----------

Rng = [1, 1, 4, 5, 1, 4]

del Rng[0]       #位置0を削除する
print(Rng)          #出力結果：[1, 4, 5, 1, 4]


del Rng[-1]       #末尾を削除する
print(Rng)          #出力結果：[1, 4, 5, 1]


Rng = [1, 8, 4, 3, 9, 0]
del Rng[1:3]
print(Rng)          #出力結果：[1, 3, 9, 0]
                    #Rng.del[-5:-3]と同じ


Rng = [1, 8, 4, 3, 9, 0]
del Rng[-5:-3]
print(Rng)
print("\n")
