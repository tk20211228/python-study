# 【セットの関数について】

s = {'a', 'b', 'c', 'd'}  # セットsを定義します。
t = {'c', 'd', 'e', 'f'}  # セットtを定義します。

u = s | t # 和集合を求めます。sとtの両方に存在する要素を集めたセットを作ります。
u = s.union(t) # 和集合を求めます。上記と同じ結果を得ます。

print(u)  # 和集合の結果を出力します。{'a', 'b', 'c', 'd', 'e', 'f'}

u = s & t # 積集合を求めます。sとtの両方に存在する要素だけを集めたセットを作ります。
u = s.intersection(t) # 積集合を求めます。上記と同じ結果を得ます。

print(u)  # 積集合の結果を出力します。{'c', 'd'}

u = s - t # 差集合を求めます。sからtの要素を取り除いたセットを作ります。
u = s.difference(t) # 差集合を求めます。上記と同じ結果を得ます。
print(u)  # 差集合の結果を出力します。{'a', 'b'}

u = s ^ t # 対称差を求めます。sとtのどちらか一方にしか存在しない要素を集めたセットを作ります。
u = s.symmetric_difference(t) # 対称差を求めます。上記と同じ結果を得ます。
print(u)  # 対称差の結果を出力します。{'a', 'b', 'e', 'f'}

s |= t # sとtの和集合を求め、その結果をsに代入します。
print(s)  # sの結果を出力します。{'a', 'b', 'c', 'd', 'e', 'f'}

# 【issubset, issuperset, isdisjoint関数について】
s = {'apple', 'banana'}  # セットsを定義します。
t = {'apple', 'banana', 'lemon'}  # セットtを定義します。
u = {'cherry'}  # セットuを定義します。

print(s.issubset(t))  # sがtの部分集合であるかを確認します。Trueが出力されます。
print(s.issuperset(t))  # sがtの上位集合であるかを確認します。Falseが出力されます。
print(t.isdisjoint(s))  # tとsが共通の要素を持たないかを確認します。Falseが出力されます。
print(t.isdisjoint(u))  # tとuが共通の要素を持たないかを確認します。Trueが出力されます。
