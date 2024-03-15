class Cliente():
    ''' Define objetos do tipo Cliente '''


    def __init__(self, nome, cpf, dt_nasc, telefone):
        ''' Constrói uma instância de Cliente '''
        self.__nome = nome
        self.__cpf = cpf
        self.__dt_nasc = dt_nasc
        self.__telefone = telefone


    @property
    def nome(self):
        ''' Retorna o nome do Cliente. '''
        return self.__nome


    @nome.setter
    def nome(self, novo_nome):
        ''' Altera o nome do Cliente.

                Requer: novo_nome ser uma string.
        '''
        if not isinstance(novo_nome, str):
            raise ValueError("O nome passado não é uma string.")
        self.__nome = novo_nome


    @property
    def cpf(self):
        ''' Retorna  o CPF do Cliente. '''
        return self.__cpf


    @cpf.setter
    def cpf(self, novo_cpf):
        ''' Altera o CPF do Cliente.

                Requer: novo_cpf ser uma string e ter 11 caracteres.
        '''
        if not isinstance(novo_cpf, str):
            raise ValueError("O CPF passado não é uma string.")
        if not novo_cpf.isdigit():
            raise ValueError("O CPF passado não é composto por dígitos.")
        if len(novo_cpf) != 11:
            raise ValueError("O CPF passado não tem 11 dígitos.")
        self.__cpf = novo_cpf


    @property
    def dt_nasc(self):
        ''' Retorna a data de nascimento do Cliente '''
        return self.__dt_nasc


    @dt_nasc.setter
    def dt_nasc(self, nova_dt_nasc):
        ''' Altera a data de nascimento do Cliente

                Requer:
                    - nova_dt_nasc ser uma tupla contendo 3 inteiros (aaaa, mm, dd).
                    - aaaa > 1800
                    - 0 < mm < 13
                    - 0 < dd < 32
        '''
        if not isinstance(nova_dt_nasc, tuple):
            raise ValueError("A data passada não é uma tupla.")
        if len(nova_dt_nasc) != 3:
            raise ValueError("A tupla não tem 3 dígitos.")
        if(not isinstance(nova_dt_nasc[0], int) and
           not isinstance(nova_dt_nasc[1], int) and
           not isinstance(nova_dt_nasc[2], int)):
            raise ValueError("A tupla não é composta por inteiros.")
        if nova_dt_nasc[0] < 1800:
            raise ValueError("O ano passado não é válido")
        if nova_dt_nasc[1] <= 0 and nova_dt_nasc[1] > 12:
            raise ValueError("O mês passado não é válido")
        if nova_dt_nasc[1] <= 0 and nova_dt_nasc[1] > 31:
            raise ValueError("O dia passado não é válido")
        self.__dt_nasc = nova_dt_nasc


    @property
    def telefone(self):
        ''' Retorna o telefone do Cliente. '''
        return self.telefone


    @telefone.setter
    def telefone(self, novo_telefone):
        ''' Altera o telefone do Cliente.

                Requer: novo_telefone ser uma string contendo dígitos.
        '''
        if not isinstance(novo_telefone, str):
            raise ValueError("O telefone passado não é uma string.")
        if not novo_telefone.isdigit():
            raise ValueError("O telefone passado não é composto por dígitos.")
