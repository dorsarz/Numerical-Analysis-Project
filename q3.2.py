import numpy as np
from scipy.integrate import quad

# تعریف تابع
def f(x):
    return np.exp(x**2)

# محاسبه انتگرال با روش گوسی (بازه 0 تا 1)
integral_gauss, error = quad(f, 0, 1)

print("--- محاسبه انتگرال با روش گوسی ---")
print(f"روش گوسی: {integral_gauss:.6f}")