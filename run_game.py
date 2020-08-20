import character_mkr as mk
from subprocess import call

def _check_status(player):
    print('*** Info card ***')
    print(' ')
    print(f'Name: {player.name}')
    print(f'Class: {player.clase}')
    print(f'Race: {player.race}')
    print(f'Aligment: {player.aligment}')
    print(f'Level: {player._level}')
    print(f'HP: {player._hp}')
    print(f'XP: {player._xp_point}')
    print(f'Sats: ')
    status = player._stats
    for k,v in status.items():
        print(f'    {k} : {v}')

def ingame():
    pass

def _player_creation():
        # Naming the character
    name = input('How you want to name him/her: ')
    
    # Assigning class
    clase = mk.assigning_class()

    # Assigning race
    race = mk.assigning_races()

    # Aligment for character
    aligment = mk.set_aligment()

    # Create character
    #try:
    player = mk.Character(name, clase, race, aligment)
    call('clear')
    print(f'{player.name} has been born old (typical).')
#except:
    #   print(f'Your character named "{name}" could not be created')

    print('--------'*4)
    print('Check out your stats')
    _check_status(player)
    print(' ')
    
    print('In game!')
    ingame() #Thowing ingame() function

def lobby():
    lobby = """
        
        Wait...
        First of all, you need to create your Alter Ego (character)

        """
    print(lobby)
    _player_creation()

def run():
    
    enter = input('Do you want to begin now? (y/n): ')
    enter.upper()
    assert enter == 'y' or enter == 'n'

    if enter == 'y':
        print('Starting game...')
        lobby()
    elif enter == 'n':
        print('Good bye then.')



if __name__ == '__main__':
    welcome = """
        Allow me to welcome you to this brand new D&D game, in which all your gaming
        experience will be in the smarter you are in making decisions based upon the narrative of events.

        Putting you in perspective: you will be reading a story, in which your character will be starring it.
        The combat is up to your imagination of how intense it might be.

        Ok, say no more and enjoy this adventure!

        ___________________________________________________________________________________________________

        """
    
    print(welcome)
    run()