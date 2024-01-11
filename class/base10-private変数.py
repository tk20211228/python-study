# private変数

class Human:

    __class_val = 'Human'  # クラス変数。全てのインスタンスで共有されます。

    def __init__(self, name, age):
        self.__name = name  # インスタンス変数。各インスタンスごとに異なる値を持ちます。# private変数　クラス外からアクセスできない
        self.__age = age  # インスタンス変数。各インスタンスごとに異なる値を持ちます。# private変数　クラス外からアクセスできない

    def print_msg(self):
        # formatメソッドを使用して文字列内に変数の値を埋め込みます。
        print('name = {}, age = {}'.format(self.__name, self.__age))


human = Human('Taro', 15)  # Humanクラスのインスタンスを作成します。
human.print_msg()  # インスタンスのメソッドを呼び出します。
