# 【try exceptの使用例】

try:
    # リストbを定義します。
    b = [10,20,30]
    # 存在しないメソッドmethod_aを呼び出そうとします。これによりAttributeErrorが発生します。
    c = b.method_a()  # 実行結果：AttributeError: 'list' object has no attribute 'method_a'
    # リストbの存在しないインデックス4を参照しようとします。これによりIndexErrorが発生します。
    a = b[4]  # 実行結果：IndexError: list index out of range
    # 0で除算しようとします。これによりZeroDivisionErrorが発生します。
    a = 10 / 0  # 実行結果：ZeroDivisionError: division by zero
    # 存在しないファイルを開こうとします。これによりFileNotFoundErrorが発生します。
    f = open('nonexistent_file.txt')  # 実行結果：FileNotFoundError: [Errno 2] No such file or directory: 'nonexistent_file.txt'
except ZeroDivisionError as e:
    # 除算エラー（ZeroDivisionError）が発生した場合の処理を記述します。
    import traceback
    traceback.print_exc()  # エラーのトレースバックを出力します。
    # print(e, type(e))
    pass
except IndexError as e:
    # インデックスエラー（IndexError）が発生した場合の処理を記述します。
    print('indexerror発生')  # 'indexerror発生'を出力します。
except FileNotFoundError as e:
    # ファイルが見つからないエラー（FileNotFoundError）が発生した場合の処理を記述します。
    print('FileNotFoundError発生')  # 'FileNotFoundError発生'を出力します。
except Exception as e:
    # 上記以外の全ての例外（Exception）が発生した場合の処理を記述します。
    print('Exception: ', e, type(e))  # 'Exception: 'と例外の内容、例外の型を出力します。
else:
    # tryブロックが例外を送出しなかった場合に実行されます。
    print('Else処理')  # 'Else処理'を出力します。
finally:
    # 例外の有無に関わらず最後に必ず実行されます。
    print('Finally処理')  # 'Finally処理'を出力します。

print('処理が完了しました。')  # '処理が完了しました。'を出力します。
