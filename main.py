# # Exercise02 ARMY GAME
num1 = eval(input('Enter a number: '))
num2 = eval(input('Enter another number: '))

def gameWithCells(x, y):
    c = x//2
    z = y//2
    return (x-c)*(y-z)

print(gameWithCells(num1, num2))

# Exercise10 CAESAR CIPHER
def whatever(code, num):
    code = code.upper()
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    for letter in code:
        if letter in code:
            findl = (alphabet.find(letter)-num)%26
            result = result + alphabet[findl]
        else:
            result = result + letter

    return result

print(whatever('aopz pz h zljyla', 7))