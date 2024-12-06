def conversion_dec_bin_hex(number):
    dec = int(number)
    binary = bin(dec)[2:]  # Supprime le préfixe "0b"
    hexa = hex(dec)[2:].upper()  # Supprime le préfixe "0x" et met en majuscules
    return f"Décimal: {dec}, Binaire: {binary}, Hexadécimal: {hexa}"

# Exemple de test
number = input("Entrez un nombre décimal: ")
print(conversion_dec_bin_hex(number))