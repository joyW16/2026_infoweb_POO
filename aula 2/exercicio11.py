import math

print("Informe o valor da base")
b = float(input())
print("Informe o valor da altura")
h = float(input())
diagonal = math.sqrt(b*b + h*h)
print(f"diagonal = {diagonal:.2f}")

# uma função não deve ter print nem input
def Diagonal (b, h):
    diagonal = math.sqrt(b*b + h*h)
    return diagonal

