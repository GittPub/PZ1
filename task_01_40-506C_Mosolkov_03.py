import numpy as np
import matplotlib.pylab as plt
import json
import os.path

x = np.arange(-15,5+0.1,0.1)

def f(x):
    return (100 * np.sqrt(np.abs(1 - 0.01 * (x ** 2))) +
            0.01 * np.abs(x + 10))

plt.grid()
plt.plot(x, f(x))
plt.xlabel('x')
plt.ylabel('f (x)')
plt.show()

if not os.path.exists('results'):
    os.mkdir('results')
res_name = os.path.join(os.getcwd(),'results','task_01_40-506C_Mosolkov_03.json')

to_json = {'x': [i for i in x], 'y': [f(i) for i in x]}
with open(res_name, 'w') as jsonfile:
    jsonfile.write(json.dumps(to_json))
