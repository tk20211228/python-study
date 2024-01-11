# 【getter, setter】

class Human:

    def __init__(self, name, age):
        # インスタンス変数の初期化
        self.__name = name
        self.__age = age
    
    def get_name(self):
        # nameのゲッター
        print('getter name を呼び出しました')
        return self.__name
    
    def get_age(self):
        # ageのゲッター
        print('getter ageを呼び出しました')
        return self.__age
    
    def set_name(self, name):
        # nameのセッター
        print('setter nameを呼び出しました')
        self.__name = name
    
    def set_age(self, age):
        # ageのセッター
        print('setter ageを呼び出しました')
        self.__age = age
    
    # nameとageに対するゲッターとセッターの設定
    name = property(get_name, set_name) # nameを指定するとget_name, set_nameが呼び出される, human.set_name()
    age = property(get_age, set_age)

    def print_msg(self):
        # nameとageの出力
        print(self.name, self.age)

human = Human('Taro', 15)
human.name = 'Jiro'  # nameのセッターを呼び出す
human.age = 18  # ageのセッターを呼び出す

name = human.name  # nameのゲッターを呼び出す
age = human.age  # ageのゲッターを呼び出す
print(name, age)
human.print_msg()

"""
このコードはPythonのゲッターとセッターの使い方を示しています。
ゲッターとセッターは、オブジェクトの属性に対するアクセスを制御するための特殊なメソッドです。
これにより、属性の値を取得したり設定したりする際に追加の処理を行うことができます。
"""