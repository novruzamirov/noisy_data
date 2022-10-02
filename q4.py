from numpy import diff

y = [1.9934, 2.1465, 2.2129, 2.1790, 2.0683, 1.9448, 1.7655, 1.5891]
x = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4]
derivation = diff(y)/diff(x)
print("Derivative at x = 0 is equal to ", derivation[0])
print("Derivative at x = 1 is equal to ", derivation[5])