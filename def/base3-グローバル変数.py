# 【グローバル変数の使用】

def printAnimal():
    global animal  # グローバル変数animalを関数内で使用するための宣言
    animal = 'Cat'  # グローバル変数animalに'Cat'を代入
    print('関数内animal = {}, id = {}'.format(animal, id(animal)))  # 関数内でのanimalの値とそのIDを出力

# animal = 'Dog'  # この行を有効にすると、関数呼び出し前のanimalの値が'Dog'になります※関数内のglobalは無効にすること。
printAnimal()  # printAnimal関数を呼び出し、結果として'関数内animal = Cat, id = (ID)'が出力されます
print('関数外animal = {}, id = {}'.format(animal, id(animal)))  # 関数外でのanimalの値とそのIDを出力。関数内で値が変更されているため、'関数外animal = Cat, id = (ID)'が出力されます
