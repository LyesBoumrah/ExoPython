def informations():
    nom = input("Entrez votre nom: ").upper()
    prenom = input("Entrez votre prenom: ")
    age = int(input("Entrez votre âge: "))
    taille = float(input("Entrez votre taille: "))
    fruits = input("Entrez vos fruits préférés: ")
    message = input("message personalisé:")
    nom_produit = input("Entrez le nom du produit: ")
    prix_produit = float(input("Entrez le prix du produit: "))
    
    return {
        "Nom": nom,
        "Prenom":prenom,
        "Âge": age,
        "Taille": taille,
        "Fruits préférés":fruits,
        "Message": message,
        "Produit": {"Nom": nom_produit,"Prix": prix_produit}
    }

if __name__ == "__main__":
    informations = saisir_informations()
    for key, value in informations.items():
        if isinstance(value, dict):
            print(f"{key}:")
            for sub_key, sub_value in value.items():
                print(f"    {sub_key}: {sub_value}")
        else:
            print(f"{key}: {value}")
