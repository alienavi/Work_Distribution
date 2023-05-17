# Work_Distribution

## Problem
- Multiple clients/countries having different kind/set of work.
- Each work has certain amount of load.
- Each employee/worker has a dedicated load capacity.
- We need to distribute work in sets such that total capacity is less than equal to employee/worker load capacity.
    ### Inputs
    - Number of countries/clients
    - Type of work
    - Load value per type
    - Time required by each work
## Solution
- Using bin packing, each work load is defined as element having different sizes which are packed/distributed into minimum required bins as per maximum load/size capacity
    ### Output
    - A list of sets of work
    - Each set contains the country name, type, and amount of work with load

## Sample Output
        {1: {'India': {'I1': 3, 'I2': 5, 'I3': 4}, 'load': 54},
        2: {'India': {'I3': 2, 'I4': 7}, 'load': 59},
        3: {'China': {'I1': 6, 'I2': 12, 'I3': 1}, 'load': 56},
        4: {'China': {'I3': 4, 'I4': 3}, 'load': 55},
        5: {'Brazil': {'I1': 3, 'I2': 3, 'I3': 5}, 'load': 58},
        6: {'Brazil': {'I3': 6}, 'load': 56},
        7: {'Brazil': {'I3': 6}, 'load': 56},
        8: {'Brazil': {'I3': 6}, 'load': 56},
        9: {'Brazil': {'I3': 6}, 'load': 56},
        10: {'Sri Lanka': {'I1': 9, 'I2': 8, 'I3': 0}, 'load': 52},
        11: {'Sri Lanka': {'I3': 6}, 'load': 56},
        .
        .
        .
        .
        }
Each set can be assigned to one employee/worker.

---
### TODO:
- Divide each set into numbers of employees present.