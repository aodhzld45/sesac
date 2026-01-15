from abc import ABC, abstractmethod
# 결제(Payments) - 추상 클래스
# - 결제 방식을 택함.
# - 승인/ 취소 프로세스 - @abstractmethod
# - 현금 / 카드
class Payments(ABC):
    def __init__(self, money, name):
        self.money = money
        self.name = name
        
    def pay(self, price):
        if self.money >= price:
            self.money -= price
            return True
        elif self.money < price:
            return False
        
    def __str__(self):
        return f"현재 결제 수단 : {self.name}의 잔액은 {self.money}입니다."     
    
    @abstractmethod
    def approve(self, amount): # 승인
        pass

    @abstractmethod
    def cancel(self, amount): # 취소
        pass
    
