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

adress = Adress()

adress.input_adress(client)