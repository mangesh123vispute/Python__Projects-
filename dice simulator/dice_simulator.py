import random


ch=int(input("Enter your choice: \n1.ROll the dice \n2. exit\n"))
print('\n' * 90)
while(ch!=1 and ch!=2):
    print("Enter correct choice")
    ch = int(input("Enter your choice: \n1.ROll the dice \n2. exit\n"))
    print('\n' * 90)

while(ch!=2):
    print('\n' * 90)
    num=random.randint(1,6)
    print('Your dice display number',num,'\n')
    ch=int(input("Enter your choice: \n1.ROll the dice \n2. exit\n"))

    print('\n' * 90)
    while (ch != 1 and ch != 2):
        print("Enter correct choice")
        ch = int(input("Enter your choice: \n1.ROll the dice \n2. exit\n"))

        print('\n' * 90)


