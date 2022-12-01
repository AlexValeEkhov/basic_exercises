# Вывести последнюю букву в слове
word = 'Архангельск'
# ???

print('Задание: Вывести последнюю букву в слове:')
letters = list(word)
print(letters[-1])


# Вывести количество букв "а" в слове
print('Вывести количество букв "а" в слове:')
word = 'Архангельск'
# ???

c = 0
for letter in word:
    if letter.capitalize() == "А":
        c += 1

print(c)

# Вывести количество гласных букв в слове
word = 'Архангельск'
# ???

print('Вывести количество гласных букв в слове:')
alphabet = ['А', 'О', 'У', 'Ы', 'Э', 'Е', 'Ё', 'И', 'Ю', 'Я']
c = 0
for letter in word:
    if letter.capitalize() in alphabet:
        c += 1
print(c)    


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
# ???

print('Вывести количество слов в предложении:')
words = sentence.split()
print(len(words))

# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
# ???

print('Вывести первую букву каждого слова на отдельной строке:')
words = sentence.split()
for word in words:
    letters = list(word)
    print(letters[0])

# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
# ???

print('Вывести усреднённую длину слова в предложении:')
words = sentence.split()
letter_total = 0
for word in words:
    letter_total += len(word)
print(letter_total/len(words))

# Другой вариант решения.

words = sentence.split()
letters = sentence.replace(" ", '')
print(len(letters)/len(words))
