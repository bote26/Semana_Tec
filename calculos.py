import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

class Trayectorias:
    def __init__(self, rNueva):
        self.rNueva = rNueva
        
        # Constantes
        self.rTierra = 1
        self.mSol = 1.989 * 10**30
        self.G = 6.674 * 10**-11
        self.GMs = 39.478 
        
        # 3ra ley de Kepler
        self.a = (self.rTierra + self.rNueva) / 2 
        self.pt = np.sqrt(self.a**3)
        self.T = self.pt / 2

        self.pn = np.sqrt(self.rNueva**3)
        self.Tn = self.pn / 2

    def calcular(self):
        # Calcular delta v

        deltaV1 = (np.sqrt(self.G * self.mSol / self.rTierra))*(np.sqrt((2*self.rNueva)/(self.rTierra + self.rNueva)) - 1)
        deltaV2 = (np.sqrt(self.G * self.mSol / self.rNueva))*(1 - np.sqrt((2*self.rTierra)/(self.rTierra + self.rNueva)))

        deltaV1_ms = deltaV1 * 1000
        deltaV2_ms = deltaV2 * 1000

        
        # Calcular theta 
        theta = 360* ((1/2) - (self.T / self.pn))
        deltaV1_Aa = deltaV1 * 31536000 / (149.6 * 10**6)

        return deltaV1_ms, deltaV2_ms, theta, self.T

    # Definimos las ecuaciones diferenciales
    def hohmann_transfer(self, state, t):
        x, y, vx, vy = state  
        r = np.sqrt(x**2 + y**2)  

        # Ecuaciones diferenciales
        dxdt = vx
        dydt = vy
        dvxdt = -self.GMs * x / r**3
        dvydt = -self.GMs * y / r**3
        
        return [dxdt, dydt, dvxdt, dvydt]

    def coordenadas(self):


        x0 = self.rNueva   # Posición inicial en UA (en la órbita de la Tierra)
        y0 = 0.0   # Posición inicial en UA
        vx0 = 0.0  # Velocidad inicial en X (UA/año)
        vy0 = self.rNueva / self.Tn * np.pi  # Velocidad orbital inicial en Y (UA/año)

        # Estado inicial [x, y, vx, vy]
        initial_state = [x0, y0, vx0, vy0]

        # Tiempo de integración (en años)
        t = np.linspace(0, 300, 10000)  # Simulamos 2 años, con 1000 puntos

        # Resolviendo las ecuaciones diferenciales
        solution = odeint(self.hohmann_transfer, initial_state, t)

        # Extraemos las soluciones
        x = solution[:, 0]
        y = solution[:, 1]
        return x, y

    def coordenadasTierra(self):


        x0 = 1   # Posición inicial en UA (en la órbita de la Tierra)
        y0 = 0.0   # Posición inicial en UA
        vx0 = 0.0  # Velocidad inicial en X (UA/año)
        vy0 = 2 * np.pi  # Velocidad orbital inicial en Y (UA/año)

        # Estado inicial [x, y, vx, vy]
        initial_state = [x0, y0, vx0, vy0]

        # Tiempo de integración (en años)
        t = np.linspace(0, 100, 10000)  # Simulamos 2 años, con 1000 puntos

        # Resolviendo las ecuaciones diferenciales
        solution = odeint(self.hohmann_transfer, initial_state, t)

        # Extraemos las soluciones
        x = solution[:, 0]
        y = solution[:, 1]
        return x, y
    
    