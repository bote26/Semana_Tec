import streamlit as st
import pandas as pd
import numpy as np
from datetime import timedelta
import matplotlib.pyplot as plt
from calculos import Trayectorias

st.title("Diseño de órbitas de transferencia entre cuerpos celestes")
st.markdown('''
Este proyecto tiene como objetivo calcular y simular trayectorias de transferencia entre cuerpos celestes utilizando la Transferencia de Hohmann como modelo principal, una de las maniobras más eficientes en términos de combustible para viajes espaciales. Mediante la implementación de modelos matemáticos basados en las leyes de conservación de energía y momento angular, buscamos optimizar las rutas entre la órbita de la Tierra y cuerpos como asteroides o planetas. El proyecto permite realizar los cálculos necesarios para determinar el tiempo de viaje, los incrementos de velocidad y la energía requerida para completar la misión de manera eficiente. Con estas herramientas, se ofrece una visión detallada y precisa del diseño de trayectorias espaciales.

**Bienvenidos a Orbital Pathway**\n
Orbital Pathway es una plataforma interactiva que apoya este proyecto, diseñada específicamente para calcular y visualizar trayectorias de lanzamiento desde la Tierra hacia otros cuerpos celestes en el sistema solar. Utilizamos modelos orbitales precisos y herramientas científicas avanzadas para simular las rutas más eficientes, como la Transferencia de Hohmann y otras trayectorias interplanetarias.''')

# Create a DataFrame with the radii of the planets
planet_radii = {
    'Mercurio': 0.387,
    'Venus': 0.723,
    'Tierra': 1.0,
    'Marte': 1.524,
    'Júpiter': 5.203,
    'Saturno': 9.58,
    'Urano': 19.23,
    'Neptuno': 30.06
}

df = pd.DataFrame(list(planet_radii.items()), columns=['Planeta', 'Radio (UA)'])
# st.table(df)
st.subheader("¡Comencemos!")
option = st.selectbox(
    "¿Qué planeta deseas visitar?",
    ("Mercurio", "Venus", "Tierra", "Marte", "Júpiter", "Saturno", "Urano", "Neptuno"),
)


a = planet_radii[option]

Planeta = Trayectorias(a)

deltaV1_ms, deltaV2_ms, theta, tiempo = Planeta.calcular()
st.latex(r"\Delta V_1 \text{ (m/s)}: " + str(np.round(deltaV1_ms,3)))
st.latex(r"\Delta V_2 \text{ (m/s)}: " + str(np.round(deltaV2_ms,3)))
st.latex(r"\text{Ángulo de lanzamiento (grados):}: " + str(np.round(theta,3))+ "^\circ")
st.latex(r"\text{Tiempo de viaje (años)}: " + str(np.round(tiempo,3)))

x,y = Planeta.coordenadas()
xt, yt = Planeta.coordenadasTierra()

# Graficar la trayectoria
plt.figure(figsize=(8, 8))
plt.plot(x, y, label='Trayectoria de Hohmann')
plt.plot(0, 0, 'o', label='Sol', markersize=10, color='orange')  
plt.plot(0, a, 'o', label=f'{option}', markersize=5, color='blue') 
plt.plot(0, -1, 'o', label=f'Tierra', markersize=5, color='green') 
plt.plot(xt, yt, label='Órbita de la Tierra', color='green') 

plt.xlabel('Posición en X (UA)')
plt.ylabel('Posición en Y (UA)')
plt.title('Simulación de la Transferencia de Hohmann')
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')  # Asegurar escala igual en X e Y
plt.legend()
plt.show()

st.pyplot(plt)

plt.figure(figsize=(8, 8))
plt.plot(x, y, label='Trayectoria de Hohmann')
plt.plot(0, 0, 'o', label='Sol', markersize=10, color='orange')  
plt.plot(a * np.sin(np.deg2rad(theta)), a * np.cos(np.deg2rad(theta)), 'o', label=f'{option}', markersize=5, color='blue') 
plt.plot(0, -1, 'o', label='Tierra', markersize=5, color='green') 
plt.plot(xt, yt, label='Órbita de la Tierra', color='green') 

plt.xlabel('Posición en X (UA)')
plt.ylabel('Posición en Y (UA)')
plt.title('Simulación de la Posición de Lanzamiento')
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')  # Asegurar escala igual en X e Y
plt.legend()
plt.show()

st.pyplot(plt)

