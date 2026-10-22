def cryptage(message, decalage):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    resultat = ""
    for lettre in message:
        if lettre in alphabet:
            position = alphabet.index(lettre)
            nouvelle_position = (position + decalage) % 26
            nouvelle_lettre = alphabet[nouvelle_position]
            resultat += nouvelle_lettre

        else: 
            resultat += lettre

    return resultat

print(cryptage("je suis de passage", 3))