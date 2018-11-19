class Animal:
    weight = 0  # kg
    name = ""
    voice = ""

    def __init__(self, name, voice, weight):
        self.name = name
        self.voice = voice
        self.weight = weight

    def feed(self, food):
        self.weight += food * 0.05

    def check_kind(self):
        return self.voice


class MilkAnimal(Animal):
    milk_count = 0  # liter
    sex = "male"

    def __init__(self, name, voice, weight, sex="male"):
        super().__init__(name, voice, weight)
        self.milk_count = 0
        self.sex = sex

    def feed(self, food):
        super().feed(food)
        if self.sex == "female":
            self.milk_count += food * 0.15

    def milk(self):
        if self.sex == "male":
            print("Самца доить нельзя")
            return 0
        take_milk = self.milk_count
        self.milk_count = 0
        return take_milk

    def check_kind(self):
        voice = super().check_kind()
        if voice.lower() == "мууу":
            return "Корова"
        elif voice.lower() == "меее":
            return "Коза"
        else:
            return "Млекопитающее"


class Bird(Animal):
    eggs_count = 0
    sex = "male"

    def __init__(self, name, voice, weight, sex="male"):
        super().__init__(name, voice, weight)
        self.eggs_count = 0
        self.sex = sex

    def feed(self, food):
        super().feed(food)
        if self.sex == "female":
            self.eggs_count += 1

    def take_eggs(self):
        if self.sex == "male":
            print("Самцы яиц не несут")
            return 0
        eggs = self.eggs_count
        self.eggs_count = 0
        return eggs

    def check_kind(self):
        voice = super().check_kind()
        if voice.lower() == "ко-ко-ко":
            return "Курица"
        elif voice.lower() == "кря-кря":
            return "Утка"
        elif voice.lower() == "га-га-га":
            return "Гусь"
        else:
            return "Птица"


class Sheep(Animal):
    wool = 0  # kg

    def __init__(self, name, voice, weight):
        super().__init__(name, voice, weight)
        self.wool = 0

    def feed(self, food):
        super().feed(food)
        self.wool += 0.5

    def cut_wool(self):
        wool_count = self.wool
        self.wool = 0
        return wool_count

    def check_kind(self):
        return "Овца"


cow = MilkAnimal("Манька", "Мууу", 350, "female")
goose1 = Bird("Серый", "Га-га-га", 10, "female")
goose2 = Bird("Белый", "Га-га-га", 12)
chicken1 = Bird("Ко-ко", "Ко-ко-ко", 2, "female")
chicken2 = Bird("Кукареку", "Ко-ко-ко", 3)
duck = Bird("Кряква", "Кря-кря", 6, "female")
sheep1 = Sheep("Барашек", "Беее", 43)
sheep2 = Sheep("Кудрявый", "Беее", 39)
goat1 = MilkAnimal("Рога", "Меее", 50, "female")
goat2 = MilkAnimal("Копыта", "Меее", 54)

animals = [goose1, goose2, chicken1, chicken2, cow, duck, sheep1, sheep2, goat1, goat2]

cow.feed(20)
goose1.feed(3)
goose2.feed(3)
chicken1.feed(1)
chicken2.feed(2)
duck.feed(2.5)
sheep1.feed(9)
sheep2.feed(12)
goat1.feed(7)
goat2.feed(9)

take_eggs = goose1.take_eggs() + goose2.take_eggs() + duck.take_eggs() + chicken1.take_eggs() + chicken2.take_eggs()
take_milk = cow.milk() + goat1.milk() + goat2.milk()
take_wool = sheep1.cut_wool() + sheep2.cut_wool()



sum_weight = 0
max_weight = 0
max_weight_animal = ""
for animal in animals:
    sum_weight += animal.weight
    if max_weight < animal.weight:
        max_weight = animal.weight
        max_weight_animal = animal.check_kind()

print("Общий вес всех животных: {} кг".format(sum_weight))
print("Самый большой вес имеет {}. Вес составляет {} кг".format(max_weight_animal, max_weight))
print("Получено шерсти: {} кг".format(take_wool))
print("Получено яиц: {} шт".format(take_eggs))
print("Получено молока: {} л".format(take_milk))



