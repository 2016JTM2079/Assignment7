state={'Uttrakhand' : '010','Delhi' : '100','Punjab': '111','Haryana': '101'}
district={'Roorkee':'101','Rohini ': '100','Bathinda':'001','Hissar':'000'}
landmark={'IIT ROORKEE': '000','IIT DELHI':'001','IIT ROPAR':'010','IIT ROHTAK':'100'}


d = {
    'Name': 'username',
    'Landmark': 'landmark',
    'District': 'district',
    'State': 'state',
    
}

n = 1
d = [ map(str,raw_input().split()) for x in range(n)]
print d


def encode(d):
	print d
	for key in state:
    	print('Key: %s' % key)
	if key == d[3]:
	print(" The value for key_2 is %s." % my_dict[key]) 
	
	

