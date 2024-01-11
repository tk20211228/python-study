# 【辞書型の基本】

car = {'brand': 'Toyota', 'model': 'Prius', 'year': 2015, 1: 100}  # 辞書型の変数carを定義します。キーと値のペアで構成されています。

print(car['brand'])  # 'Toyota'を出力します。carの'brand'キーの値を表示します。
print(car.get('bran', 12))  # 12を出力します。carに'bran'キーが存在しないため、デフォルト値の12を表示します。

print(car.get(1))  # 100を出力します。carの1キーの値を表示します。

print(car.keys())  # dict_keys(['brand', 'model', 'year', 1])を出力します。carの全キーを表示します。
print(car.values())  # dict_values(['Toyota', 'Prius', 2015, 100])を出力します。carの全値を表示します。
print(car.items())  # dict_items([('brand', 'Toyota'), ('model', 'Prius'), ('year', 2015), (1, 100)])を出力します。carの全キーと値のペアを表示します。

# 【辞書型のループ処理】
for k, v in car.items():  # carの全キーと値のペアに対してループ処理を行います。
    print('key = {}, value = {}'.format(k, v))  # 'key = brand, value = Toyota'などを出力します。各キーと値を表示します。

# 【辞書型のキー存在チェック】
if 'bran' in car:  # carに'bran'キーが存在するかチェックします。
    print('carのブランドは{}'.format(car['brand']))  # 何も出力されません。'bran'キーは存在しないため、このprint文は実行されません。
