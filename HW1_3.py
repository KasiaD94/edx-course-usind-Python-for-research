# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 19:04:32 2020
Compute and store R=1000 random values from 0-1 as x.
Compute the moving window average for x for values 
of n_neighbors ranging from 1 to 9 inclusive.
Store x as well as each of these averages as consecutive lists 
in a list called Y.
@author: Kasia
"""
import statistics
import random
import plotly
from plotly.offline import iplot, init_notebook_mode
from plotly import tools
import plotly.graph_objs as go
init_notebook_mode(connected=True)

def moving_window_average(x, n_neighbors):
    n = len(x)
    width = n_neighbors*2 + 1
#    print (x2)
#    print("------------------------------------")
    x2 = [x[0]]*n_neighbors + x + [x[-1]]*n_neighbors
#    print (x)
    # To complete the function,
    # return a list of the mean of values from i to i+width for all values i 
    # from 0 to n-1.
    mean_x2 = []
    for i in range(n + n_neighbors):
#        print(i)
        mean_value = sum(x2[i-n_neighbors : i+n_neighbors+1])/width
        mean_x2.append(mean_value)
            
#    trace = {'type': 'bar', 'x': list(range(n)), 'y': mean_x2[n_neighbors:]}
#    plotly.offline.plot({'data': [trace]})
#    trace2 = {'type': 'bar', 'x': list(range(n)), 'y': x}
#    plotly.offline.plot({'data': [trace2]}) 

    return mean_x2[n_neighbors:]
       
R = 1000
x = []
for i in range(R):
    x.append(random.uniform(0,1))

print(moving_window_average(x,5))
Y = [x, moving_window_average(x, 5)]
ranges = [max(x) - min(x) for x in Y]
print(ranges)