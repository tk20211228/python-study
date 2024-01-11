# クラスの多重継承

# 【ClassAの定義】
class ClassA:  # ClassAというクラスを定義します

    def __init__(self, name):  # 初期化メソッドを定義します。nameという引数を取ります
        self.a_name = name  # インスタンス変数a_nameを定義し、引数nameの値を代入します
    
    def print_a(self):  # print_aというメソッドを定義します
        print('ClassAのメソッド実行')  # 文字列を出力します
        print('a = {}'.format(self.a_name))  # a_nameの値を出力します
    
    def print_hi(self):  # print_hiというメソッドを定義します
        print('A hi')  # 文字列を出力します

# 【ClassBの定義】
class ClassB:  # ClassBというクラスを定義します

    def __init__(self, name):  # 初期化メソッドを定義します。nameという引数を取ります
        self.b_name = name  # インスタンス変数b_nameを定義し、引数nameの値を代入します
    
    def print_b(self):  # print_bというメソッドを定義します
        print('ClassBのメソッド実行')  # 文字列を出力します
        print('b = {}'.format(self.b_name))  # b_nameの値を出力します
    
    def print_hi(self):  # print_hiというメソッドを定義します
        print('B hi')  # 文字列を出力します

# 【NewClassの定義】
class NewClass(ClassA, ClassB):  # ClassAとClassBを継承したNewClassというクラスを定義します

    def __init__(self, a_name, b_name, name):  # 初期化メソッドを定義します。a_name, b_name, nameという引数を取ります
        ClassA.__init__(self, a_name)  # ClassAの初期化メソッドを呼び出します
        ClassB.__init__(self, b_name)  # ClassBの初期化メソッドを呼び出します
        self.name = name  # インスタンス変数nameを定義し、引数nameの値を代入します
    
    def print_new_name(self):  # print_new_nameというメソッドを定義します
        print('name = {}'.format(self.name))  # nameの値を出力します
    
    def print_hi(self):  # print_hiというメソッドを定義します
        ClassA.print_hi(self)  # ClassAのprint_hiメソッドを呼び出します
        ClassB.print_hi(self)  # ClassBのprint_hiメソッドを呼び出します
        print('NewClass hi')  # 文字列を出力します

# 【インスタンスの生成とメソッドの実行】
sample = NewClass('AName', 'BName', 'New Class Name')  # NewClassのインスタンスを生成します

sample.print_a()  # print_aメソッドを実行します。結果は "ClassAのメソッド実行" "a = AName" と出力されます
sample.print_b()  # print_bメソッドを実行します。結果は "ClassBのメソッド実行" "b = BName" と出力されます
sample.print_new_name()  # print_new_nameメソッドを実行します。結果は "name = New Class Name" と出力されます
sample.print_hi()  # print_hiメソッドを実行します。結果は "A hi" "B hi" "NewClass hi" と出力されます
