from prettytable import PrettyTable
x = PrettyTable()

x.add_column("Pokemon Name", ["Butterfree", "Bulbasaur", "Blastoise", "Charmander"])
x.add_column("Types", ["Bug", "Grass", "Water", "Fire"])
print(x)


