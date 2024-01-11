# 【ファイル操作】
# ファイル出力、追記


file_path = 'resources/output.csv'  # 出力先のファイルパスを指定します。

# ファイルを書き込みモードで開きます。エンコーディングは'utf-8'、改行コードは'\n'を指定します。
f = open(file_path, mode='w', encoding='utf-8', newline='\n')
f.write('あああ\nいいい')  # ファイルに文字列を書き込みます。
f.close()  # ファイルを閉じます。これは重要なステップで、これを忘れるとデータが正しく保存されない場合があります。

# ファイルを追記モードで開きます。エンコーディングは'utf-8'、改行コードは'\n'を指定します。
with open(file_path, mode='a', encoding='utf-8', newline='\n') as f:
    list_a = [
        ['A', 'B', 'C'],
        ['あ', 'い', 'う']
    ]
    # リストの各要素をファイルに書き込みます。各要素はカンマで区切られます。
    for x in list_a:
        f.write('\n')  # 新しい行を開始します。
        f.write(','.join(x))  # リストの要素をカンマで結合し、その結果をファイルに書き込みます。
    # f.writelines(list_a[0])

