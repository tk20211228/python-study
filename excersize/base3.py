# じゃんけん　勝った場合はループの外、負けた場合3回でループの外、あいこはあいこと表示

# 【敵の手を生成する関数】
def generate_enemy_hand():
    while True:  # 無限ループを作成します。この関数はジェネレータとして機能します。
        yield '1'  # グーを表します。
        yield '2'  # チョキを表します。
        yield '3'  # パーを表します。

# 【自分が勝つかどうかを判断する関数】
def is_win(my_hand, enemy_hand):
    if my_hand == '1' and enemy_hand == '2':  # グーはチョキに勝ちます。
        return True
    elif my_hand == '2' and enemy_hand == '3':  # チョキはパーに勝ちます。
        return True
    elif my_hand == '3' and enemy_hand == '1':  # パーはグーに勝ちます。
        return True
    return False  # 上記のいずれでもない場合は、自分の負けです。

# 【手の辞書】
hands_dict = {
    '1': 'グー',  # 1はグーを表します。
    '2': 'チョキ',  # 2はチョキを表します。
    '3': 'パー'  # 3はパーを表します。
}

from random import randint  # ランダムな数を生成するための関数をインポートします。

lose_count = 0  # 負けた回数をカウントする変数を初期化します。
enemy_hands = generate_enemy_hand()  # 敵の手を生成するジェネレータを初期化します。

# 【メインループ】
while True:  # 無限ループを作成します。
    my_hand = input('何を出しますか? 1:グー, 2:チョキ, 3:パー')  # ユーザーに入力を求めます。
    if my_hand not in ('1', '2', '3'):  # 入力が1, 2, 3のいずれでもない場合はエラーメッセージを表示します。
        print('間違った入力です')
        continue  # 次のループに進みます。
    enemy_hand = str(randint(1,3))  # 敵の手をランダムに選びます。
    print('あなたの出した手は: {}, 相手の出した手は: {}'.format(hands_dict.get(my_hand), hands_dict.get(enemy_hand)))  # 両者の手を表示します。
    if my_hand == enemy_hand:  # 両者の手が同じ場合はあいこです。
        print('あいこ')
    elif is_win(my_hand, enemy_hand):  # 自分が勝った場合は勝ちメッセージを表示します。
        print('あなたは勝ちました')
        break  # ループを抜けます。
    else:  # 自分が負けた場合は負けメッセージを表示します。
        lose_count += 1  # 負けた回数をカウントアップします。
        if lose_count == 3:  # 負けた回数が3回になった場合はゲームオーバーメッセージを表示します。
            print('あなたは負けました')
            break  # ループを抜けます。
        else:  # それ以外の場合は再チャレンジメッセージを表示します。
            print('あなたは負けました。再チャレンジ')
