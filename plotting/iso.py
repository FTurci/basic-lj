import natsort
import glob
import numpy as np
import matplotlib.pyplot as plt
import stringato

files = natsort.natsorted(glob.glob("/Users/francesco/Repos/basic-lj/isobars/*.txt"))

ps,temps,rhos = [],[],[]
for f in files:
    P = stringato.num_word("P",f)
    T = stringato.num_word("T",f)
    rho = np.loadtxt(f, skiprows=2)[:,-1].mean()
    ps.append(P), temps.append(T),rhos.append(rho)



plt.scatter(rhos,temps,c=ps, cmap =plt.cm.rainbow)
table = np.array([ps,temps,rhos]).T
print(table)
print(np.where(np.diff(table[:,0]))[0])
datasets = np.split(table, np.where(np.diff(table[:,0]))[0]+1)
print(datasets)
for d in datasets:
    plt.plot(d[:,2],d[:,1], 'k--')
plt.xlabel(r"$\rho$")
plt.ylabel("T")
plt.show()