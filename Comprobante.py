from factura import Impresion
ip = Impresion
class Comprobant():    
    
    def __init__(self):
 
        ipr = input(ip.Impresion())  

        if ipr == "2":
          return impre()
  
    
    def impre():
    
        print(self.esta_nom)
        print(self.ruc)
        print(self.dv)
        print(self.tel)
        print("Factura")
        print("FA-00",numero)
        print(client)
        print(cant_artic)
        print(producto)
        print(cant)
        print(self.gen_a)
        print("Subtotal:",self.sub_total)
        print("ITMBS:+",self.itbms_f)
        if self.sub_total <= 600 and self.sub_total >= 200:
            self.total = print("Reducción del 15%: -",self.desc_15,"\nTotal:",self.tot_itbms - self.desc_15)
        elif self.sub_total >= 100:
            self.total = print("Reducción del 10%: -",self.desc_10,"\nTotal:",self.tot_itbms - self.desc_10)
        else:
            self.total = print("Total:",self.tot_itbms)
        
        print(self.total)
        
        #comprobante
        print(self.esta_nom)
        print(self.ruc)
        print(self.dv)
        print(self.tel)
        print("Comprobante")
        print("CR-00",numero)
        print(client)
        print(cant_artic)
        print(producto)
        print(cant)
        print(self.gen_a)
        print("Subtotal:",self.sub_total)
        print("ITMBS:+",self.itbms_f)
        if self.sub_total <= 600 and self.sub_total >= 200:
            self.total = print("Reducción del 15%: -",self.desc_15,"\nTotal:",self.tot_itbms - self.desc_15)
        elif self.sub_total >= 100:
            self.total = print("Reducción del 10%: -",self.desc_10,"\nTotal:",self.tot_itbms - self.desc_10)
        else:
            self.total = print("Total:",self.tot_itbms)
        
        print(self.total)

p1 = Comprobant()
