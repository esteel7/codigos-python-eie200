import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# -------------------------
# Parámetros del circuito RC
# -------------------------
R = 1e3       # ohm
C = 1e-6      # F

# -------------------------
# Sistema H(s) = 1 / (1 + R C s)
# Numerador y denominador en polinomio de s
# -------------------------
num = [1.0]
den = [R*C, 1.0]
system = signal.TransferFunction(num, den)

# -------------------------
# Vector de frecuencias (rad/s) para bode
# (elegimos amplio rango)
# -------------------------
w = np.logspace(1, 6, 1000)          # rad/s
f = w / (2 * np.pi)                  # convertir a Hz para graficar

# -------------------------
# Calcular Bode (mag en dB, fase en grados)
# signal.bode devuelve w (rad/s), mag(dB), phase(deg)
# -------------------------
w_out, mag, phase = signal.bode(system, w=w)

# -------------------------
# Frecuencia de corte teórica (Hz)
# -------------------------
fc = 1.0 / (2.0 * np.pi * R * C)
omega_c = 2.0 * np.pi * fc

# calcular H(jw) en el punto de corte para anotaciones exactas
Hc = 1.0 / (1.0 + 1j * omega_c * R * C)
mag_c = 20.0 * np.log10(np.abs(Hc))
phase_c = np.angle(Hc, deg=True)

# -------------------------
# Preparar la figura y anotar
# -------------------------
plt.figure(figsize=(9,6))

# Magnitud
ax1 = plt.subplot(211)
ax1.semilogx(f, mag, label=r'$20\log_{10}|H(j\omega)|$')
ax1.set_ylabel('Magnitud [dB]')
ax1.set_title(r'Diagrama de Bode: $H(j\omega)=\dfrac{1}{1+j\omega RC} = \dfrac{1}{1 + j 2\pi f R C}$', fontsize=11)
ax1.grid(True, which='both', ls='--', alpha=0.6)

# línea y punto en fc
ax1.axvline(fc, color='r', linestyle='--', linewidth=1)
ax1.scatter([fc], [mag_c], color='r', zorder=5)
ax1.annotate(fr'$f_c={fc:.2f}\,\mathrm{{Hz}}$', xy=(fc, mag_c),
             xytext=(fc*1.6, mag_c+6),
             arrowprops=dict(arrowstyle='->', lw=0.8),
             fontsize=9)
ax1.annotate(fr'$H(j\omega_c)\approx {mag_c:.2f}\ \mathrm{{dB}}$', xy=(fc, mag_c),
             xytext=(fc*1.6, mag_c-10), fontsize=9)

# Fase
ax2 = plt.subplot(212, sharex=ax1)
ax2.semilogx(f, phase, label=r'$\angle H(j\omega)$')
ax2.set_ylabel('Fase [°]')
ax2.set_xlabel('Frecuencia $f$ [Hz]')
ax2.grid(True, which='both', ls='--', alpha=0.6)

# marcar fc en fase
ax2.axvline(fc, color='r', linestyle='--', linewidth=1)
ax2.scatter([fc], [phase_c], color='r', zorder=5)
ax2.annotate(fr'$\angle H(j\omega_c)\approx {phase_c:.1f}^\circ$',
             xy=(fc, phase_c),
             xytext=(fc*1.6, phase_c-30),
             arrowprops=dict(arrowstyle='->', lw=0.8),
             fontsize=9)

plt.tight_layout()
plt.show()
