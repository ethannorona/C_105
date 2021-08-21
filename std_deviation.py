import math
import csv

with open("data.csv", newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)
    
data = file_data[0]

#To find mean
def mean(data):
    n = len(data)
    total = 0
    
    for x in data:
        total += int(x)
        
    mean = total/n
    return mean

#Squaring and getting the values
squared_list = []

for number in data:
    a = int(number) - mean(data)
    a = a**2
    squared_list.append(a)
    
#Getting sum
sum = 0

for i in squared_list:
    sum = sum + i
    
#Dividing sum by total values
result = sum/(len(data) - 1)

#Finding standard deviation by taking sqaure root of result
std_deviation = math.sqrt(result)

print("Standard Deviation is -> " + str(std_deviation))