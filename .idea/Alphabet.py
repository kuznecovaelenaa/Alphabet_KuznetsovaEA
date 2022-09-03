# Необходимо написать функцию которая будет принимать на вход любую строку с латинскими буквами и возвращать вместо этой буквы ее позицию в алфавите(”а” = 1, “b” = 2 и т.д.). Если что то в строке не является буквой, то этот символ игнорируется и не возвращается.

# Пример
# alphabet_position("The sunset sets at twelve o' clock.")

# output:
# "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"

# 1вариант - (ASCII Table)

text = input('alphabet_position: ')
text = text.lower()
text = text.replace(" ", "")
text = ''.join(filter( lambda x: x in 'abcdefghijklmnopqrstuvwxyz', text))
list = []
for character in text:
    number = ord(character) - 96
    list.append(number)
convertList = ' '.join([str(x) for x in list])
print()
print("output:")
print(convertList)



# 2 вариант. У меня не получилось вывести ответ в строчку, только в столбец

# alphabet = {'a': '1',
#     'b': '2',
#     'c': '3',
#     'd': '4',
#     'e': '5',
#     'f': '6',
#     'g': '7',
#     'h': '8',
#     'i': '9',
#     'j': '10',
#     'k': '11',
#     'l': '12',
#     'm': '13',
#     'n': '14',
#     'o': '15',
#     'p': '16',
#     'q': '17',
#     'r': '18',
#     's': '19',
#     't': '20',
#     'u': '21',
#     'v': '22',
#     'w': '23',
#     'x': '24',
#     'y': '25',
#     'z': '26',
# }

# text = input('alphabet_position: ')
# new_text = text.lower()
# new_text2 = new_text.replace(" ", "")
# new_text3 = ''.join(filter( lambda x: x in 'abcdefghijklmnopqrstuvwxyz', new_text2))
# print()
# print("output:")
# for x in new_text3:
#     print(alphabet[x])