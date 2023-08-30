import unittest as ut
import XO 

class testcase1(ut.TestCase):
    def testA(self):
        self.assertEqual(XO.zona(20,2,4),40,'XO.zona 20/2*4')
        
    def testB(self):
        self.assertEqual(XO.zona(-20,5,5),-20,'XO.zona -20/5*5')
        
    def testC(self):
        self.assertNotEqual(XO.zona(20,0,6),ZeroDivisionError,'Ошибка деления на ноль')
        
ut.main()
    
        
class testcase2(ut.TestCase):
    def testA(self):
        self.assertEqual(XO.g(20,2),40,'XO.g 20*2')
        
    def testB(self):
        self.assertEqual(XO.g(20,0),0,'XO.g 20*0')   


         
ut.main()       
class testcase3(ut.TestCase):
    def testA(self):
        self.assertEqual(XO.plus(1,2,3),6,'XO.plus 1+2+3')
        
    def testB(self):
        self.assertEqual(XO.plus(-1,-2,-3),-6,'XO.plus -1+-2+-3') 
        
ut.main()
