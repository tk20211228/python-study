# 【ノンローカル変数とinner関数の使用】
# inner関数は、外側の関数outerの変数outer_valueを参照し、その値を変更するために使用されます。
# これは、nonlocalキーワードを使用して実現されています。

def outer():
    outer_value = '外側の変数'  # 外側の関数で変数を定義します。
    def inner():
        nonlocal outer_value  # nonlocalキーワードを使用して、外側の関数の変数を参照します。
        outer_value = '内側の変数'  # 外側の関数の変数を変更します。
        print('inner: outer_value = {}, id = {}'.format(outer_value, id(outer_value)))  # 変更後の変数とそのIDを表示します。
    inner()  # 内側の関数を呼び出します。
    print('outer: outer_value = {}, id = {}'.format(outer_value, id(outer_value)))  # 外側の関数の変数とそのIDを表示します。

outer()  # 外側の関数を呼び出します。

# 【実行結果】
# inner: outer_value = 内側の変数, id = 140420971215440
# outer: outer_value = 内側の変数, id = 140420971215440
# これは、nonlocalキーワードにより、内側の関数から外側の関数の変数を変更できることを示しています。
# また、変数のIDが同じであることから、同じ変数を参照していることがわかります。
