def conversion_dec(number):
    dec = int(number)
    binary = bin(dec)[2:]  # Supprime le préfixe "0b"
    hexa = hex(dec)[2:].upper()  # Supprime le préfixe "0x" et met en majuscules
    return f"Décimal: {dec}, Binaire: {binary}, Hexadécimal: {hexa}"

def conversion_hex(number):
    dec = int(number, 16)  # Convertir la chaîne hexadécimale en nombre décimal
    binary = bin(dec)[2:]  # Convertir le nombre décimal en binaire et supprimer le préfixe "0b"
    return f"Hexadécimal: {number}, Décimal: {dec}, Binaire: {binary}"

def conversion_bin(number):
    dec = int(number, 2)  # Convertir la chaîne binaire en nombre décimal
    hexa = hex(dec)[2:].upper()  # Convertir le nombre décimal en hexadécimal et supprimer le préfixe "0x" et mettre en majuscules
    return f"Binaire: {number}, Décimal: {dec}, Hexadécimal: {hexa}"

# Exemple de test
number = input("Entrez un nombre décimal: ")
print(conversion_dec(number))