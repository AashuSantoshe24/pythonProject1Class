letters = ['a', 'b', 'c', 'd', 'e', 'f', 'i', 'j', 'k', 'l', 'm']
letters_tuple = ('a', 'b', 'c', 'd', 'e', 'f', 'i', 'j', 'k', 'l', 'm')
letters_list = {'a', 'b', 'c', 'd', 'e', 'f', 'i', 'j', 'k', 'l', 'm'}
#filters for vowels

def is_vowel(letters):
    vowel = ['a', 'e', 'i', 'o', 'u']
    return letters in vowel

def is_vowel_1(letters_tuple):
    vowel = ['a', 'e', 'i', 'o', 'u']
    return letters_tuple in vowel

result = is_vowel('p')
print(result)

vowels = filter(is_vowel, letters)
print(list(vowels))

vowel_tuple = filter(is_vowel_1, letters_tuple)
print(list(vowel_tuple))