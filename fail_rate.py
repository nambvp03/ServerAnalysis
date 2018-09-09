import random

number_of_test=2
mean=44829
server=6
iteration=100000
hour=2
sum_of_fail_rate=0
avg_of_fail_rate=0
#standard_fail_rate=0.049
#error_percentage=0
#sum_of_error_percentage=0
#avg_of_error_percentage=0

def get_random_list():
	server_list=[]
	while len(server_list)<server:
		param_list=[]
		while len(param_list)<iteration:
			param_list.append(int(random.expovariate(1/mean)))
		server_list.append(param_list)
	return server_list

for test in range(0,number_of_test):

	fail_rate=0
	success_rate=0
	fail_iteration=0

	server_data=get_random_list()
	#print(len(server_data))
	#print(*server_data, sep="\n")
 
	for i in range(0,iteration):
		server_fail_count=0
		for j in range(0,server-1):
			for k in range(j+1,server):
				diff=abs(server_data[j][i]-server_data[k][i])
				if diff<hour:
					server_fail_count += 1
		if server_fail_count>0:
			fail_iteration +=1

	print("___",test+1,"___")
	fail_rate=(fail_iteration*100)/iteration
	print("Fail Rate =",fail_rate,"%")

	success_rate=100-fail_rate
	print("Success Rate =",success_rate,"%")

	sum_of_fail_rate += fail_rate

	#sum_of_error_percentage += (fail_rate - standard_fail_rate)*100/standard_fail_rate


print("____________________________________")
avg_of_fail_rate=sum_of_fail_rate/number_of_test
print("Avg Fail Rate",avg_of_fail_rate,"%")

#print("_____________________________________")
#error_percentage=(avg_of_fail_rate - standard_fail_rate)*100/standard_fail_rate
#print("____Error percentage",error_percentage,"%")

#print("_____________________________________")
#avg_of_error_percentage=sum_of_error_percentage/number_of_test
#print("Avg Error percentage",avg_of_error_percentage,"%")
