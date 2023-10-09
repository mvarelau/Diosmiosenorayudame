#2-50
#2-50
n=float(input("Ingrese un número del 2 al 50: "))
a= 0
while (a<n and 2<=n<=50):
  a+=1
  if n%a!=0:
    continue
  print(f"Los divisores de {n} son: {a}")
