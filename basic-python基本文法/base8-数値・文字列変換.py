# 【intとstrの変換】
int_num = 12  # 整数型の変数を定義します。
str_num = str(int_num)  # 整数型の変数を文字列型に変換します。
print(str_num)  # '12'を出力します。str_numは文字列型に変換されたためです。
print(type(str_num))  # <class 'str'>を出力します。str_numの型はstrです。
float_num = -20.5  # 浮動小数点数型の変数を定義します。
str_float = str(float_num)  # 浮動小数点数型の変数を文字列型に変換します。
print(str_float)  # '-20.5'を出力します。str_floatは文字列型に変換されたためです。
print(type(str_float))  # <class 'str'>を出力します。str_floatの型はstrです。

# 【strからintとfloatへの変換】
msg = '12'  # 文字列型の変数を定義します。
int_msg = int(msg)  # 文字列型の変数を整数型に変換します。
float_msg = float(msg)  # 文字列型の変数を浮動小数点数型に変換します。

print('value = {}, type = {}'.format(int_msg, type(int_msg)))  # 'value = 12, type = <class 'int'>'を出力します。int_msgは整数型に変換されたためです。
print('value = {}, type = {}'.format(float_msg, type(float_msg)))  # 'value = 12.0, type = <class 'float'>'を出力します。float_msgは浮動小数点数型に変換されたためです。

