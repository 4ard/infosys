class Customer:
    def __init__(self, name, address, phone, contact_person):
        self.__name = self.validate_field(name, "Имя")
        self.__address = self.validate_field(address, "Адрес")
        self.__phone = self.validate_field(phone, "Телефон")
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

    # Геттеры и сеттеры (остаются без изменений)

    @staticmethod
    def validate_field(value, field_name):
        if not value or not isinstance(value, str):
            raise ValueError(f"{field_name} должно быть непустой строкой.")
        return value

    def __str__(self):
        return f"{self.short_version()} | Полная информация: {self.full_version()}"

    def short_version(self):
        return f"Заказчик: {self.__name}, Телефон: {self.__phone}"

    def full_version(self):
        return (f"Имя: {self.__name}, "
                f"Адрес: {self.__address}, "
                f"Телефон: {self.__phone}, "
                f"Контактное лицо: {self.__contact_person}")

    def __eq__(self, other):
        if not isinstance(other, Customer):
            return NotImplemented
        return (self.__name == other.__name and
                self.__address == other.__address and
                self.__phone == other.__phone and
                self.__contact_person == other.__contact_person)
#

