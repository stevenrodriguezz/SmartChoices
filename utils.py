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

interest = {
    "credit": 1.3,
    "investment": 1.1,
    "student loans": 1.05
}

class Player:
    def __init__(self, job, salary, credit_score, student_loans):
        self.set_logged_in(False)
        self.set_job(job)
        self.set_salary(salary)
        self.set_bank(0)
        self.set_debt(0)
        self.set_investment_account(0)
        self.set_credit_score(credit_score)
        self.set_student_loans(student_loans)
        self.set_taxes(salary)
        self.set_monthly_income()
        self.set_monthly_taxes()
        self.set_credit_limit()

    def get_logged_in(self):
        return self.__logged_in

    def set_logged_in(self, is_logged_in):
        self.__logged_in = is_logged_in

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

    def get_debt(self):
        return self.__debt

    def set_debt(self, debt):
        self.__debt = round(debt, 2)

    def get_investment_account(self):
        return self.__investment_account

    def set_investment_account(self, money):
        self.__investment_account = round(money, 2)

    def get_credit_score(self):
        return self.__credit_score

    def set_credit_score(self, credit_score):
        self.__credit_score = credit_score

    def get_student_loans(self):
        return self.__student_loans

    def set_student_loans(self, debt):
        self.__student_loans = debt
    
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

    def get_monthly_taxes(self):
        return self.__monthly_taxes

    def set_monthly_taxes(self):
        self.__monthly_taxes = round(((self.get_taxes()) / 12), 2)

    def get_credit_limit(self):
        return self.__credit_limit

    def set_credit_limit(self):
        multiplier = 1
        if self.get_credit_score() < 400:
            multiplier = 0.25
        elif self.get_credit_score() < 500:
            multiplier = 0.5
        elif self.get_credit_score() < 600:
            multiplier = 0.75
        elif self.get_credit_score() < 700: 
            multiplier = 1
        elif self.get_credit_score() < 800:
            multiplier = 1.25
        else:
            multiplier = 1.5
        self.__credit_limit = round(self.get_monthly_income() * multiplier - self.get_debt(), 2)


    job = property(get_job, set_job)
    salary = property(get_salary, set_salary)
    bank = property(get_bank, set_bank)
    credit_score = property(get_credit_score, set_credit_score)
    debt = property(get_debt, set_debt)
    taxes = property(get_taxes, set_taxes)
    monthly_income = property(get_monthly_income, set_monthly_income)
    monthly_taxes = property(get_monthly_taxes, set_monthly_taxes)
    credit_limit = property(get_credit_limit, set_credit_limit)

    def bank_transaction(self, money):
        self.set_bank(self.get_bank() + money)

    def debt_transaction(self, debt):
        self.set_debt(self.get_debt() + debt)

    def debt_accrual(self):
        self.set_debt(self.get_debt() * interest["credit"])

    def investment_transaction(self, money):
        self.set_investment_account(self.get_investment_account() + money)

    def investment_accrual(self):
        self.set_investment_account(self.get_investment_account() * interest["investment"])

    def student_loans_transaction(self, money):
        self.set_student_loans(self.get_student_loans() + money)

    def student_loans_accrual(self):
        self.set_student_loans(self.get_student_loans() * interest["student loans"])

    def round_start_routine(self):    
        self.bank_transaction(self.get_monthly_income())


def start_game(players):
    for player in players:
        player.round_start_routine()
        print(f"""Your job is {player.get_job()} \n your salary is {player.get_salary()} so you make {round(player.get_salary() / 12, 2)} per month \n
                you pay {round(player.get_monthly_taxes(), 2)} in taxes, thus your income is {player.get_monthly_income()} per month \n
                you have {player.get_bank()} in bank \n your credit score is {player.get_credit_score()} \n 
                you have {player.get_debt()} debt \n your credit limit is {player.get_credit_limit()} \n
                you have {player.get_investment_account()} money invested \n
                you have {player.get_student_loans()} in student loans \n \n""")