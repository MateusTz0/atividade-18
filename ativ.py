# Crie um dicionário chamado notas com as chaves: Matemática, Português, História. Atribua valores (notas) e exiba a média.

notas = {"matematica": 8,
         "portugues": 9,
         "historia": 7}
soma = notas["matematica"] + notas["portugues"] + notas["historia"]
media = soma / 3
final = int(media)
print("o valor aproximado é",final)