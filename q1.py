import numpy as np
from sympy import symbols, Poly, simplify, interpolating_poly
from scipy.interpolate import CubicSpline

x_pts = [1, 2, 3, 4, 5, 6]
y_pts = [1, 3, 5, 8, 5, 2]

X = symbols('X')

# 1. Lagrange Interpolation
lagrange_poly = interpolating_poly(len(x_pts), X, x_pts, y_pts)
print("=== Lagrange Interpolation Polynomial ===")
print("f(X) =", simplify(lagrange_poly))
print()

# 2. Cubic Spline Interpolation
spline = CubicSpline(x_pts, y_pts, bc_type='natural')
print("=== Natural Cubic Spline (Piecewise) ===")

for i in range(len(x_pts) - 1):
    a, b, c, d = spline.c[:, i]
    x_i = x_pts[i]
    
    expr = a*(X - x_i)**3 + b*(X - x_i)**2 + c*(X - x_i) + d
    poly_standard = Poly(expr.expand(), X)
    poly_rounded = Poly([round(float(coef), 4) for coef in poly_standard.all_coeffs()], X)
    
    print(f"Interval [{x_pts[i]}, {x_pts[i+1]}]: S_{i}(X) = {poly_rounded.as_expr()}")