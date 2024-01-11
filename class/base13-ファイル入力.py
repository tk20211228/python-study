#【ファイル入力の学習】

file_path = 'resources/input.csv'  # ファイルパスを指定します
f = open(file_path, mode='r', encoding='utf-8')  # ファイルを開きます

# line = f.read() # 中身全体を読み込む方法
# print(line)

# lines = f.readlines() # ファイルの全行をリストとして読み込む方法
# print(lines)
# for x in lines:
#     print(x.rstrip('\n')) # 行末の改行を削除して出力

# line = f.readline() # ファイルの一行を読み込む方法
while (line := f.readline()):  # ファイルの全行を一行ずつ読み込む方法
    print(line.rstrip('\n'))  # 行末の改行を削除して出力
    # line = f.readline()

f.close()  # ファイルを閉じます
# →　メモリを食う。ほかの処理でファイルに開けない
# withを使うと、ブロックが終了した時点で自動的にファイルを閉じてくれます
with open(file_path, mode='r', encoding='utf-8') as f:
    lines = f.readlines()  # ファイルの全行をリストとして読み込みます
    print(lines)  # ファイルの内容を出力します

# ファイルが閉じられているので、これはエラーを引き起こします
print(f.read())

"""
このコードはPythonでのファイル入力の基本的な使い方を示しています。
ファイルを開く、読み込む、閉じるという基本的な操作を学ぶことができます。
また、with文を使うと、ファイルを自動的に閉じることができるため、リソースの管理が容易になります。
"""