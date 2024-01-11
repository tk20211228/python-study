# 【enumerateの使用例】

fruits = ['grape', 'Pine', 'Apple']  # リストfruitsを定義します。

# enumerate関数を使用して、リストのインデックスと値を取得します。
for index, value in enumerate(fruits):
    print('index = {}'.format(index))  # インデックスを出力します。実行結果は0, 1, 2が順に表示されます。
    print('value = {}'.format(value))  # 値を出力します。実行結果は'grape', 'Pine', 'Apple'が順に表示されます。

# 【zipの使用例】

classA = ['Taro', 'Hanako', 'Jiro']  # リストclassAを定義します。
classB = ['Katsuo', 'Wakame', 'Taro']  # リストclassBを定義します。

# zip関数を使用して、2つのリストの要素を同時に取得します。
for A, B in zip(classA, classB):
    print('classA student: {}'.format(A))  # classAの学生を出力します。実行結果は'Taro', 'Hanako', 'Jiro'が順に表示されます。
    print('classB student: {}'.format(B))  # classBの学生を出力します。実行結果は'Katsuo', 'Wakame', 'Taro'が順に表示されます。

# 【whileループの使用例】

count = 0  # 変数countを0で初期化します。

# countが10より小さい間、ループを続けます。
while count < 10: 
    print(count)  # countの値を出力します。実行結果は0から9までの数値が順に表示されます。
    count += 1  # countの値を1増やします。

