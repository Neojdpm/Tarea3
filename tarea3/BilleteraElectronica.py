'''
Created on 30/4/2015

@author: Daniel
@author: Dayana Rodrigues
'''
from datetime import datetime

class BilleteraElectronica(object):
    id=0    #Identificador estatico
    def __init__(self, nombres, apellidos, CI, PIN):
        self.nombres=nombres
        self.apellidos=apellidos
        self.CI=CI
        self.__PIN=PIN
        self.__creditos=[]
        self.__debitos=[]
        self.__saldo=0
        self.identificador=BilleteraElectronica.id
        BilleteraElectronica.id+=1
    
    def saldo(self):
        return self.__saldo
    
    def creditos(self):
        return self.__creditos
    
    def debitos(self):
        return self.__debitos
    
    def recarga(self, monto, fecha, idlocal):
        if type(monto)!=type(1) or monto<=0:
            print("Error en el monto")
        elif datetime!=type(fecha):
            print("Error en la fecha")
        else:
            self.__creditos.append([monto,fecha,idlocal])
            self.__saldo+=monto
        return self.__saldo

    def consumir(self, monto, fecha, idestacionamiento, clavePIN):
        if type(monto)!=type(1) or monto<=0:
            print("Error en el monto")
        elif datetime!=type(fecha):
            print("Error en la fecha")
        else:
            if self.__saldo<monto:
                print("Saldo insuficiente")
            elif clavePIN!=self.__PIN:
                print("Clave PIN incorrecta")
            else:
                self.__saldo-=monto
                self.__debitos.append([monto,fecha,idestacionamiento])
        return self.__saldo
            
    
    