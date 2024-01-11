# インスタンス変数、クラス変数

class SampleA():
    class_val = 'class val' # クラス変数。全てのインスタンスで共有されます。

    def set_val(self):
        self.instance_val = 'instance val' # インスタンス変数。各インスタンスごとに異なる値を持つことができます。
    
    def print_val(self):
        print('クラス変数 = {}'.format(self.class_val)) # クラス変数を出力します。
        print('インスタンス変数 = {}'.format(self.instance_val)) # インスタンス変数を出力します。

instance_a = SampleA() # インスタンス化。SampleAクラスのインスタンスを作成します。
instance_a.set_val() # インスタンス変数を設定します。
print(instance_a.instance_val) # インスタンス変数を出力します。結果：'instance val'
instance_a.print_val() # クラス変数とインスタンス変数を出力します。結果：'class val', 'instance val'
print(SampleA.class_val) # クラス変数を出力します。結果：'class val'
print(instance_a.__class__.class_val) # クラス変数を出力します。結果：'class val'
instance_b = SampleA() #新たなインスタンスを作成します。
instance_b.set_val() # インスタンス変数を設定します。
instance_b.print_val() # クラス変数とインスタンス変数を出力します。結果：'class val', 'instance val'
instance_a.__class__.class_val = 'class val 2' # クラス変数を変更します。全てのインスタンスでこの新しい値が反映されます。
instance_b.print_val() # クラス変数とインスタンス変数を出力します。結果：'class val 2', 'instance val'

print('*'*100) # 区切り線を出力します。
print(id(instance_a.__class__.class_val)) # クラス変数のIDを出力します。全てのインスタンスで同じIDが出力されます。
print(id(instance_b.__class__.class_val)) # クラス変数のIDを出力します。全てのインスタンスで同じIDが出力されます。

