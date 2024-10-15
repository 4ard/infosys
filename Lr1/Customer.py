class Customer:
    def __init__(self, name, address, phone, contact_person):
        self.__name = name
        self.__address = address
        self.__phone = phone
        self.__contact_person = contact_person

    # Геттеры
    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone

    def get_contact_person(self):
        return self.__contact_person

    # Сеттеры
    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_phone(self, phone):
        self.__phone = phone

    def set_contact_person(self, contact_person):
        self.__contact_person = contact_person

    def __str__(self):
        return f"Заказчик: {self.__name}, Адрес: {self.__address}, Телефон: {self.__phone}, Контактное лицо: {self.__contact_person}"
