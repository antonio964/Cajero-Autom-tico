#------USUARIO Y CONTRASEÑA------
Saldo = 10000
Contraseña = 1313
while True:
    U = input("Escriba Usuario: ")
    if U==("Admin"):  
#-------MENÚ Y OPCIONES--------        
        while True:        
            C=int(input("Escriba su Contraseña: "))
            if C==Contraseña:
                print("Menú")
                print("1. Ver Saldo")
                print("2. Depositar")
                print("3. Retirar")
                print("4. Salir")
                while True:
                    o=int(input("SELECCIONE UNA OPCIÓN: "))
#-------OPCIÓN 1 DEL MENÚ------                 
                    if o==1:
                        print("Usted tiene un saldo de: "+str(Saldo))
                        break
#-------OPCIÓN 2 DEL MENÚ--------              
                    elif o==2:
                        print("Menú")
                        print("1: S/ 20.00")
                        print("2: S/ 50.00")
                        print("3: S/ 100.00")
                        print("4: S/ 150.00")
                        print("5: S/ 500.00")
                        print("6: Salir")
                        D=int(input("Seleccione una cantidad: "))
                        if D==1:
                            Saldo=Saldo+20
                            break
                        elif D==2:
                            Saldo=Saldo+50
                            break
                        elif D==3:
                            Saldo=Saldo+100
                            break
                        elif D==4:
                            Saldo=Saldo+150
                            break
                        elif D==5:
                            Saldo=Saldo+500
                            break
                        else:
                            print("opción incorrecta")
                            break
#-------OPCIÓN 3 DEL MENÚ---------                        
                    elif o==3:
                        print("Menú")
                        print("1: S/ 20.00")
                        print("2: S/ 50.00")
                        print("3: S/ 100.00")
                        print("4: S/ 150.00")
                        print("5: S/ 500.00")
                        print("6: Salir")
                        R=int(input("Seleccione una cantidad: "))
                        if R==1:
                            Saldo=Saldo-20
                            break
                        elif R==2:
                            Saldo=Saldo-50
                            break
                        elif R==3:
                            Saldo=Saldo-100
                            break
                        elif R==4:
                            Saldo=Saldo-150
                            break
                        elif R==5:
                            Saldo=Saldo-500
                            break
                        
                        else:
                            print("opción incorrecta")
                            break
#-------ERRORES---------
            else:   
                print("Contraseña Incorrecta")                
    else:
        print("USUARIO INCORRECTO") 

    




