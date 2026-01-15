import queue

class ProductSlotQueue:
    def __init__(self, product):
        self.product = product
        self.slot_queue = queue.Queue()  # FIFO

    def fill(self, count: int):
        if not isinstance(count, int):
            print("count는 정수여야 합니다.")
            return False
        if count <= 0:
            print(f"상품을 채울려면 count가 1 이상이어야 합니다. 상품코드 = {self.product.code} / 상품명 = {self.product.name}")
            return False

        for _ in range(count):
            self.slot_queue.put(self.product)

        print(f"현재 {self.product.name} 상품이 {count}개 채워졌습니다. (총 재고: {self.stock()}개)")
        return True

    # 상품 한개씩 컷
    def dispense_one(self):
        if self.slot_queue.empty():
            print("품절입니다.")
            return None
        return self.slot_queue.get()

    def stock(self):
        return self.slot_queue.qsize()
