class Person():
    type_fio = str
    words_fio = 3
    not_letter_in_fio = 0
    min_len_words_fio = 3

    type_age = int
    min_age = 14
    max_age = 150

    type_weight = float
    min_weight = 25.0

    type_passport = str
    not_num_in_passport = 0
    len_series = 4
    len_num = 6

    def __init__(self, fio, age, passport, weight):

        if self.verify_fio(fio) == 4:
            self.__fio = fio
        if self.verify_age(age) == 2:
            self.__age = age
        if self.verify_passport(passport) == 4:
            self.__passport = passport
        if self.verify_weight(weight) == 2:
            self.__weight = weight

    @property
    def fio(self):
        return self.__fio

    @fio.setter
    def fio(self, fio):
        self.verify_fio(fio)
        self.__fio = fio

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,age):
        self.verify_age(age)
        self.__age = age

    @property
    def passport(self):
        return self.__passport

    @passport.setter
    def passport(self, passport):
        self.verify_passport(passport)
        self.__passport = passport

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.verify_weight(weight)
        self.__weight = weight

    @classmethod
    def verify_fio(cls, value):
        checking = 0

        if cls.type_fio == type(value):
            checking += 1
        else:
            raise TypeError("ФИО должно быть строкой")

        if cls.words_fio == len(value.split(" ")):
            checking += 1
        else:
            raise TypeError("Неверный формат записи ФИО")

        if cls.not_letter_in_fio == len([x for x in value.split(" ") if x.isalpha() == False]):
            checking += 1
        else:
            raise TypeError("В ФИО можно использовать только буквенные символы")

        if cls.min_len_words_fio == len([x for x in value.split(' ') if len(x) >= 1]):
            checking += 1
        else:
            raise TypeError("В ФИО должно быть хотя бы по одному символу")

        return checking

    @classmethod
    def verify_age(cls, value):
        checking = 0

        if cls.type_age == type(value):
            checking += 1
        else:
            raise TypeError("Введите целое число")

        if cls.min_age <= value <= cls.max_age:
            checking += 1
        else:
            raise TypeError("Возраст должен быть не меньше 14 и не больше 150")

        return checking

    @classmethod
    def verify_passport(cls, value):
        checking = 0

        if cls.type_passport == type(value):
            checking += 1
        else:
            raise TypeError("Серия и номер паспорта должны быть строкой")

        if cls.not_num_in_passport == len([x for x in value.split(" ") if x.isdigit() == False]):
            checking += 1
        else:
            raise TypeError("В серии и номере паспорта должны быть только цифры")

        if cls.len_series == len(value.split(" ")[0]):
            checking += 1
        else:
            raise TypeError("Введите серию паспорта из 4 цифр и номер паспорта из 6, разделенных пробелом")

        if cls.len_num == len(value.split(" ")[1]):
            checking += 1
        else:
            raise TypeError("Введите серию паспорта из 4 цифр и номер паспорта из 6, разделенных пробелом")

        return checking

    @classmethod
    def verify_weight(cls, value):
        checking = 0

        if cls.type_weight == type(value):
            checking += 1
        else:
            raise TypeError("Введите вес с точностью до десятых, например, 65.0")

        if cls.min_weight <= value:
            checking += 1
        else:
            raise TypeError("Вес должен быть не меньше 25 кг")

        return checking

p = Person('Иванов Иван Иванович', 50, '2222 333333', 85.0)

print(p.fio)
print(p.age)
print(p.passport)
print(p.weight)

p.fio = "Антон Павлович Чехов"
p.age = 35
p.passport = "1111 999999"
p.weight = 75.0

print(p.fio)
print(p.age)
print(p.passport)
print(p.weight)