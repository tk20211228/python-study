#1
num = 10  # 整数型の変数numを定義します。値は10です。

#2
print(type(num))  # numの型を出力します。結果は<class 'int'>となります。

#3
num_str = str(num)  # numを文字列型に変換し、num_strに代入します。

#4
num_list = [num_str, '20', '30']  # リストnum_listを定義します。要素はnum_str, '20', '30'です。
print('num_list = {}'.format(num_list))  # num_listを出力します。結果は['10', '20', '30']となります。

#5
num_list.append('40')  # num_listに'40'を追加します。

#6
num_tuple = tuple(num_list)  # num_listをタプルに変換し、num_tupleに代入します。

#7
val = input()  # ユーザーからの入力を受け取り、valに代入します。
num_tuple += (val,)  # num_tupleにvalを追加します。

#8
num_set = {'40', '50', '60'}  # セットnum_setを定義します。要素は'40', '50', '60'です。
print('num_tuple = {}'.format(num_tuple))  # num_tupleを出力します。結果は('10', '20', '30', '40', 'ユーザーの入力')となります。
print('num_set = {}'.format(num_set))  # num_setを出力します。結果は{'40', '50', '60'}となります。

#9
print(set(num_tuple) | num_set)  # num_tupleとnum_setの和集合を出力します。結果は{'10', '20', '30', '40', '50', '60', 'ユーザーの入力'}となります。

#10
num_dict = {
    num_tuple: num_str  # 辞書型の変数num_dictを定義します。キーはnum_tuple、値はnum_strです。
}

#11
print(len(num_list))  # num_listの長さ（要素の数）を出力します。結果は4となります。

#12
print(num_dict.get('MyKey', 'Does not exist'))  # num_dictからキー'MyKey'の値を取得します。存在しない場合は'Does not exist'を出力します。

#13
num_list.extend(['50', '60'])  # num_listに'50'と'60'を追加します。
print('num_list = {}'.format(num_list))  # num_listを出力します。結果は['10', '20', '30', '40', '50', '60']となります。

#14
val = input()  # ユーザーからの入力を受け取り、valに代入します。
is_under_50 = int(val) < 50  # valを整数型に変換し、その値が50未満であるかを判定します。結果はTrueまたはFalseとなります。
print('is_under_50 = {}'.format(is_under_50))  # is_under_50を出力します。

#15
print(f'num_str = {num_str}')  # num_strを出力します。結果は'10'となります。

#16
print(dir(num_dict))  # num_dictの持つメソッド一覧を出力します。
