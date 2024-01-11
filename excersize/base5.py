# base5.py

#【抽象クラスとポリモーフィズムの学習】
from abc import abstractmethod, ABCMeta  # abcモジュールからabstractmethodとABCMetaをインポートします

#【抽象クラスの定義】
class Animals(metaclass=ABCMeta):  # ABCMetaをメタクラスとして持つAnimalsという抽象クラスを定義します

    @abstractmethod  # 抽象メソッドを定義します
    def speak(self):  # speakというメソッドを定義します
        pass  # 抽象メソッドなのでpassを記述します

#【具象クラスの定義】
class Dog(Animals):  # Animalsクラスを継承したDogクラスを定義します

    def speak(self):  # speakメソッドをオーバーライドします
        print('わん')  # 'わん'を出力します

class Cat(Animals):  # Animalsクラスを継承したCatクラスを定義します
    
    def speak(self):  # speakメソッドをオーバーライドします
        print('にゃー')  # 'にゃー'を出力します

class Sheep(Animals):  # Animalsクラスを継承したSheepクラスを定義します

    def speak(self):  # speakメソッドをオーバーライドします
        print('めー')  # 'めー'を出力します

class Other(Animals):  # Animalsクラスを継承したOtherクラスを定義します

    def speak(self):  # speakメソッドをオーバーライドします
        print('そんな動物いない')  # 'そんな動物いない'を出力します

#【ユーザー入力とポリモーフィズムの実行】
number = input('好きな動物は？ 1: 犬、2: 猫, 3:羊')  # ユーザーに入力を求めます

if number == '1':  # 入力が'1'なら
    animal = Dog()  # Dogクラスのインスタンスを生成します
elif number == '2':  # 入力が'2'なら
    animal = Cat()  # Catクラスのインスタンスを生成します
elif number == '3':  # 入力が'3'なら
    animal = Sheep()  # Sheepクラスのインスタンスを生成します
else:  # それ以外なら
    animal = Other()  # Otherクラスのインスタンスを生成します

animal.speak()  # speakの呼び出し（ポリモーフィズム）

"""
このコードは抽象クラスとポリモーフィズムの基本的な使い方を示しています。
抽象クラスは具体的な実装を持たず、一部または全部が子クラスによって実装されるべきメソッドを定義します。
ポリモーフィズムは、同じインターフェースを持つオブジェクトを同じように扱うことができる特性を指します。
"""
