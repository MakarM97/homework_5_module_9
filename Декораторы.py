def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if is_prime_number(result):
            print("Простое")
        else:
            print("Составное")
        return result

    def is_prime_number(num):
        if num <= 1:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        i = 3
        while i * i <= num:
            if num % i == 0:
                return False
            i += 2
        return True

    return wrapper
@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)