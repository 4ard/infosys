class Customer:
    def __init__(self, name, address, phone, contact_person):
        self.__name = self.validate_field(name, "Имя")
        self.__address = self.validate_field(address, "Адрес")
        self.__phone = self.validate_field(phone, "Телефон")
        self.__contact_person = self.validate_field(contact_person, "Контактное лицо")

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
        self.__name = self.validate_field(name, "Имя")

    def set_address(self, address):
        self.__address = self.validate_field(address, "Адрес")

    def set_phone(self, phone):
        self.__phone = self.validate_field(phone, "Телефон")

    def set_contact_person(self, contact_person):
        self.__contact_person = self.validate_field(contact_person, "Контактное лицо")

    # Общий статический метод валидации
    @staticmethod
    def validate_field(value, field_name):
        if not value or not isinstance(value, str):
            raise ValueError(f"{field_name} должно быть непустой строкой.")
        return value

    def __str__(self):
        return (f"Заказчик: {self.__name}, "
                f"Адрес: {self.__address}, "
                f"Телефон: {self.__phone}, "
                f"Контактное лицо: {self.__contact_person}")
