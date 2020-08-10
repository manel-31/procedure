#gardien de phare

#definition de la fonction
def hauteurparcourue(nbr,h):
    print('pour',nbr,' marches de ',h,' cm , il parcoure',(nbr*h*2*5*7)/100,' m par semaine')

#le programme principal
nbr=float(input('entez le nombre de pas :'))
h=float(input('entrez la hauteur des pas '))

hauteurparcourue(nbr,h)
print('hello')
print('tester modif sur branche git')
