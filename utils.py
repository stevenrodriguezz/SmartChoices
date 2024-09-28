#########################################
# For Steven: OOP example
#########################################
# class Rectangle:
#     def __init__(self):
#         self.length = 10
#         self.width = 15

#     def calculate_area(self):
#         return self.length * self.width

# square1 = Rectangle()
# print(square1.calculate_area())
#########################################

tax_per_bracket = [0.1, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37]
income_per_bracket = [11600, 47150, 100525, 191950, 243725, 609350]

prior_bracket_taxes = [(income_per_bracket[0] * tax_per_bracket[0]),
                    ((income_per_bracket[1] - income_per_bracket[0]) * tax_per_bracket[1]),
                    ((income_per_bracket[2] - income_per_bracket[1]) * tax_per_bracket[2]),
                    ((income_per_bracket[3] - income_per_bracket[2]) * tax_per_bracket[3]),
                    ((income_per_bracket[4] - income_per_bracket[3]) * tax_per_bracket[4]),
                    ((income_per_bracket[5] - income_per_bracket[4]) * tax_per_bracket[5])]

class Player:
    def __init__(self, job, salary):
        self.set_job(job)
        self.set_salary(salary)
        self.set_bank(0)
        self.set_taxes(salary)
        self.set_monthly_income()

    def get_job(self):
        return self.__job

    def set_job(self, job):
        self.__job = job

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    def get_bank(self):
        return self.__bank

    def set_bank(self, money):
        self.__bank = round(money, 2)
    
    def get_taxes(self):
        return self.__taxes

    def set_taxes(self, salary):
        if self.get_salary() < income_per_bracket[0]:
            self.__taxes = round(self.get_salary() * tax_per_bracket[0], 2)

        elif self.get_salary() < income_per_bracket[1]:
            self.__taxes = round(prior_bracket_taxes[0] + 
                            ((self.get_salary() - income_per_bracket[0]) * tax_per_bracket[1]), 2)

        elif self.get_salary() < income_per_bracket[2]:
            self.__taxes = round(prior_bracket_taxes[0] + prior_bracket_taxes[1] 
                            + ((self.get_salary() - income_per_bracket[1]) * tax_per_bracket[2]), 2)

        elif self.get_salary() < income_per_bracket[3]:
            self.__taxes = round(prior_bracket_taxes[0] + prior_bracket_taxes[1] + prior_bracket_taxes[2]
                            + ((self.get_salary() - income_per_bracket[2]) * tax_per_bracket[3]), 2)

        elif self.get_salary() < income_per_bracket[4]:
            self.__taxes = round(prior_bracket_taxes[0] + prior_bracket_taxes[1] + prior_bracket_taxes[2]
                            + prior_bracket_taxes[3] 
                            + ((self.get_salary() - income_per_bracket[3]) * tax_per_bracket[4]), 2)

        elif self.get_salary() < income_per_bracket[5]:
            self.__taxes = round(prior_bracket_taxes[0] + prior_bracket_taxes[1] + prior_bracket_taxes[2]
                            + prior_bracket_taxes[3] + prior_bracket_taxes[4]
                            + ((self.get_salary() - income_per_bracket[4]) * tax_per_bracket[5]), 2)
        
        elif self.get_salary() < income_per_bracket[6]:
            self.__taxes = round(prior_bracket_taxes[0] + prior_bracket_taxes[1] + prior_bracket_taxes[2]
                            + prior_bracket_taxes[3] + prior_bracket_taxes[4] + prior_bracket_taxes[5]
                            + ((self.get_salary() - income_per_bracket[5]) * tax_per_bracket[6]), 2)

    def get_monthly_income(self):
        return self.__monthly_income

    def set_monthly_income(self):
        self.__monthly_income = round(((self.get_salary() - self.get_taxes()) / 12), 2)

    job = property(get_job, set_job)
    salary = property(get_salary, set_salary)
    bank = property(get_bank, set_bank)
    taxes = property(get_taxes, set_taxes)
    monthly_income = property(get_monthly_income, set_monthly_income)

    def bank_transaction(self, money):
        self.set_bank(self.get_bank() + money)

    def round_start_routine(self):    
        self.bank_transaction(self.get_monthly_income())


def start_game(players):
    for player in players:
        player.round_start_routine()
        print(f"""Your job is {player.get_job()} \n your salary is {player.get_salary()} so you make {round(player.get_salary() / 12, 2)} per month \n
                you pay {round(player.get_taxes() / 12, 2)} in taxes, thus your income is {player.get_monthly_income()} per month \n
                you have {player.get_bank()} in bank \n \n""")