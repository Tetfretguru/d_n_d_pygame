

class Character:
    def __init__(self, name, clase, level, race, aligment, xp_point):
        self.name = name
        self.clase = clase 
        self.level = level
        self.race = aligment
        self.xp_point = xp       
        self._stats = stats

        
    
class Stats(Character):
    def __init__(self, name):
        super().__init__(name)

    @property
    def _generate(self):
        pass
