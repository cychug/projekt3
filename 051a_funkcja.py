def hello(name):
    great = "Hi " + name
    print(great)


hello("Chris")


def hello1(name):
    return "Hi " + name


print(hello1("Chris"))


def tip_amount(amount, percentage):
  return amount + amount * percentage / 100


amount = float(input("Amount: "))
percentage = float(input("Percentage: "))
print("Amount: $", amount, "percentage", percentage, "%", "Total amount: $", tip_amount(amount, percentage))
