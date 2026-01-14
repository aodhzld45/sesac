class Inventory:
    def __init__(self):
        self.weapon_list = []
                
    # 인벤토리에 무기들을 집어넣을거야, 근데 어떻게 넣을거야?       
    def add_weapon(self, weapon):
        self.weapon_list.append(weapon)
       
    def show_weapon_lst(self):
        for weapons in self.weapon_list:
            print(f"인벤토리 무기: {weapons}")
            
         
     

        
        
    
    
        
    
        
        
        
        