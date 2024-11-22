import random

def sum_odd_even(arr):
    odd_sum = sum(num for num in arr if num % 2 != 0)
    even_sum = sum(num for num in arr if num % 2 == 0)
    return odd_sum, even_sum

random_numbers = [random.randint(1, 100) for _ in range(10)]
odd_sum, even_sum = sum_odd_even(random_numbers)
print(f"Random numbers: {random_numbers}\nSum of odd numbers: {odd_sum}\nSum of even numbers: {even_sum}")
