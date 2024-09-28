class Player:
    def __init__(self, job, salary):
        self.set_job(job)
        self.set_salary(salary)
        self.set_bank(0)

    def get_job(self, job):
        return self.__job

    def set_job(self, job):
        self.__job = job

    def get_salary(self, salary):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    def get_bank(self):
        return self.__bank

    def set_bank(self, income):
        self.__bank = income

    bank = property(get_bank, set_bank)

    

player1 = Player("Mechanic", 1000)
player1.set_bank(1000)
print(player1.get_bank())
