def encode(password):
    new = []
    for i in password:
        number = int(i)
        number += 3
        if number >= 10:
            number -= 10
        new.append(number)
    return ''.join(str(i) for i in new)

def decode(password: str) -> str:
    ret = ""
    for char in password:
        char = int(char) - 3
        if char < 0:
            char = 10 + char
        ret += str(char)
    return ret

def main():
    while True:
        #print(encoder(1234))
        print("Menu")
        print("------------- ")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        option = int(input("Please enter an option: "))
        if option == 1:
            password = input("Please enter your password to encode: ")
            password = encode(password)
            print("Your password has been encoded and stored!")
            #print(encode(password))
        elif option == 2:
            print(f"The encoded password is {password}, and the original password is {decode(password)}")
        elif option == 3:
            break
        else:
            print("Enter valid number")

if __name__ == '__main__':
    main()





