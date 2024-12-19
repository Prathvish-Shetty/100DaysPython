# new_list = [new_item for item in list if test]

numbers = [1, 2, 3]
new_numbers = [number+1 for number in numbers]
print(numbers)
print(new_numbers)

name = "India"
letters_list = [letter for letter in name]
print(letters_list)

range_list = [i*2 for i in range(0, 5)]
print(range_list)

alphabets = ['a', 'b', 'c', 'dd']
short_alphabet = [alphabet.upper() for alphabet in alphabets if len(alphabet) < 2]
print(short_alphabet)