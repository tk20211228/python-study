# 【高階関数の解説】

# 高階関数とは、他の関数を引数として受け取ったり、結果として関数を返す関数のことを指します。
# 以下のコードは高階関数の一例です。

# def print_hello():
#     print('hello')  # 'hello'を出力する関数

# def print_goodbye():
#     print('goodbye')  # 'goodbye'を出力する関数

# var = ['AA', 'BB', print_hello, print_goodbye]  # 配列に関数を格納
# var[2]()  # 配列の3番目の要素（print_hello関数）を実行 -> 'hello'が出力される
# var[3]()  # 配列の4番目の要素（print_goodbye関数）を実行 -> 'goodbye'が出力される

# 【関数を引数として受け取る高階関数の例】
def print_world(msg):
    print('{} world'.format(msg))  # 引数として受け取ったメッセージと'world'を結合して出力する関数

def print_konnichiwa():
    print('こんにちは')  # 'こんにちは'を出力する関数

def print_hello(func):
    func('hello')  # 引数として受け取った関数に'hello'を渡して実行
    return print_konnichiwa  # print_konnichiwa関数を返す

# 高階関数print_helloにprint_world関数を引数として渡す
var = print_hello(print_world)  # -> 'hello world'が出力され、print_konnichiwa関数が返される
var()  # 返されたprint_konnichiwa関数を実行 -> 'こんにちは'が出力される
