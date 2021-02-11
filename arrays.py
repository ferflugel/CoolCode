import numpy as np 

# Just some testing code for now

'''
value:            [...]
net change:       [...]
'''

previous_table = np.array([[10, 10, 10, 10, 10, 10, 10, 10, 10, 10], np.zeros(10)])
table = np.array([[10, 10, 10, 10, 8, 10, 9, 10, 10, 10], np.zeros(10)])

for i in range(10):
    table[1, i] = table[0, i] - previous_table[0, i]

print("Past:")
print(previous_table)
print("Current: table")
print(table)