import math

a_i = [229168.50747390,-429449.7206839,199330.41355048,28226.22049280,0,0,-34712.81875914,0,
       33820.10886195,-25379.82656589,8386.14942934,-1360.44512548,89.14545378]

for i in a_i:
    print (i)

def series(x):
    
    coeficients = a_i
    total_sum = 0

    for i in range(0,len(coeficients)):
        first_log = math.log(x)
        second_log = math.log(first_log)
        final_log = second_log**(i)
        total_sum += coeficients[i]*(final_log)
        print (i,first_log,second_log,final_log,total_sum)
#checar se está funcionando
print (series(2))

def power_quarter(x):

    return (x)**(-1/4)

def log_quot(x):
    
    return x/(math.log)

def S(x):

    return (log_quot(x))*(1+ (power_quarter(series(x))))


