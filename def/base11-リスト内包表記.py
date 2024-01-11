# 【リスト内包表記の解説】

list_a = (1,2,3,'a',4,'b') # タプル

list_b = [x*2 for x in list_a if type(x) == int] # list_aのリスト # list_aの整数要素を2倍にした新しいリストを作成します。結果は[2, 4, 6, 8]です。
print(list_b)
list_c = [x for x in range(100) if x % 7 == 0] # 0から99までの数値で、7で割り切れる数値のリストを作成します。結果は7の倍数のリストです。
print(list_c)


# 【辞書とリスト内包表記の解説】

dict_a = {
    'a': 'Apple',
    'b': 'Banana'
}
list_c = [dict_a.get(x) for x in list_a if type(x) == str] # list_aの文字列要素をキーとして辞書から値を取得し、新しいリストを作成します。結果は['Apple', 'Banana']です。
print(list_c)


# 【タプルとリスト内包表記の解説】

list_a = tuple(x for x in range(100)) # 0から99までの数値を要素とするタプルを作成します。結果は0から99までの数値が順に並んだタプルです。
print(type(list_a)) # 結果は<class 'tuple'>です。


# 【関数とリスト内包表記の解説】

def func(n): # 2からn-1までの数値でnを割り切れるものがあるかどうかをチェックする関数です。
    for x in range(2, n):
        if n % x == 0:
            return True
    return False

list_a = [func(x) for x in range(100) if func(x) == False] # 0から99までの数値で、上記の関数がFalseを返す数値のリストを作成します。結果は素数のリストです。
print(list_a)