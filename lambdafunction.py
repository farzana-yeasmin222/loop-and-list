# Problem 2:
words = ["hi", "python", "is", "cool", "code", "a"]
check = lambda w: len(w) > 3
long_words = [word for word in words if check(word)]
print(long_words) 

# problem 1:

#The Challenge: You are given a list of product prices. You need to write a function that takes this list and a "Discount Percentage." Inside the function, use a list comprehension to create a new list where each price is reduced by that percentage.

prices = [100, 250, 400, 50]
def calculate_discount(product_prices, discount):
    calculated_percentage = discount / 100
    reduced_price = [price - (price * calculated_percentage) for price in product_prices]
    return reduced_price


x = calculate_discount(prices,5)
print(x)



