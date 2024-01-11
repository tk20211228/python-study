# 【例外の自作とその使用例】

class MyException(Exception):  # MyExceptionという新しい例外を作成します。これはExceptionを継承しています。
    pass  # 特別な動作は定義していません。

def devide(a, b):  # devideという関数を定義します。この関数は2つの数値を引数に取り、割り算を行います。
    if b == 0:  # もし割る数が0であれば
        raise MyException('0では割り切れません')  # MyExceptionを発生させ、'0では割り切れません'というメッセージを付けます。
    else:  # もし割る数が0でなければ
        return a / b  # 割り算の結果を返します。

try:  # tryブロックを開始します。
    c = devide(10, 0)  # devide関数に10と0を引数として渡します。この結果、MyExceptionが発生します。
except Exception as e:  # 任意の例外が発生した場合
    print(e, type(e))  # 例外のメッセージとその型を出力します。この場合、'0では割り切れません'とMyExceptionが出力されます。
