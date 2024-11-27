import time

class Menu:
    def __init__(self,category,name,price,weight,ingredients):
        self.category = category
        self.name = name
        self.price = price
        self.weight = weight
        self.ingredients = ingredients
    
    def __str__(self):
        return f"{self.category}: {self.name}({self.weight} г) - {self.price} руб."

    def add_menu(self,menu,dish):
        menu.append(dish)

    def print_menu(self,dish):
        print(dish)
        print(f"Состав блюда: {", ".join(self.ingredients)}\n")

class Restaurant:
    def __init__(self,title,menu):
        self.title = title
        self.menu = menu
        self.pay_order = "Ожидание оплаты заказа"
        self.status_order = "успешно принят"

    def payment_order(self,client):
        print(f"Статус оплаты заказа, клиента {client.name}:\n")
        time.sleep(3)
        print(f"{self.pay_order}")
        self.pay_order = "Заказ оплачен"
        time.sleep(3)
        print(f"{self.pay_order}")
        self.pay_order = "Оплата получена"
        time.sleep(3)
        print(f"{self.pay_order}")
    
    def accept_order(self,client):
        print(f"Статус заказа клиента {client.name}:\n")
        time.sleep(3)
        print(f"Клиент {client.name}, ваш заказ {self.status_order}")
        self.status_order = "успешно оформлен"
        time.sleep(3)
        print(f"Клиент {client.name}, ваш заказ {self.status_order}")

class Client:
    def __init__(self):
        self.name = ""
        self.list_order = []

    def input_name(self):
        self.name = input("Клиент, введите своё имя: ")

    def input_order(self):
        order = ""
        while order != ".":
            order = input(f"Клиент {self.name} введите блюдо из меню: ")
            self.list_order.append(order.capitalize())
        del self.list_order[len(self.list_order)-1]

class Adress:
    def __init__(self):
        self.street = ""
        self.house = ""
        self.entrance = ""
        self.floor = ""
        self.apartment = ""

    def __str__(self):
        return f"ул. {self.street}, д. {self.house}, под. {self.entrance}, этаж {self.floor}, кв. {self.apartment}"

    def input_adress(self,client):
        print(f"Клиент {client.name}, укажите точный адрес:\n")
        self.street = input("Улица: ")
        self.house = input("Дом: ")
        self.entrance = input("Подъезд: ")
        self.floor = input("Этаж: ")
        self.apartment = input("Квартира: ")

class Order:
    def __init__(self,client):
        self.name = client.name
        self.list_order = client.list_order
        self.deliv_order = "Собран"
        
    def __str__(self):
        return f"{self.name}"
        
    def sum_order(self,menu):
        s = 0
        for o_item in self.list_order:
            for m_item in menu:
                if o_item == m_item.name:
                    s += m_item.price
        return f"Итоговая сумма заказа: {s} руб."
        
    def print_order(self,menu):
        print(f"Заказ клиента {self.name}:\n")
        for o_item in self.list_order:
            for m_item in menu:
                if o_item == m_item.name:
                    print(f"{o_item} - {m_item.price} руб.")
                    break
            else:
                print(f"\nБлюда {o_item} нет в меню!\n")
        print(f"\n{self.sum_order(menu)}")

    def delivery_order(self,adress):
        print(f"Статус доставки заказа клиента {self.name} по адресу {adress}:\n")
        time.sleep(3)
        print(f"{self.deliv_order}")
        self.deliv_order = "В пути"
        time.sleep(3)
        print(f"{self.deliv_order}")
        self.deliv_order = "Доставлен"
        time.sleep(3)
        print(f"{self.deliv_order}")