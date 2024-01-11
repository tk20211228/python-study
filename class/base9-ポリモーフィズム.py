# 【ポリモーフィズム】

from abc import abstractmethod, ABCMeta # 抽象クラスを作成するためのモジュールをインポート

class Human(metaclass=ABCMeta): # 親クラス

    def __init__(self, name): # 初期化メソッド
        self.name = name # インスタンス変数nameを定義
    
    @abstractmethod # 抽象メソッドを定義
    def say_something(self):
        pass

    def say_name(self): # インスタンスメソッドを定義
        print(self.name) # インスタンス変数nameを出力

class Woman(Human): # Humanクラスを継承したWomanクラス
    
    def say_something(self): # 抽象メソッドをオーバーライド
        print('女性: 名まえは={}'.format(self.name)) # 女性の名前を出力

class Man(Human): # Humanクラスを継承したManクラス
    
    def say_something(self): # 抽象メソッドをオーバーライド
        print('男性: 名まえは={}'.format(self.name)) # 男性の名前を出力


# 【ポリモーフィズム】
num = input('0か1を入力してください') # ユーザーからの入力を受け取る
if num == '0': # 入力が0の場合
    human = Man('Taro') # Manクラスのインスタンスを生成
elif num == '1': # 入力が1の場合
    human = Woman('Hanako') # Womanクラスのインスタンスを生成
else: # それ以外の入力の場合
    print('入力が間違っています') # エラーメッセージを出力
human.say_something() # say_somethingメソッドを呼び出す

"""
このコードはポリモーフィズムを学習するためのものです。
ポリモーフィズムとは、同じインターフェースでデータを操作するOOPの原則を指します。
具体的には、同じメソッド名say_somethingを持つManクラスとWomanクラスがあり、
それぞれのクラスで異なる振る舞いをします。
"""
