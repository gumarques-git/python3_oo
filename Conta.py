class Conta:
    'Definindo Objeto Conta'

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ... {}".format(type(self)))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite


    def extrato(self):
        print('Saldo de {} do titular {}'.format(self.__saldo, self.__titular))


    def deposita(self, valor):
        self.__saldo += valor


    def __pode_sacar(self, valor_a_sacar):
        return valor_a_sacar <= (self.__saldo + self.__limite)


    def saca(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))


    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)


    @property
    def saldo(self):
        return self.__saldo


    @property
    def titular(self):
        return self.__titular


    @property # Criando getter
    def limite(self):
        return self.__limite


    @limite.setter #Criando Setter
    def limite(self, limite):
        self.__limite = limite


    @staticmethod # Criando metodo estatico
    def codigo_banco():
        return '001'  #Supondo que seja Bando do Brasil

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}