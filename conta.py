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
    
    def saca(self,valor):
        self.__saldo -= valor

    def transfere(self,destino,valor):
        self.saca(valor)
        destino.deposita(valor)

