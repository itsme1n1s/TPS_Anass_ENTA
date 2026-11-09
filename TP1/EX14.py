import pyfiglet

Title = pyfiglet.print_figlet("MAD->EURO", colors="yellow")

mad = float(input("donne moi le montant en MAD: "))
taux = float(input("donne moi le taux de change: "))
euro = mad / taux

print(f"le montant en euro est: {euro:.2f}")