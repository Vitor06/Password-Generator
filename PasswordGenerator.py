import random
import string


def menu():
    print('Password Generator')
    print()
    print('1-Numbers') 
    print('2-Numbers, letters and special characters')
    print('3-Exit')


def generate_password(option,length_password):
    password = []

    numbers = list(string.digits)
    letters = list(string.ascii_letters)
    special_characters = list(string.punctuation)

    numbers_digits = round(0.3*length_password)
    letters_digits = round(0.5*length_password)
    special_characters_digits = round(0.2*length_password)

    if(option==1):
         for d in range(length_password):
            password.append(random.choice(numbers))

    elif(option==2):
        for d in range(numbers_digits):
            password.append(random.choice(numbers))

        for d in range(letters_digits):
            password.append(random.choice(letters))
        
        for d in range(special_characters_digits):
            password.append(random.choice(special_characters))
      
    else:
        print('Invalid option')
        
    random.shuffle(password)
    return 'Password :' +  ''.join(password)

  
def main():
    menu()
    input_user = 0
    options = [1,2]
    while(input_user!=3):
        print('---------------')
        input_user = int(input('Option : '))
        input_length = int(input('Password length: '))
        if(input_user in options):
            print(generate_password(input_user,input_length))

main()
