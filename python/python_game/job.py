from weapon import Sword, Staff, Bow

class Job:
    def __init__(self, name, allowed_weapon_cls):
        self.name = name
        self.allowed_weapon_cls = allowed_weapon_cls

    def can_use(self, weapon):
        return isinstance(weapon, self.allowed_weapon_cls)
    
    
class Warrior(Job):
    def __init__(self):
        super().__init__("전사", Sword) 
        
class Mage(Job):
    def __init__(self):
        super().__init__("마법사", Staff)
        
class Archer(Job):
    def __init__(self):
        super().__init__("궁수", Bow)