import random
class Attack:
    def __init__(self, name, type,attack_type, power, accuracy,priority):
        self.name = name#Attack name – something just to identify the attack
        self.type = type#Attack typing, which can be Normal, Fire, Water, etc.
        self.attack_type = attack_type
        #Physical or Special, depending on whether the attack uses the Pokémon's Attack or Special Attack stat
        self.power = power#Attack power, which is the base damage it deals
        self.accuracy = accuracy
        #Certain attacks can miss, such as Hyper Beam, which has 90% accuracy
        self.priority = priority 
    #Moves like Quick Attack have higher priority than normal moves

#class status_attack:
#Maybe i will add status attacks like Toxic, Thunder Wave, etc but for now i will just make a simulator that only use damage attacks

class Pokemon:
    def __init__(self, name,types, stats, attacks):
        self.name = name #Name of the Pokémon, which is used to identify the Pokémon
        self.types = types 
        #Pokémon types can be Normal, Fire, Water, etc. Some Pokémon have more than one type—for example, Bulbasaur is both Grass and Poison type. This is used to calculate the effectiveness of attacks.
        self.hp = stats["hp"] 
        #A Pokémon's HP, which represents its health. When its HP reaches 0, the Pokémon faints.
        self.attack = stats["attack"] 
        #Pokémon's Attack, which is used to calculate the damage of physical attacks
        self.defence = stats["defence"] 
        #defence of the Pokémon, used to calculate the damage it takes from physical attacks
        self.speed = stats["speed"] 
        #Pokémon speed, which is used to determine which Pokémon attacks first
        self.sp_attack = stats["sp_attack"] 
        #Pokémon's special attack, which is used to calculate the damage of special attacks
        self.sp_defence = stats["sp_defence"] 
        #A Pokémon's Special defence, which is used to calculate the damage it takes from special attacks
        self.attacks = attacks 
        #List of Pokémon moves—the attacks a Pokémon can use in battle. Here, we’ll use a `.choice` method to select up to 6 moves, with the selection being random.
def pokemon_accuracy(attack):
    accuracy = random.randint(1,100)
    if accuracy <= attack.accuracy:
        return True
    else:
        return False
#This function make the battle, it simulate 500 battle bitween pokemons so i take 1 pokemon anda another they will fight 500 times, a pokemon cant battle him self
def pokemon_damage(attacker, defender, attack):
    #global attacker_damage
    if attack.attack_type == "Physical": #See if the attack is physical or special and calculate the damage accordingly
        attacker_damage = ((((2*100/5)+2)*attack.power*((attacker.attack)/defender.defence))/50)+2 #calculate the damage of the attack based on the attacker's stats and the defender's stats
        if attack.type in attacker.types:
            attacker_damage = attacker_damage * 1.5 #STAB (Same Type Attack Bonus) is a 1.5x multiplier applied to attacks that match the Pokémon's type
            multiplier = 1
            for type in defender.types:
                multiplier *= pokemon_types[attack.type][type]#Calculate the effectiveness of the attack based on the defender's types
            if random.randint(1,24)==1:
                            multiplier *=1.5
            attacker_damage = attacker_damage*multiplier
        else:
            multiplier = 1
            for type in defender.types:
                multiplier *= pokemon_types[attack.type][type]
            if random.randint(1,24)==1:
                multiplier *=1.5
            attacker_damage = attacker_damage*multiplier
    else:
        attacker_damage = ((((2*100/5)+2)*attack.power*((attacker.sp_attack)/defender.sp_defence))/50)+2 #calculate the damage of the attack based on the attacker's stats and the defender's stats
        if attack.type in attacker.types:
            attacker_damage = attacker_damage * 1.5 #STAB (Same Type Attack Bonus) is a 1.5x multiplier applied to attacks that match the Pokémon's type
            multiplier = 1
            for type in defender.types:
                multiplier *= pokemon_types[attack.type][type]#Calculate the effectiveness of the attack based on the defender's types
            if random.randint(1,24)==1:
                            multiplier *=1.5
            attacker_damage = attacker_damage*multiplier
        else:
            multiplier = 1
            for type in defender.types:
                multiplier *= pokemon_types[attack.type][type]
            if random.randint(1,24)==1:
                            multiplier *=1.5
            attacker_damage = attacker_damage*multiplier
    return attacker_damage
#In this function pokemon will simulate 500 battle with eatch other, first e calculate de hp of both pokemon and them e select the attack for both, after the attack is selecter e check for priority attacks, else e check for speed diference, if the pokemons have the same speed i choose 1 randomly, an them i use the function pokemon_damage to calculate the pokemon damage
def batalha(pokemon1, pokemon2):
    #global pokemon1_hp, pokemon2_hp, pokemon1_hp_battle, pokemon2_hp_battle,pokemon1_attack,pokemon2_attack,pokemon1_damage,pokemon2_damage, pokemon1_types, pokemon2_types, pokemon1_victories I think this is not necessary because i will return the pokemon1_victories and i will use it to calculate the percentage of victories of the pokemon1
    battle = 0
    pokemon1_victories = 0 
    pokemon1_hp = (((2 * pokemon1.hp + 31+(252/4)) * 100) // 100 + 100 + 10)
    pokemon2_hp = (((2 * pokemon2.hp + 31+(252/4)) * 100) // 100 + 100 + 10)
    pokemon1_hp_battle = pokemon1_hp
    pokemon2_hp_battle = pokemon2_hp
    while battle < 500:
        pokemon1_hp_battle = pokemon1_hp
        pokemon2_hp_battle = pokemon2_hp
        while ((pokemon1_hp_battle>0)and(pokemon2_hp_battle>0)):
            pokemon1_attack = random.choice(pokemon1.attacks)
            pokemon2_attack = random.choice(pokemon2.attacks)
            if pokemon1_attack.priority==pokemon2_attack.priority:
                if pokemon1.speed > pokemon2.speed:
                    while True:
                        if pokemon1_hp_battle>0:
                            if pokemon_accuracy(pokemon1_attack): #Checks for accuracy also
                                pokemon1_damage = pokemon_damage(pokemon1,pokemon2,pokemon1_attack)
                                pokemon2_hp_battle -= pokemon1_damage
                            else:
                                pokemon1_damage = 0
                        if pokemon2_hp_battle<=0:
                            battle +=1
                            pokemon1_victories+=1
                            break
                        
                        if pokemon2_hp_battle>0: #If pokemon still alive
                            if pokemon_accuracy(pokemon2_attack):
                                pokemon2_damage = pokemon_damage(pokemon2,pokemon1,pokemon2_attack)
                                pokemon1_hp_battle -= pokemon2_damage
                            else:
                                pokemon2_damage = 0

                        if pokemon1_hp_battle<=0:
                            battle +=1
                            break

                if pokemon1.speed < pokemon2.speed:
                    while True:
                        if pokemon2_hp_battle>0:
                            if pokemon_accuracy(pokemon2_attack):
                                pokemon2_damage = pokemon_damage(pokemon2,pokemon1,pokemon2_attack)
                                pokemon1_hp_battle -= pokemon2_damage
                            else:
                                pokemon2_damage = 0
                        if pokemon1_hp_battle<=0:
                            battle +=1
                            break
                        
                        if pokemon1_hp_battle>0:
                            if pokemon_accuracy(pokemon1_attack):
                                pokemon1_damage = pokemon_damage(pokemon1,pokemon2,pokemon1_attack)
                                pokemon2_hp_battle -= pokemon1_damage
                            else:
                                pokemon1_damage = 0 

                        if pokemon2_hp_battle<=0:
                            battle +=1
                            pokemon1_victories   += 1
                            break
                
                if pokemon1.speed == pokemon2.speed:
                    escolha = random.choice([1,2])
                    if escolha == 1:
                        while True:
                            if pokemon1_hp_battle>0:
                                if pokemon_accuracy(pokemon1_attack):
                                    pokemon1_damage = pokemon_damage(pokemon1,pokemon2,pokemon1_attack)
                                    pokemon2_hp_battle -= pokemon1_damage
                                else:
                                    pokemon1_damage = 0
                            if pokemon2_hp_battle<=0:
                                battle +=1
                                pokemon1_victories+= 1
                                break
                            
                            if pokemon2_hp_battle>0:
                                if pokemon_accuracy(pokemon2_attack):
                                    pokemon2_damage = pokemon_damage(pokemon2,pokemon1,pokemon2_attack)
                                    pokemon1_hp_battle -= pokemon2_damage
                                else:
                                    pokemon2_damage = 0
    
                            if pokemon1_hp_battle<=0:
                                battle +=1
                                break
                    else:
                        while True:
                            if pokemon2_hp_battle>0:
                                if pokemon_accuracy(pokemon2_attack):
                                    pokemon2_damage = pokemon_damage(pokemon2,pokemon1,pokemon2_attack)
                                    pokemon1_hp_battle -= pokemon2_damage
                                else:
                                    pokemon2_damage = 0
                            if pokemon1_hp_battle<=0:
                                battle +=1
                                break
                            
                            if pokemon1_hp_battle>0:
                                if pokemon_accuracy(pokemon1_attack):
                                    pokemon1_damage = pokemon_damage(pokemon1,pokemon2,pokemon1_attack)
                                    pokemon2_hp_battle -= pokemon1_damage
                                else:
                                    pokemon1_damage = 0

                            if pokemon2_hp_battle<=0:
                                battle +=1
                                pokemon1_victories+= 1
                                break
                #dar dano
            if pokemon1_attack.priority > pokemon2_attack.priority:
                while True:
                    if pokemon1_hp_battle>0:
                        pokemon1_damage = pokemon_damage(pokemon1,pokemon2,pokemon1_attack)
                        pokemon2_hp_battle -= pokemon1_damage
                    if pokemon2_hp_battle<=0:
                        battle +=1
                        pokemon1_victories += 1
                        break
                    
                    if pokemon2_hp_battle>0:
                        pokemon2_damage = pokemon_damage(pokemon2,pokemon1,pokemon2_attack)
                        pokemon1_hp_battle -= pokemon2_damage

                    if pokemon1_hp_battle<=0:
                        battle +=1
                        break
                
            if pokemon2_attack.priority > pokemon1_attack.priority:
                while True:
                    if pokemon2_hp_battle>0:
                        pokemon2_damage = pokemon_damage(pokemon2,pokemon1,pokemon2_attack)
                        pokemon1_hp_battle -= pokemon2_damage
                    if pokemon1_hp_battle<=0:
                        battle +=1
                        break
                    
                    if pokemon1_hp_battle>0:
                        pokemon1_damage = pokemon_damage(pokemon1,pokemon2,pokemon1_attack)
                        pokemon2_hp_battle -= pokemon1_damage

                    if pokemon2_hp_battle<=0:
                        battle +=1
                        pokemon1_victories += 1
                        break
    return(pokemon1_victories)
#that’s basically where I look for weaknesses and super-effective attacks
pokemon_types = {
    "Normal":{
            "Normal": 1,
            "Fighting": 1,
            "Fly": 1,
            "Poison": 1,
            "Ground": 1,
            "Rock": 0.5,
            "Bug": 1,
            "Ghost": 0,
            "Steel": 0.5,
            "Fire": 1,
            "Water": 1,
            "Grass": 1,
            "Electric": 1,
            "Psychic": 1,
            "Ice": 1,
            "Dragon": 1,
            "Dark": 1,
            "Fairy": 1,
        },
    "Fighting":{
            "Normal": 2,
            "Fighting": 1,
            "Fly": 0.5,
            "Poison": 0.5,
            "Ground": 1,
            "Rock": 2,
            "Bug": 0.5,
            "Ghost": 0,
            "Steel": 2,
            "Fire": 1,
            "Water": 1,
            "Grass": 1,
            "Electric": 1,
            "Psychic": 0.5,
            "Ice": 2,
            "Dragon": 1,
            "Dark": 2,
            "Fairy": 0.5,
        },
    "Fly":{
            "Normal": 1,
            "Fighting": 2,
            "Fly": 1,
            "Poison": 1,
            "Ground": 1,
            "Rock": 0.5,
            "Bug": 2,
            "Ghost": 1,
            "Steel": 0.5,
            "Fire": 1,
            "Water": 1,
            "Grass": 2,
            "Electric": 0.5,
            "Psychic": 1,
            "Ice": 1,
            "Dragon": 1,
            "Dark": 1,
            "Fairy": 1,
         },
    "Poison":{
            "Normal": 1,
             "Fighting": 1,
             "Fly": 1,
             "Poison": 0.5,
             "Ground": 0.5,
             "Rock": 0.5,
             "Bug": 1,
             "Ghost": 0.5,
             "Steel": 0,
             "Fire": 1,
             "Water": 1,
             "Grass": 2,
             "Electric": 1,
             "Psychic": 1,
             "Ice": 1,
             "Dragon": 1,
             "Dark": 1,
             "Fairy": 2,
        },
    "Ground":{
            "Normal": 1,
            "Fighting": 1,
            "Fly": 0,
            "Poison": 2,
            "Ground": 1,
            "Rock": 2,
            "Bug": 0.5,
            "Ghost": 1,
            "Steel": 2,
            "Fire": 2,
            "Water": 1,
            "Grass": 0.5,
            "Electric": 1,
            "Psychic": 1,
            "Ice": 1,
            "Dragon": 1,
            "Dark": 1,
            "Fairy": 1,
        },
    "Rock":{
            "Normal": 1,
            "Fighting":0.5,
            "Fly": 2,
            "Poison": 1,
            "Ground": 0.5,
            "Rock": 1,
            "Bug": 2,
            "Ghost": 1,
            "Steel": 0.5,
            "Fire": 2,
            "Water": 1,
            "Grass": 1,
            "Electric": 1,
            "Psychic": 1,
            "Ice": 2,
            "Dragon": 1,
            "Dark": 1,
            "Fairy": 1,
        },
    "Bug":{
            "Normal": 1,
            "Fighting": 0.5,
            "Fly": 0.5,
            "Poison": 0.5,
            "Ground": 1,
            "Rock": 0.5,
            "Bug": 1,
            "Ghost": 0.5,
            "Steel": 0.5,
            "Fire": 0.5,
            "Water": 1,
            "Grass": 2,
            "Electric": 1,
            "Psychic": 2,
            "Ice": 1,
            "Dragon": 1,
            "Dark": 2,
            "Fairy": 0.5,
        },
    "Ghost":{
            "Normal": 0,
            "Fighting": 1,
            "Fly": 1,
            "Poison": 1,
            "Ground": 1,
            "Rock": 1,
            "Bug": 1,
            "Ghost": 2,
            "Steel": 0.5,
            "Fire": 1,
            "Water": 1,
            "Grass": 1,
            "Electric": 1,
            "Psychic": 2,
            "Ice": 1,
            "Dragon": 1,
            "Dark": 0.5,
            "Fairy": 1,
        },
    "Steel":{
            "Normal": 1,
            "Fighting": 1,
            "Fly": 1,
            "Poison": 1,
            "Ground": 1,
            "Rock": 2,
            "Bug": 1,
            "Ghost": 1,
            "Steel": 0.5,
            "Fire": 0.5,
            "Water": 0.5,
            "Grass": 1,
            "Electric": 0.5,
            "Psychic": 1,
            "Ice": 2,
            "Dragon": 1,
            "Dark": 1,
            "Fairy": 2,
        },
    "Fire":{
            "Normal": 1,
            "Fighting": 1,
            "Fly": 1,
            "Poison": 1,
            "Ground": 1,
            "Rock": 0.5,
            "Bug": 2,
            "Ghost": 1,
            "Steel": 2,
            "Fire": 0.5,
            "Water": 0.5,
            "Grass": 2,
            "Electric": 1,
            "Psychic": 1,
            "Ice": 2,
            "Dragon": 0.5,
            "Dark": 1,
            "Fairy": 1,
        },
    "Water":{
            "Normal": 1,
            "Fighting": 1,
            "Fly": 1,
            "Poison": 1,
            "Ground": 2,
            "Rock": 2,
            "Bug": 1,
            "Ghost": 1,
            "Steel": 1,
            "Fire": 2,
            "Water": 0.5,
            "Grass": 0.5,
            "Electric": 1,
            "Psychic": 1,
            "Ice": 1,
            "Dragon": 0.5,
            "Dark": 1,
            "Fairy": 1,
        },
    "Grass":{
            "Normal": 1,
            "Fighting": 1,
            "Fly": 0.5,
            "Poison": 0.5,
            "Ground": 2,
            "Rock": 2,
            "Bug": 0.5,
            "Ghost": 1,
            "Steel": 0.5,
            "Fire": 0.5,
            "Water": 2,
            "Grass": 0.5,
            "Electric": 1,
            "Psychic": 1,
            "Ice": 1,
            "Dragon": 0.5,
            "Dark": 1,
            "Fairy": 1,
        },
    "Electric":{
            "Normal": 1,
            "Fighting": 1,
            "Fly": 2,
            "Poison": 1,
            "Ground": 0,
            "Rock": 1,
            "Bug": 1,
            "Ghost": 1,
            "Steel": 1,
            "Fire": 1,
            "Water": 2,
            "Grass": 0.5,
            "Electric": 0.5,
            "Psychic": 1,
            "Ice": 1,
            "Dragon": 0.5,
            "Dark": 1,
            "Fairy": 1,
        },
    "Psychic":{
            "Normal": 1,
            "Fighting": 2,
            "Fly": 1,
            "Poison": 2,
            "Ground": 1,
            "Rock": 1,
            "Bug": 1,
            "Ghost": 1,
            "Steel": 0.5,
            "Fire": 1,
            "Water": 1,
            "Grass": 1,
            "Electric": 1,
            "Psychic": 0.5,
            "Ice": 1,
            "Dragon": 1,
            "Dark": 0,
            "Fairy": 1,
        },
    "Ice":{
            "Normal": 1,
            "Fighting": 1,
            "Fly": 2,
            "Poison": 1,
            "Ground": 1,
            "Rock": 1,
            "Bug": 1,
            "Ghost": 1,
            "Steel": 0.5,
            "Fire": 0.5,
            "Water": 0.5,
            "Grass": 2,
            "Electric": 1,
            "Psychic": 1,
            "Ice": 0.5,
            "Dragon": 2,
            "Dark": 1,
            "Fairy": 1,
        },
    "Dragon":{
            "Normal": 1,
            "Fighting": 1,
            "Fly": 1,
            "Poison": 1,
            "Ground": 1,
            "Rock": 1,
            "Bug": 1,
            "Ghost": 1,
            "Steel": 0.5,
            "Fire": 1,
            "Water": 1,
            "Grass": 1,
            "Electric": 1,
            "Psychic": 1,
            "Ice": 1,
            "Dragon": 2,
            "Dark": 1,
            "Fairy": 0,
        },
    "Dark":{
            "Normal": 1,
            "Fighting": 0.5,
            "Fly": 1,
            "Poison": 1,
            "Ground": 1,
            "Rock": 1,
            "Bug": 1,
            "Ghost": 2,
            "Steel": 1,
            "Fire": 1,
            "Water": 1,
            "Grass": 1,
            "Electric": 1,
            "Psychic": 2,
            "Ice": 1,
            "Dragon": 1,
            "Dark": 0.5,
            "Fairy": 0.5,
        },
    "Fairy":{
            "Normal": 1,
            "Fighting": 2,
            "Fly": 1,
            "Poison": 0.5,
            "Ground": 1,
            "Rock": 1,
            "Bug": 1,
            "Ghost": 1,
            "Steel": 0.5,
            "Fire": 0.5,
            "Water": 1,
            "Grass": 1,
            "Electric": 1,
            "Psychic": 1,
            "Ice": 1,
            "Dragon": 2,
            "Dark": 2,
            "Fairy": 1,
        },   
}

#Create the attacks , name, type, Physical or special could be stats but im lazy to do that, power , accuracy, priority
#Attacks like Hyper beam have been Reworked because i dont wanna do the mechanic that makes the pokemon who uses Hyper Beam rest for 1 turn :)
#Normal Attacks
tackel = Attack("Tackel", "Normal", "Physical", 40, 100, 0)
bodyslam = Attack("Body Slam", "Normal", "Physical", 85, 100, 0)
quickattack = Attack("Quick Attack", "Normal", "Physical", 40, 100, 1)
extremespeed = Attack("Extreme Speed", "Normal", "Physical", 80, 100, 2)
slash = Attack("Slash", "Normal", "Physical", 70, 100, 0)
scratch = Attack("Scratch", "Normal", "Physical", 40, 100, 0)
hyperbeam = Attack("Hyper Beam", "Normal", "Special", 120 , 90, -1) 
hypervoice = Attack("Hyper Voice", "Normal", "Special", 90, 100, 0)
hyperfang = Attack("Hyper Fang", "Normal", "Physical", 80, 90, 0)
razorwind = Attack("Razor Wind", "Normal", "Special", 80, 100, -1)
triattack = Attack("Tri Attack", "Normal", "Special", 90, 100, 0)
uproar = Attack("Uproar", "Normal", "Special", 90, 100, 0)
#Fighting Attacks
aurasphere = Attack("Aura_Sphere", "Fighting", "Special", 80, 100,0)
brickbreak = Attack("Brick Break", "Fighting", "Physical", 75, 100, 0)
closecombat = Attack("Close Combat", "Fighting", "Physical", 110, 100, 0)
focusblast = Attack("Focus Blast", "Fighting", "Special", 120, 70,0)
machpunch = Attack("Mach Punch", "Fighting", "Physical", 40, 100, 1)
sacredsword = Attack("Sacred Sword", "Fighting", "Physical", 90, 100, 0)
vacuumwave = Attack("Vacuum Wave", "Fighting", "Special", 40, 100, 1)
collisioncourse = Attack("Collision Course", "Fighting","Physical", 100,100,0)
hammerarm = Attack("Hammer Arm", "Fighting", "Physical", 100,90,0)
rochsmash = Attack("Rock Smash", "Fighting", "Physical", 40, 100, 0)
superpower = Attack("Super Power", "Fighting", "Physical", 125, 100, 0)
vitalthrow = Attack("Vital Throw","Fighting", "Physical", 70, 100, -5)
#Fly Attacks
wingattack = Attack("Wing Attack","Fly","Physical", 60, 100, 0)
pluck = Attack("Pluck", "Fly", "Physical", 65, 100, 0)
peck = Attack("Peck", "Fly", "Physical", 35, 100,0)
hurricane = Attack("Hurricane", "Fly", "Special", 110, 70, 0)
acrobatics = Attack("Acrobatics", "Fly", "Physical", 55, 100, 0)
aeroblast = Attack("Aeroblast", "Fly", "Special", "105", 90, 0)
airslash = Attack("Air Slash", "Fly", "Special", 80, 95, 0)
chatter = Attack("Chatter","Fly", "Special", 80, 100, 0)
aircutter = Attack("Air Cutter", "Fly","Special",65,95,0)
floatyfall = Attack("Floaty Fall", "Fly","Physical", 95, 95,0)
breakwind = Attack("Break Wind", "Fly","Special", 100, 85, 0)
bravebird = Attack("Brave Bird", "Fly","Physical", 130, 100, 0)
#Poison Attacks
venoshock = Attack("Venoshock", "Poison", "Special", 65, 100, 0)
smog = Attack("Smog","Poison", "Special", 30, 80, 0)
sludgewave = Attack("Sludge Wave", "Poison", "Special", 95, 100, 0)
sludgebomb = Attack("Sludge Bomb", "Poison", "Special", 100, 100, 0)
sludge = Attack("Sludge", "Poison", "Special", 70, 100, 0)
poisontail = Attack("Poison Tail", "Poison", "Physical", 60, 100, 0)
poisonsting = Attack("Poison Sting", "Poison", "Physical", 30, 100, 0)
poisonjab = Attack("Poison Jab", "Poison", "Physical", 85, 100, 0)
poisonfang = Attack("Poison Fang", "Poison", "Physical", 60, 100, 0)
noxioustorque = Attack("Noxious Torque", "Poison", "Physical", 110, 100, 0)
gunkshot = Attack("Gunk Shot", "Poison", "Physical", 130, 80,0)
acid = Attack("Acid", "Poison", "Special", 40, 100, 0)
#Ground Attacks
boneclub = Attack("Bone Club", "Ground", "Physical", 70, 85, 0)
bulldoze = Attack("Bulldoze", "Ground","Physical", 70, 100, 0)
drillrun = Attack("Drill Run", "Ground", "Physical", 85, 95, 0)
earthpower = Attack("Earth Power", "Ground", "Special", 90, 100, 0)
earthquake = Attack("Earthquake", "Ground", "Physical", 120, 100, 0)
mudbomb = Attack("Mud Bomb", "Ground", "Special", 65,85,0)
mudshot = Attack("Mud Shot", "Ground", "Special", 55,95,0)
highhorsepower = Attack("High Horsepower", "Ground", "Physical", 95, 95, 0)
headlongrush = Attack("Headlong Rush", "Ground", "Physical", 120, 95, 0)
thousandwaves = Attack("Thousand Waves", "Ground", "Physical", 90,100,0)
stompingtantrum = Attack("Stomping Tantrum","Ground" ,"Physical", 75, 100, 0)
schorchingsands = Attack("Schorching Sands", "Ground", "Special", 70, 100, 0)
#Rock Attacks
accelerock = Attack("Accelerock", "Rock", "Physical", 40, 100, 1) #I Know Licanrock is the only one that learn this move but i dont care, i just want to make a simulator
ancientpower = Attack("Ancient Power", "Rock", "Special", 60, 100, 0)
mightycleave = Attack("Mighty Cleave", "Rock", "Physical", 95, 100, 0)
powergem = Attack("Power Gem", "Rock", "Special", 80, 100, 0)
rockslide = Attack("Rock Slide", "Rock", "Physical", 75, 90, 0)
rockthrow = Attack("Rock Throw", "Rock", "Physical", 50, 90, 0)
meteorbeam = Attack("Meteor Beam", "Rock", "Special", 120, 90, -1)
stoneedge = Attack("Stone Edge", "Rock", "Physical", 100, 80, 0)
stoneaxe = Attack("Stone Axe", "Rock", "Physical", 65, 100, 0)#Maybe i will add rocks stick web climate etc but for now i will just balance some attacks
diamondstorm = Attack("Diamond Storm", "Rock", "Physical", 110, 95, 0)
headsmash = Attack("Head Smash", "Rock", "Physical", 110, 80, -1)
rockwrecker = Attack("Rock Wrecker", "Rock", "Physical", 120, 90, -1)

#Bug Attacks
bugbuzz = Attack("Bug Buzz", "Bug", "Special", 90, 100, 0)
bugbite = Attack("Bug Bite", "Bug", "Physical", 60, 100, 0)
attackorder = Attack("Attack Order", "Bug", "Physical", 95, 100, 0)
firstimpression = Attack("First Impression", "Bug", "Physical", 85, 100, 1)
megahorn = Attack("Megahorn", "Bug", "Physical", 120, 85, 0)
x_scissor = Attack("X-Scissor", "Bug", "Physical", 80, 100, 0)
strugglebug = Attack("Struggle Bug", "Bug", "Special", 50, 100, 0)
signalbeam = Attack("Signal Beam", "Bug", "Special", 75, 100, 0)
pollenpuff = Attack("Pollen Puff", "Bug", "Special", 90, 100, 0)
steamroller = Attack("Steamroller", "Bug", "Physical", 70, 100, 0)
silverwind = Attack("Silver Wind", "Bug", "Special", 75, 100, 0)
furrycutter = Attack("Fury Cutter", "Bug", "Physical", 50, 95, 0)

#Ghost Attacks
shadowball = Attack("Shadow Ball", "Ghost", "Special", 80, 100, 0)
shadowclaw = Attack("Shadow Claw", "Ghost", "Physical", 70, 100, 0)
shadowpunch = Attack("Shadow Punch", "Ghost", "Physical", 60, 100, 0)
shadowsneak = Attack("Shadow Sneak", "Ghost", "Physical", 40, 100, 1)
bittermalice = Attack("Bitter Malice", "Ghost", "Special", 90, 100, 0)
astralbarrage = Attack("Astral Barrage", "Ghost", "Physical", 120, 100, 0)
hex = Attack("Hex", "Ghost", "Special", 70, 100, 0)
ominouswind = Attack("Ominous Wind", "Ghost", "Special", 75, 100, 0)
phantomforce = Attack("Phantom Force", "Ghost", "Physical", 90, 100, -1)
poltergeist = Attack("Poltergeist", "Ghost", "Physical", 110, 90, 0)
moongeistbeam = Attack("Moongeist Beam", "Ghost", "Special", 100, 100, 0)
nightshade = Attack("Night Shade", "Ghost", "Special", 100, 100, 0)
#Steel Attacks
bulletpunch = Attack("Bullet Punch", "Steel", "Physical", 40, 100, 1)
flashcannon = Attack("Flash Cannon", "Steel", "Special", 80, 100, 0)
ironhead = Attack("Iron Head", "Steel", "Physical", 80, 100, 0)
irotail = Attack("Iron Tail", "Steel", "Physical", 100, 75, 0)
makeitrain = Attack("Make It Rain", "Steel", "Special", 120, 100, 0)
metalclaw = Attack("Metal Claw", "Steel", "Physical", 50, 95, 0)
meteormash = Attack("Meteor Mash", "Steel", "Physical", 90, 90, 0)
smartstrike = Attack("Smart Strike", "Steel", "Physical", 70, 100, 0)
steelbeam = Attack("Steel Beam", "Steel", "Special", 110, 95, -1)
steelwing = Attack("Steel Wing", "Steel", "Physical", 70, 90, 0)
sunsteelstrike = Attack("Sunsteel Strike", "Steel", "Physical", 100, 100, 0)
mirrorshot = Attack("Mirror Shot", "Steel", "Special", 70, 85, 0)
#Fire Attacks
firespin = Attack("Fire Spin", "Fire", "Special", 40, 85, 0)
flamethrower = Attack("Flamethrower", "Fire", "Special", 90, 100, 0)
fireblast = Attack("Fire Blast", "Fire", "Special", 110, 85, 0)
firepunch = Attack("Fire Punch", "Fire", "Physical", 75, 100, 0)
temperflare = Attack("Temper Flare", "Fire", "Physical", 75, 100, 0)
firefang = Attack("Fire Fang", "Fire", "Physical", 65, 100, 0)
sacredfire = Attack("Sacred Fire", "Fire", "Physical", 100, 95, 0)
mysticalfire = Attack("Mystical Fire", "Fire", "Special", 75, 100, 0)
heatwave = Attack("Heat Wave", "Fire", "Special", 95, 90, 0)
flamecharge = Attack("Flame Charge", "Fire", "Physical", 50, 100, 0)
ember = Attack("Flame Burst", "Fire", "Special", 40, 100, 0)
blazingtorque = Attack("Blazing Torque", "Fire", "Physical", 80, 100, 0)
#Water Attacks
watergun = Attack("Water Gun", "Water", "Special", 40, 100, 0)
waterpulse = Attack("Water Pulse", "Water", "Special", 60, 100, 0)
waterfall = Attack("Waterfall", "Water", "Physical", 80, 100, 0)
hydropump = Attack("Hydro Pump", "Water", "Special", 110, 80, 0)
surf = Attack("Surf", "Water", "Special", 90, 100, 0)
aquajet = Attack("Aqua Jet", "Water", "Physical", 40, 100, 1)
scald = Attack("Scald", "Water", "Special", 80, 100, 0)
liquidation = Attack("Liquidation", "Water", "Physical", 85, 100, 0)
aquatail = Attack("Aqua Tail", "Water", "Physical", 90, 90, 0)
bubble = Attack("Bubble", "Water", "Special", 50, 100, 0)
chillingwater = Attack("Chilling Water", "Water", "Special", 70, 100, 0)
crabhammer = Attack("Crab Hammer", "Water", "Physical", 100, 90, 0)
#Grass Attacks
branchpoke = Attack("Branch Poke", "Grass", "Physical", 70, 100, 0)
gigadrain = Attack("Giga Drain", "Grass", "Special", 80, 100, 0)
megadrain = Attack("Mega Drain", "Grass", "Special", 45, 100, 0)
flowertrick = Attack("Flower Trick", "Grass", "Physical", 90, 100, 0)
grassyglide = Attack("Grassy Glide", "Grass", "Physical", 70, 100, 1)
woodhammer = Attack("Wood Hammer", "Grass", "Physical", 110, 100, 0)
magicalleaf = Attack("Magical Leaf", "Grass", "Special", 60, 100, 0)
vinewhip = Attack("Vine Whip", "Grass", "Physical", 45, 100, 0)
leafblade = Attack("Leaf Blade", "Grass", "Physical", 90, 100, 0)
energyball = Attack("Energy Ball", "Grass", "Special", 90, 100, 0)
seedbomb = Attack("Seed Bomb", "Grass", "Physical", 80, 100, 0)
razorleaf = Attack("Razor Leaf", "Grass", "Physical", 55, 95, 0)
#Electric Attacks
buzzybuzz = Attack("Buzzy Buzz", "Electric", "Special", 90, 100, 0)
boltbreak = Attack("Bolt Break", "Electric", "Physical", 90, 100, 0)
boltstrike = Attack("Bolt Strike", "Electric", "Physical", 130, 85, 0)
Discharge = Attack("Discharge", "Electric", "Special", 80, 100, 0)
chargebeam = Attack("Charge Beam", "Electric", "Special", 50, 90, 0)
electroweb = Attack("Electroweb", "Electric", "Special", 55, 95, 0)
nuzzle = Attack("Nuzzle", "Electric", "Physical", 30, 100, 1)
spark = Attack("Spark", "Electric", "Physical", 65, 100, 0)
supercellslam = Attack("Supercell Slam", "Electric", "Physical", 100, 95, 0)
thunder = Attack("Thunder", "Electric", "Special", 110, 70, 0)
thunderbolt = Attack("Thunderbolt", "Electric", "Special", 90, 100, 0)
thunderpunch = Attack("Thunder Punch", "Electric", "Physical", 75, 100, 0)
#Psychic Attacks
zenheadbutt = Attack("Zen Headbutt", "Psychic", "Physical", 80, 90, 0)
psychic = Attack("Psychic", "Psychic", "Special", 90, 100, 0)
psyshock = Attack("Psyshock", "Psychic", "Special", 80, 100, 0)
psystrike = Attack("Psystrike", "Psychic", "Special", 100, 100, 0)
psybeam = Attack("Psybeam", "Psychic", "Special", 65, 100, 0)
psychocut = Attack("Psycho Cut", "Psychic", "Physical", 70, 100, 0)
psyblade = Attack("Psyblade", "Psychic", "Physical", 85, 100, 0)
psychoboost = Attack("Psycho Boost", "Psychic", "Special", 130, 90, 0)
psychicfangs = Attack("Psychic Fangs", "Psychic", "Physical", 85, 100, 0)
extrassensory = Attack("Extrasensory", "Psychic", "Special", 80, 100, 0)
luminacrash = Attack("Lumina Crash", "Psychic", "Special", 80, 100, 0)
psyshieldbash = Attack("Psyshield Bash", "Psychic", "Physical", 70, 95, 0)
#Ice
aurorabeam = Attack("Aurora Beam", "Ice", "Special", 65, 100, 0)
avalanche = Attack("Avalanche", "Ice", "Physical", 60, 100, 0)
blizzard = Attack("Blizzard", "Ice", "Special", 110, 70, 0)
freeze_dry = Attack("Freeze-Dry", "Ice", "Special", 70, 100, 0)
icebeam = Attack("Ice Beam", "Ice", "Special", 90, 100, 0)
iceshard = Attack("Ice Shard", "Ice", "Physical", 40, 100, 1)
icepunch = Attack("Ice Punch", "Ice", "Physical", 75, 100, 0)
icefang = Attack("Ice Fang", "Ice", "Physical", 65, 95, 0)
icywind = Attack("Icy Wind", "Ice", "Special", 55, 95, 0)
icehammer = Attack("Ice Hammer", "Ice", "Physical", 100, 90, 0)
iceburn = Attack("Ice Burn", "Ice", "Special", 110, 90, -1)
mountaingale = Attack("Mountain Gale", "Ice", "Physical", 100, 85, -1)
#Dragon
outrage = Attack("Outrage", "Dragon", "Physical", 110, 100, -1)
breakingswipe = Attack("Breaking Swipe", "Dragon", "Physical", 60, 100, 0)
dracometeor = Attack("Draco Meteor", "Dragon", "Special", 130, 90, -1)
dragonclaw = Attack("Dragon Claw", "Dragon", "Physical", 80, 100, 0)
dragonpulse = Attack("Dragon Pulse", "Dragon", "Special", 85, 100, 0)
dragonbreath = Attack("Dragon Breath", "Dragon", "Special", 60, 100, 0)
dragonrush = Attack("Dragon Rush", "Dragon", "Physical", 100, 75, 0)
dragontail = Attack("Dragon Tail", "Dragon", "Physical", 60, 90, 0)
dynamaxcannon = Attack("Dynamax Cannon", "Dragon", "Special", 100, 100, 0)
roaroftime = Attack("Roar of Time", "Dragon", "Special", 120, 90, -1)
spacialrend = Attack("Spacial Rend", "Dragon", "Special", 100, 95, 0)
glaiverush = Attack("Glaive Rush", "Dragon", "Physical", 100, 100, -1)
#Dark
suckerpunch = Attack("Sucker Punch", "Dark", "Physical", 70, 100, 1)
knockoff = Attack("Knock Off", "Dark", "Physical", 65, 100, 0)
darkpulse = Attack("Dark Pulse", "Dark", "Special", 80, 100, 0)
crunch = Attack("Crunch", "Dark", "Physical", 80, 100, 0)
ceaselessedge = Attack("Ceaseless Edge", "Dark", "Physical", 65, 100, 0)
darkestlariat = Attack("Darkest Lariat", "Dark", "Physical", 85, 100, 0)
baddybad = Attack("Baddy Bad", "Dark", "Special", 90, 100, 0)
fierywrath = Attack("Fiery Wrath", "Dark", "Special", 80, 100, 0)
snarl = Attack("Snarl", "Dark", "Special", 55, 95, 0)
kottowclive = Attack("Kottow Clive", "Dark", "Physical", 85, 100, 0)
bite = Attack("Bite", "Dark", "Physical", 60, 100, 0)
wickedblow = Attack("Wicked Blow", "Dark", "Physical", 80, 100, 0)
#Fairy
alluringvoice = Attack("Alluring Voice", "Fairy", "Special", 80, 100, 0)
dazzlinggleam = Attack("Dazzling Gleam", "Fairy", "Special", 80, 100, 0)
disarmingvoice = Attack("Disarming Voice", "Fairy", "Special", 40, 100, 0)
fairywind = Attack("Fairy Wind", "Fairy", "Special", 40, 100, 0)
magicaltorque = Attack("Magical Torque", "Fairy", "Physical", 100, 100, 0)
playrough = Attack("Play Rough", "Fairy", "Physical", 90, 90, 0)
spiritbreak = Attack("Spirit Break", "Fairy", "Physical", 75, 100, 0)
sparklyswirl = Attack("Sparkly Swirl", "Fairy", "Special", 90, 100, 0)
fleurcannon = Attack("Fleur Cannon", "Fairy", "Special", 120, 90, -1)
mistyexplosion = Attack("Misty Explosion", "Fairy", "Special", 110, 100, -1)
lightofruin = Attack("Light of Ruin", "Fairy", "Special", 120, 90, -1)
moonblast = Attack("Moonblast", "Fairy", "Special", 95, 100, 0)


#Pokemons
bulbasaur = Pokemon("Bulbasaur",
                    ["Grass", "Poison"],
                    stats={
                        "hp": 45,
                        "attack": 49,
                        "defence": 49,
                        "speed": 45,
                        "sp_attack": 65,
                        "sp_defence": 65
                    },
                    attacks=[tackel, smog, megadrain, quickattack]
                    )

ivysaur = Pokemon("Ivysaur",
                  ["Grass", "Poison"],
                  stats={
                      "hp": 60,
                      "attack": 62,
                      "defence": 63,
                      "speed": 60,
                      "sp_attack": 80,
                      "sp_defence": 80
                  },
                  attacks=[tackel, acid, razorleaf, megadrain, quickattack]
                  )

venusaur = Pokemon("Venusaur",
                   ["Grass", "Poison"],
                   stats={
                       "hp": 80,
                       "attack": 82,
                       "defence": 83,
                       "speed": 80,
                       "sp_attack": 100,
                       "sp_defence": 100
                   },
                   attacks=[gigadrain, sludgebomb, sludgewave, quickattack, leafblade, earthpower]
                   )
mega_venusaur = Pokemon("Mega Venusaur",
                        ["Grass","Poison"],
                        stats={
                            "hp":80,
                            "attack":100 ,
                            "defence":123,
                            "speed":80,
                            "sp_attack": 122,
                            "sp_defence":120,
                        },
                        attacks=[gigadrain, sludgebomb, sludgewave, quickattack, leafblade, earthpower]
                          )
charmander = Pokemon("Charmander",
                        ["Fire"],
                        stats={
                            "hp":39,
                            "attack":52,
                            "defence":43,
                            "speed":65,
                            "sp_attack":60,
                            "sp_defence":50,
                        },
                        attacks = [ember]
                        )

charmeleon = Pokemon("Charmeleon",
                     ["Fire"],
                     stats={
                         "hp": 58,
                         "attack":64,
                         "defence": 58,
                         "speed": 80,
                         "sp_attack": 80,
                         "sp_defence": 65,
                     },
                     attacks = [firepunch ]
                     )

charizard = Pokemon("Charizard",
                    ["Fire","Fly"],
                    stats={
                        "hp": 78,
                        "attack": 84,
                        "defence":78,
                        "speed": 100,
                        "sp_attack": 109,
                        "sp_defence": 85,
                    },
                    attacks=[flamethrower]
                    )

mega_charizard_x = Pokemon("Mega Charizard X",
                          ["Fire", "Dragon"],
                          stats={
                              "hp": 78,
                              "attack": 130,
                              "defence": 111,
                              "speed": 100,
                              "sp_attack": 130,
                              "sp_defence": 85,
                          },
                          attacks=[flamethrower, firepunch, dragonclaw, dragonpulse, heatwave, slash]
                          )

mega_charizard_y = Pokemon("Mega Charizard Y",
                          ["Fire", "Fly"],
                          stats={
                              "hp": 78,
                              "attack": 104,
                              "defence": 78,
                              "speed": 100,
                              "sp_attack": 159,
                              "sp_defence": 115,
                          },
                          attacks=[flamethrower, fireblast, heatwave, airslash, dragonpulse, hurricane]
                          )

squirtle = Pokemon("Squirtle",
                   ["Water"],
                   stats={
                       "hp": 44,
                       "attack": 48,
                       "defence": 65,
                       "speed": 43,
                       "sp_attack": 50,
                       "sp_defence": 64,
                   },
                   attacks=[tackel, watergun, bubble, aquajet]
                   )

wartortle = Pokemon("Wartortle",
                    ["Water"],
                    stats={
                        "hp": 59,
                        "attack": 63,
                        "defence": 80,
                        "speed": 58,
                        "sp_attack": 65,
                        "sp_defence": 80,
                    },
                    attacks=[watergun, waterpulse, aquajet, bite, waterfall]
                    )

blastoise = Pokemon("Blastoise",
                    ["Water"],
                    stats={
                        "hp": 79,
                        "attack": 83,
                        "defence": 100,
                        "speed": 78,
                        "sp_attack": 85,
                        "sp_defence": 105,
                    },
                    attacks=[surf, hydropump, liquidation, icebeam, flashcannon, aquajet]
                    )

mega_blastoise = Pokemon("Mega Blastoise",
                         ["Water"],
                         stats={
                             "hp": 79,
                             "attack": 103,
                             "defence": 120,
                             "speed": 78,
                             "sp_attack": 135,
                             "sp_defence": 115,
                         },
                         attacks=[surf, hydropump, liquidation, icebeam, flashcannon, aquajet]
                         )
pokedex = [bulbasaur, ivysaur,venusaur, mega_venusaur,charmander,charmeleon,charizard,mega_charizard_x, mega_charizard_y,squirtle,wartortle,blastoise,mega_blastoise ]
legendaries = []
special_forms = [mega_blastoise,mega_charizard_y,mega_charizard_x, mega_venusaur]


your_pokedex = [] #Imagine you want to simulate only Swampert vs Pikachu, u dont need to simulate all battles, u Write the pokemons name and them they will be add in this list and a loop will put them fighting, or just the legendaries or special forms

Estatistic_victories = []
while True:
    your_pokedex = []
    print("=======================")
    print("Super Pokemon Simulator")
    print("=======================")
    print("Select -1 to simulate all pokemon incluiding special forms")
    print("Select -2 to simulate all pokemons except special forms")
    print("Select -3 to simulate all pokemons except legendaries")
    print("Select -4 to simulate all pokemons except legendaries and special forms")
    print("Select -5 to simulate just legendaries")
    print("Select -6 to simulate just special forms and legendaries")
    print("Select -7 to simulate to select the pokemons type you want to simulate (If the pokemon has more than 1 type, it will be included in the simulation, the type just need to be one of the types of the pokemon)")
    print("========================")
    print("Select -8 to leave the simulator")
    print("========================")
    select = int(input(f"How many pokemons u want to select to simulate {len(pokedex)}): "))
    if select<=-13:
        while True:
            select = int(input("Pls chose something valid: "))
            if select>-13:
                break
    #All pokemon      
    if select == -1:

        for pokemon in pokedex:
            pokemon1=pokemon
            pokemon1_victories_total = 0
            for pokemon in pokedex:
                pokemon2=pokemon
                if pokemon1 != pokemon2:
                    pokemon1_victories_total+=batalha(pokemon1,pokemon2)
                else:
                    pass
            Estatistic_victories.append(pokemon1_victories_total)
        print("The victories of each pokemon are: ")
        for i in range(len(Estatistic_victories)):
            print(f"{pokedex[i].name}: {Estatistic_victories[i]} victories")
    #No special form
    if select == -2:

        your_pokedex = pokedex[:]
        for pokemon in special_forms:
            if pokemon in your_pokedex:
                your_pokedex.remove(pokemon)
        for pokemon in your_pokedex:
            pokemon1=pokemon
            pokemon1_victories_total = 0
            for pokemon in your_pokedex:
                pokemon2=pokemon
                if pokemon1 != pokemon2:
                    pokemon1_victories_total+=batalha(pokemon1,pokemon2)
                else:
                    pass
            Estatistic_victories.append(pokemon1_victories_total)
        print("The victories of each pokemon are: ")
        for i in range(len(Estatistic_victories)):
            print(f"{your_pokedex[i].name}: {Estatistic_victories[i]} victories")
    #No legendarie
    if select == -3:
        your_pokedex = pokedex[:]
        for pokemon in legendaries:
            if pokemon in your_pokedex:
                your_pokedex.remove(pokemon)
        for pokemon in your_pokedex:
            pokemon1=pokemon
            pokemon1_victories_total = 0
            for pokemon in your_pokedex:
                pokemon2=pokemon
                if pokemon1 != pokemon2:
                    pokemon1_victories_total+=batalha(pokemon1,pokemon2)
                else:
                    pass
            Estatistic_victories.append(pokemon1_victories_total)
        print("The victories of each pokemon are: ")
        for i in range(len(Estatistic_victories)):
            print(f"{your_pokedex[i].name}: {Estatistic_victories[i]} victories")
    #No legendarie and special form
    if select == -4:
        your_pokedex = pokedex[:]
        for pokemon in special_forms:
            if pokemon in your_pokedex:
                your_pokedex.remove(pokemon)
        for pokemon in legendaries:
            if pokemon in your_pokedex:
                your_pokedex.remove(pokemon)
        for pokemon in your_pokedex:
            pokemon1=pokemon
            pokemon1_victories_total = 0
            for pokemon in your_pokedex:
                pokemon2=pokemon
                if pokemon1 != pokemon2:
                    pokemon1_victories_total+=batalha(pokemon1,pokemon2)
                else:
                    pass
            Estatistic_victories.append(pokemon1_victories_total)
        print("The victories of each pokemon are: ")
        for i in range(len(Estatistic_victories)):
            print(f"{your_pokedex[i].name}: {Estatistic_victories[i]} victories")
    #Just Legendaries
    if select == -5:
        your_pokedex = legendaries[:]
        for pokemon in your_pokedex:
            pokemon1=pokemon
            pokemon1_victories_total = 0
            for pokemon in your_pokedex:
                pokemon2=pokemon
                if pokemon1 != pokemon2:
                    pokemon1_victories_total+=batalha(pokemon1,pokemon2)
                else:
                    pass
            Estatistic_victories.append(pokemon1_victories_total)
        print("The victories of each pokemon are: ")
        for i in range(len(Estatistic_victories)):
            print(f"{your_pokedex[i].name}: {Estatistic_victories[i]} victories")
    #Just Special Forms
    if select == -6:
        your_pokedex = special_forms[:]
        for pokemon in your_pokedex:
            pokemon1=pokemon
            pokemon1_victories_total = 0
            for pokemon in your_pokedex:
                pokemon2=pokemon
                if pokemon1 != pokemon2:
                    pokemon1_victories_total+=batalha(pokemon1,pokemon2)
                else:
                    pass
            Estatistic_victories.append(pokemon1_victories_total)
        print("The victories of each pokemon are: ")
        for i in range(len(Estatistic_victories)):
            print(f"{your_pokedex[i].name}: {Estatistic_victories[i]} victories")
    #Only legendaries and special forms
    if select == -7:
        your_pokedex = special_forms[:] + legendaries[:]
        for pokemon in your_pokedex:
            pokemon1=pokemon
            pokemon1_victories_total = 0
            for pokemon in your_pokedex:
                pokemon2=pokemon
                if pokemon1 != pokemon2:
                    pokemon1_victories_total+=batalha(pokemon1,pokemon2)
                else:
                    pass
            Estatistic_victories.append(pokemon1_victories_total)
        print("The victories of each pokemon are: ")
        for i in range(len(Estatistic_victories)):
            print(f"{your_pokedex[i].name}: {Estatistic_victories[i]} victories")
    #You select the type including all pokemons

    
    else:
        for i in range(select):
            pokemon_selected = input("Select a pokemon to add in the battle (name like in the pokedex ex:bulbasaur): ")
            for pokemon in your_pokedex:
                if pokemon.name.lower() == pokemon_selected.lower():
                    your_pokedex.append(pokemon)
                    print(f"{pokemon} added to the battle")
            
        for pokemon in your_pokedex:
            pokemon1 = pokemon
            for pokemon in your_pokedex:
                pokemon2 = pokemon
                if pokemon1 != pokemon2:
                    pokemon1_victories_total += batalha(pokemon1, pokemon2)
                else:
                    pass
        Estatistic_victories.append(pokemon1_victories_total)



