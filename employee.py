class Employee:
    
    raise_amt=1.05
    
    def __init__(self, first, last, pay):
        self.first=first
        self.last =last
        self.pay =pay
    
    @property # email can be accessed as an attribute
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)
     
    @property
    def fullname(self): #fullname can be accessed as an atttribute
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay =int(self.pay * self.raise_amt)    
        


    
    
        