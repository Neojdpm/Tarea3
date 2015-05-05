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
billeteraFrontera=BilleteraElectronica("H","-",11111111,"")
        
class testBilleteraElectronica(unittest.TestCase):
    
    # Casos de prueba del desarrollo TDD 
    
    def testTDD1(self):
        #Test verificacion del constructor
        #Verifica la aceptacion de caracteres especiales del espanol
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
        
    # Casos de prueba analisis de fronteras
    
    def testFrontera1(self):
        # Test de verificacion de caso frontera para la clase BilleteraElectronica
        billetera=BilleteraElectronica("","",0,"0124")
        self.assertEqual(["","",0],[billetera.nombres,billetera.apellidos,billetera.CI])
    
    def testFrontera2(self):
        # Test de verificacion de CI correcto
        self.assertRaises(TypeError,BilleteraElectronica("","","","0124"))
        
    def testFrontera3(self):
        #Test verificacion de recarga monto valido frontera numero pequeno
        saldoAntesRecarga=billeteraFrontera.saldo()
        numerochiquito=0.0000001
        self.assertEqual(billeteraFrontera.recarga(numerochiquito,fecha1,0),saldoAntesRecarga+numerochiquito)
        
    def testFrontera4(self):
        #Test verificacion de recarga monto valido frontera numero grande
        saldoAntesRecarga=billeteraFrontera.saldo()
        numerogrande=2**32
        self.assertEqual(billeteraFrontera.recarga(numerogrande,fecha1,0),saldoAntesRecarga+numerogrande)
    
    def testFrontera5(self):
        #Test verificacion de consumir monto valido frontera numero pequeno
        saldoAntesRecarga=billeteraFrontera.saldo()
        numerochiquito=0.0000001
        self.assertEqual(billeteraFrontera.consumir(numerochiquito,fecha1,0,""),saldoAntesRecarga-numerochiquito)
        
    def testFrontera6(self):
        #Test verificacion de consumir monto valido frontera numero grande
        saldoAntesRecarga=billeteraFrontera.saldo()
        numerogrande=2**32
        self.assertEqual(billeteraFrontera.consumir(numerogrande,fecha1,0,""),saldoAntesRecarga-numerogrande)
    
    
if __name__ == "__main__":
    unittest.main()