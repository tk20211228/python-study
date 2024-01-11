# 【デフォルト値、可変長引数、複数の返り値】


def sample(arg1, arg2=100):  # 'sample'関数を定義します。引数として'arg1'とデフォルト値100の'arg2'を受け取ります
    print(arg1, arg2)  # 'arg1'と'arg2'の値を出力します

# sample(200)  # 'sample'関数を呼び出し、'arg1'に200を渡します。結果として'200, 100'が出力されます

def spam(arg1, *arg2):  # 'spam'関数を定義します。引数として'arg1'と可変長引数'arg2'を受け取ります
    print("arg1 = {}, arg2 = {}".format(arg1, arg2))  # 'arg1'と'arg2'の値を出力します
    print(type(arg2))  # 'arg2'の型を出力します。結果として'<class 'tuple'>'が出力されます

spam(1,2,3,4,5)  # 'spam'関数を呼び出し、'arg1'に1、'arg2'に2,3,4,5を渡します。結果として'arg1 = 1, arg2 = (2, 3, 4, 5)'と'<class 'tuple'>'が出力されます

def spam_2(arg1, **arg2):  # 'spam_2'関数を定義します。引数として'arg1'と可変長引数'arg2'（キーワード引数）を受け取ります
    print('arg1 = {}, arg2 = {}'.format(arg1, arg2))  # 'arg1'と'arg2'の値を出力します
    print(type(arg2))  # 'arg2'の型を出力します。結果として'<class 'dict'>'が出力されます

spam_2(3, name='Taro', age=20)  # 'spam_2'関数を呼び出し、'arg1'に3、'arg2'に'name=Taro'と'age=20'を渡します。結果として'arg1 = 3, arg2 = {'name': 'Taro', 'age': 20}'と'<class 'dict'>'が出力されます

def spam_3(arg1, *arg2, **arg3):  # 'spam_3'関数を定義します。引数として'arg1'、可変長引数'arg2'、キーワード引数'arg3'を受け取ります
    print(arg1, arg2, arg3)  # 'arg1'、'arg2'、'arg3'の値を出力します

spam_3(1,2,3,4,5,name='Taro', age=15)  # 'spam_3'関数を呼び出し、'arg1'に1、'arg2'に2,3,4,5、'arg3'に'name=Taro'と'age=15'を渡します。結果として'1 (2, 3, 4, 5) {'name': 'Taro', 'age': 15}'が出力されます

def sample_2():  # 'sample_2'関数を定義します。この関数は複数の値を返します
    return 1, 2, 3  # 1, 2, 3を返します

a,b, c = sample_2()  # 'sample_2'関数を呼び出し、返り値を'a'、'b'、'c'に代入します
print(a,b,c)  # 'a'、'b'、'c'の値を出力します。結果として'1 2 3'が出力されます
