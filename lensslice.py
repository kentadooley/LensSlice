# Your code below:
toppings = ["pepperoni", "pineapple", "Cheese","sausage", "olives", "anchovies", "mushrooms"]

#2 checkpoint 

price = [2, 6, 1, 3, 2, 7, 2]

#3 checkpoint
num_two_dollar_slices = price.count(2)
print(num_two_dollar_slices)

#4 Checkpoint
num_pizzas = len(toppings)


#5 Checkpoint
print("we sell", num_pizzas, "different kinds of pizza!")

#6 checkpoint
pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "Cheese"], [3, "Sausage"], [2, "olives"], [7, "anchovies"], [2, "muchrooms"]]

print(pizza_and_prices)

#Checkpoint 7 sorting and slicing pizza
pizza_and_prices.sort()
print(pizza_and_prices)

#checkpoint 9 cheapest pizza
cheapest_pizza = pizza_and_prices[0]
print(cheapest_pizza)

#checkpoint 10 most expensive pizza 
priciest_pizza = pizza_and_prices[-1]
print(priciest_pizza)

#checkpoint 11 remove anchovies
pizza_and_prices.pop(-1)
print(pizza_and_prices)


#checkpoint 12 adding peppers 
pizza_and_prices.insert(1,[2.5, "Peppers"])
pizza_and_prices.sort()
print(pizza_and_prices)


#checkpoint 13 + 14  three cheapest 
three_cheapest = pizza_and_prices[0:4]
print(three_cheapest)
