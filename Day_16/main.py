from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Name", ["Kyal", "Aye", "Htoo", "Hnin", "Htet"])
table.add_column("School", ["Raffle", "CIC", "KMITL", "UIT", "UIT"])
table.add_column("City", ["Bangkok", "Mudon", "Mudon", "Yangon", "Yangon"])
table.align = "l"

print(table)