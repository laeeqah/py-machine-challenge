#numpy challenge 1

print("Challenge 1")

import numpy as np

arr = np.arange(1,21,1)

value = np.mean(arr)
print("The mean is: ",value)

my_standard = np.std(arr)
print("The standard is: ",my_standard)

var = np.var(arr)
print("The Variance is: ",np.var(arr))

#numpy challenge 2
from matplotlib import pyplot as plt

nums = np.array ([0.5 ,0.7, 1, 1.2, 1.3, 2.1])
bins = np.array([0, 1, 2, 3])

plt.title("Histogram of nums against bins")
plt.xlabel("nums")
plt.ylabel("bins")

plt.hist(nums,bins, color = "orange")
plt.show()
