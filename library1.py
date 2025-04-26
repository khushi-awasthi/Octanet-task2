# from matplotlib import pyplot as plt
# x=[5,2,9,4,7]
# y=[10,5,8,4,2]
# # plt.plot(x,y)
# # plt.bar(x,y)
# # plt.hist(x,y)
# plt.scatter(x,y)
# plt.show()

# from matplotlib import pyplot as plt

# slices=[7,2,2,13]
# activities=['Sleeping','Eating','Working','Playing']
# cols=['c','m','r','b']

# plt.pie(slices,labels=activities,
#         colors=cols,
#         startangle=90,
#         shadow=True,
#         explode=(0,0.1,0,0),
#         autopct="%1.lf%%")
# plt.title("PIE PLOT")
# plt.show()

import numpy as np
import matplotlib.pyplot as plt

def f(t):
    return np.exp(-t)*np.cos(2*np.pi*t)
t1=np.arange(0.0,5.0,0.1)
t2=np.arange(0.0,5.0,0.002)

plt.subplot(211)
plt.plot(t1,f(t1),"bo",t2,f(t2))

plt.subplot(212)
plt.plot(t2,np.cos(2*np.pi*t2))
plt.show()