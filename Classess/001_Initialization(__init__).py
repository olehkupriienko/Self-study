class Point2D:
    """Точка на плоскости."""

    # Инициализирующий метод (специальный метод с __)
    def __init__(self, x, y):
        self.x = x  # Поля читаются и записываются через 'self'
        self.y = y  # 'self' указывает на текущий экземпляр класса

    # Обычный метод объекта (метод экземпляра класса) имеет те же правила,
    # наименования, что и обычные функции
    def distance_to_zero_point(self):
        """Вернуть расстояние до центра координат."""
        return (self.x**2 + self.y**2)**0.5


if __name__ == "__main__":

    print(Point2D)
    print(Point2D.distance_to_zero_point)

    # Создание объекта (экземпляра класса)
    # Передаем параметры, которые теперь требует '__init__()'
    # Параметр 'self' не передается явно, но содержит ссылку на 'p'
    point1 = Point2D(3, 4)
    point2 = Point2D(10, 25)
    print(Point2D.distance_to_zero_point(point2))

    # При выводе объекта на экран по умолчанию отображается имя класса
    print(point1)
    print(point2)

    # После инициализации доступны атрибуты 'p.x' и 'p.y',
    # где хранятся переданные при создании объекта значения
    print(point1.x, point1.y)  # 3 4
    print(point2.x, point2.y)  # 10 25

    # Вызов обычного метода
    print(f"Расстояние до центра координат: {point1.distance_to_zero_point()}")  # 5
    print(f"Расстояние до центра координат: {round(point2.distance_to_zero_point(), 2)}")  # 26.93
    print(point2)