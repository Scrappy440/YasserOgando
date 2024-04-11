def encode(password):
    new = []
    for i in password:
        number = int(i)
        number += 3
        if number >= 10:
            number -= 10
        new.append(number)
    return ''.join(str(i) for i in new)

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
            encode(password)
            print("Your password has been encoded and stored!")
            #print(encode(password))
        elif option == 2:
            pass
        elif option == 3:
            break
        else:
            print("Enter valid number")

if __name__ == '__main__':
    main()





