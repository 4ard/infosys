import json

class BaseCustomer:
    def __init__(self, name, phone):
        self.__name = self.validate_field(name, "Имя")
        self.__phone = self.validate_field(phone, "Телефон")

    @staticmethod
    def validate_field(value, field_name):
        if not value or not isinstance(value, str):
            raise ValueError(f"{field_name} должно быть непустой строкой.")
        return value

    def short_version(self):
        return f"Заказчик: {self.__name}, Телефон: {self.__phone}"

    def get_name(self):
        return self.__name

    def get_phone(self):
        return self.__phone

class Customer(BaseCustomer):
    def __init__(self, name, address, phone, contact_person):
        super().__init__(name, phone)  # Вызов конструктора базового класса
        self.__address = self.validate_field(address, "Адрес")
        self.__contact_person = self.validate_field(contact_person, "Контактное лицо")

    @classmethod
    def from_json(cls, json_data):
        data = json.loads(json_data)
        return cls(
            name=data.get('name'),
            address=data.get('address'),
            phone=data.get('phone'),
            contact_person=data.get('contact_person')
        )

    @classmethod
    def from_string(cls, string_data):
        parts = string_data.split(';')
        if len(parts) != 4:
            raise ValueError("Строка должна содержать 4 поля, разделенные ';'.")
        return cls(
            name=parts[0].strip(),
            address=parts[1].strip(),
            phone=parts[2].strip(),
            contact_person=parts[3].strip()
        )

    def full_version(self):
        return (f"Имя: {self.__name}, "
                f"Адрес: {self.__address}, "
                f"Телефон: {self.__phone}, "
                f"Контактное лицо: {self.__contact_person}")

    def __str__(self):
        return f"{self.short_version()} | Полная информация: {self.full_version()}"

class CustomerSummary(BaseCustomer):
    def __init__(self, customer, inn, ogrn):
        super().__init__(customer.get_name(), customer.get_phone())  # Вызов конструктора базового класса
        self.__inn = inn
        self.__ogrn = ogrn

    def __str__(self):
        return (f"Краткая информация: {self.short_version()}, "
                f"ИНН: {self.__inn}, "
                f"ОГРН: {self.__ogrn}")

