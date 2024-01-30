# Tes Rekam (w)
with open('text.txt', 'w', encoding='utf-8') as f:
    f.write('Halo')

# Menambahkan (a)
with open('text.txt', 'a') as f:
    f.write(', My name is Elang')

# Membaca 'r'
with open('text.txt', 'r') as f:
    print(f.read())

