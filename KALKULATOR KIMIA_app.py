import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def dose_response(x, A, B, C):
    return A / (1 + (x / C)**B)

# Konsentrasi (mg/L)
x_data = np.array([50, 100, 150, 200, 250])

# % inhibisi atau % aktivitas
y_data = np.array([20, 38, 55, 70, 85])

# Tebakan awal parameter
initial_guess = [100, 1, 100]

params, covariance = curve_fit(dose_response, x_data, y_data, p0=initial_guess)

A, B, IC50 = params

print(f"Nilai IC50 / EC50 = {IC50:.2f} mg/L")

x_fit = np.linspace(min(x_data), max(x_data), 500)
y_fit = dose_response(x_fit, A, B, IC50)

plt.scatter(x_data, y_data, label="Data Eksperimen")
plt.plot(x_fit, y_fit, label="Kurva Sigmoidal")
plt.axhline(50, linestyle="--")
plt.axvline(IC50, linestyle="--", label=f"IC50 = {IC50:.2f} mg/L")

plt.xlabel("Konsentrasi (mg/L)")
plt.ylabel("% Inhibisi / Aktivitas")
plt.legend()
plt.show()
