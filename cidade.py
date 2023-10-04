pais_a=80000
taxa_a=0.03
pais_b=200000
taxa_b=0.015
anos=0
while pais_a < pais_b:
    pais_a=pais_a*taxa_a+pais_a
    pais_b=pais_b*taxa_b+pais_b
    anos=anos+1
print("Número de anos necessários: ", anos)