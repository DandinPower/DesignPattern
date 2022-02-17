class Skill:

    def __init__(self,name):
        self.name = name 

    def attack():
        pass

class Charge(Skill):

    def __init__(self,name):
        self.name = name 
    
    def attack(self,attackPlayer,attackedPlayer):
        damage = attackedPlayer.strength - attackedPlayer.defense
        print(f'{attackPlayer.name} 使出了{self.name} 造成了{damage}點傷害')
        return damage
        
class MentalFire(Skill):

    def __init__(self,name):
        self.name = name 
    
    def attack(self,attackPlayer,attackedPlayer):
        if (attackPlayer.mp >= 5):
            attackPlayer.mp = attackedPlayer.mp - 5 
            damage = 2 * attackPlayer.wisdom
            print(f'{attackPlayer.name} 使出了{self.name} 造成了{damage}點傷害')
        else:
            print(f'{attackPlayer.name} 魔力沒了 造成了{damage}點傷害')
            damage = 0
        return damage


class Hero:

    def __init__(self,name,hp,mp,strength,wisdom,defense):
        self.name = name
        self.hp = hp 
        self.mp = mp 
        self.strength = strength
        self.wisdom = wisdom 
        self.defense = defense
        self.skill = None

    def addSkill(self,name):
        if (name == '衝撞'):
            self.skill = Charge(name)
        else:
            self.skill = MentalFire(name)

    def attack(self, opponent):
        damage = self.skill.attack(self,opponent)
        return damage

    def getAttack(self,damage):
        self.hp = self.hp - damage
        print(f'{self.name}受到了 {damage}點傷害')
        print(f'{self.name} 血量剩餘{self.hp}')

class Game:

    def __init__(self):
        self.player1 = None
        self.player2 = None 
        self.round = 0 
        self.start = False 
    
    def setPlayer1(self,player):
        self.player1 = player
    
    def setPlayer2(self,player):
        self.player2 = player 

    def checkHp(self):
        if (self.player1.hp <= 0):
            print(f'{self.player1.name} lose')
            print(f'{self.player2.name} win')
            self.start = False
        elif(self.player2.hp <= 0):
            print(f'{self.player1.name} win')
            print(f'{self.player2.name} lose')
            self.start = False

    def startGame(self):
        self.start = True 
        while(self.start):
            if (self.round % 2 == 0):
                damage = self.player1.attack(self.player2)
                self.player2.getAttack(damage) 
            elif (self.round % 2 == 1):
                damage = self.player2.attack(self.player1)
                self.player1.getAttack(damage) 
            self.round += 1
            self.checkHp()

def main():
    player1 = Hero('player1',100,50,10,10,5)
    player1.addSkill('衝撞')
    player2 = Hero('player2',100,50,10,10,5)
    player2.addSkill('聖火')
    myGame = Game()
    myGame.setPlayer1(player1)
    myGame.setPlayer2(player2)
    myGame.startGame()

if __name__ == "__main__":
    main()