
import os
class Impresion():
    
    def __init__(self):
        
        nombre_productos = []
        precio_productos = []
        productos_g = []
        
        #arreglo y variables con self
        self.artic_a = nombre_productos
        self.prec_a = precio_productos
        self.gen_a = productos_g

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
    
            #ingresando datos
            client = input("Nombre del cliente: ")
            cant_artic = float(input("Cantidad de artículos: "))
            producto = input("Descripción:")
            cant = float(input("Precio: "))

            #variables
            self.artic = cant_artic
            self.produc = producto
            self.prec = cant
            
            #precio por cantidad de producto
            self.artic_a.append(self.produc)
            self.prec_a.append(self.artic * self.prec)

            #Subtotal por cantidad
            self.subtotal_cant = (self.artic * self.prec)
            
            # Subtotal
            total = 0
            for suma in self.prec_a:
                total = total + suma
            self.sub_total = total
            
            #En General
            self.gen_a.extend(("Nombre del producto: " + self.produc + ", " + "Precio:",self.prec , "Cantidad:" ,self.artic,"subtotal de cantidad comprada:", self.subtotal_cant))
           
            #ITBMS
            self.itbms_f = (self.sub_total * 0.07)
            str(round(self.itbms_f,2))
            self.tot_itbms = (self.sub_total + self.itbms_f)

            #descuento
            self.desc_15 = (self.sub_total * 0.15)
            self.desc_10 = (self.sub_total * 0.10)
            
            #las transacciones
            print(self.gen_a)
            print("Subtotal:",self.sub_total)
            print("ITMBS:+",self.itbms_f)

            #Descuento
            if self.sub_total <= 600 and self.sub_total >= 200:
                self.total = print("Reducción del 15%: -",self.desc_15,"\nTotal:",self.tot_itbms - self.desc_15)
            elif self.sub_total >= 100:
                self.total = print("Reducción del 10%: -",self.desc_10,"\nTotal:",self.tot_itbms - self.desc_10)
            else:
                self.total = print("Total:",self.tot_itbms)

            #Total
            return(self.total)
            
            print("[2].Volver a cotizacion")
            print("[0].Volver al menú")
            
            #importacion
            from cotizacion_p import Cotizacion
            cr = Cotizacion()

            cotizacion = input()
            if cotizacion == "2":
              return cr
           
            menu = input()
            
            if menu == "0":
              print("Ok")
              break

p1 = Impresion()
