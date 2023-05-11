# Vous allez créer une classe InventoryProductEntry qui a pour role 
# de représenter une entrée d'inventaire pour un produit spécifique.
from clement.classes.product_classes import Product

class InventoryProductEntry:
    # Initialisation de la classe, en prenant en argument un objet Product et une quantité initiale
    def __init__(self, product:Product, quantity):
        self.product = product # Le produit
        self.quantity = quantity # un entier qui représente le nombre des pièces du produit en question
        self.sales = 0 # stocke le total des revenues des ventes du produit (somme(quantité * prix))
        self.expenses = 0 # stocke le total des dépenses pour restocker le produit


    #Méthode Sell
    """
    La méthode sell est utilisée pour retirer la quantité vendue du produit depuis le stock.
    Elle met également à jour les ventes totales pour le produit.
    
    """
    def sell(self, quantity):
        if self.quantity < quantity:
            print(f"Le stock du produit {self.product.name} est insuffisant.")
            return False
        else:
            self.quantity -= quantity
            self.sales += quantity * self.product.price
            return True
        
    
    #Méthode Restock
    """
    La méthode restock est utilisée pour augmenter la quantité en stock lorsqu'un nouveau stock de produit est reçu. 
    Elle met également à jour les dépenses totales pour restocker ce produit.
    """
    def restock(self, quantity):
        self.quantity += quantity
        self.expenses += quantity * self.product.cost
        return True

    #Méthode repr
    """
    La méthode repr est utilisée pour fournir une représentation en chaîne de caractères de l'objet InventoryProductEntry, 
    qui contient des informations utiles telles que le nom du produit, la marque, la quantité en stock et le prix du produit.

    """
    def __repr__(self):
        return f"{type(self.product).__name__} , {self.product.marque,} , quantité en stock: {self.quantity},  prix:{self.product.price}"
        # Retourner une chaîne de caractères formatée contenant le nom du produit, la marque, la quantité en stock et le prix du produit.