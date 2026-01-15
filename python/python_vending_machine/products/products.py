class Products:
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price
        
    def __str__(self):
        return f"상품의 {self.code} / {self.name} / {self.price}"
    
    def show_info(self, slot_info):
    
        if slot_info:
            text = "재고 있음"
        else:
            text = "재고 없음"
    
        return print(f"상품 = {self.code} / {self.name} / {self.price} / {text}")
     