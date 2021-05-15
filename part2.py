class Personal:
    def __init__(self, fullname, personal_id):
        self.fullname = fullname
        self.personal_id = personal_id
        self.salary = 0
        self.count_of_hours = 0
        self.productivity = 0

    def calculate_productivity(self):
        return f'Процент продуктивности: {self.count_of_hours * 100 / 40}'

    def calculate_salary(self, *args):
        return args


class Manager(Personal):
    def __init__(self, fullname, personal_id, salary, count_of_hours):
        super().__init__(fullname, personal_id)
        self.salary = salary
        self.count_of_hours = count_of_hours
        self.productivity = count_of_hours * 100 / 40

    def calculate_salary(self):
        return f'Имя: {self.fullname}\nПерсональный номер: {self.personal_id}\nЗаработная плата: {self.salary}'


class Secretary(Personal):
    def __init__(self, fullname, personal_id, salary, count_of_hours):
        super().__init__(fullname, personal_id)
        self.salary = salary
        self.count_of_hours = count_of_hours
        self.productivity = count_of_hours * 100 / 40

    def calculate_salary(self):
        return f'Имя: {self.fullname}\nПерсональный номер: {self.personal_id}\nЗаработная плата: {self.salary}'


class Seller(Personal):
    def __init__(self, fullname, personal_id, salary, count_of_sales, count_of_hours):
        super().__init__(fullname, personal_id)
        self.salary = salary + count_of_sales * 50
        self.count_of_sales = count_of_sales
        self.count_of_hours = count_of_hours
        self.productivity = count_of_hours * 100 / 40

    def calculate_salary(self):
        return f'Имя: {self.fullname}\nПерсональный номер: {self.personal_id}\n' \
               f'Заработная плата: {self.salary}'


class ShopWorker(Personal):
    def __init__(self, fullname, personal_id, count_of_hours):
        super().__init__(fullname, personal_id)
        self.count_of_hours = count_of_hours
        self.salary = count_of_hours * 100
        self.productivity = count_of_hours * 100 / 40

    def calculate_salary(self):
        return f'Имя: {self.fullname}\nПерсональный номер: {self.personal_id}\n' \
               f'Заработная плата: {self.salary}'


class ReplacementSecretary(Personal):
    def __init__(self, fullname, personal_id, count_of_hours):
        super().__init__(fullname, personal_id)
        self.count_of_hours = count_of_hours
        self.salary = count_of_hours * 100
        self.productivity = count_of_hours * 100 / 40

    def calculate_salary(self):
        return f'Имя: {self.fullname}\nПерсональный номер: {self.personal_id}\n' \
               f'Заработная плата: {self.salary}'


manager = Manager('Барсбек Канаткулов', 1, 45000, 18)
print(manager.calculate_salary())
print(manager.calculate_productivity())
print()

secretary = Secretary('Алымкул Тилекбаев', 2, 20000, 38)
print(secretary.calculate_salary())
print(secretary.calculate_productivity())
print()

seller = Seller('Айпери Шалымбекова', 3, 20000, 20, 38)
print(seller.calculate_salary())
print(seller.calculate_productivity())
print()

shop_worker_1 = ShopWorker('Бакыт Рустамов', 4, 25)
print(shop_worker_1.calculate_salary())
print(shop_worker_1.calculate_productivity())
print()

shop_worker_2 = ShopWorker('Алтынай Ширинбаева', 5, 40)
print(shop_worker_2.calculate_salary())
print(shop_worker_2.calculate_productivity())
print()

replacement_secretary = ReplacementSecretary('Жанар Рыскулов', 6, 33)
print(replacement_secretary.calculate_salary())
print(replacement_secretary.calculate_productivity())
print()

amount = 0
lst = [manager, secretary, seller, shop_worker_1, shop_worker_2, replacement_secretary]
for i in lst:
    amount += i.salary
print(f'Общая сумма: {amount}')

lst2 = [i.productivity for i in lst]
the_most_productive = {}
the_most_unproductive = {}
for i in lst:
    if max(lst2) == i.productivity:
        the_most_productive[i.fullname] = i.productivity
    elif min(lst2) == i.productivity:
        the_most_unproductive[i.fullname] = i.productivity
print(f'Самый продуктивный: {the_most_productive}')
print(f'Самый непродуктивный: {the_most_unproductive}')
