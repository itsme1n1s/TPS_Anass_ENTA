import pyfiglet

Title = pyfiglet.print_figlet("Prix a payer", colors="green")

qt = float(input("donne moi la quantite de produit: "))
prix = float(input("donne moi le prix du produit: "))
total = qt * prix
prixf = total * 0.15
montant_de_reduction = total - prixf

print(f"le prix total est: {total:.2f}")
print(f"le montant de reduction est: {montant_de_reduction:.2f}")
print(f"le prix a payer est: {prixf:.2f}")