import random
import string
def generate_random_word(N):
    letters = string.ascii_lowercase + 'абвгдеєжзиіїйклмнопрстуфхцчшщьюя'
    return ''.join(random.choice(letters) for i in range(N))
M = int(input("Введіть кількість слів M: "))
N = int(input("Введіть довжину кожного слова N: "))
words = [generate_random_word(N) for i in range(M)]
result = ' '.join(words)
print(result)
