# 【関数の定義と呼び出し】

def print_hello():  # 'print_hello'という名前の関数を定義します
    print('Hello World')  # 関数が呼び出されると'Hello World'と出力します

print_hello()  # 'print_hello'関数を呼び出します。結果として'Hello World'が出力されます

# 【関数の引数と戻り値】

def num_max(a: int, b: int):  # 'num_max'という名前の関数を定義します。引数として整数'a'と'b'を受け取ります
    print('a = {}, b = {}'.format(a, b))  # 関数が呼び出されると'a'と'b'の値を出力します
    if a > b:  # 'a'が'b'より大きい場合
        return a  # 'a'を戻り値として返します
    else:  # 'a'が'b'より小さいまたは等しい場合
        return b  # 'b'を戻り値として返します
print(num_max(b=100,a=20))  # 'num_max'関数を呼び出し、'a'に20、'b'に100を渡します。結果として100が出力されます
print(num_max())  # 'num_max'関数を呼び出しますが、引数が指定されていないためエラーが発生します
