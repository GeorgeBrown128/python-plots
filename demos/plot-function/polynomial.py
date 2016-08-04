import numpy as np
import matplotlib.pyplot as plt

# Create a range between -5 and 5, 1000 points.
x = np.linspace(-5, 5, 1000)

# Plot the polynomials -3 - 3
plt.plot(x, x**1, x, x**2, x, x**3)
plt.plot(x, x**-1, x, x**-2, x, x**-3)

# Add a title and labels.
plt.title("Polynomial Functions")
plt.xlabel("x")
plt.ylabel("y")
plt.legend([
    r'$x^1$', r'$x^2$', r'$x^3$',
    r'$x^{-1}$', r'$x^{-2}$', r'$x^{-3}$'
])

# Set the axies.
plt.axis([-5,5,-5,5])

# Save the figure. Note this must happen before showing the figure.
plt.savefig('polynomial.eps', format='eps')

# Show the figure on the screen.
plt.show()
