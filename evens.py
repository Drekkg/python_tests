# def even_number_of_evens(numbers):
#     """
#     Should raise a type error if a list is not passe into the function
#     error: message: "Anlist was not passed into the function"
#     if the number is empty return false
#     if the number of even numbers is odd return false
#     if the number of even numbers is 0 return false
#     if the number of even numbers is even return True
#     """
#     if isinstance(numbers, list):
#         evens = sum([1 for n in numbers if n % 2 == 0])
#         return True if evens and evens % 2 == 0 else False
#     else:
#         raise TypeError("A list was not passed into the function")

#     return (True)


# if __name__ == '__main__':
#     print(even_number_of_evens(5))
