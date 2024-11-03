resultados = [
    ("Equipe A", [80, 90, 85]),
    ("Equipe B", [70, 75, 80]),
    ("Equipe C", [90, 95, 100]),
    ("Equipe D", [60, 65, 70])
]

medias = []
for equipe, pontuacoes in resultados:
    media = sum(pontuacoes) / len(pontuacoes)
    medias.append((equipe, media))

medias.sort(key=lambda x: x[1], reverse=True)

print("Classificação final:")
for equipe, media in medias:
    print(f"{equipe}: {media:.2f}")
