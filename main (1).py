def Imposto(taxa, Custo):
  return (1 + taxa / 100) * Custo


taxa = float(input("Digite o imposto: "))
custo = float(input("Custo: "))

print("O imposto é:", Imposto(taxa, custo))
