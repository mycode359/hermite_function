import numpy as np
import matplotlib.pyplot as plt
from scipy.special import hermite
from scipy.integrate import quad
from math import factorial

# Set up the plotting style
plt.style.use('seaborn')
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 12

# Define the normalized Hermite function formula (your equation 2)
def hermite_function(n, x):
    """
    Calculate the Hermite function of order n at position x
    using the exact quantum mechanical formula:
    
    ψₙ(x) = (1/(√(2ⁿ n! √π))) * Hₙ(x) * e^(-x²/2)
    
    where Hₙ(x) is the nth Hermite polynomial
    """
    # Normalization constant
    normalization = 1.0 / np.sqrt(2**n * factorial(n) * np.sqrt(np.pi))
    
    # Get the Hermite polynomial of degree n
    Hn = hermite(n)
    
    # Calculate the full function
    return normalization * Hn(x) * np.exp(-x**2 / 2)

# Create a grid of x values
x = np.linspace(-4, 4, 1000)

# Plot the first 5 Hermite functions
plt.figure(figsize=(12, 8))
for n in range(5):
    y = hermite_function(n, x)
    plt.plot(x, y, label=f'n = {n}', linewidth=2)
    
plt.title('Hermite Functions $\psi_n(x)$ (Quantum Harmonic Oscillator Basis)', pad=20)
plt.xlabel('Position (x)')
plt.ylabel('$\psi_n(x)$')
plt.legend(loc='upper right')
plt.grid(True, alpha=0.3)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.tight_layout()
plt.show()

# Verify orthonormality by numerical integration
print("Orthonormality Check:")
print("---------------------")
print(" n | m | Integral | Expected")
print("---|---|---|---------")

tolerance = 1e-5
for n in range(3):
    for m in range(3):
        # Compute the overlap integral
        integral, _ = quad(lambda x: hermite_function(n, x) * hermite_function(m, x), -np.inf, np.inf)
        
        # Compare with expected Kronecker delta
        expected = 1.0 if n == m else 0.0
        result = "✓" if abs(integral - expected) < tolerance else "✗"
        
        print(f" {n} | {m} | {integral:.6f} | {expected} {result}")

# Plot probability densities |ψₙ(x)|²
plt.figure(figsize=(12, 8))
for n in range(4):
    y = hermite_function(n, x)
    plt.plot(x, y**2, label=f'n = {n}', linewidth=2)
    
plt.title('Probability Densities $|\psi_n(x)|^2$', pad=20)
plt.xlabel('Position (x)')
plt.ylabel('$|\psi_n(x)|^2$')
plt.legend(loc='upper right')
plt.grid(True, alpha=0.3)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.tight_layout()
plt.show()

# Plot higher energy states
plt.figure(figsize=(12, 8))
for n in [5, 10, 15, 20]:
    y = hermite_function(n, x)
    plt.plot(x, y, label=f'n = {n}', linewidth=2)
    
plt.title('Higher Order Hermite Functions', pad=20)
plt.xlabel('Position (x)')
plt.ylabel('$\psi_n(x)$')
plt.legend(loc='upper right')
plt.grid(True, alpha=0.3)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.tight_layout()
plt.show()
