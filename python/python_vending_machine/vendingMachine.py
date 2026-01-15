from products.productSlotQueue import ProductSlotQueue

class VendingMachine:
    def __init__(self):
        self.product_slots = {}
        
    def register_slot(self, slot):
        code = slot.product.code
        self.product_slots[code] = slot    
    
    def fill_product(self, product_object, count):
        code = product_object.product.code                 
        # 기존 상품 재고 추가
        slot = self.product_slots.get(code)
        if slot is None:
            print("존재하지 않는 상품 코드입니다.")
            return False

        ok = slot.fill(count)
        if ok:
            print(f"[리필] {code} +{count}개 (현재 재고: {slot.stock()})")
        return ok

    def show_products(self):
        # 상품 목록 출력 
        print("==== 자판기 상품 목록 ====")
        for code in sorted(self.product_slots.keys()):
            slot = self.product_slots[code]
            p = slot.product
            status = "재고 있음" if slot.stock() > 0 else "재고 없음"
            print(f"[{p.code}] {p.name} / {p.price}원 / 재고:{slot.stock()} ({status})")

    def buy(self, product_object, count):
        code = product_object.product.code                 

        # 상품 n개 구매(출고)
        slot = self.product_slots.get(code)
        
        bought = []
        for _ in range(count):
            item = slot.dispense_one()
            if item is None:
                print("중간에 품절이 발생했습니다.")
                return None
            bought.append(item)
        
        if slot is None:
            print("존재하지 않는 상품 코드입니다.")
            return None

        print(f"[구매완료] {product_object.product.name} / 남은 재고:{slot.stock()}")
        return bought
    
    
