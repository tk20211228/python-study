#【メタクラスの作成】

class MetaException(Exception):  # 独自の例外クラスを作成
    pass

class Meta1(type):  # type(デフォルトのメタクラス)

    def __new__(metacls, name, bases, class_dict):  # メタクラスの__new__メソッドをオーバーライド
        print('metacls = {}'.format(metacls))  # メタクラス名を表示
        print('name = {}'.format(name))  # クラス名を表示
        print('bases = {}'.format(bases))  # 基底クラスを表示
        print('class_dict = {}'.format(class_dict))  # クラスの属性を表示
        # if 'my_var' not in class_dict.keys():
        #     raise MetaException('my_varを定義してください。')
        for base in bases:  # 継承しているクラス
            if isinstance(base, Meta1):  # 継承元がMeta1であるかチェック
                raise MetaException('継承できません')  # finalクラス
        return super().__new__(metacls, name, bases, class_dict)  # 親クラスの__new__メソッドを呼び出す

#【クラスの作成】
class ClassA(metaclass=Meta1):  # メタクラスを指定してクラスを作成
    a = '123'  # クラス変数
    my_var = 'AAA'  # クラス変数
    pass

#【クラスの継承】
class SubClassA(ClassA):  # ClassAを継承したクラスを作成
    pass
""" メタクラスはクラスの振る舞いを制御するための高度なテクニックです。ここでは、メタクラスを使用してクラスの作成と継承を制御しています。 """
