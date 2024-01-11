# 演習4
class CharacterAlreadyExistException(Exception): #【例外クラス】キャラクターがすでに存在する場合に発生する例外
    pass

class AllCharacters: #【クラス】全キャラクターを管理するクラス

    all_characters = [] # 全キャラクターのリスト
    alive_characters = [] # 生存しているキャラクターのリスト
    dead_characters = [] # 死亡したキャラクターのリスト

    @classmethod
    def character_append(cls, name): #【メソッド】キャラクターを追加する
        if name in cls.all_characters: # キャラクターがすでに存在する場合は例外を発生
            """ 
            if...inはPythonの文法で、ある要素がリストや辞書などのコレクション型の中に存在するかどうか
            を確認するために使用します。
            """
            raise CharacterAlreadyExistException('キャラクターはすでに存在します')
        cls.all_characters.append(name) # 全キャラクターのリストに追加
        cls.alive_characters.append(name) # 生存キャラクターのリストに追加
    
    @classmethod
    def character_delete(cls, name): #【メソッド】キャラクターを削除（死亡）する
        cls.dead_characters.append(name) # 死亡キャラクターのリストに追加
        cls.alive_characters.remove(name) # 生存キャラクターのリストから削除

class Character: #【クラス】キャラクターを表すクラス

    def __init__(self, name, hp, offense, defense): # 初期化メソッド
        AllCharacters.character_append(name) # キャラクターを全キャラクターリストに追加
        self.name = name # キャラクターの名前
        self.hp = hp # キャラクターのHP
        self.offense = offense # キャラクターの攻撃力
        self.defense = defense # キャラクターの防御力
    
    def attack(self, enemy, critical_point=1): #【メソッド】敵を攻撃する
        if self.hp <= 0: # 自分のHPが0以下の場合、攻撃できない
            print('キャラクターはすでに死んでいます')
            return
        attack_point = self.offense - enemy.defense # 攻撃力から敵の防御力を引いた値が攻撃点
        attack_point = 1 if attack_point <= 0 else attack_point # 攻撃点が0以下の場合、1にする
        enemy.hp -= attack_point * critical_point # 敵のHPから攻撃点を引く
        if enemy.hp <= 0: # 敵のHPが0以下の場合、敵を死亡リストに移動
            AllCharacters.character_delete(enemy.name)
    
    def critical_hit(self, enemy): #【メソッド】クリティカルヒット（攻撃力が2倍）
        self.attack(enemy, 2)

character_a = Character('A', 10, 5, 3) # キャラクターAを作成（HP:10, 攻撃力:5, 防御力:3）
character_b = Character('B', 8, 6, 2) # キャラクターBを作成（HP:8, 攻撃力:6, 防御力:2）

print(character_b.hp) # キャラクターBのHPを表示（結果：8）
character_a.critical_hit(character_b) # キャラクターAがキャラクターBにクリティカルヒット（結果：キャラクターBのHPが2になる）
print(character_b.hp) # キャラクターBのHPを表示（結果：2）
print(AllCharacters.alive_characters) # 生存キャラクターリストを表示（結果：['A', 'B']）
print(AllCharacters.dead_characters) # 死亡キャラクターリストを表示（結果：[]）
character_a.attack(character_b) # キャラクターAがキャラクターBを攻撃（結果：キャラクターBのHPが-1になり、死亡）
print(AllCharacters.alive_characters) # 生存キャラクターリストを表示（結果：['A']）
print(AllCharacters.dead_characters) # 死亡キャラクターリストを表示（結果：['B']）
character_b.attack(character_a) # 死亡したキャラクターBがキャラクターAを攻撃（結果：攻撃できない）
character_c = Character('A', 20, 5, 3) # キャラクターAがすでに存在するため、例外が発生
