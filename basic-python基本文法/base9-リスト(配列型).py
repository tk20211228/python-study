# 【リストの基本】
# list_a = [1,2,3,4]
# list_b = []
#
# print(list_a)  # [1, 2, 3, 4]を出力します。list_aの全要素を表示します。
# print(list_a[-2])  # 3を出力します。list_aの後ろから2番目の要素を表示します。
#
# list_a = [1, [1,2,'apple'],3,'banana']
#
# print(list_a[1][2])  # 'apple'を出力します。list_aの2番目の要素（リスト）の3番目の要素を表示します。
# print(list_a)  # [1, [1, 2, 'apple'], 3, 'banana']を出力します。list_aの全要素を表示します。
# list_a[1][2] = 'lemon'  # list_aの2番目の要素（リスト）の3番目の要素を'lemon'に変更します。
# print(list_a)  # [1, [1, 2, 'lemon'], 3, 'banana']を出力します。list_aの全要素を表示します。
# list_a.reverse()  # list_aの要素の順序を逆にします。
# print(list_a)  # ['banana', 3, [1, 2, 'lemon'], 1]を出力します。list_aの全要素を表示します。
#
# 【リスト関数】
#
list_a = [1,2,3,4,5]
list_b = list_a[:3]  # list_aの最初から3番目までの要素をlist_bにコピーします。
print(list_b)  # [1, 2, 3]を出力します。list_bの全要素を表示します。
print(list_a[0:5:2])  # [1, 3, 5]を出力します。list_aの最初から5番目までの要素を2つ飛ばしで表示します。
#
# 【append, extend, insert, clear関数】
list_a.append('apple')  # list_aの最後に'apple'を追加します。
print(list_a)  # [1, 2, 3, 4, 5, 'apple']を出力します。list_aの全要素を表示します。
list_a.extend(['banana', 'lemon'])  # list_aの最後に'banana'と'lemon'を追加します。
print(list_a)  # [1, 2, 3, 4, 5, 'apple', 'banana', 'lemon']を出力します。list_aの全要素を表示します。
list_a.insert(1, 'grape')  # list_aの2番目の位置に'grape'を挿入します。
print(list_a)  # [1, 'grape', 2, 3, 4, 5, 'apple', 'banana', 'lemon']を出力します。list_aの全要素を表示します。
# list_a.clear()  # list_aの全要素を削除します。
# print(list_a)  # []を出力します。list_aは全要素が削除されたため、空のリストになります。
#
# 【remove, pop, count関数】
list_a.remove(3)  # list_aから最初に見つかった3を削除します。
print(list_a)  # [1, 'grape', 2, 4, 5, 'apple', 'banana', 'lemon']を出力します。list_aの全要素を表示します。
value = list_a.pop(1)  # list_aの2番目の要素を削除し、その要素をvalueに代入します。
print(list_a)  # [1, 2, 4, 5, 'apple', 'banana', 'lemon']を出力します。list_aの全要素を表示します。
print(value)  # 'grape'を出力します。valueにはlist_aからpopした要素が代入されています。
print(list_a.count('banana'))  # 1を出力します。list_aに'banana'が1つ含まれているためです。
print(list_a.index('apple'))  # 4を出力します。list_aにおける'apple'の位置（インデックス）を表示します。
#
# 【copy関数】
list_b = list_a.copy()  # list_aの全要素をlist_bにコピーします。
print(list_a)  # [1, 2, 4, 5, 'apple', 'banana', 'lemon']を出力します。list_aの全要素を表示します。
list_b[0]='AAAAA'  # list_bの最初の要素を'AAAAA'に変更します。
print(list_a)  # [1, 2, 4, 5, 'apple', 'banana', 'lemon']を出力します。list_aの全要素を表示します。list_bの変更はlist_aに影響を与えません。
#
# 【sort, reverse関数】
list_a = ['banana', 'lemon', 'apple', 'grape']
print(list_a)  # ['banana', 'lemon', 'apple', 'grape']を出力します。list_aの全要素を表示します。
list_a = sorted(list_a)  # list_aの要素をソート（昇順）します。
list_a.reverse()  # list_aの要素の順序を逆にします。
print(list_a)  # ['lemon', 'grape', 'banana', 'apple']を出力します。list_aの全要素を表示します。
