from abc import ABC, abstractmethod

class Weapon(ABC):
    def __init__(self, name, skill):
        self.name = name
        self.skill = skill
        
    @abstractmethod
    def use_skill(self):
        print(f"[무기스킬] {self.skill}!")
        
class Sword(Weapon):
    def __init__(self, name):
        super().__init__(name, "베기")
        
    def use_skill(self):
        print(f"[무기스킬] {self.skill}!")
        
class Staff(Weapon):
    def __init__(self, name):
        super().__init__(name, "마법 발동")
        
    def use_skill(self):
        print(f"[무기스킬] {self.skill}!")

class Bow(Weapon):
    def __init__(self, name):
        super().__init__(name, "화살 발사")

