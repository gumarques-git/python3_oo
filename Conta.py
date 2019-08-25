class Conta:
    'Definindo Objeto Conta'

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ... {}".format(type(self)))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self,__limite = limite

    def extrato(self):
        print('Saldo de {} do titular {}'.format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        self.__saldo -= valor