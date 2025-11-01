
# Método de Euler - Ecuación Diferencial Separable

## Problema
Se desea resolver la ecuación diferencial:
\[
\frac{dy}{dt} = t \cdot y
\]
con la condición inicial:
\[
y(0) = 1
\]
en el intervalo \( t \in [0,1] \) y con paso \( h = 0.2 \).

---

## Solución Analítica (Separación de Variables)

1. Partimos de:
   \[
   \frac{dy}{y} = t \; dt
   \]
2. Integramos ambos lados:
   \[
   \int \frac{1}{y} dy = \int t dt
   \]
   \[
   \ln(y) = \frac{t^2}{2} + C
   \]
3. Aplicamos la condición inicial \( y(0) = 1 \):
   \[
   \ln(1) = 0 = C
   \]
4. Entonces la **solución exacta** es:
   \[
   y(t) = e^{t^2 / 2}
   \]

---

## Solución Numérica (Método de Euler)

El método de Euler se define como:
\[
y_{n+1} = y_n + h \cdot f(t_n, y_n)
\]

En este caso:
\[
f(t, y) = t \cdot y
\]

---

## Resultados

| t | y (Aprox) | y (Exacta) |
|---|-----------|------------|
| 0.0 | 1.00000 | 1.00000 |
| 0.2 | 1.00000 | 1.02020 |
| 0.4 | 1.04000 | 1.08329 |
| 0.6 | 1.12320 | 1.19722 |
| 0.8 | 1.25798 | 1.37713 |
| 1.0 | 1.45926 | 1.64872 |

---

## Archivos

- **euler_separable.py** → Contiene el código en Python con la solución analítica y numérica.
- **README.md** → Explicación del problema y los pasos realizados.

---

## Conclusión
El método de Euler aproxima la solución de manera sencilla, aunque presenta una ligera diferencia con respecto a la solución exacta. A medida que el paso \( h \) disminuye, la aproximación mejora.
