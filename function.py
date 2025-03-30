import numpy as np
import matplotlib.pyplot as plt
from scipy.special import hermite

def H(n, x):
    """Hermite polynomial of order n evaluated at x."""
    return hermite(n)(x)

# Example: Plot H₀(x) to H₃(x)
x = np.linspace(-4, 4, 500)
for n in range(4):
    plt.plot(x, H(n, x), label=f"n={n}")
plt.title("Hermite Polynomials $H_n(x)$")
plt.xlabel("x"), plt.ylabel("$H_n(x)$")
plt.legend(), plt.grid(True), plt.show()
