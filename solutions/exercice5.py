#!/bin/python3.6

class VerificationInput(object):
          def __init__(self):
                    self.s = ""
          
          def setData(self):
                    self.s = input("Vous avez quelques choses à dire : ")

          def getData(self):
                    print(self.s.upper())

unSuperObjet = VerificationInput()
unSuperObjet.setData()
unSuperObjet.getData()