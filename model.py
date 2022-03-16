class Empresa:

    def __init__(self, nome_empresa, cnpj):
        self.nome = nome_empresa
        self.cnpj = cnpj
        self.funcionarios = [ ]
    
    def cadastrar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def get_funcionarios(self):
        return self.funcionarios
    
    def excluir_funcionario(self, matricula):
        for funcionario in self.funcionarios:
            if funcionario.matricula == matricula:
                self.funcionarios.remove(funcionario)
                return True
        return False

    def set_funcionario(self, matricula, novo_nome = None, nova_matricula = None, 
    nova_idade = None, novo_sexo = None, novo_cpf = None, novo_salario = None, nova_rua = None, 
    nova_cidade = None, novo_estado = None, novo_cep = None):

        for funcionario in self.funcionarios:
            if funcionario.matricula == matricula:
                print(funcionario)
                if novo_nome != None:
                    funcionario.nome = novo_nome
                
                if nova_matricula != None:
                    funcionario.matricula = nova_matricula
                
                if nova_idade != None:
                    funcionario.idade = nova_idade
                
                if novo_sexo != None:
                    funcionario.sexo = novo_sexo
            
                if novo_cpf != None:
                    funcionario.cpf = novo_cpf
                
                if novo_salario != None:
                    funcionario.salario = novo_salario
                
                if nova_rua != None:
                    funcionario.endereco.rua = nova_rua
                
                if nova_cidade != None:
                    funcionario.endereco.cidade = nova_cidade
                
                if novo_estado != None:
                    funcionario.endereco.estado = novo_estado
                
                if novo_cep != None:
                    funcionario.endereco.cep = novo_cep

        return funcionario

    def get_funcionario_por_matricula(self, matricula):
        for funcionario in self.funcionarios:
            if funcionario.matricula == matricula:
                return funcionario

    def get_funcionario_por_cpf(self, cpf):
        for funcionario in self.funcionarios:
            if funcionario.cpf == cpf:
                return funcionario

    def get_funcionarios_por_cidade(self, cidade):
        lista = [ ]

        for funcionario in self.funcionarios:
            if funcionario.endereco.cidade == cidade:
                lista.append(funcionario)
        return lista

    def get_funcionarios_por_estado(self, estado):
        lista = [ ]

        for funcionario in self.funcionarios:
            if funcionario.endereco.estado == estado:
                lista.append(funcionario)
        return lista
    
    def get_funcionarios_por_salario_maior_ou_igual(self, salario):
        #lista os funcionario que tem um salário maior ou igual ao que foi passado        
        lista = [ ]

        for funcionario in self.funcionarios:
            if float(funcionario.salario) >= float(salario):
                lista.append(funcionario)
        return lista

    def get_funcionarios_por_salario_menor_ou_igual(self, salario):
        #lista os funcionarios que tem um salario menor ou igual ao que foi passado
        lista = [ ]

        for funcionario in self.funcionarios:
            if float(funcionario.salario) <= float(salario):
                lista.append(funcionario)
        return lista

    def get_funcionarios_por_sexo(self, sexo):
        lista = [ ]

        for funcionario in self.funcionarios:
            if funcionario.sexo.upper() == sexo.upper():
                lista.append(funcionario)
        return lista
    
    def get_funcionarios_por_sexo_e_ganham_mais_x(self, sexo, salario):
        #Listar todos os Funcionários dependendo do sexo e do salário que foi passado
        #X seria o salario que foi passado
        lista = [ ]

        for funcionario in self.funcionarios:
            if funcionario.sexo.upper() == sexo.upper():
                if float(funcionario.salario) >= float(salario):
                    lista.append(funcionario)
        return lista
    
    def get_funcionarios_por_estado_e_ganham_entre_x_e_y(self, estado, salario1, salario2):
        #Listar os Funcionários que são do estado passado por parametro
        # e também os dois salários
        lista = [ ]

        for funcionario in self.funcionarios:
            if funcionario.endereco.estado.upper() == estado.upper():
                if float(funcionario.salario) >= float(salario1) and float(funcionario.salario) <= float(salario2):
                    lista.append(funcionario)
        return lista
                    
    
    def get_funcionarios_por_letra(self, letra):
        lista = [ ]
        
        for funcionario in self.funcionarios:
            if funcionario.nome[0] == letra:
                lista.append(funcionario)
        return lista
    
    def get_funcionario_por_maior_salario(self, sexo):
        maior_salario = 0.0
        maior_funcionario = None

        for funcionario in self.funcionarios:
            if funcionario.sexo.upper() == sexo.upper():
                if float(funcionario.salario) > float(maior_salario):
                    maior_funcionario = funcionario
                    maior_salario = maior_funcionario.salario
        print(maior_funcionario)

    def get_funcionario_por_menor_salario(self, sexo):
        menor_salario = 999999999
        menor_funcionario = None

        for funcionario in self.funcionarios:
            if funcionario.sexo.upper() == sexo.upper():
                if float(funcionario.salario) < float(menor_salario):
                    menor_funcionario = funcionario
                    menor_salario = menor_funcionario.salario
        print(menor_funcionario)
        
    def get_funcionario_por_maior_idade(self, sexo):
        #Mostrar o Funcionário mais velho
        maior_idade = 0
        maior_funcionario = None

        for funcionario in self.funcionarios:
            if funcionario.sexo.upper() == sexo.upper():
                if int(funcionario.idade) > int(maior_idade):
                    maior_funcionario = funcionario
                    maior_idade = maior_funcionario.idade
        print(maior_funcionario)
        
    def get_funcionario_por_menor_idade(self, sexo):
        #Mostrar o Funcionário mais novo
        menor_idade = 9999
        menor_funcionario = None

        for funcionario in self.funcionarios:
            if funcionario.sexo.upper() == sexo.upper():
                if int(funcionario.idade) < int(menor_idade):
                    menor_funcionario = funcionario
                    menor_idade = menor_funcionario.idade
        print(menor_funcionario)

    def get_funcionarios_cadeirante(self, cadeirante):
        lista = [ ]

        for funcionario in self.funcionarios:
            if funcionario.cadeirante.upper() == cadeirante.upper():
                lista.append(funcionario)
        return lista
    
    def get_aposentadoria(self):
        """
        Pesquisei no google com quantos anos se aposenta apareceu isso dai 

        Têm direito a se aposentar por idade homens que completaram 65 anos 
        e tenham, no mínimo, 20 anos de contribuição, 
        e mulheres que completaram 62 anos e, no mínimo, 15 anos de contribuição.

        aí eu quis arredondar todo mundo para 60
        """
        lista = [ ]

        aposentadoria = 60

        for funcionario in self.funcionarios:
            verif = funcionario.idade
            if verif < 60:
                subtracao = aposentadoria - funcionario.idade
                lista.append(funcionario)
                print(f"\n \n Falta {subtracao} para a sua aposentadoria. {funcionario} ")
            elif verif >= 60:
                lista.append(funcionario)
                print(f"\n \n Não precisa mais trabalhar. Vá para casa descansar guerreiro. {funcionario} ")
        return lista

class Funcionario:

    def __init__(self, nome_funcionario, matricula, idade, sexo, cpf, salario, cadeirante, endereco):
        self.nome = nome_funcionario
        self.matricula = matricula
        self.idade = idade
        self.sexo = sexo
        self.cpf = cpf
        self.salario = salario
        self.cadeirante = cadeirante
        self.endereco = endereco

    def __str__(self):
        return f"""
        Matrícula: {self.matricula} 
        Nome: {self.nome}
        Idade: {self.idade}
        Sexo: {self.sexo}
        CPF: {self.cpf}
        Salário: {self.salario}
        Mora no estado {self.endereco.estado}, na cidade {self.endereco.cidade}, e na rua {self.endereco.rua}
        Cep: {self.endereco.cep}

        """

class Endereco:

    def __init__(self, rua, cidade, estado, cep):
        self.rua = rua
        self.cidade = cidade
        self.estado = estado
        self.cep = cep