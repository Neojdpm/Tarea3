'''
Created on 30/4/2015

@author: Daniel
@author: Dayana Rodrigues
'''
from datetime import datetime

class BilleteraElectronica(object):
    id=0    #Identificador estatico
    def __init__(self, nombres, apellidos, CI, PIN):
        #Verificacion de CI, levanta excepcion
        if type(CI)!=type(1) or CI<0:
            raise TypeError
        else: self.CI=CI
        self.nombres=nombres
        self.apellidos=apellidos
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
        try:
            monto+=0.0 #Verificacion del monto
        except:
            print("Error en el monto")
            return self.__saldo
        
        if monto<=0:
            print("El monto debe ser mayor a 0")
        elif datetime!=type(fecha):
            print("Error en la fecha")
        else:
            self.__creditos.append([monto,fecha,idlocal])
            self.__saldo+=monto
        return self.__saldo

    def consumir(self, monto, fecha, idestacionamiento, clavePIN):
        try:
            monto+=0.0 #Verificacion del monto
        except:
            print("Error en el monto")
            return self.__saldo
        
        if monto<=0:
            print("El monto debe ser mayor a 0")
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
            
    
    