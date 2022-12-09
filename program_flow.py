hour = int(input('What is the hour in 24 hour format? '))
name = input('What is your name? ')
print('The hour is', hour)

if hour < 12:
   print(f'Good morning {name} 🌞')
elif hour < 16:
   print(f'Good afternoon {name} 🌞')
elif hour < 20:
    print(f'Good evening {name} 🌙')
else:
    print(f'Good night {name} 🌙')

if hour < 12:
    print(f'{hour }AM')
else:
    print(f'{hour - 12}PM')


score = float(input('What is your score? '))
print('I got', score)

if score >= 70:
    print(f'first class')
elif score >= 60:
    print(2.1) 
elif score >= 50:
    print(2.2)
elif score >= 40:
    print(f'third class')
else:
    print(f'fail')

for j in [0, 1, 2]:
    print(j)
print()
for j in range(3):
    print(j)
print()
i =0
for j in range(10):
    i+=5 # i = i + 5
    print(i)

range(10) # -> 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
range(3, 10) # 3, 4, 5, 6, 7, 8, 9
range(3, 10, 2) # -> 3, 5, 7, 9
range(2, 10, 3) # -> 2, 5, 8

for i in range(2, 30, 5):
    if i %11 == 0:
        print('A factor of 11 is seen, terminating loop....')
        break
    if i % 6 == 0:
        print('A factor of 6 is seen, moving to the next iteration...')
        continue
    print(i)

text = 'Python is second to none'
length = len(text)
print(length)
i = 0
while i < length:
    x = text[i]
    i += 1
    if x == 'y':
        continue
    if x == 'o':
        break
    print(x.upper())

for char in text:
    if char == 'y':
        continue
    if char == 'o':
        break
    print(char.upper())

word = input('Enter a sentence: ') # I am a boy that is 12 years old.
vowel_count = 0
consonant_count = 0
numbers_count = 0
special_characters_count = 0
for char in word:
    char = char.lower()
    if char.isalpha():
        if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
            vowel_count += 1
        else:
            consonant_count += 1
    elif char.isnumeric():
        numbers_count += 1
    else:
        special_characters_count +=1
print(f'There are {vowel_count} vowels in the sentence')
print(f'There are {consonant_count} consonants in the sentence')
print(f'There are {numbers_count} numbers in the sentence')
print(f'There are {special_characters_count} special characters in the sentence')


chr()

calculateAge = lambda birthYear: 2022 - birthYear
