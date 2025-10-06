import numpy as np
import matplotlib.pyplot as plt

# Parámetros del circuito RC
R = 1e3       # 1 kΩ
C = 1e-6      # 1 µF

# Frecuencia en Hz
f = np.logspace(1, 6, 1000)   # de 10 Hz a 1 MHz
omega = 2 * np.pi * f

# Función de transferencia H(jω)
H = 1 / (1 + 1j * omega * R * C)

# Magnitud (en dB) y fase (en grados)
mag = 20 * np.log10(np.abs(H))
phase = np.angle(H, deg=True)

# Frecuencia de corte
fc = 1 / (2 * np.pi * R * C)

# Gráficos
plt.figure(figsize=(8,6))

# --- Magnitud ---
plt.subplot(2,1,1)
plt.semilogx(f, mag, label='|H(f)|')
plt.axvline(fc, color='r', linestyle='--', label=f'f_c = {fc:.1f} Hz')
plt.title('Diagrama de Bode - Filtro RC (H(f) = 1 / (1 + j2πfRC))')
plt.ylabel('Magnitud [dB]')
plt.legend()
plt.grid(True, which='both', ls='--')

# --- Fase ---
plt.subplot(2,1,2)
plt.semilogx(f, phase, label='∠H(f)')
plt.axvline(fc, color='r', linestyle='--')
plt.ylabel('Fase [°]')
plt.xlabel('Frecuencia f [Hz]')
plt.grid(True, which='both', ls='--')

plt.tight_layout()
plt.show()
