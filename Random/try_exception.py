num1=input("Enter number")
num2=input("Enter number")


try:
    print("The sum of two number is ",int(num1)+int(num2))

except Exception as e:
    print(e)

print("This line is very importent")