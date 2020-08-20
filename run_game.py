import character_mkr as mk
from subprocess import call
import datetime
import csv

def _update_player_card(player):
    f = open('player_card.csv', "w")
    writer = csv.writer(f)
    writer.writerow([player.name, player.clase, player.race, player.aligment, player._level, player._hp, player._xp_point, player._stats])
    
    f.close()

def _save_player_card(player):
    file_name = 'player_card.csv'

    f = open('player_card.csv', 'w')
    writer = csv.DictWriter(f, fieldnames=['name', 'clase', 'race', 'aligment', 'level', 'hp', 'xp','stats'])
    writer.writeheader()
    f.close()


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


def lobby():
    lobby = """
        
        Wait...
        First of all, you need to create your Alter Ego (character)

        """
    print(lobby)
    player = mk.player_creation()
    _check_status(player)

    print(' ')
    check = "Continue (c) / Roll again (r): "
    msg = input(check)
    
    assert msg == 'c' or msg == 'r'

    if msg == 'c':
        _save_player_card(player)
        _update_player_card(player)
        #ingame()
    elif msg == 'r':
        player = mk.player_creation() 
        _check_status(player)

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