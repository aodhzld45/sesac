from products.productSlotQueue import ProductSlotQueue
from products.products import Products

from payments.cardPayments import CardPayments
from payments.cashPayments import CashPayments
  
from vendingMachine import VendingMachine

# from person import Person

# 테스트 케이스
cola = Products("A1", "콜라", 1500)
cider = Products('A2', "사이다", 1500)
water = Products('A3', "물", 500)

product1 = ProductSlotQueue(cola)
product2 = ProductSlotQueue(cider)
product3 = ProductSlotQueue(water) 

product1.fill(5)
product2.fill(3)
product3.fill(0) # 에러 -> fill count 0

vm = VendingMachine()
vm.register_slot(product1)
vm.register_slot(product2)
vm.register_slot(product3)

vm.fill_product(product1, 9)
vm.fill_product(product2, 0)
vm.fill_product(product3, 2)

vm.buy(product1, 5)

vm.show_products()



