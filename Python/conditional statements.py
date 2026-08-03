#if statements
n=5
if(n<10):
    print("Number is small")
    print("This block is always execute")



    #if-else statements

    n=50
if(n<10):
    print("Number is small")
else:
    print("Number is large")
    print("This statemet is always execute")


    #if_elif_else statements

    num=10
    if(num==0):
        print("Number is zero")
    elif(num>5):
        print("Number is greater than 5")
    else:
        print("Number is less than 5")


        # nested if-else statements 
        #example one

    num=5
    if(num>0):
            print("Number is possitive")
    if(num<0):
             print("Number is less than 10")


      #example two 

n1=-12
if(n1!=0):
   if(n1>=0):
     print("Number is possitive")
   else:
     print("Number is negative")
else:
   print("Number is zero")

#elif ladder
a = 12
b = 1
c = 23
d = 1

if (a > b and a > c and a > d):
    print("a is greater")
elif (b > a and b > c and b > d):
    print("b is greater")
elif (c > a and c > b and c > d):
    print("c is greater")
else:
    print("d is greater")