<<<<<<< HEAD
def prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if prime(num)]

n = input().split()

numbers = list(map(int, n))
=======
def prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if prime(num)]

n = input().split()

numbers = list(map(int, n))
>>>>>>> 2a979e4717352ef20e11fce5aa6c52f3c54e7091
print(filter_prime(numbers))