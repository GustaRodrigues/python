
class Conta:
    #Constructor
    def __init__(self, numero, titular, saldo, limite=1500.0):
        self.__numero = int(numero)
        self.__titular = titular
        self.__saldo = float(saldo)
        self.__limite = float(limite)
        self.__codigo_banco = "001"

    #Getters & Setters
    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    #Verifications
    def __tem_saldo(self, valor):
        return valor <= (self.__saldo + self.__limite)

    #Methods
    def extrato(self):
        print("Saldo disponível: R${}".format(self.__saldo))

    def deposita(self, valor):
        self.__saldo += valor
        print("Saldo atual: R${}".format(self.__saldo))

    def sacar(self, valor):
        if self.__tem_saldo(valor):
            self.__saldo -= valor
            print("Saldo atual: R${}".format(self.__saldo))
        else:
            print("Desculpe, seu saldo é insuficiente para concluir a operação :(")

    def transferir(self, conta, valor):
        if self.__tem_saldo(valor):
            self.sacar(valor)
            conta.deposita(valor)
        else:
            print("Desculpe, seu saldo é insuficiente para concluir a operação :(")

    #Static Methods
    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}
