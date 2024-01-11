# 【Map関数の解説】

list_a = [1,2,3,4,5] # 整数のリストを定義します。
map_a = map(lambda x: x * 2, list_a) # map関数を使用して、list_aの各要素を2倍にします。

for x in map_a: # map_aの各要素を出力します。
    print(x) # 実行結果は2, 4, 6, 8, 10です。

man = { # 辞書を定義します。
    'name': 'Ichiro',
    'age': '18',
    'country': 'Japan'
}
map_man = map(lambda x: x + ',' + man.get(x), man) # map関数を使用して、辞書の各キーと値を結合します。

for x in map_man: # map_manの各要素を出力します。
    print(x) # 実行結果は"name,Ichiro", "age,18", "country,Japan"です。

def calcurate(x, y, z): # 3つの引数を受け取る関数を定義します。
    if z == 'plus': # zが'plus'の場合、xとyを足します。
        return x + y
    elif z == 'minus': # zが'minus'の場合、xからyを引きます。
        return x - y

map_sample = map(calcurate, range(5), [3,3,3,3,3], ['plus', 'minus', 'plus', 'minus', 'plus']) # map関数を使用して、calcurate関数を各引数に適用します。

for x in map_sample: # map_sampleの各要素を出力します。
    print(x) # 実行結果は3, -2, 5, 0, 7です。
