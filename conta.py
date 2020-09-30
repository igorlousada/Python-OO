class ContaCorrente:
    def __init__(self,numero,titular,saldo,limite=1000):
        print("Construindo Objeto...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo {} do titular {}.".format(self.__saldo,self.__titular))

    def deposita(self,valor):
        self.__saldo += valor
    def __pode_saca(self,valor_a_sacar):
        valor_disponivel = self.__limite + self.saldo
        return valor_a_sacar <= valor_disponivel
    def saca(self,valor):
        if(self.__pode_saca(valor)):
            self.__saldo -= valor
        else:
            print("limite ultrapassado")    

    def transfere(self,destino,valor):
        self.saca(valor)
        destino.deposita(valor)
    @property        
    def saldo(self):
        return self.__saldo
    @property    
    def titular(self):
        return self.__titular
    @property   
    def limite(self):
        return self.__limite
    @limite.setter
    def limite(self,valor):
        self.__limite = valor    

