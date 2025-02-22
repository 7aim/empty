from collections import Counter

paragraf = """
Sabahin erken saatlerinde, doğa yavaş yavaş uyaniyor.
Kuşlar, kuşlar neşeyle öterek, yeni bir günün habercisi oluyor.
Rüzgar hafif hafif esiyor, esiyor; ağaçlarin yapraklarini okşuyor.
Her şey, her şey taze ve umut dolu; her şey yeniden başliyor."""

print(Counter(paragraf)) #counts how many of each character there are.

newparagraf = paragraf.lower().split()
print(Counter(newparagraf))
print(Counter(newparagraf).most_common(1))


