# 【ジェネレータ関数の使用】
def generator(max):  # 'generator'という名前のジェネレータ関数を定義します。引数として'max'を受け取ります。
    print('ジェネレータ作成')  # ジェネレータが作成されたことを示すメッセージを出力します。
    for n in range(max):  # 0から'max'までの範囲でループを実行します。
        try:
            x = yield n  # 'n'をyieldし、次にジェネレータが呼び出されたときに送信される値を'x'に代入します。
            print('x = {}'.format(x))  # 'x'の値を出力します。
            print('yield実行')  # yieldが実行されたことを示すメッセージを出力します。
        except ValueError as e:  # ValueErrorが発生した場合、以下のコードを実行します。
            print('throwを実行しました')  # 'throw'が実行されたことを示すメッセージを出力します。

gen = generator(10)  # 'generator'関数を呼び出し、その結果を'gen'に代入します。この時点ではジェネレータはまだ実行されていません。
next(gen)  # 'gen'ジェネレータを1ステップ進めます。これにより、'ジェネレータ作成'と'yield実行'のメッセージが出力されます。
gen.send(100)  # 'gen'ジェネレータに値100を送信します。これにより、'x = 100'と'yield実行'のメッセージが出力されます。
# gen.throw(ValueError('Invalid Value'))  # 'gen'ジェネレータにValueErrorを送信します。これにより、'throwを実行しました'のメッセージが出力されます。
# gen.close()  # 'gen'ジェネレータを閉じます。これ以降、'gen'ジェネレータは使用できません。
next(gen)  # 'gen'ジェネレータを1ステップ進めます。これにより、'yield実行'のメッセージが出力されます。
# for x in gen:  # 'gen'ジェネレータのすべての要素に対してループを実行します。
#     print('x = {}'.format(x))  # 各要素の値を出力します。
# send