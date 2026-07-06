import numpy as np
from scipy.integrate import trapezoid, simpson

# تعریف تابع انتگرال‌ده
def f(x):
    return np.exp(x**2)

# تعریف بازه و تعداد نقاط (مثلاً ۱۰۰ سطر داده برای دقت بالا)
x = np.linspace(0, 1, 101)
y = f(x)

# ۱. محاسبه انتگرال با روش ذوزنقه‌ای
integral_trapezoidal = trapezoid(y, x)

# ۲. محاسبه انتگرال با روش سیمسون
integral_simpson = simpson(y, x)

print("--- محاسبه انتگرال با روش‌های عددی ---")
print(f"روش ذوزنقه‌ای: {integral_trapezoidal:.6f}")
print(f"روش سیمسون: {integral_simpson:.6f}")