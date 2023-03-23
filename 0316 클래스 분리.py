#클래스 분리
#Player 클래스
class Player:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def attack_monster(self, monster):
        print(f"{self.name}이(가) {monster.name}을(를) 공격했습니다.")
        damage = self.attack
        monster.defend(damage)

    def defend(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            print(f"{self.name}이(가) 죽었습니다.")
        else:
            print(f"{self.name}의 체력이 {self.hp} 남았습니다.")

#Monster 클래스
class Monster:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def attack_player(self, player):
        print(f"{self.name}이(가) {player.name}을(를) 공격했습니다.")
        damage = self.attack
        player.defend(damage)

    def defend(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            print(f"{self.name}이(가) 죽었습니다.")
        else:
            print(f"{self.name}의 체력이 {self.hp} 남았습니다.")

#Game 클래스
class Game:
    def __init__(self):
        self.player = None
        self.monster = None

    def create_player(self, name, hp, attack):
        self.player = Player(name, hp, attack)

    def create_monster(self, name, hp, attack):
        self.monster = Monster(name, hp, attack)

    def fight(self):
        while self.player.hp > 0 and self.monster.hp > 0:
            self.player.attack_monster(self.monster)
            if self.monster.hp <= 0:
                break
            self.monster.attack_player(self.player)
            if self.player.hp <= 0:
                break

game = Game()
game.create_player("Alice", 100, 10)
game.create_monster("Goblin", 50, 5)
game.fight()
