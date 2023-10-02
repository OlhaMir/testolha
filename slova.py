input_string = input("Введіть рядок зі словами, розділеними комами і/або пробілами: ")
words =(r'[,\s]+', input_string)
min_length = float('inf')
max_length = 0
for word in words:
    word = word.strip() 
    word = word.replace(",", "") 
    word_length = len(word)
    if word_length > max_length:
        max_length = word_length
    if word_length < min_length:
        min_length = word_length
print(f"Найменше слово має довжину {min_length} символів.")
print(f"Найбільше слово має довжину {max_length} символів.")