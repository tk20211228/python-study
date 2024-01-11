# 【サブジェネレータ】

def sub_sub_generator():  # サブサブジェネレータ関数を定義します
    yield "Sub Subのyield"  # 最初のyield値を返します
    return "sub sub のreturn"  # 最終的なreturn値を返します

def sub_generator():  # サブジェネレータ関数を定義します
    yield "subのyield"  # 最初のyield値を返します
    res = yield from sub_sub_generator()  # サブサブジェネレータから値を取得します
    print("sub res = {}".format(res))  # サブサブジェネレータのreturn値を表示します
    return "subのreturn"  # 最終的なreturn値を返します

def generator():  # ジェネレータ関数を定義します
    yield "generatorのyield"  # 最初のyield値を返します
    res = yield from sub_generator()  # サブジェネレータから値を取得します
    print('gen res = {}'.format(res))  # サブジェネレータのreturn値を表示します
    return 'generatorのreturn'  # 最終的なreturn値を返します

gen = generator()  # ジェネレータ関数を呼び出します
print(next(gen))  # "generatorのyield"を出力します
print(next(gen))  # "subのyield"を出力します
print(next(gen))  # "Sub Subのyield"を出力します
print(next(gen))  # "sub res = sub sub のreturn"を出力します
print(next(gen))  # "gen res = subのreturn"を出力します

# 実行結果：
# generatorのyield
# subのyield
# Sub Subのyield
# sub res = sub sub のreturn
# gen res = subのreturn
