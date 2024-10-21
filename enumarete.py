
vogais=["julio","luiz","jv","jg","delei",56,78.6]

for indices,nomes in enumerate(vogais,start=1):
 print(f"O indice {indices} corresponde a {nomes}")  

for  indices,nomes in enumerate(vogais,start=1):  
 print(f"Indices {indices}, Nomes {nomes} , Tipos: {type(nomes).__name__} ")