

texto=input("Insira um texto qualquer: ").lower()
quantidade_vogais=0


if  "a" in texto or "\u00E1" in texto:
    quantidade_vogais+=texto.count("a")+texto.count("\u00E1")
if  "e"  in texto or  "\u00E9" in texto:
    quantidade_vogais+=texto.count("e")+texto.count("\u00E9")
if  "i" in texto or "\u00ED" in texto:
    quantidade_vogais=+texto.count("i")+texto.count("\u00ED")
if  "o" in texto:
    quantidade_vogais+=texto.count("o")
if  "u" in texto:
    quantidade_vogais+=texto.count("u")

print("Quantidade de vogais: "+ str(quantidade_vogais))