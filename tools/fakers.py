from faker import Faker

class Fake:
    """
    Класс для генерации случайных данных.
    """
    def __init__(self, faker: Faker):
        """
        :param faker: экземпляр класса Faker, который будет использоваться для генерации случайных данных.
        """
        self.faker = faker

    def text(self) -> str:
        """
        Генерирует случайный текст.
        :return: Строка со случайным текстом (str).
        """
        return self.faker.text()

    def uuid4(self) -> str:
        """
        Генерирует случайный UUID4.
        :return: Строка с UUID4 (str).
        """
        return self.faker.uuid4()

    def email(self) -> str:
        """
        Генерирует случайный Email.
        :return: Строка со случайным Email (str).
        """
        return self.faker.email()

    def sentence(self) -> str:
        """
        Генерирует случайное предложение.
        :return: Строка со случайным предложением (str).
        """
        return self.faker.sentence()

    def password(self) -> str:
        """
        Генерирует случайный пароль.
        :return: Строка со случайным паролем (str).
        """
        return self.faker.password()

    def last_name(self) -> str:
        """
        Генерирует случайный LastName.
        :return: Строка со случайным LastName (str).
        """
        return self.faker.last_name()

    def first_name(self) -> str:
        """
        Генерирует случайный FirstName.
        :return: Строка со случайным FirstName (str).
        """
        return self.faker.first_name()

    def middle_name(self) -> str:
        """
        Генерирует случайный MiddleName.
        :return: Строка со случайным MiddleName (str).
        """
        return self.faker.first_name()

    def integer(self, start: int = 1, end: int = 100) -> int:
        """
        Генерирует случайное целое число.
        :param start: Минимальное значение случайного числа.
        :param end: Максимальное значение случайного числа.
        :return: Случайное целое число (int).
        """
        return self.faker.random_int(min=start, max=end)

    def estimated_time(self) -> str:
        """
        Генерирует случайный период времени.
        :return: Случайный период времени (str).
        """
        return f"{self.integer(start=1, end=10)} weeks"

    def max_score(self) -> int:
        """
        Генерирует случайное значение поля maxScore.
        :return: Случайное значение поля maxScore от 50 до 100 (int)
        """
        return self.integer(start=50, end=100)

    def min_score(self) -> int:
        """
        Генерирует случайное значение поля minScore.
        :return: Случайное значение поля maxScore от 0 до 30 (int)
        """
        return self.integer(start=0, end=30)

fake = Fake(faker=Faker())