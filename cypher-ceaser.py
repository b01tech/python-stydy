ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'w', 'v', 'x', 'y', 'z']

print("Cryptography system")


def chose_dir():
    dir_value = input('Do you want encode or decode?\n')
    if dir_value == 'encode':
        direction = 1
        return direction
    elif dir_value == 'decode':
        direction = -1
        return direction
    else:
        print("Input not valid.")
        chose_dir()


def chose_shift():
    shift_num = int(input('Type the shift number: '))
    return shift_num


def read_msg():
    msg = input('Write your message: ')
    return msg


def cryptography(msg, shift, dir):
    crypt_msg = []
    for l in msg:
        position = ALPHABET.index(l)
        new_position = position + (shift * dir)
        while new_position > len(ALPHABET):
            new_position -= len(ALPHABET)
        crypt_msg.append(ALPHABET[new_position])
    crypt_msg = ''.join(crypt_msg)
    print(crypt_msg)


dir = chose_dir()
shift = chose_shift()
msg = read_msg()
cryptography(msg, shift, dir)
