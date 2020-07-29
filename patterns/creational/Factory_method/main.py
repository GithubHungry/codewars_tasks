from abc import abstractmethod, ABC


class Creator(ABC):
    """
        Класс Создатель объявляет фабричный метод, который должен возвращать объект
        класса Продукт. Подклассы Создателя обычно предоставляют реализацию этого
        метода.
    """

    @abstractmethod
    def factory_method(self):
        """
                Возможна реализация фабричного метода по умолчанию.
        """
        pass

    def other_operation(self) -> str:
        """
            Здесь описывается базовая бизнес-логика класса(создателя), кот. основана на объектах Продуктов,
            возвращаемыъ фабричным методом. одклассы могут косвенно изменять эту
            бизнес-логику, переопределяя фабричный метод и возвращая из него другой
            тип продукта.
        """
        # Вызываем фабричный метод, чтобы получить объект-продукт.
        product = self.factory_method()

        # Далее, работаем с этим продуктом.
        result = 'Creator worked with: {}'.format(product.operation())

        return result


"""
    Конкретные Создатели переопределяют фабричный метод для того, чтобы изменить тип
    результирующего продукта.
"""


class ConcreteCreator1(Creator):
    """
        Обратите внимание, что сигнатура метода по-прежнему использует тип
        абстрактного продукта, хотя фактически из метода возвращается конкретный
        продукт. Таким образом, Создатель может оставаться независимым от конкретных
        классов продуктов.
    """

    def factory_method(self) -> 'ConcreteProduct1':
        return ConcreteProduct1()


class ConcreteCreator2(Creator):
    def factory_method(self) -> 'ConcreteProduct2':
        return ConcreteProduct2()


class Product(ABC):
    """
        Интерфейс Продукта объявляет операции, которые должны выполнять все
        конкретные продукты.
    """

    @abstractmethod
    def operation(self) -> str:
        pass


"""
    Конкретные Продукты предоставляют различные реализации интерфейса Продукта.
"""


class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct1}"


class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct2}"


def client_code(creator: Creator) -> None:
    """
    Клиентский код работает с экземпляром конкретного создателя, хотя и через
    его базовый интерфейс. Пока клиент продолжает работать с создателем через
    базовый интерфейс, вы можете передать ему любой подкласс создателя.
    """

    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.other_operation()}", end="")


if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1.")
    client_code(ConcreteCreator1())
    print("\n")

    print("App: Launched with the ConcreteCreator2.")
    client_code(ConcreteCreator2())
