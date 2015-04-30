'''
Created on 30/4/2015

@author: Daniel
'''
import datetime

class BilleteraElectronica(object):
    id=0    #Identificador estatico
    def __init__(self, nombres, apellidos, CI, PIN):
        self.__nombres=nombres
        self.__apellidos=apellidos
        self.__CI=CI
        self.__PIN=PIN
        self.creditos=[]
        self.debitos=[]
        self.__saldo=0
        self.identificador=id
        BilleteraElectronica.id+=1
    
    def saldo(self):
        return self.__saldo
    
    def recarga(self, monto, fecha, idlocal):
        if type(monto)!=type(int) or monto<=0:
            print("Error en el monto")
        elif type(datetime)!=type(fecha):
            print("Error en la fecha")
        else:
            self.__creditos.append([monto,fecha,idlocal])
            self.__saldo+=monto

    def consumir(self, monto, fecha, idestacionamiento, clavePIN):
        if type(monto)!=type(int) or monto<=0:
            print("Error en el monto")
        elif type(datetime)!=type(fecha):
            print("Error en la fecha")
        else:
            if self.__saldo<monto:
                print("Saldo insuficiente")
            elif clavePIN!=self.__PIN:
                print("Clave PIN incorrecta")
            else:
                self.__saldo-=monto
                self.__debitos.append([monto,fecha,idestacionamiento])
                
            
    
    