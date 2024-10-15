class Customer:
    def __init__(self, name, address, phone, contact_person):
        self.__name = self.validate_name(name)
        self.__address = self.validate_address(address)
        self.__phone = self.validate_phone(phone)
        self.__contact_person = self.validate_contact_person(contact_person)

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
        self.__name = self.validate_name(name)

    def set_address(self, address):
        self.__address = self.validate_address(address)

    def set_phone(self, phone):
        self.__phone = self.validate_phone(phone)

    def set_contact_person(self, contact_person):
        self.__contact_person = self.validate_contact_person(contact_person)

    # Статические методы валидации
    @staticmethod
    def validate_name(name):
        if not name or not isinstance(name, str):
            raise ValueError("Имя должно быть непустой строкой.")
        return name

    @staticmethod
    def validate_address(address):
        if not address or not isinstance(address, str):
            raise ValueError("Адрес должен быть непустой строкой.")
        return address

    @staticmethod
    def validate_phone(phone):
        if not phone or not isinstance(phone, str):
            raise ValueError("Телефон должен быть непустой строкой.")
        return phone

    @staticmethod
    def validate_contact_person(contact_person):
        if not contact_person or not isinstance(contact_person, str):
            raise ValueError("Контактное лицо должно быть непустой строкой.")
        return contact_person

    def __str__(self):
        return f"Заказчик: {self.__name}, Адрес: {self.__address}, Телефон: {self.__phone}, Контактное лицо: {self.__contact_person}"
