# setter, getter その2

class Human:

    def __init__(self, name, age):
        # インスタンス変数の初期化
        self.__name = name
        self.__age = age
    
    @property
    def name(self): # getter
        # nameのゲッター
        print('getter nameが呼ばれました')
        return self.__name
    
    @property
    def age(self):
        # ageのゲッター
        print('getter ageを呼ばれました')
        return self.__age
    
    @name.setter
    def name(self, name):
        # nameのセッター
        print('setter nameが呼ばれました')
        self.__name = name
    
    @age.setter
    def age(self, age):
        # ageのセッター
        print('setter ageが呼ばれました')
        # 年齢が0未満の場合はエラーメッセージを表示
        if age < 0:
            print('0以上の値を設定してください')
            return
        self.__age = age

human = Human('Koichi', 22)
human.name = 'Makoto'  # nameのセッターを呼び出す
print(human.name)  # nameのゲッターを呼び出す
human.age = -1  # ageのセッターを呼び出す
print(human.age)  # ageのゲッターを呼び出す

"""
このコードはPythonのプロパティの使い方を示しています。
プロパティは、オブジェクトの属性に対するアクセスを制御するための特殊なメソッドです。
これにより、属性の値を取得したり設定したりする際に追加の処理を行うことができます。
"""
