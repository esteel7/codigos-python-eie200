import numpy as np
import matplotlib.pyplot as plt

# --- Datos ---
clinica_A = np.array([34, 46, 33, 47])
clinica_B = np.array([41, 40, 39, 40])
valor_real = 40

# --- Estadísticos ---
media_A = np.mean(clinica_A)
media_B = np.mean(clinica_B)
desv_A = np.std(clinica_A, ddof=1)
desv_B = np.std(clinica_B, ddof=1)

# --- Figura con 3 subgráficos ---
fig, axes = plt.subplots(1, 3, figsize=(14, 4), sharey=True)
plt.subplots_adjust(wspace=0.3)

# 1) Barras con desviación estándar
ax = axes[0]
clinicas = ['Clínica A', 'Clínica B']
medias = [media_A, media_B]
errores = [desv_A, desv_B]
ax.bar(clinicas, medias, yerr=errores, capsize=6, alpha=0.7)
ax.axhline(valor_real, linestyle='--', linewidth=1)
ax.set_title('Promedio ± desviación estándar')
ax.set_ylabel('Hematocrito (%)')
ax.grid(True, axis='y', linestyle=':')

# 2) Dispersión individual con medias
ax = axes[1]
x_A = np.full(len(clinica_A), 1) + np.random.uniform(-0.05, 0.05, len(clinica_A))
x_B = np.full(len(clinica_B), 2) + np.random.uniform(-0.05, 0.05, len(clinica_B))
ax.scatter(x_A, clinica_A, alpha=0.8, label='A')
ax.scatter(x_B, clinica_B, alpha=0.8, label='B')
ax.plot([1, 2], [media_A, media_B], 'ko', label='Media')
ax.axhline(valor_real, linestyle='--', linewidth=1)
ax.set_xticks([1, 2])
ax.set_xticklabels(['Clínica A', 'Clínica B'])
ax.set_title('Dispersión de mediciones')
ax.grid(True, axis='y', linestyle=':')
ax.legend()

# 3) Boxplot
ax = axes[2]
ax.boxplot([clinica_A, clinica_B], labels=['Clínica A', 'Clínica B'], widths=0.6, patch_artist=True)
ax.axhline(valor_real, linestyle='--', linewidth=1)
ax.set_title('Diagrama de caja')
ax.grid(True, axis='y', linestyle=':')

fig.suptitle('Comparación de exactitud (media) y precisión (dispersión)', y=1.03)
plt.show()

# Imprime resumen numérico
print(f"Clínica A: media = {media_A:.2f}%, s = {desv_A:.2f}%")
print(f"Clínica B: media = {media_B:.2f}%, s = {desv_B:.2f}%")