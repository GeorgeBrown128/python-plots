import numpy as np
import matplotlib.pyplot as plt

# Create a range between 0 and 2pi
x = np.arange(0, 2*np.pi, np.pi/100)
# Compute the sine of each point in range y
y = np.sin(x)

# Plot x against y on the plot.
plt.plot(x, y)
# Add a title.
plt.title("sin(x)")
plt.xlabel("x")
plt.ylabel("y")
# Save the figure. Note this must happen before showing the figure.
plt.savefig('sine.eps', format='eps')
# Show the figure on the screen.
plt.show()
