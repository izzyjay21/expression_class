class Expression:
  def __init__(self, num1, num2, num3):
      self.num1 = num1
      self.num2 = num2
      self.num3 = num3

  def calculate_addition(self):
      total = self.num1 + self.num2 + self.num3
      return total

# Creating objects and calling the method to calculate the addition
expression1 = Expression(5, 10, 15)
result1 = expression1.calculate_addition()
print(f"The addition of numbers {expression1.num1}, {expression1.num2}, and {expression1.num3} is: {result1}")

expression2 = Expression(2, 3, 4)
result2 = expression2.calculate_addition()
print(f"The addition of numbers {expression2.num1}, {expression2.num2}, and {expression2.num3} is: {result2}")