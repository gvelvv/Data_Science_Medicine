class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        full_name = self.name + ' ' + self.surname
        return full_name

    def get_total_income(self):
        total = sum(self._income.values())
        return total


unit = Position('Ivan', 'Ivanov', 'CEO', 100, 20)
print(unit.get_full_name())
print(unit.get_total_income())
