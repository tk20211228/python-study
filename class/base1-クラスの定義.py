# 【クラスの定義とその使用例】

class Car: # Carという名前のクラスを定義します。
    """車クラス""" 
    country = 'Japan' # クラス変数を定義します。これはすべてのインスタンスで共有されます。
    year = 2019 # クラス変数を定義します。
    name = 'Prius' # クラス変数を定義します。
    def print_name(self): # インスタンスメソッドを定義します。selfはインスタンス自身を指します。
        print('print_name実行') # メソッドが呼び出されたことを示すメッセージを出力します。
        print(self.name) # インスタンスのname属性を出力します。

my_car = Car() # Carクラスのインスタンスを作成します。これをmy_carという名前の変数に代入します。
print(my_car.year) # my_carインスタンスのyear属性を出力します。結果は2019です。
my_car.print_name() # my_carインスタンスのprint_nameメソッドを呼び出します。結果は"print_name実行"と"Prius"が出力されます。
list_a = ['apple', 'banana', Car()] # リストを作成します。その中には文字列とCarクラスの新しいインスタンスが含まれています。
# second_car = list_a[2]() # この行はエラーを引き起こします。list_a[2]はCarクラスのインスタンスであり、呼び出し可能なオブジェクトではありません。
list_a[2].print_name() # リストの3番目の要素（Carクラスのインスタンス）のprint_nameメソッドを呼び出します。結果は"print_name実行"と"Prius"が出力されます。
help(Car) # Carクラスのヘルプ情報を出力します。これにはクラスの説明、メソッドのリスト、属性のリストなどが含まれます。
