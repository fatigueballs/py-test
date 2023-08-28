import random
points = 0
qn = 0
print ("Welcome to this test \nur mom")

while qn < 5 :
    a = random.randint(0,99)
    b = random.randint(0,99)
    ans = a + b
    print ("What is ", a, "+ ", b, "? ")
    ui = int(input("answer = "))

    if ui == ans :
        print ("correct") 
        points = points + 1

    else :
        print ("wrong")

    qn = qn + 1

else :
    print ("Your total is", points, "/ 5")





