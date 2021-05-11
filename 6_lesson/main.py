# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.

'''
#Возможно не правильно понял задачу, но реализовал так вот:
from time import sleep

class TrafficLight:

    def running(self):
        __color = {'Красный': 7, 'Желтый': 2, 'Зеленый': 5} #хотел использовать как словать, но что то не пошло...
        i = 0
        while i <= 3: # было 2, но потом целенаправленно сделал бесконечный цикл
            if i == 0:
                print('Красный (7 сек)')
                sleep(7)
                i += 1
            elif i ==1:
                print('Желтый (2 сек)')
                sleep(2)
                i += 1
            elif i == 2:
                print('Зеленый (8 сек)')
                sleep(5)
                i += 1
            else:
                i = 0

run = TrafficLight()
run.running()
'''

# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * число см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т

'''
class Road:

    def __init__(self, lenght, width):
        self.lenght = lenght # длина
        self.width = width #ширина
        self.mass = 25 # масса
        self.depth = 5 # толщина

    def mass_asphalt(self):
        return self.lenght * self.width * self.mass * self.depth

road = Road(2,2)
print(road.mass_asphalt())
'''

# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

'''
class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self, name, surname, position, salary, prize):  # по уроку думал тут не обязательно их указывать, но без них не хотел работать?
        super().__init__(name, surname, position, salary, prize)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus') # что то get я долго "искал" и понимал...


worker = Position('Иван', 'Петров', 'Менеджер', 25000, 10000)
print(worker.get_full_name())
print(worker.get_total_income())
'''


# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

'''
class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
        return f'{self.name} движется'

    def stop(self):
        return f'{self.name} остановился'

    def show_speed(self):
        return f'{self.name} едет со скоростью {self.speed}'



# с направлением признаться не понял что и как сделать, написал "предположение", надо только новый параметр передавать
#    def turn(self, direction):
#       if direction = 'Left':
#            return f'{self.name} повернул налево'
#        if direction = 'right':
#            return f'{self.name} повернул направо'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f'{self.name} Превышает скорость!{self.speed}'
        else:
            return f'{self.name} едет со скоростью {self.speed}'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f'{self.name} Превышает скорость!{self.speed}'
        else:
            return f'{self.name} едет со скоростью {self.speed}'


class PoliceCar(Car):  # в задаче не было указано что делать с этим классом. Предположил,но наверное такое надо в каждый класс вшить проверку.
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police_chek(self):
        if self.is_police == 1:
            return f'{self.name} полицейский транспорт'
        else:
            return f'{self.name} гражданский транспорт'


car_1 = Car(100, 'Синий', 'BMW', 0)
print(car_1.go())
print(car_1.stop())
print(car_1.show_speed())
print('*******' * 5)
town_car = TownCar(40, 'красный', 'Nissan', 0)
print(town_car.go())
print(town_car.stop())
print(town_car.show_speed())
print('*******' * 5)
town_car_2 = TownCar(90, 'красный', 'Nissan', 0)
print(town_car_2.go())
print(town_car_2.stop())
print(town_car_2.show_speed())
print('*******' * 5)
sport_car = SportCar(70, 'зеленый', 'Lada', 0)
print(sport_car.go())
print(sport_car.stop())
print(sport_car.show_speed())
print('*******' * 5)
work_car = WorkCar(20, 'зеленый', 'Lada', 0)
print(work_car.go())
print(work_car.stop())
print(work_car.show_speed())
print('*******' * 5)
work_car_2 = WorkCar(120, 'зеленый', 'Audi', 0)
print(work_car_2.go())
print(work_car_2.stop())
print(work_car_2.show_speed())
print('*******' * 5)
police_car = PoliceCar(60, 'белый', 'Hummer', 1)
print(police_car.go())
print(police_car.stop())
print(police_car.show_speed())
print(police_car.police_chek())
print('*******' * 5)
'''

# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

'''
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки {self.title}.'
        
class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Нарисованно {self.title}'

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Нарисованно {self.title}'

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'нарисованно {self.title}'


kanz = Stationery('канцеляркой')
print(kanz.draw())
pen = Pen('ручкой')
print(pen.draw())
pencil = Pencil('карандашом')
print(pencil.draw())
handle = Handle('маркером')
print(handle.draw())
'''
