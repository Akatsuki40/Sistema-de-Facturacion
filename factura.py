import os
class Impresion():
    #def __init__(self):
      # se imprimen los datos
        #self.numero = 1
    def __init__(self):
        
        numero = 0 #consecuente
    
        while True:
            numero = numero + 1 #Aumenta el num de factura
            os.system("clear")#Limpia la pantalla
            
            print("El Gram Almacen")
            print("RUC 564-35-98512")
            print("DV 34")
            print("Telefono: 666-66666")
            print("Factura")
    #____________________________________________
    
            print("FA-00",numero)#Imprime el numero de Factura
            #Solo para simular distintas facturas
    
  
            input("Nombre del cliente: ")
            cant_artic = input("Cantidad de artículos: ")
            print("Descripción:")
            input("")
            cant = input("Cantidad a comprar: ")

            print("[3].Volver a cotizacion")
            print("[2].Imprimir")
            print("[0].Volver al menú")
            
            from cotizacion_p import Cotizacion
            cr = Cotizacion()

            cotizacion = input()
            if cotizacion == "3":
              return cr
           
            menu = input()
            
            if menu == "0":
              print("Ok")
              break

p1 = Impresion()
