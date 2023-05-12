import os
import json
import readline
import treelib
import clement.classes.tree_clients_structured as Tree_clients_structured
import clement.classes.inventory_manager as Inventory_manager

from unidecode import unidecode
from classes.product_classes import *
from clement.generation.hierarchy import generate_class_hierarchy


# Define the prompt_for_instance function 
# that takes a class name as a string as input
def prompt_for_instance(cls):
    # Get the class object from the class name string
    # Get the names of the constructor arguments
    arg_names = cls.__init__.__code__.co_varnames[1:]
    # Prompt the user for the values of the arguments 
    print(cls.__name__,":")
    args = [input("Enter the value for {}: ".format(name)) for name in arg_names]
    # Create an instance of the class using the entered values
    return cls(*args)

# on cree une classe Tree qui herite de treelib.Tree
# et rajoute deux fonctionnalités supplémentaires
# get_penultimate_nodes -> recupère les avant derniers noeuds
# get_children_nodes -> recupère les noeud terminaux
class TreeExt(treelib.Tree):
    def __init__(self):
        super().__init__()
    
    def get_penultimate_nodes(self):
        penultimate_nodes = set()
        for node in self.all_nodes():
            if not self.children(node.identifier):
                parent_node = self.parent(node.identifier)
                if parent_node is not None and not self.children(node.identifier):
                    penultimate_nodes.add(parent_node.identifier)
        return penultimate_nodes
    
    # Define a function to get the immediate children nodes of a specified node
    def get_children_nodes(self, node_name):
        children_nodes = []
        node = self.get_node(node_name)
        if node is not None:
            children = self.children(node.identifier)
            children_nodes = [child.identifier for child in children]
        return children_nodes

def sep():
    print("====================")

def main():

    inventory_manager = Inventory_manager.InventoryManager()
    # write code to read json file as dict
    local_path = os.path.dirname(os.path.abspath(__file__))
    json_data = json.load(open(os.path.join(local_path, 'json_data.json'), "rb"))
    json_str = json.dumps(json_data)
    json_data = (unidecode(json_str))
    json_dict = json.loads(json_data)

    class_tree = TreeExt()
    class_tree.create_node(tag="Product Classe Hierarchy", identifier="racine")
    Tree_clients_structured.create_tree_from_dict(class_tree, "racine", json_dict)


    readline.set_completer_delims('\t\n')
    readline.parse_and_bind("tab: complete")

    # Define a function to handle user input
    def auto_complete(text, list):
        matching_entry = [entry for entry in list if entry.startswith(text)]
        if len(matching_entry) == 1:
            entry_name = matching_entry[0]
            remaining_text = entry_name[len(text):]
            if remaining_text:          
                readline.insert_text(remaining_text)
                readline.redisplay()
                
    def set_autocomplete(list):
        readline.set_completer(lambda text, state: auto_complete(text,list))

    while True:
        print("""
			What would you like to do? :
			A. Add a product to stock
			R. Restock a product quantity
			S. Sell a product quantity
			D. Remove a product from stock
			L. List the products in stock
			B. Show the current balance
			Q. Quit
		""")

        
        choice = input("Enter your choice: ")
        choice = choice.upper()
        
        if choice == "A":
            # write code to get class tree hierachy
            # convert the tree object to TreeExt to get the new functionalities 
            # described above in TreeExt class
            
            # ecrire le code pour récupérer les avant dernier noeuds de classe
            # (dernier niveau de catégories de produits)
            product_classes = class_tree.get_penultimate_nodes()
        
            sep()

            # write code to print list of product_classes
            print(product_classes)
            set_autocomplete(product_classes)
            category = input("Enter the category of the product: ")
            
            # Get the immediate children nodes of node 'B'
            children_nodes = class_tree.get_children_nodes(category)
            # write code to print list of children_nodes
            print(children_nodes)
            set_autocomplete(children_nodes)
            product_name = input("Enter your product choice: ")   
            #print(f"{name} has been added to stock with a quantity of {quantity}.")

            # write code to create a instance of classe product_name
            product_entry = prompt_for_instance(globals()[product_name])
            quantity = int(input("Enter quantity: "))
            # write code to add product_entry and quantity in Inventory Manager
            inventory_manager.add_product(product_entry, quantity)

        elif choice == "R":
            name = input("Enter the name of the product: ")
            quantity = int(input("Enter the quantity to restock: "))
            product = inventory_manager.get_product(name)
            inventory_manager.restock_product(product, quantity)


        elif choice == "S":
            name = input("Enter the name of the product: ")
            quantity = int(input("Enter the quantity to sell: "))
            product = inventory_manager.get_product(name)
            inventory_manager.sell_product(product, quantity)

        elif choice == "D":
            name = input("Enter the name of the product: ")
            # write code to get product
            product = inventory_manager.get_product(name)
            #if product:
            if product:
                inventory_manager.remove_product(product) # write code to remove product
                print(f"{name} has been removed from stock.")
            else:
                print(f"{name} is not in stock.")

        elif choice == "L":
            inventory_manager.list_products()

        elif choice == "B":
            # write code to print current balance
            print(f"Current balance : {inventory_manager.current_balance()} euros")            
        elif choice == "Q":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == '__main__':
    main()
