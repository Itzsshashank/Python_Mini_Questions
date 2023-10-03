import statistics

# Sample list of numbers
numbers = [10, 15, 20, 25, 30]

# To calculate the mean
mean = statistics.mean(numbers)

# To calculate the median
median = statistics.median(numbers)

# To calculate the standard deviation
std_deviation = statistics.stdev(numbers)

print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std_deviation)
