# 文字列型

# fruit = 'apple' # ""
# print(fruit)  # "apple"を出力します。
# print(type(fruit))  # <class 'str'>を出力します。

# print(fruit * 10)  # "appleappleappleappleappleappleappleappleappleapple"を出力します。

# new_fruit = fruit + ' banana'
# print(new_fruit)  # "apple banana"を出力します。

# # """
# fruits = """apple
# banana
# grape
# """
# print(fruits)  # "apple\nbanana\ngrape\n"を出力します。改行を含めて表示する

# fruit = 'banana'
# print(fruit[2])  # "n"を出力します。

# 【bytes型への変換】
# encode, decode(bytes[]型の関数) => bytes[]　データベースに保存するときによく使われる
# byte_fruit = fruit.encode('utf-8')

# print(byte_fruit)  # b'banana'を出力します。
# print(type(byte_fruit))  # <class 'bytes'>を出力します。
# str_fruit = byte_fruit.decode('shift-jis')  # エラーが発生します。'utf-8'でエンコードしたものを'decode'する際は同じ'utf-8'を使用する必要があります。
# print(str_fruit)
# print(type(str_fruit))

# 【count関数】

# msg = 'ABCDEABC'

# print(msg.count('ABCDEF'))  # 1を出力します。'ABCDEF'がmsg文字列内に1回存在するためです。

# 【startswith, endswith関数】

# print(msg.startswith('ABCD'))  # Trueを出力します。msg文字列が'ABCD'で始まるためです。
# print(msg.endswith('FABC'))  # Falseを出力します。msg文字列が'FABC'で終わらないためです。

# 【strip, rstrip, lstrip関数】

# print(msg.strip('ACB'))  # 'DE'を出力します。msg文字列の両端から'ACB'の文字を取り除いた結果です。
# print(msg.rstrip('ACB'))  # 'ABCDE'を出力します。msg文字列の右端から'ACB'の文字を取り除いた結果です。
# print(msg.lstrip('ACB'))  # 'DEABC'を出力します。msg文字列の左端から'ACB'の文字を取り除いた結果です。

# 【upper, lower, swapcase関数の使用例】
# msg = 'abcABC'
# msg_u = msg.upper()  # 'abcABC'を全て大文字に変換します。結果は'ABCABC'です。
# msg_l = msg.lower()  # 'abcABC'を全て小文字に変換します。結果は'abcabc'です。
# msg_s = msg.swapcase()  # 'abcABC'の大文字と小文字を入れ替えます。結果は'ABCabc'です。

# print(msg_u)  # 'ABCABC'を出力します。
# print(msg_l)  # 'abcabc'を出力します。
# print(msg_s)  # 'ABCabc'を出力します。

# 【replace関数の使用例】
# msg = 'ABCDEABC'
# msg_r = msg.replace('ABC', 'abc', -1)  # 'ABCDEABC'の'ABC'を全て'abc'に置換します。結果は'abcDEabc'です。第三引数の-1は、置換する回数を指定します。-1は無制限を意味します。
# print(msg_r)  # 'abcDEabc'を出力します。 


# 【capitalize関数】
# msg = 'hELLO world'
# print(msg.capitalize())  # 'Hello world'を出力します。msg文字列の最初の文字を大文字に、それ以外の文字を小文字にした結果です。

# 【文字列の一部取り出し、format関数、文字列から数値への変換、islower, isupper関数】
msg = 'h '
print(msg.isupper())  # Falseを出力します。msg文字列が全て大文字ではないためです。
print(msg.islower())  # Trueを出力します。msg文字列が全て小文字であるためです。

msg = 'hello, my name is taro'

print(msg[0:10:2])  # 'hlo y'を出力します。
"""
ここで、msg[0:10:2]はPythonのスライス機能を使用しています。
0:10:2は、0番目から10番目までの文字を取り出し、その際に2つ飛ばしで取り出すことを意味します。
つまり、0, 2, 4, 6, 8番目の文字を取り出します。その結果、'hlo y'という文字列が得られます。
スライスの一般的な形式は[start:end:step]で、startは開始位置、endは終了位置、stepはステップ数（取り出す間隔）を指定します。
"""

print(msg[:6])  # 'hello,'を出力します。
"""
ここで、msg[:6]はPythonのスライス機能を使用しています。
:6は、最初から6番目までの文字を取り出すことを意味します。
つまり、0, 1, 2, 3, 4, 5番目の文字を取り出します。その結果、'hello,'という文字列が得られます。
"""

print(msg[::2])  # 'hlo ynm s ao'を出力します。
"""
ここで、msg[::2]はPythonのスライス機能を使用しています。
::2は、最初から最後までの文字を取り出し、その際に2つ飛ばしで取り出すことを意味します。
つまり、0, 2, 4, 6, 8番目の文字を取り出します。その結果、'hlo ynm s ao'という文字列が得られます。
"""

print(msg[1:6])  # 'ello,'を出力します。
"""
ここで、msg[1:6]はPythonのスライス機能を使用しています。
1:6は、1番目から6番目までの文字を取り出すことを意味します。
つまり、1, 2, 3, 4, 5番目の文字を取り出します。その結果、'ello,'という文字列が得られます。
"""

# 【文字列のフォーマット】
name = 'Hanako'
msg1 = f'my name is {name}' # 3.6
msg2 = f'my name is {name=}' # 3.8

# Python 3.6以降では、f文字列（フォーマット済み文字列リテラル）を使用して、文字列内に変数の値を埋め込むことができます。
# ここでは、変数nameの値（'Hanako'）を文字列内に埋め込んでいます。
# f文字列は、文字列の前にfまたはFを付け、文字列内の{}で囲んだ部分に変数名を記述することで、その部分が変数の値に置き換えられます。
print(msg1)  # 'my name is Hanako'を出力します。

# Python 3.8以降では、f文字列で変数名とその値を一緒に出力することができます。
# これは、デバッグ時に変数の名前と値を一緒に出力したいときなどに便利です。
# {name=}と記述すると、'name=Hanako'のように、変数名とその値が一緒に出力されます。
print(msg2)  # 'my name is name=Hanako'を出力します。

msg = '12.21'
int_msg = float(msg)
print(int_msg)  # 12.21を出力します。msg文字列を浮動小数点数に変換した結果です。
print(type(int_msg))  # <class 'float'>を出力します。int_msgの型はfloatです。
# 【find, index, rfind, rindex関数】

msg = 'ABCDEABC'
print(msg.find('ABC'))  # 0を出力します。'ABC'がmsg文字列内に最初に出現する位置です。
print(msg.index('ABC'))  # 0を出力します。'ABC'がmsg文字列内に最初に出現する位置です。
print(msg.rfind('ABC'))  # 5を出力します。'ABC'がmsg文字列内に最後に出現する位置です。
print(msg.rindex('ABC'))  # 5を出力します。'ABC'がmsg文字列内に最後に出現する位置です。
print(msg.rfind('ABDC'))  # -1を出力します。'ABDC'がmsg文字列内に存在しないためです。
