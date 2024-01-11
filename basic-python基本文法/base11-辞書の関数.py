# 辞書の関数

car = {'brand': 'Toyota', 'model': 'Prius', 'year': 2015}  # 辞書型の変数carを定義します。キーと値のペアで構成されています。

tmp_dict = {'country': 'Japan', 'prefecture': 'Aichi', 'model': 'カローラ'}  # 辞書型の変数tmp_dictを定義します。キーと値のペアで構成されています。
car.update(tmp_dict)  # carの辞書にtmp_dictの辞書を追加します。
print(car)  # 更新後のcarを出力します。{'brand': 'Toyota', 'model': 'カローラ', 'year': 2015, 'country': 'Japan', 'prefecture': 'Aichi'}が出力されます。
car['city'] = 'Toyota-shi'  # carの辞書に新たなキー'city'とその値'Toyota-shi'を追加します。
car['year'] = 2017  # carの辞書の'year'キーの値を2017に更新します。
print(car)  # 更新後のcarを出力します。{'brand': 'Toyota', 'model': 'カローラ', 'year': 2017, 'country': 'Japan', 'prefecture': 'Aichi', 'city': 'Toyota-shi'}が出力されます。

value = car.popitem()  # carの辞書から最後のキーと値のペアを削除し、そのペアをvalueに代入します。
print(car)  # 更新後のcarを出力します。{'brand': 'Toyota', 'model': 'カローラ', 'year': 2017, 'country': 'Japan', 'prefecture': 'Aichi'}が出力されます。
print(value)  # valueを出力します。('city', 'Toyota-shi')が出力されます。

value = car.pop('model')  # carの辞書から'model'キーとその値を削除し、その値をvalueに代入します。
print(car)  # 更新後のcarを出力します。{'brand': 'Toyota', 'year': 2017, 'country': 'Japan', 'prefecture': 'Aichi'}が出力されます。
print(value)  # valueを出力します。'カローラ'が出力されます。

car.clear()  # carの辞書から全てのキーと値を削除します。
print(car)  # 更新後のcarを出力します。{}が出力されます。
del car  # carを完全に削除します。
print(car)  # carを出力しようとするとエラーが発生します。carは存在しないためです。

