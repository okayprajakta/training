# x=["hello","hell"]
# y= filter(lambda x: len(x)>3,x)
# print(list(y))y


#x = sorted(x, key= lambda y : y[0])

def freak(x):
    print("Hello", x[0], x[1])
    return x[0]
 
 
x = [(1, "Pizza"),(4, "Pasta"),(2, "shake"),(3,"Cake")]
x = sorted(x, key = freak)
print(x)

# Example: Sorting by length of strings
words = ['banana', 'apple', 'cherry', 'date']
sorted_by_length = sorted(words, key=len)
print(sorted_by_length)  

# Example: Sorting a list of tuples by the second element
data = [(1, 'one'), (3, 'three'), (2, 'two')]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data) 