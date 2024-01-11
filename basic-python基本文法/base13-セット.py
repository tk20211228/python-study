# 【セットの基本】
# Pythonのセットは、重複する要素を持たないコレクションです。順序も保持されません。
# 以下の例では、'a'と12が重複していますが、セットでは一度しか表示されません。

set_a = {'a', 'b', 'c', 'd', 'a', 12}  

# セットの出力
# 重複する要素は一度しか表示されません。順序も保持されません。
print(set_a)  # {'d', 'a', 'c', 'b', 12}

# セット内に特定の要素が存在しないことを確認
# 'e'はset_aに存在しないため、Trueが出力されます。
print('e' not in set_a)  # True

# セット内に特定の要素が存在することを確認
# 12はset_aに存在するため、Trueが出力されます。
print(12 in set_a)  # True

# セットの長さ（要素の数）を取得
# 重複する要素は一度しかカウントされません。
print(len(set_a))  # 5

# 【セットの操作】
# add, remove, discard, pop, clearメソッドを使用してセットを操作します。

# addメソッドで要素を追加
set_a.add('e')
print(set_a)  # {'d', 'a', 'c', 'b', 'e', 12}

# removeメソッドで要素を削除
set_a.remove('e')
print(set_a)  # {'d', 'a', 'c', 'b', 12}

# removeメソッドで存在しない要素を削除しようとするとエラーになる
# set_a.remove('E')

# discardメソッドで要素を削除
# 存在しない要素を削除しようとしてもエラーにならない
set_a.discard(12)
print(set_a)  # {'d', 'a', 'c', 'b'}
set_a.discard(12)  

print(set_a)  # {'d', 'a', 'c', 'b'}

# popメソッドで要素を取り出す
# 取り出される要素はランダム
val = set_a.pop()
print(val)  # 'd'など、ランダムな要素
print(set_a)  # {'a', 'c', 'b'}など、取り出された要素を除いたセット

# clearメソッドで全要素を削除
set_a.clear()
print(set_a)  # set()
