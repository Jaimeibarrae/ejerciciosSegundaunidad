def piraminde ():
    spaces = 10-1
    asterist = 1
    for lines in range(10):
        while spaces >= 0: 
            print ('%s%s%s' % ((' '*spaces), ('0'*asterist), (' '*spaces)))
            spaces -= 1
            asterist += 2
piraminde()
input("")
