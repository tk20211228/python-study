# 【特殊関数】

class Human:

    # コンストラクタ：インスタンスが生成される際に自動的に呼び出されます。
    def __init__(self, name, age, phone_number):
        self.name = name  # インスタンス変数
        self.age = age  # インスタンス変数
        self.phone_number = phone_number  # インスタンス変数

    # __str__メソッド：インスタンスを文字列として表現するためのメソッドです。
    def __str__(self):
        return 'name = {}, age = {}, phone_number: {}'.format(self.name, self.age, self.phone_number)  
        # 実行結果：name = Elsa, age = 20, phone_number: 08011111111

    # __hash__メソッド：インスタンスのハッシュ値を返すメソッドです。
    def __hash__(self):
        print('hash関数が呼ばれました')  # 実行結果：hash関数が呼ばれました
        return hash(self.name + self.phone_number)  # 名前と電話番号の結合文字列のハッシュ値を返します。

    # __bool__メソッド：インスタンスの真偽値を返すメソッドです。
    def __bool__(self):
        if self.age > 20:
            return True  # 年齢が20より大きい場合、Trueを返します。
        else:
            return False  # 年齢が20以下の場合、Falseを返します。

    # __len__メソッド：インスタンスの長さ（要素数）を返すメソッドです。
    def __len__(self):
        print('lenが呼ばれました')  # 実行結果：lenが呼ばれました
        return 2  # ここでは2を返します。

woman = Human('Elsa', 20, '08011111111')  # Humanクラスのインスタンスを生成
woman2 = Human('Elsa', 22, '08022222222')  # Humanクラスのインスタンスを生成
print(hash(woman))  # womanのハッシュ値を表示
print(hash(woman2))  # woman2のハッシュ値を表示

# 辞書のキーとしてインスタンスを使用
dict_a = {
    woman: 'AAA'
}
print(dict_a)  # 辞書を表示

# インスタンスの真偽値を評価
if woman:
    print('WomanはTrue')  # 実行結果：WomanはTrue
if woman2:
    print('Woman2はTrue')  # 実行結果：Woman2はTrue

print(len(woman))  # womanの長さ（要素数）を表示
print(Human.__name__)  # クラス名を表示

# Pythonの公式ドキュメント：https://docs.python.org/ja/3/reference/datamodel.html#special-method-names
