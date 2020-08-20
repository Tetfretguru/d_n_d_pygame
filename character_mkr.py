import random
import dices as d

class Character:
    def __init__(self, name, clase, race, aligment):
        self.name = name
        self.clase = clase 
        self._level = 1
        self.race = race
        self.aligment = aligment
        self._xp_point = 0
        self._hp = 100       
        self._stats = _new_stats()

def _roll_dices():
    tiros = []
    sim = 0
    while sim < 4:
        dado = d.roll_d6()
        tiros.append(dado)
        sim += 1
   
    values = sorted(tiros)
    values.pop(0)
    value = sum(values)
    return value

def _new_stats():
    strength = _roll_dices()
    dexterity = _roll_dices()
    intelligence = _roll_dices()
    wisdom = _roll_dices()
    charisma = _roll_dices()

    stats = {
        'STR':strength,
        'DEX':dexterity,
        'INT':intelligence,
        'WIS':wisdom,
        'CHA':charisma
    }
    return stats

    
def assigning_class():
    
    clases = ('Warrior', 'Mage', 'Hunter', 'Vampire')
    print('Select a class for your character: ')
    print('_____________________')
    print(f'1: {clases[0]} |2: {clases[1]} |3: {clases[2]} |4: {clases[3]}')

    msg = """
    
    Which class do you choose?
    >>
    """
    option = input(msg)

    if option == '1':
        clase = clases[0]
        return clase
    elif option == '2':
        clase = clases[1]
        return clase
    elif option == '3':
        clase = clases[2]
        return clase
    elif option == '4':
        clase = clases[3]
        return clase
    else:
        print('There is no such an option.')
        assigning_class()

def assigning_races():
    races = ('Human', 'Elf', 'Orc', 'Undead')
    print('Please select the race you want for your character to be: ')
    print('_____________________')
    print(f'1: {races[0]} |2: {races[1]} |3: {races[2]} |4: {races[3]}')

    msg = """
    
    Which class do you choose?
    >>
    """
    option = input(msg)
    if option == '1':
        race = races[0]
        return race
    elif option == '2':
        race = races[1]
        return race
    elif option == '3':
        race = races[2]
        return race
    elif option == '4':
        race = races[3]
        return race
    else:
        print('There is no such an option.')
        assigning_race()     

def set_aligment():
    aligments = ('Good', 'Neutral/Good', 'Neutral', 'Neutral/Evil', 'Evil')
    print('The aligment will further in the adventure define the prices you will get: ')
    print('_____________________')
    print(f'1: {aligments[0]} | 2: {aligments[1]} | 3: {aligments[2]} | 4: {aligments[3]} | 5: {aligments[4]} |')

    msg = """
    
    What is your aligment
    >>
    """
    option = input(msg)
    if option == '1':
        aligment = aligments[0]
        return aligment
    elif option == '2':
        aligment = aligments[1]
        return aligment
    elif option == '3':
        aligment = aligments[2]
        return aligment 
    elif option == '4':
        aligment = aligments[3]
        return aligment
    elif option == '5':
        aligment = aligments[4]
        return aligment 
    else:
        print('No option typed allowed')
        set_aligment()  

