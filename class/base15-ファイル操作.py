# with base15.py
# 【ファイル操作】
# 'with' ステートメントとコンテキストマネージャを使用してファイルを操作します。

class WithTest:
    # WithTestクラスの定義。このクラスはコンテキストマネージャとして機能します。

    def __init__(self, file_name):
        # 初期化メソッド。ファイル名を受け取り、それをインスタンス変数に保存します。
        print('init called')
        self.__file_name = file_name
    
    def __enter__(self):
        # enterメソッド。ファイルを開き、自身のインスタンスを返します。
        print('enter called')
        self.__file = open(self.__file_name, mode='w', encoding='utf-8')
        return self
    
    def write(self, msg):
        # writeメソッド。メッセージを受け取り、それをファイルに書き込みます。
        self.__file.write(msg)

    def __exit__(self, exc_type, exc_val, traceback):
        # exitメソッド。ファイルを閉じます。
        print('exit called')
        self.__file.close()
    
with WithTest('resources/output.txt') as t:
    # 'with' ステートメントを使用して、WithTestクラスのインスタンスを作成し、
    # そのコンテキスト内でファイル操作を行います。
    print('with の中')
    t.write('ああああああ')

# """ コンテキストマネージャは、リソースのセットアップとクリーンアップを自動化するためのものです。
# 'with' ステートメントと一緒に使用すると、ファイルのようなリソースを効率的に管理できます。 """