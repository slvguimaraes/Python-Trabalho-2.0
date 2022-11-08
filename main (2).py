def converter(h, m):
  if 0 < h<= 12 and 0 < m <60:
    print(f"{h}: {m} AM")
  elif 12 < h < 24 and 0 < m < 60:
    print(f"(h - 12):{m} PM")
  else:
    print("Valor invalido")
while True:
 h = int(input("Digite a hora:"))
 if h == 999:
     break
 m = int(input("Digite o minuto:"))  
converter(h,m)
print ("="*5)