class Person:
    def __init__(self):
        # 지불가능한 결제 방식들.
        self.wallet = {}
        
    def run(self, vm):
        vm.run(self.wallet)
        
    def add_payment(self, payment):
        self.wallet[payment.name] = payment
        
    def show_budget(self):
        for key, value in self.wallet.items():
            print(key, value)
    
    