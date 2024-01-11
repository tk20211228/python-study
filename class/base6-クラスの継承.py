# 【クラスの継承】

class Person: # 親クラス

    def __init__(self, name, age): # 初期化メソッド
        self.name = name # 名前をインスタンス変数に設定
        self.age = age # 年齢をインスタンス変数に設定
    
    def greeting(self): # 挨拶メソッド
        print('hello {}'.format(self.name)) # 名前を使って挨拶を表示
    
    def say_age(self): # 年齢を表示するメソッド
        print('{} years old'.format(self.age)) # 年齢を表示

class Employee(Person): # Personクラスを継承したEmployeeクラス

    def __init__(self, name, age, number): # 初期化メソッド
        super().__init__(name, age) # 親クラスの初期化メソッドを呼び出す
        self.number = number # 電話番号をインスタンス変数に設定
    
    def say_number(self): # 電話番号を表示するメソッド
        print('my number is = {}'.format(self.number)) # 電話番号を表示
    
    def greeting(self): # 挨拶メソッドをオーバーライド
        super().greeting() # 親クラスの挨拶メソッドを呼び出す
        print('I\'m employee phone_number = {}'.format(self.number)) # 電話番号を表示

    # def greeting(self, age): # オーバロードできない
    #     print('オーバーロード')
man = Employee('Tonegawa', 45, '08011111111') # Employeeクラスのインスタンスを生成
man.greeting() # 挨拶メソッドを呼び出す（結果：'hello Tonegawa'と'I'm employee phone_number = 08011111111'が表示される）
man.say_age() # 年齢を表示するメソッドを呼び出す（結果：'45 years old'が表示される）
man.say_number() # 電話番号を表示するメソッドを呼び出す（結果：'my number is = 08011111111'が表示される）
