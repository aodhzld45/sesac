
from abc import ABC, abstractmethod
from job import Warrior, Mage, Archer
from weapon import Sword, Staff, Bow
from Inventory import Inventory

class Character(ABC):
    # 모든 캐릭터는 이름, 직업, 무기
    # 생성 시 이름/직업은 필수
    def __init__(self, name, role, weapon=None):
        if not name or str(name).strip() == "":
            return print(f"이름(name)은 필수입니다.")
        if not role or str(role).strip() == "":
            return print(f"직업(job)은 필수입니다.")
        self.name = name
        self.role = role
        self.weapon = weapon
        self.is_connect = False

        if weapon is not None:
            self.equip_weapon(weapon)
            
    def connect_status(self):
        return self.is_connect
        
    def connett_on(self):
        print(f"{self.name}({self.role})님이 접속하였습니다.") 
    
    def connect_off(self):
        print(f"{self.name}({self.role})님이 접속 종료하였습니다.")    
        
        
    def equip_weapon(self, weapon):
        self.weapon = weapon
                
        if self.role.can_use(weapon) == False:
            print(f"제대로 끼셈")
        else:
            print(f"{self.name}이(가) 이건 제가 잘 다루는 거죠라며 꺼드럭댄다.")
            

    # 공격하기
    def attack(self):
        if not self.role.can_use(self.weapon):
            return print(f"{self.name}({self.role.name})의 역할에 맞지 않는 무기입니다.")
                
        if self.weapon:
            return print(f"{self.name}({self.role.name})(이)가 {self.weapon.name}(으)로 공격!")
        else:
            return print(f"{self.name}({self.role.name})의 장착된 무기가 없습니다.")
        
    # 무기스킬사용
    def skill_active(self):
        if not self.role.can_use(self.weapon):
            return print(f"이건 내 역할에 맞지 않아요.")
        if self.weapon:
            print(f"{self.name}({self.role.name})가 {self.weapon.name} 스킬 사용!")
            self.weapon.use_skill()
        else:
            print("무기가 없습니다. 무기를 장착한 뒤 사용하세요.")

# p1 = Character("서현석", Warrior(), Sword())

p2 = Character("홍길동", Mage(), Sword('기본검'))

inv = Inventory()

inv.add_weapon("짱좋은검")

inv.add_weapon("겁나좋은검")

inv.show_weapon_lst()

# p2.equip_weapon(Sword())
p2.equip_weapon(Staff("기본 지팡이"))

# p1.attack()
# p1.skill_active()

# p1.equip_weapon(Staff())

# p2.attack()

# p2.skill_active()



