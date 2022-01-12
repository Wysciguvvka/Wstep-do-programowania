class Employee:
    def __init__(self, first_name, last_name, annual_salary):
        if not isinstance(first_name, str) or not isinstance(last_name, str):
            raise TypeError("Nazwa nie jest typu str")
        if not isinstance(annual_salary, (int, float)):
            raise TypeError("Wartość wypłaty nie jest liczbą")
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, raise_amt=2000):
        if not isinstance(raise_amt, (int, float)):
            raise TypeError("Wartość podwyżki nie jest liczbą")
        self.annual_salary += raise_amt
