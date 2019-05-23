# Example use of lists
import math

dataset = [1.23, 2.10, 9.24, 3.34, 6.42, 1.01, 0.32, 5.43, 9.22, 6.10]
sum = 0.0
squared = 0.0
count = 0

print ('Dataset: ')
for sample in dataset:
    print (' - ' + str(sample))
    sum += sample
    squared += sample ** 2
    count += 1
print ()

average = sum / count
stdDev = math.sqrt( squared / count )

print ('Average = ' + str(average))
print ('Standard deviation = ' + str(stdDev))
print ('Count = ' + str(count))
