from abc import ABC, abstractmethod

class Device(ABC): # 부모 클래스
    def __init__(self, device_id, name):
        self.device_id = device_id
        self.name = name
        self.is_status = False
        
    @abstractmethod
    def power_on(self):
        if not self.is_status:
            self.is_status = True
        print(f"기기 id = {self.device_id} 의, {self.name}의 전원을 켭니다.")
    
    @abstractmethod
    def power_off(self):
        if self.is_status:
            self.is_status = False
        print(f"{self.name}의 전원을 끕니다.")
        
    @abstractmethod
    def status_check(self):
        status_str = "켜짐" if self.is_status else "꺼짐"
        return f"{self.name} (ID: {self.device_id}) 상태: {status_str}"