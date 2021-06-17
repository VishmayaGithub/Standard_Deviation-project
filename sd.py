import csv
import math

with open('data.csv') as f:
    read = csv.reader(f)
    file_data = list(read)

data = file_data[0]

def c_mean(data):
    l = len(data)
    total = 0
    for i in data:
        total +=int(i)
    mean = total/l
    return mean  

squ = []
for i in data:
    a = int(i) - c_mean(data)   
    a = a**2
    squ.append(a)   

b = 0
for n in squ:
    b+=n

d = b/(len(data)-1)   

standard_d = math.sqrt(d)

print('Standard deviation -->',standard_d)