# 【forループの基本】

for i in range(10): # 0から9までの範囲でループを行います。
    print(i) # iの値を出力します。実行結果は0から9までの数値が順に表示されます。

for _ in range(100): # 100回ループを行いますが、ループ変数は使用しません。"_"は一般的に繰り返しをするときに、使われるものです。
    # print('A') # 'A'を出力しますが、現在はコメントアウトされているため実行されません。
    pass # 何もしない。ここではループを100回回すだけで何も行いません。

for i in range(2,20,3): # 2から19までの範囲で、3つ飛ばしでループを行います。
    print(i) # iの値を出力します。実行結果は2, 5, 8, 11, 14, 17が順に表示されます。

# 【リストとタプルのループ】
# sample = ['John', 'Paul', 'George', 'Ringo'] # リストの場合
sample = ('John', 'Paul', 'George', 'Ringo') # タプルの場合

for member in sample: # sampleの各要素に対してループを行います。
    print(member) # memberの値を出力します。実行結果は'John', 'Paul', 'George', 'Ringo'が順に表示されます。

# 【辞書のループ】
human = {
    'Name': 'Taro',
    'Age': 20,
    'gender': 'Man'
} # 'Name', 'Age', 'gender'というキーを持つ辞書を定義します。

for h in human: # humanの各キーに対してループを行います。
    print(h, human.get(h)) # キーとその値を出力します。実行結果は'Name Taro', 'Age 20', 'gender Man'が順に表示されます。
