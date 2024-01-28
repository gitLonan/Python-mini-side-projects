import random, time, sys, os
import time


behaviour_agressive = "agressive"
behaviour_protector = "protect"
behaviour_neutral = "neutral"


class Knight:
    def __init__(self,name, dmg=5, health=20):
        self.name = name
        self.health = health
        self.dmg = dmg
        self.pattern = ''
        self.action = 0

    def action_to_do(self):
        """Logic for what action does the knight do based on his behavior"""

        _num = random.randint(1,9)
        if self.pattern == behaviour_neutral:
            if _num in range(1,3+1):
                self.action = 1 #"attack"
            elif _num in range(4,6+1):
                self.action = 2 #"protect"
            elif _num in range(7,9+1):
                self.action = 3 #"rest"
        elif self.pattern == behaviour_agressive:
            if _num in range(1,4+1):
                self.action = 1
            elif _num in range(4,6+1):
                self.action = 2
            elif _num in range(7,9+1):
                self.action = 3
        elif self.pattern == behaviour_protector:
            if _num in range(1,2+1):
                self.action = 1
            elif _num in range(3,7+1):
                self.action = 2
            elif _num in range(8,9+1):
                self.action = 3
    


class Animation:
    def draw(player_1, player_2):
        head ="O"
        body = "-+-"
        legs = "/ \\"
        sword_prot = "|"
        sword_attack = "/"
        sword_attack_2 = "\\"
        os.system("cls")
        if player_1 == 1 and player_2 == 1: #should be 1 1
            stance_player = f"""
    {head:>5}{sword_attack:>3} {sword_attack_2:<1} {head:>2} 
    {body:>6}{sword_attack}   {sword_attack_2}{body:>2}
    {legs:>6}  {legs:>6}
                            """
            print(stance_player)
        if player_1 == 3 and player_2 == 3: #should be 3 3
            stance_player = f"""
    {head:>3}   {head:>8} 
    {body:>4}   {body:>8}
    {legs:>4}   {legs:>8}
                            """
            print(stance_player)
        if player_1 == 2 and player_2 == 2: #should be 2 2
            stance_player = f"""
    {head:>3}{sword_prot:>2}   {sword_prot:>4}{head:>2} 
    {body:>4}{sword_prot}   {sword_prot:>4}{body:>3}
    {legs:>4}{sword_prot}   {sword_prot:>4}{legs:>3}
                            """
            print(stance_player)
        if player_1 == 1 and player_2 == 2: #should be 1 2
            stance_player = f"""
    {head:>5}{sword_attack:>3}  {sword_prot:>2}{head:>2} 
    {body:>6}{sword_attack} {sword_prot:>4}{body:>3}   
    {legs:>6}   {sword_prot:>3}{legs:>3}
                            """
            print(stance_player)
        if player_1 == 1 and player_2 == 3: #should be 1 3
            stance_player = f"""
    {head:>5}{sword_attack:>3}  {head:>4} 
    {body:>6}{sword_attack} {body:>7}   
    {legs:>6}   {legs:>6}
                            """
            print(stance_player)        
        if player_1 == 2 and player_2 == 1: #should be 2 1
            stance_player = f"""
    {head:>3}{sword_prot:>2}   {sword_attack_2:<2} {head:>1} 
    {body:>4}{sword_prot}    {sword_attack_2}{body:>2}   
    {legs:>4}{sword_prot}   {legs:>5}
                            """
            print(stance_player)
        if player_1 == 2 and player_2 == 3: #should be 2 3
            stance_player = f"""
    {head:>3}{sword_prot:>2}   {head:>6} 
    {body:>4}{sword_prot}    {body:>6}   
    {legs:>4}{sword_prot}   {legs:>7}
                            """
            print(stance_player)
        if player_1 == 3 and player_2 == 1: #should be 3 1
            stance_player = f"""
    {head:>3}  {sword_attack_2:>3}{head:>3} 
    {body:>4}   {sword_attack_2:>2}{body:>3}
    {legs:>4}   {legs:>5}
                            """
            print(stance_player)
        if player_1 == 3 and player_2 == 2: #should be 3 2
            stance_player = f"""
    {head:>3}    {sword_prot:>5}{head:>2} 
    {body:>4}   {sword_prot:>5}{body:>3}
    {legs:>4}   {sword_prot:>5}{legs:>3}
                            """
            print(stance_player)



def behaviour_pattern(behaviour_agressive, behaviour_protector,behaviour_neutral, player_1, player_2):
    stringer = f"""
                In this little game your Knights will fight automatically
                They can choose between 'attack, defend, rest' 
                Choose what type of behavior you want your knight to have
                        1. Agressive
                        2. Protector
                        3. Neutral
                sir {player_1.name} is on the left
                sir {player_2.name} is on the right
                """
    print(stringer)
    while True:
        p_1 = input("Choose player 1: ")
        p_2 = input("Choose player 2: ")
        try:
            p_1 = int(p_1)
            p_2 = int(p_2)
        except:
            continue
        if 0 < p_1 < 4 and 0 < p_2 < 4:
            break 
    if p_1 == 1: player_1.pattern = behaviour_agressive
    elif p_1 == 2: player_1.pattern = behaviour_protector
    else: player_1.pattern = behaviour_neutral

    if p_2 == 1: player_2.pattern = behaviour_agressive
    elif p_2 == 2: player_2.pattern = behaviour_protector
    else: player_2.pattern = behaviour_neutral

    return p_1, p_2


def name_creation():
    player_1 = input("Type your full Knights name ---Player 1---- : ")
    player_2 = input("Type your full Knights name ---Player 2---- : ")
    yes = input("Are you satisfied (yes or no)")
    if yes.lower() == "yes" and player_1 != player_2: #shoud be yes
        return (player_1, player_2)
    else:
        print("Name not valid")
        name_creation()
        return (player_1, player_2)

def battle(player_1, player_2):
    if player_1.action == 1 and player_2.action == 1:
        player_1.health -= player_2.dmg-2
        player_2.health -= player_1.dmg-2
    elif player_1.action == 1 and player_2.action == 2 or player_1.action == 2 and player_2.action == 1:
        pass
    elif player_1.action == 1 and player_2.action == 3:
        player_2.health -= player_1.dmg
    elif player_1.action == 3 and player_2.action == 1:
        player_1.health -= player_2.dmg

def health_printing(player_1, player_2):
    print(f"sir {player_1.name} health: {player_1.health}")
    print(f"sir {player_2.name} health: {player_2.health}")

def end_of_battle(player_1, player_2):
    if player_1.health <= 0 and player_2.health > 0:
        os.system("cls")
        print(f"""  
                    
                    sir {player_2.name} has won the duel
                    
                    """)
        return True
    elif player_2.health <= 0 and player_1.health > 0:
        os.system("cls")
        print(f"""
                    
                    sir {player_1.name} has won the duel
                    
                    """)
        return True
    elif player_2.health <= 0 and player_1.health <= 0:
        os.system("cls")
        print("""
                    
                    Both Knights have died honorably
              
              """)
        return True

def main(behaviour_agressive, behaviour_protector,behaviour_neutral):
    player_name_1, player_name_2 = name_creation()
    
    player_1_dmg = 5
    player_2_dmg = 5

    player_1 = Knight(player_name_1, player_1_dmg)
    player_2 = Knight(player_name_2, player_2_dmg)

    player_pattern_1, player_pattern_2 = behaviour_pattern(behaviour_agressive, behaviour_protector,behaviour_neutral, player_1, player_2)
    print(player_1.pattern, player_2.pattern)


    while True:
        player_1.action_to_do()
        player_2.action_to_do()
        #print(player_1.action, player_2.action, end="")
        Animation.draw(player_1.action, player_2.action)
        battle(player_1, player_2)
        health_printing(player_1, player_2)
        bool  = end_of_battle(player_1, player_2)
        if bool == True:
            break
        time.sleep(1)
    
    sys.exit()


main(behaviour_agressive,behaviour_protector, behaviour_neutral)