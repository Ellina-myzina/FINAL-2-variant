# README

# «СИСТЕМА ОНЛАЙН-ЗАКАЗА ЕДЫ»

## Описание

Данный проект представляет собой приложение, в котором пользователи могут просматривать меню, размещать заказы и отслеживать статус доставки. 

Код программы позволяет вводить данные пользователя, вводить пользователям блюда из меню и отслеживать статус своего заказа. Код состоит из следующих классов, в которых есть необходимые методы, которые выполняют определенный задачи.

## Классы и методы

### 1.	Класс Menu

В этом классе хранится информация о блюде: категория блюда, название блюда, цена, вес и состав блюда:

![image](https://github.com/user-attachments/assets/b8a98c43-4392-4cb0-bc9a-62e719dd57f5)

### Методы класса Menu:

•	Метод **__str__(self)** позволяет получить строковое представление об информации блюда, включая его название:

![image](https://github.com/user-attachments/assets/e84b08c2-cd9b-4c33-a6dc-33c9f759e020)

•	Метод **add_menu(self, menu, dish)** добавляет блюдо в список menu[]:

![image](https://github.com/user-attachments/assets/b4a88cdf-9010-490c-99a3-c309ada5510d)

•	Метод **print_menu(self, dish)** выводит информацию о блюде:

![image](https://github.com/user-attachments/assets/08ace9f3-9927-4fe1-bf1b-dceab13da6e9)

### 2.	Класс Restaurant

Представляет ресторан с названием и меню, а также атрибут о статусе оплаты заказа и атрибут о статусе заказа:

![image](https://github.com/user-attachments/assets/db88f51b-0523-47cc-a65a-0cbef8b12974)

### Методы класса Restaurant:

•	Метод **pyment_order(self,client)** выводит информацию о статусе оплаты заказа клиента, используя функцию **sleep** из модуля **time** для имитации отслеживания статуса оплаты:

![image](https://github.com/user-attachments/assets/107122fb-5e4c-4f56-98fa-c02f9ad8e22d)

•	Метод **accept_order(self,client)** выводит информацию о статусе заказа клиента, используя функцию **sleep** из модуля **time** для имитации отслеживания статуса заказа:

![image](https://github.com/user-attachments/assets/ca76d41b-4bc8-42f4-81e3-04ad2ca5c53b)

### 3.	Класс Client

Содержит имя клиента и список заказанных блюд клиентом:

![image](https://github.com/user-attachments/assets/09b87982-25a9-46bc-a7d8-77cce1004af6)

### Методы класса Client:

•	Метод **input_name(self)** запрашивает у пользователя имя:

![image](https://github.com/user-attachments/assets/c9486530-b472-459e-919c-a54826cbfc28)

•	Метод **input_order(self)** просит ввести пользователя блюда из меню и добавляет каждое блюдо в список:
![image](https://github.com/user-attachments/assets/9ed8a31a-d1fc-4abe-8d5b-1968abdbf6a7)

### 4.	Класс Adress

Содержит полный адрес клиента: улицу, дом, подъезд, этаж, квартиру:

![image](https://github.com/user-attachments/assets/d29ede0f-dccd-4b4d-abd7-8b2a03aacbe1)

### Методы класса Adress:

•	Метод **__str__(self)** позволяет получить строковое представление адреса доставки:

![image](https://github.com/user-attachments/assets/4b656a5a-c662-4383-b688-68cb71f834d6)

•	Метод **input_adress(self,client)** запрашивает у клиента точный адрес доставки:

![image](https://github.com/user-attachments/assets/321ab7d3-66a1-4248-9514-6bfaa7efaa08)

### 5.	Класс Order

Хранит информацию о клиенте, заказе клиента и статусе доставки заказа:

![image](https://github.com/user-attachments/assets/78180c1f-2d8b-4e87-b171-16452a718e05)

### Методы класса Order:

•	Метод **__str__(self)** позволяет получить строковое представление об имени клиента:

![image](https://github.com/user-attachments/assets/27496879-0b78-4a0e-a96d-919109e24748)

•	Метод **sum_order(self, menu)** считает сумму заказа клиента:

![image](https://github.com/user-attachments/assets/76396d0e-569d-4444-9aef-6deed57e37fc)

•	Метод **print_order(self, menu)** подробно выводит заказ клиента, его и сумму и выводит фразу, если клиент ввел не то блюдо: 

![image](https://github.com/user-attachments/assets/b0057512-ec9c-4eda-a365-590b28224b2f)

•	Метод **delivery_order(self,adress)** выводит информацию о статусе доставки заказа клиента, используя функцию **sleep** из модуля **time** для имитации отслеживания статуса доставки заказа:

![image](https://github.com/user-attachments/assets/2011ca15-5e74-43fc-9645-56d0f0d91874)

## Использование программы:

1.	Запустите программу;
2.	Введите ваше имя и адрес доставки;
3.	Введите блюда из меню, вводя их названия. Чтобы завершить выбор, введите точку (.);
4.	После ввода данных клиента и блюд из меню, программа выведет информацию о вашем заказе, итоговой сумме, а также статус заказа, статусы оплаты и доставки заказа.

## Пример работы программы:

![image](https://github.com/user-attachments/assets/224ad9ea-a31d-4157-976c-3a876959a80b)
![image](https://github.com/user-attachments/assets/1ae288d2-b283-4131-ad85-2d20c2c97676)
![image](https://github.com/user-attachments/assets/c08bfd61-c8c2-4da5-8fbc-8cf1bc00a282)
