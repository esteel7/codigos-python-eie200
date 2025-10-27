import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import cont2discrete

# --- Discretización planta (ZOH) ---
Ts = 0.1
num_c = [20.0]
den_c = [50.0, 1.0]
b, a, _ = cont2discrete((num_c, den_c), Ts, method='zoh')[:3]
b = b.flatten()
a = a.flatten()
b0 = b[0] if len(b) > 0 else 0.0
b1 = b[1] if len(b) > 1 else 0.0
a1 = a[1] if len(a) > 1 else 0.0

# --- Control PI (forma incremental vía Tustin) ---
Kp, Ti = 0.8, 9.0
K0 = Kp + Kp*Ts/(2*Ti)
K1 = -Kp + Kp*Ts/(2*Ti)

# --- Simulación lazo cerrado ---
t = np.arange(0, 60 + Ts, Ts)
Ref = np.ones_like(t)

y = np.zeros_like(t, dtype=float)
Usim = np.zeros_like(t, dtype=float)
y1 = 0.0
u1 = 0.0
e1 = 0.0

for k in range(len(t)):
    # control
    e = Ref[k] - y1
    u = u1 + K0*e + K1*e1
    # saturación
    u = min(max(u, 0.0), 100.0)
    # planta
    yk = -a1*y1 + b0*u + b1*u1
    # guardar
    y[k] = yk
    Usim[k] = u
    # actualizar
    y1, u1, e1 = yk, u, e

# --- Gráficas (figuras separadas) ---
plt.figure()
plt.plot(t, y, marker='+', linestyle='None', label='Simulation')
plt.plot(t, Ref, linestyle='--', label='Reference')
plt.xlabel('Time [s]'); plt.ylabel('Response')
plt.title('Closed-loop response')
plt.legend(); plt.grid(True)

plt.figure()
plt.plot(t, Usim, marker='+', linestyle='None', label='Control signal')
plt.xlabel('Time [s]'); plt.ylabel('Control signal')
plt.title('Control effort')
plt.legend(); plt.grid(True)
plt.show()