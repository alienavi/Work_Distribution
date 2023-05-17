# importing libraries
import numpy as np
from pprint import pprint
# definitions
'''
Inputs :
    # Number of countries
    # types of work
    # Number of work
    # time required per work type
Output :
    # Optimized work allocation for all employees
'''

# test data set
total_work = {
    'India': {
        'I1' : 3,
        'I2' : 5,
        'I3' : 6,
        'I4' : 10
    },
    'China': {
        'I1' : 6,
        'I2' : 12,
        'I3' : 5,
        'I4' : 6
    },
    'Brazil': {
        'I1' : 3,
        'I2' : 3,
        'I3' : 30,
        'I4' : 3
    },
    'Sri Lanka': {
        'I1' : 9,
        'I2' : 8,
        'I3' : 42,
        'I4' : 0
    },
    'Nepal': {
        'I1' : 5,
        'I2' : 22,
        'I3' : 1,
        'I4' : 14
    },
    'Singapore': {
        'I1' : 32,
        'I2' : 8,
        'I3' : 2,
        'I4' : 10
    }
}
work_time = {
    'I1':4,
    'I2':2,
    'I3':8,
    'I4':5
    }

capacity = 60
bins = {}
res = 1
for key_c in total_work :
    #! get country wise work data
    country = total_work[key_c]
    load = 0
    allocation = {}
    allocation[key_c] = {}
    for key_i in country :
        #! for each type of work iterate load
        allocation[key_c][key_i] = 0
        for i in range(country[key_i]) :
            #! iterate over each number of work per work type
            load += work_time[key_i] #* Increment the load
            if(load >= capacity) : #* check load vs capacity
                bins[res] = allocation
                bins[res]['load'] = load - work_time[key_i]
                load = work_time[key_i]
                res += 1
                allocation = {}
                allocation[key_c] = {}
                allocation[key_c][key_i] = 0
                allocation[key_c][key_i] += 1
                load += work_time[key_i]
            else :
                allocation[key_c][key_i] += 1
            #print(i, allocation, load)
    bins[res] = allocation
    bins['load'] = load
pprint(bins)