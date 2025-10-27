import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import cont2discrete, dlti, dstep, lti, step

# continuo
Gp = lti([20],[50,1])
t_cont, y_cont = step(Gp)

# discreto (ZOH)
Ts = 0.1
b,a,_ = cont2discrete(([20],[50,1]), Ts, method='zoh')[:3]
Gz = dlti(b,a,dt=Ts)
t_disc, y_disc = dstep(Gz)
t_disc = np.squeeze(t_disc)
y_disc = np.squeeze(y_disc)

plt.plot(t_cont, y_cont, label='Continuo')
plt.step(t_disc, y_disc, where='post', label='Discreto (ZOH)')
plt.xlabel('Tiempo [s]')
plt.ylabel('Salida al escalón')
plt.legend(); plt.grid(True)
plt.show()