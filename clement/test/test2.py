
import sys
import unittest
sys.path.extend(['.','..'])

#Import des classes à tester
from clement.classes.product_classes import Chaise, Pantalon
from clement.classes.inventory_manager import InventoryManager


inventory_manager = InventoryManager()
# Instanciation d'objets Chaise et Pantalon pour les tests
chaise = Chaise("materiau2", "couleur2", "dimension2", 50, 100, "Ikea")
pantalon = Pantalon("M", "noir", "jeans", 150, 200,"Zara")

inventory_manager.add_product(chaise, 5)
print(inventory_manager.get_product('Chaise').product.name)

