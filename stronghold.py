from math import *

x1, z1 = float(input("Ваша первая X-координата из первой точки: ")), float(input("Ваша первая Z-координата из первой точки: "))
alpha1 = float(input("Угол полета из первой точки: "))
x2, z2 = float(input("Ваша первая X-координата из второй точки: ")), float(input("Ваша первая Z-координата из второй точки: "))
alpha2 = float(input("Угол полета из второй точки: "))

z = (x2 + tan(radians(alpha2))*z2 - tan(radians(alpha1))*z1 - x1)/(tan(radians(alpha2))-tan(radians(alpha1)))
x = tan(radians(alpha1))*(z-z1) + x1
print(int(x))
print(int(z))
