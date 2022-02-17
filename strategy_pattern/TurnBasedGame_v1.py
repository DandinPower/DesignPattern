class Skill:

    def __init__(self,name,skillType):
        self.name = name 
        self.type = skillType

    def attack():
        pass

    def getType(self):
        return self.type
        
class Hero:

    def __init__(self,name,hp,mp,strength,wisdom,defense):
        self.name = name
        self.hp = hp 
        self.mp = mp 
        self.strength = strength
        self.wisdom = wisdom 
        self.defense = defense
        self.skill = []

    def addSkill(self,name,type):
        self.skill.append(Skill(name,type))

    def attack(self,index,opponentDefense):
        skill = self.skill[index] 
        if (skill.getType() == '物理'):
            damage = self.strength - opponentDefense
            print(f'{self.name} 使出了{skill.name} 造成了{damage}的{skill.getType()}傷害')
        elif (skill.getType() == '魔法'):
            if (self.mp >= 5):
                self.mp -= 5
                damage = self.wisdom * 2
                print(f'{self.name} 使出了{skill.name} 造成了{damage}的{skill.getType()}傷害')
            else:
                damage = 0
                print(f'{self.name}魔力不足 造成了{damage}的{skill.getType()}傷害')
        else:
            damage = 0
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
                damage = self.player1.attack(0,self.player2.defense)
                self.player2.getAttack(damage) 
            elif (self.round % 2 == 1):
                damage = self.player2.attack(0,self.player1.defense)
                self.player1.getAttack(damage) 
            self.round += 1
            self.checkHp()

def main():
    player1 = Hero('player1',100,50,10,10,5)
    player1.addSkill('衝撞','物理')
    player2 = Hero('player2',100,50,10,10,5)
    player2.addSkill('聖火','魔法')
    myGame = Game()
    myGame.setPlayer1(player1)
    myGame.setPlayer2(player2)
    myGame.startGame()

if __name__ == "__main__":
    main()