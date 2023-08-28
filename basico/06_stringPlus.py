text = "Aprendiendo Python"

if 'Python' in text:
  print("Hay vas")
else:
  print("pues...")

print(f"tamaño: {len(text)}" )
print(f"upper: {text.upper()}" )
print(f"lower: {text.lower()}" )
print(f"count (a): {text.lower().count('a')} en {text}" )
print(f"swapcase: {text.swapcase()}" )
print(f"start: {text.startswith('Apre')}" )
print(f"end: {text.endswith('hon')}" )

print(f"replace: {text.replace('Python','JS')}" )

text2 = "este es un titulo"
print(text2)
print(f"capitalize: {text2.capitalize()}")
print(f"title: {text2.title()}")
print(f"is digit: {text2.isdigit()}")
text2 = "123"
print(f"is digit (potencial): {text2.isdigit()}")

text3 = "hola mundo"
size = len(text3)
print(f"size: {size}")
print(f"ultimo: {text3[size-1]}")
print(f"ultimo pero sin tener que calcular: {text3[-1]}")

print(f"slicing: {text3[0:5]}")
print(f"slicing: {text3[5:size]}")
print(f"slicing: {text3[5:]}")
print(f"slicing: {text3[:5]}")

print(f"slicing: {text[0:11:2]}")
print(f"slicing: {text[::2]}")