Subaru = 0
Emilia = 0
Rem = 0
Stella = 0
Roswaal = 0

while(Roswaal == 0) :
    inp = input("Dating with Emilia ? : ")
    if(inp == "Y") :
        inp = input("Run into Stella ? : ")
        if(inp == "Y") :
            Emilia += 1
            Subaru += 1
        continue
    inp = input("Dating with Rem ? : ")
    if(inp == "Y") :
        inp = input("Run into Stella ? : ")
        if(inp == "Y") :
            Rem += 1
            Subaru += 1
        continue
    inp = input("Dating with Stella ? : ")
    if(inp == "Y") :
        Stella += 1
        Subaru += 1
        continue
    inp = input("Dating with Roswaal ? : ")
    if(inp == "Y") :
        Roswaal += 1
        Subaru += 1
    elif(inp == "N") :
        break

print ("Subaru : " + str(Subaru))
print ("Emilia : " + str(Emilia))
print ("Rem : " + str(Rem))
print ("Stella : " + str(Stella))
print ("Roswaal : " + str(Roswaal))

