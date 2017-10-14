import random
def log(hero_hp,monster_hp):
    if hero_hp <0:
        hero_hp = 0
    if monster_hp < 0:
        monster_hp = 0
   print("Your hero has {} hp and the monster has {} hp".format(hero_hp,monster_hp))
def hero_attack():
    hit_chance = random.randint(1,100)
    if hit_chance <= 30:
        print("You missed!")
        return 0
    else:
        return random.randint(350,450)
def monster_attack():
    hit_chance = random.randint(1,100)
    if hit_chance <= 20:
        print("Monster missed!")
        return 0
    else:
        return random.randint(250,350)
def hero_defend():
    defend_chance = random.randint(1,100)
    if defend_chance <= 30:
        print("Defend failed!!!")
        return 1
    else:
        print("Defend success!!!")
        return 0
def item_heal(n):
    if n == 0:
        print("hero cannot heal (no healing potion left)")
        return 0
    heal = random.randint(350,700)
    print ("Hero's hp was restored by {} points\n{} healing potion left".format(heal,n-1))
    return heal
hero_hp = 1500; monster_hp = 2000; berserk_damage = 1
healing_potion = 2; berserk_potion = 1
while hero_hp > 0 and monster_hp > 0:
    log(hero_hp,monster_hp)
    inp = input("(A)ttack/(D)efend/(U)se item : ")
    if inp == "A":
        hero_atk = hero_attack()*berserk_damage
        if hero_atk != 0:
            print ("The monster loses {} hp".format(hero_atk))
        monster_hp-=hero_atk
    if inp == "U":
        inp_item = input("(H)ealing potion/(B)erserk potion : ")
        if inp_item == "H":
            hero_hp += item_heal(healing_potion)
            print("Your hero has {} hp".format(hero_hp))
            healing_potion -= 1
        elif inp_item == "B" and berserk_potion > 0:
            berserk_potion -= 1
            berserk_damage = 2
            print("Berserk mode : on")
    if berserk_damage == 2: 
        print ("The hero loses 150 hp from berserk mode")
        hero_hp -= 150
    defend = 1
    if inp == "D":
        defend = hero_defend()
    if monster_hp <= 0:
        break
    monster_atk = monster_attack()*defend
    if monster_atk != 0:
        print ("The hero loses {} hp".format(monster_atk))
    hero_hp-=monster_atk
log(hero_hp,monster_hp)
if hero_hp > 0:
    print ("Victory")
elif monster_hp > 0:
    print ("Defeat")
else:
    print ("Draw")

