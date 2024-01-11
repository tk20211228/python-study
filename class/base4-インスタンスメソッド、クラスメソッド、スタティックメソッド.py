# インスタンスメソッド、クラスメソッド、スタティックメソッド

class Human:

    class_name = "Human" # クラス変数。全てのインスタンスで共有されます。

    def __init__(self, name, age): # コンストラクタ。インスタンスが生成される際に自動的に呼び出されます。
        self.name = name # インスタンス変数。各インスタンスごとに異なる値を持ちます。
        self.age = age # インスタンス変数。各インスタンスごとに異なる値を持ちます。
    
    def print_name_age(self): # インスタンスメソッド。インスタンス変数を操作するためのメソッドです。
        print('インスタンスメソッド実行') # 実行結果：インスタンスメソッド実行
        print('name = {}, age = {}'.format(self.name, self.age)) # 実行結果：name = 桜木, age = 18
    
    @classmethod
    def print_class_name(cls, msg): # クラスメソッド。クラス変数を操作するためのメソッドです。
        print('クラスメソッド実行') # 実行結果：クラスメソッド実行
        print(cls.class_name) # クラス変数。実行結果：Human
        print(msg) # 引数で渡されたメッセージ。実行結果：こんにちは

    @staticmethod
    def print_msg(msg): # スタティックメソッド。クラスやインスタンスとは無関係に動作します。
        print('スタティックメソッド実行') # 実行結果：スタティックメソッド実行
        print(msg) # 引数で渡されたメッセージ。実行結果：hello static


Human.print_class_name('こんにちは') # クラスメソッドの呼び出し。実行結果：クラスメソッド実行、Human、こんにちは
man = Human('桜木', 18) # Humanクラスのインスタンスを生成。nameに'桜木'、ageに18を設定。
man.print_name_age() # インスタンスメソッドの呼び出し。実行結果：インスタンスメソッド実行、name = 桜木, age = 18
man.print_msg('hello static') # スタティックメソッドの呼び出し。実行結果：スタティックメソッド実行、hello static
Human.print_msg('hello static') # スタティックメソッドの呼び出し。実行結果：スタティックメソッド実行、hello static
