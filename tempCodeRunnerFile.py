n = int(input());
a = int(n % 2);
if a != 0:
    print("Weird") 
elif(a >= 2 & a <= 5):
    print("Not Weird")
elif(a >= 6 & a <= 20):
    print("Weird") 
elif(a == 0 & a >= 20):
    print("Weird")       