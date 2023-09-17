import random

chars = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
def random_string(n: int):
    b = [random.choice(chars) for _ in range(n)]
    return ''.join(b)
