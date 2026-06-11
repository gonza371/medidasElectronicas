import matplotlib.pyplot as plt
import numpy as np

# Datos extraídos de la tabla
fase = np.array([0, 30, 60, 90, 120, 148.32])

# Valores de Vo/Vi
vo_vi_rms = np.array([0, 0.17, 0.48, 0.74, 0.88, 0.97])   # (1) True RMS
vo_vi_medio = np.array([0, 0.06, 0.25, 0.51, 0.72, 0.90]) # (2) Valor Medio

# Crear la figura y los ejes
fig, ax = plt.subplots(figsize=(10, 6))

# Graficar las dos curvas (también agrandé un poco los marcadores a markersize=8)
ax.plot(fase, vo_vi_rms, marker='o', linestyle='-', color='blue', 
        linewidth=2, markersize=8, label='True RMS ($V_o/V_i$ 1)')

ax.plot(fase, vo_vi_medio, marker='s', linestyle='--', color='red', 
        linewidth=2, markersize=8, label='Valor Medio ($V_o/V_i$ 2)')

# Configurar los límites de los ejes
ax.set_xlim(0, 180)
ax.set_ylim(0, 1)

# Configurar las marcas (ticks) de la cuadrícula
ax.set_xticks(np.arange(0, 181, 30))
ax.set_xticks(np.arange(0, 181, 10), minor=True)

ax.set_yticks(np.arange(0, 1.1, 0.2))
ax.set_yticks(np.arange(0, 1.1, 0.1), minor=True)

# Añadir la cuadrícula (grid)
ax.grid(which='major', color='black', linestyle='-', linewidth=0.8)
ax.grid(which='minor', color='gray', linestyle=':', linewidth=0.5)


# --- NUEVOS TAMAÑOS ---

# 1. Agrandar los números de los ejes (ticks)
ax.tick_params(axis='both', which='major', labelsize=14)

# 2. Agrandar las letras de los ejes
ax.set_xlabel('Fase (°)', fontsize=16, fontweight='bold')
ax.set_ylabel(r'$\frac{V_o}{V_i}$', fontsize=22, rotation=0, labelpad=25, fontweight='bold')

# 3. Agrandar el título principal
ax.set_title('Relación de Tensión vs. Ángulo de Conducción', fontsize=18, fontweight='bold')

# 4. Agrandar la leyenda
ax.legend(loc='lower right', fontsize=14, framealpha=1, edgecolor='black')

# Ajustar los márgenes y mostrar
plt.tight_layout()
plt.show()