import pandas as pd
import numpy as np
# Creamos un DataFrame utilizando Pandas
data = {'Nombre': ['Henry', 'Zine', 'Smith', 'Grisely'],
    'Edad': [25, 21, 23, 27],
    'Ciudad': ['Huanuco', 'Huanuco', 'Tocache', 'Huanuco']}
df = pd.DataFrame(data)
# Mostramos el DataFrame
print("DataFrame original:")
print(df)
print()
# Operaciones con NumPy
# Calcular la edad promedio utilizando NumPy
edades = df['Edad'].values  # Convertir la columna 'Edad' a un array NumPy
edad_promedio = np.mean(edades)
print(f"Edad promedio: {edad_promedio}")
# Añadir una nueva columna calculada utilizando NumPy
df['Edad_al_cuadrado'] = np.square(edades)
print("\nDataFrame con columna 'Edad_al_cuadrado' añadida:")
print(df)
