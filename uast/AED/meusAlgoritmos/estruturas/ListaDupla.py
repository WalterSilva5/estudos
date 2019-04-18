class ListaDupla(object):
    def __init__(self):
        self.fim = None
        self.inicio = None
        self.tam = 0
        
    class No:
        def __init__(self, value):
            self.proximo = None
            self.anterior = None
            self.value = value;
        
        def printNo(self):
            print(self.value)
            if self.proximo is not None:
                self.proximo.printNo()
                
        def printNoReverce(self):
            print(self.value)
            if self.anterior is not None:
                self.anterior.printNo()
                
                
            
    def insertEnd(self, value):
        no = self.No(value)
        if self.tam == 0:
            self.inicio = no
            self.fim = no
            self.tam = self.tam +1
        else:
            no.anterior = self.fim
            self.fim.proximo = no
            self.fim = no
        
            
    def insertMeio(self, index, value):
        pass
    
    def insertIni(self,value):
        no = self.No(value)
        no.proximo = self.inicio
        if self.inicio is not None:
            self.inicio.anterior = no
        else:
            self.fim = no
        self.inicio = no;
        self.tam = self.tam +1
        
    
    def insert(self, index, value):
        if(self.tam == 0 or index > self.tam):
            self.insertEnd(value)
        elif index < 0 :
            self.insertIni(value)
        else:
            self.insertMeio(index,value)
            
        
            
    def printList(self):
        self.inicio.printNo()
    
    def printListReverce(self):
        self.fim.printNoReverce()
        
        
lista = ListaDupla()
lista.insertEnd("wanderson")
lista.insertEnd("wanderson1")
lista.insertEnd("wanderson2")
lista.insertIni("wanderson0")

lista.printList();