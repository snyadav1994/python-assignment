print ("assignment 3")
str=raw_input("Enter your string :")
lwr=str.lower()
print lwr
sum=0

for i in lwr:
    a = ord(i)-96
    print a
    
    sum += a
    

print sum

while(sum>9) :
     z=sum%10
     sum = z +(sum/10)
   
print "lucky number is",sum
 








    
  