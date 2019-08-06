letter = input()
vowel = ['a', 'e', 'i', 'o', 'u']
status = letter.isalpha()
if status:
    if letter in vowel:
        print("Vowel")
    else:
        print("Consonant")
else:
    print("invalid")
