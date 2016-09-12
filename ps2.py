import random
import math

count =0
user_count=input("Enter number of users")
for points in range(user_count):
	(x,y)=(random.random()*2- 1, random.random()*2-1)
	print(x,y)
	var1=math.pow(x,2)
	var2=math.pow(y,2)
	var3=var1+var2
	var3=math.pow(var3,0.5)
	if var3<=1:
		count += 1
		continue
print count
efficiency=count/float(user_count)*100
print("The number of user in the circle area :",efficiency)




