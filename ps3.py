state={'Uttrakhand' : '010','Delhi' : '100','Punjab': '111','Haryana': '101'}
district={'Roorkee':'101','Rohini ': '100','Bathinda':'001','Hissar':'000'}
landmark={'IIT ROORKEE': '000','IIT DELHI':'001','IIT ROPAR':'010','IIT ROHTAK':'100'}

print "1.add 2.modify 3.delete 4.query" 

a=input("enter the operation you want to perform")

if a==1: 
	stt=raw_input("enter the state name you want to add") 
	code=raw_input("enter the code name you want to add for state")
	state.update({stt:code}) 
	cty=raw_input("enter the landmark name you want to add") 
	cde=raw_input("enter the code name you want to add for landmark") 
	landmark.update({cty:cde})
 	dstrt=raw_input("enter the district name you want to add") 
	cod=raw_input("enter the code name you want to add for district") 
	district.update({dstrt:cod})
if a==2:
 	s1=raw_input("enter the state whose code you want to modify\n") 
	c1=raw_input("enter the new code\n") 
	if s1 in state.keys(): 
		state.update({s1:c1}) 
	else : 
		print 'not a valid state' 
	d1=raw_input("enter the district whose code you want to modify\n") 
	c2=raw_input("enter the new code\n") 
	if d1 in district.keys(): 
		district.update({d1:c2}) 
	else : 
		print 'not a valid district' 
	l1=raw_input("enter the landmark whose code you want to modify\n") 
	c3=raw_input("enter the new code\n") 
	if t3 in landmark.keys(): 
		landmark.update({l1:c3}) 
	else : 
		print 'not a valid landmark' 
else : 
	l1=raw_input("enter the customer name\n") 
	l2=raw_input("enter the customer district\n") 
	l3=raw_input("enter the customer landmark\n") 
	l4=raw_input("enter the customer state\n") 
	if l1 in state.keys(): 
		print "CC_NO = " state.get(l4, default=None) 
	if l1 in district.keys(): 
		print district.get(l2, default=None) 
	if l1 in landmark.keys(): 
		print landmark.get(l3, default=None) 
	print "Human Readable code" 
	if l1 in state.keys(): 
		print 
		if l1 in state.keys(): 
			print state.get(l4, default=None) 
		if l1 in district.keys(): 
			print district.get(l2, default=None) 
		if l1 in city.keys(): 
			print city.get(l3, default=None) 
print state



if a==3:
	b=raw_input("enter the state want to delete\n") 
	if b in state.keys(): 
		del state[b] 
	else : 
		print "not a valid key" 
	b=raw_input("enter the city want to delete\n")
	if b in city.keys():
 		del city[b] 
	else : 
	print "not a valid key" 
	b=raw_input("enter the district want to delete\n") 
	if b in district.keys(): 
		del district[b] 
	else : 
		print "not a valid key"


