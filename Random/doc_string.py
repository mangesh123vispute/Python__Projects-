# a=15
# b=17
# c=sum((a,b))
# print(c)

# function which return nothing

def funciotn1():
    print("i am mangesh")


funciotn1()
# print(funciotn1())                              as function is not returning any thing you will get None when you print it

# function which returns something

def function2(a,b):
    ''' This is doc string , and i am learning what is doc string very easyly thanks'''

    return f"sum of a and b is {a+b}"

s=function2(10,20)
print(s)

print(function2.__doc__)

# what is function docstring
# docsting is nothing but fist string written under any fuction wich tells information about the function