'''
Created on 30/4/2015

@author: Daniel
@author: Dayana Rodrigues
'''
import unittest
from BilleteraElectronica import *

fecha1=datetime(2015,4,25)
fecha2=datetime(2015,8,25)
billetera=BilleteraElectronica("Pingüinación","Pe-ñascos",24981045,"0124")
billetera2=BilleteraElectronica("Juan","Pepito",20991820,"Tumama")

class testBilleteraElectronica(unittest.TestCase):
    
    def testTDD1(self):
        #Test verificacion del constructor
        #Verifica la aceptacion de caracteres especiales del español
        self.assertEqual(["Pingüinación","Pe-ñascos",24981045],[billetera.nombres,billetera.apellidos,billetera.CI])
    
    def testTDD2(self):
        #Test verificacion de valores iniciales
        self.assertEqual(billetera.saldo(),0)
    
    def testTDD3(self):
        #Test verificacion de identificadores
        self.assertNotEqual(billetera.identificador,billetera2.identificador)
    
    def testTDD4(self):
        #Test verificacion de recarga base
        saldoAntesRecarga=billetera.saldo()
        self.assertEqual(billetera.recarga(100,fecha1,0),saldoAntesRecarga+100)
    
    def testTDD5(self):
        #Test verificacion de consumo base
        saldoAntesRecarga=billetera.saldo()
        self.assertEqual(billetera.consumir(100,fecha2,0,"0124"),saldoAntesRecarga-100)
    
    def testTDD6(self):
        #Test verificacion de credito/debito base
        self.assertEqual(billetera.creditos(),[[100,fecha1,0]])
        self.assertEqual(billetera.debitos(),[[100,fecha2,0]])
    
    def testTDD7(self):
        #Test verificacion de recarga base
        saldoAntesRecarga=billetera.saldo()
        self.assertEqual(billetera.recarga("100",fecha1,0),saldoAntesRecarga)
    
    def testTDD8(self):
        #Test verificacion de recarga base
        saldoAntesRecarga=billetera.saldo()
        self.assertEqual(billetera.consumir(100.0,fecha1,0,"0124"),saldoAntesRecarga)
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()