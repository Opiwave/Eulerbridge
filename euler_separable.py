# euler_separable.py
# Resolución de una ecuación diferencial separable con el método de Euler
# Ecuación: dy/dt = t * y ,  y(0) = 1

from math import exp

def euler(dy_dt, y0, t0, t_final, h):
    t = t0
    y = y0
    resultados = [(t, y)]
    while t < t_final:
        y = y + h * dy_dt(t, y)
        t = round(t + h, 1)
        resultados.append((t, y))
    return resultados

# Definimos la ecuación diferencial
def f(t, y):
    return t * y

# Parámetros iniciales
y0 = 1.0
t0 = 0.0
t_final = 1.0
h = 0.2

# Solución aproximada con método de Euler
sol_aprox = euler(f, y0, t0, t_final, h)

# Solución exacta: y(t) = e^(t^2 / 2)
sol_exac = [(t, exp(t**2 / 2)) for t, _ in sol_aprox]

# Mostramos resultados
print("t\tAprox\t\tExacta")
for (t, ya), (_, ye) in zip(sol_aprox, sol_exac):
    print(f"{t:.1f}\t{ya:.5f}\t{ye:.5f}")
