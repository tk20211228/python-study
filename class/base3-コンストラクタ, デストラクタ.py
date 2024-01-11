# コンストラクタ, デストラクタ

# 【クラスの定義】
class SampleClass:

    # 【コンストラクタ】
    def __init__(self, msg, name=None): # コンストラクタが呼ばれるときに実行されるメソッドです。
        print('コンストラクタが呼ばれました') # 実行結果：コンストラクタが呼ばれました
        self.msg = msg # インスタンス変数msgを定義します。
        self.name = name # インスタンス変数nameを定義します。
    
    # 【デストラクタ】
    def __del__(self): # デストラクタが呼ばれるときに実行されるメソッドです。
        print('デストラクタが実行されました') # 実行結果：デストラクタが実行されました
        print('name = {}'.format(self.name)) # 実行結果：name = Jiro

    # 【メソッドの定義】
    def print_msg(self): # msgを出力するメソッドです。
        print(self.msg) # 実行結果：Hello
    
    def print_name(self): # nameを出力するメソッドです。
        print(self.name) # 実行結果：Jiro

# 【インスタンスの生成とメソッドの呼び出し】
var_1 = SampleClass('Hello', 'Jiro') # SampleClassのインスタンスを生成します。msgに'Hello'、nameに'Jiro'を設定します。
var_1.print_msg() # print_msgメソッドを呼び出します。実行結果：Hello
var_1.print_name() # print_nameメソッドを呼び出します。実行結果：Jiro

# 【インスタンスの削除】
del var_1 # var_1を削除します。これによりデストラクタが呼び出されます。
