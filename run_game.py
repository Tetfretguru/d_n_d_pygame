from character_mkr import Character

def main():
    lobby = """
        
        Wait...
        First of all, you need to create your Alter Ego (character)

        """
    print(lobby)

    name = input('How you want to name him/her: ')
    clase = 



def run():
    
    enter = input('Type "BEGIN" to start the campaign...')

    if enter != "BEGIN":
        print('Boooooooring. Bye')
    elif enter == "begin" or enter == "Begin":
        print('In capital, please. Show me some emotion, yo!!')
        print(' ')
        run()
    else:
        print('Let´s go!')
        main()



if __name__ == '__main__':
    welcome = """
        Allow me to welcome you to this brand new D&D game, in which all your gaming
        experience will be in the smarter you are in making decisions based in the narrative of events.

        Putting you in perspective: you will be reading a story, in which your character will be starring it.
        The combat is up to your imagination of how intense might be.

        Ok, say no more and enjoy this adventure!

        ___________________________________________________________________________________________________

        """
    
    print(welcome)
    run()