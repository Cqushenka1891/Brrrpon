import random

class Pet:
    def __init__(self, mast="sobak", namee="Bober", hunger=100, schastie=100):
        self.mast = mast
        self.namee = namee
        self.hunger = hunger
        self.schastie = schastie

    def den_psa(self):
        self.hunger -= 5
        self.schastie -= 5
        print("𓃡𓃡𓃡𓃡𓃡𓃡𓃡𓃡𓃡𓃡𓃡Pios begal za hvostom𓃡𓃡𓃡𓃡𓃡𓃡𓃡𓃡𓃡𓃡𓃡")
        if self.hunger <= 0:
            self.jrat()
            print("𓃡𓃡𓃡𓃡𓃡𓃡𓃡𓃡𓃡𓃡𓃡Pios poel i stal tolsi𓃡𓃡𓃡𓃡𓃡𓃡𓃡𓃡𓃡𓃡𓃡")
        elif self.schastie <= 0:
            self.igrat()
            print("𓃡𓃡𓃡𓃡𓃡𓃡𓃡𓃡𓃡𓃡𓃡Pios poigral i stal veseliy𓃡𓃡𓃡𓃡𓃡𓃡𓃡𓃡𓃡𓃡𓃡")
        print("𓃡𓃡𓃡𓃡𓃡𓃡𓃡𓃡𓃡𓃡𓃡Konec dnya psa𓃡𓃡𓃡𓃡𓃡𓃡𓃡𓃡𓃡𓃡𓃡")



    def jrat(self):
        if self.hunger >= 100:
            self.hunger = 100
        else:
            self.hunger += 10
            self.home.food -= 5


    def igrat(self):
        self.schastie += 10

    def str(self):
        return f"{self.namee} is э {self.mast}, Eda:{self.hunger}, Schastie:{self.schastie}"
class Human:
    def __init__(self, name="Хуман", job=None, home=None, car=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home
        self.pet = Pet()

    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)

    def eat(self):
        if self.home.food <=0:
            self.shopping("food")
        else:
            if self.satiety >=100:
                self.satiety = 100
                return
            self.satiety+=5
            self.home.food-=5

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety-=4

    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                manage = "fuel"
            else:
                self.to_repair()
                return
        if manage == "fuel":
            print("============Я заправился============")
            self.money -= 100
            self.car.fuel += 100
        elif manage == "food":
            print("============Купил еды============")
            self.money -= 50
            self.home.food += 50
        elif manage == "delicacies":
            print("============Вкусно============")
            self.gladness+=10
            self.satiety+=2
            self.money-=15

    def chill(self):
        self.gladness+=10
        self.home.mess+=5

    def clean_home(self):
        self.gladness-=5
        self.home.mess = 0

    def to_repair(self):
        self.car.strength+=100
        self.money-=50

    def days_indexes(self, day):
        day = f" Today the {day} of {self.name}'s life "
        print(f"{day:=^50}")
        human_indexes = self.name + "'s indexes"
        print(f"{human_indexes:^50}")
        print(f"Деньги – {self.money}")
        print(f"СатиеЧо? – {self.satiety}")
        print(f"Счастье – {self.gladness}")
        home_indexes = "Home indexes"
        print(f"{home_indexes:^50}")
        print(f"Еда – {self.home.food}")
        print(f"Мусор – {self.home.mess}")
        car_indexes = f"{self.car.brand} car indexes"
        print(f"{car_indexes:^50}")
        print(f"Топливо – {self.car.fuel}")
        print(f"Мощьььь – {self.car.strength}")
        pet_indexes = "Jivotina indexes"
        print(f"{pet_indexes:^50}")
        print(f"Пиос голод - {self.pet.hunger}")
        print(f"Пиос счастие - {self.pet.schastie}")

    def is_alive(self):
        if self.gladness<0:
            print("============ДиПрИсИя…============")
            return False
        if self.satiety<0:
            print("============СмЭрт…============")
            return False
        if self.money<-500:
            print("============Банкрот…============")
            return False

    def live(self, day):
        self.pet.den_psa()
        if self.is_alive() == False:
            return False
        if self.home is None:
            print("============Чото там ин зе хаус============")
            self.get_home()
        if self.car is None:
            self.get_car()
            print(f"============Купил машину {self.car.brand}============")
        if self.job is None:
            self.get_job()
            print(f"============У меня нет работы.Пора устроиться {self.job.job} с моей зарплатой {self.job.salary}============")
        self.days_indexes(day)
        dice = random.randint(1,4)
        if self.satiety<20:
            print("============Пойду поем============")
            self.eat()
        elif self.gladness < 20:
            if self.home.mess>15:
                print("============Я хотел отдохнуть, но тут так грязно. . .\nПоэтому, пора убраться============")
                self.clean_home()
            else:
                print("============Пора отдохнуть============")
                self.chill()
        elif self.money<0:
            print("============Начал работать============")
            self.work()
        elif self.car.strength<15:
            print("============Я должон поченить мою машину============")
            self.to_repair()
        elif dice == 1:
            print("============Пора отдохнуть============")
            self.chill()
        elif dice == 2:
            print("============Начало работы============")
            self.work()
        elif dice == 3:
            print("============Уборка============")
            self.clean_home()
        elif dice == 4:
            print("============Время кариэса!============")
            self.shopping(manage="delicacies")

class Auto:
        def __init__(self, brand_list):
            self.brand = random.choice(list(brand_list))
            self.fuel = brand_list[self.brand]["fuel"]
            self.strength = brand_list[self.brand]["strength"]
            self.consumption = brand_list[self.brand]["consumption"]

        def drive(self):
            if self.strength > 0 and self.fuel >= self.consumption:
                self.fuel -= self.consumption
                self.strength -= 1
                return True
            else:
                print("The car cannot move")
                return False

brands_of_car = {
    "BMW":{"fuel":100, "strength":100, "consumption": 6},
    "Lada":{"fuel":50, "strength":40, "consumption": 10},
    "Volvo":{"fuel":70, "strength":150, "consumption": 8},
    "Ferrari":{"fuel":80, "strength":120, "consumption": 14},
    "Jigul":{"fuel": 60, "strength": 70,"consumption": 7},
    "KartoshkoMobil":{"fuel": 100, "strength": 100,"consumption": 5},
    "Gazel":{"fuel": 90, "strength": 80,"consumption": 10},
    "Avtobus!": {"fuel": 150, "strength": 150, "consumption": 8},
            }

class House:
    def __init__(self):
        self.mess = 0
        self.food = 0

job_list = {
    "Java developer":
    {"salary":50, "gladness_less": 10 },
    "Python developer":
    {"salary":40, "gladness_less": 3 },
    "C++ developer":
    {"salary":45, "gladness_less": 25 },
    "Rust developer":
    {"salary":70, "gladness_less": 1 },
    "Uborshik":
    {"salary":30, "gladness_less": 3},
    "Kassir":
    {"salary":40, "gladness_less": 10},
    "Voditel":
    {"salary":60, "gladness_less": 5},
    "Rabotnik zavoda":
    {"salary":40, "gladness_less": 10},
    "Povar":
    {"salary":60, "gladness_less": 3},
        }

class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]

nick = Human(name="Nick")

for day in range(1, 20):
    if nick.live(day) == False:
        break