class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'profit': wage, 'bonus': bonus}

class Position(Worker):
    def get_full_name(self):
        return f'Полное имя сотрудника: {self.name} {self.surname}'

    def get_total_income(self):
        return f'Зарплата сотрудника {sum(self._income.values())}'

manager = Position('Petr', 'Petrov', 'Boss', 100000, 30000)
print(manager.get_full_name())
print(manager.position)
print(manager.get_total_income())