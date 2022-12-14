class Shoes:
    def __init__(self, name, price):
        self.name = name
        self.price = float(price)

    def check_budget(self, budget):
        if not isinstance(budget, (int, float)):
            print("Invalid entry! Please enter a number.")

    def change(self, budget):
        return budget - self.price

    def buy(self, budget):
        self.check_budget(budget)

        if budget >= self.price:
            print(f"You can cop some {self.name}")
            if budget == self.price:
                print("You have the exact amount of money to buy these shoes.")

            else:
                print(
                    f"You can buy these shoes and you have ${self.change(budget)} for a change"
                )
            exit()
