class Encapsulation:
    def __init__(self):
        self._protectedVar = 'Nick'
        self.__privateVar = 'Perkins'
    
    # This function prints the data of the protected variable.
    def getProtected(self):
        print(self._protectedVar)
    # This function sets the data of the protected variable.
    def setProtected(self, protected):
        self._protectedVar = protected
    # This function prints the data of the private variable.
    def getPrivate(self):
        print(self.__privateVar)
    #This function sets the data of the private variable.
    def setPrivate(self, private):
        self.__privateVar = private
    
obj = Encapsulation()
obj.getProtected()
obj.getPrivate()
obj.setProtected('Eric')
obj.setPrivate('Gross')
obj.getProtected()
obj.getPrivate()  
