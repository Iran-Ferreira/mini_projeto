from model import *

empresa = Empresa("A Melhor", "33930202")

MENU = """
    ------------------------------------------------------------------------
                                 Oxente Sistemas
    ------------------------------------------------------------------------
    1............Cadastrar Novo Funcionário
    2............Excluir Funcionário
    3............Alterar Funcionário
    4............Pesquisar Funcionário(por matrícula)
    5............Pesquisar Funcionário(por CPF)
    6............Listar Funcionários
    7............Listar todos os Funcionários(Da cidade pesquisada)
    8............Listar todos os Funcionários(Do estado pesquisado)
    9............Listar todos os Funcionários(Que ganham mais ou igual ao salário pesquisado)
    10...........Listar todos os Funcionários(Que ganham menos ou igual ao salário pesquisado)
    11...........Listar todos os Funcionários(Do sexo pesquisado)
    12...........Listar todos os Funcionários(Do sexo pesquisado e ganham mais ou igual ao salário pesquisado)
    13...........Listar todos os Funcionários(Do estado pesquisado e ganham entre os salários pesquisado)
    14...........Listar todos os Funcionários(Que começam com a letra pesquisada)
    15...........Mostrar o Funcionário que ganha o maior salário
    16...........Mostrar a Funcionário que ganha o menor salario
    17...........Mostrar o Funcionário mais velho
    18...........Mostrar o Funcionário mais novo
    19...........Listar todos os Funcionários cadeirantes
    20...........Listar todos os Funcionários que irá se aposentar nos próximos anos
    0............Sair
    """

opcao = " "

while True:
    print(MENU)
    opcao = input("\n Digita a sua opção: ")

    if opcao == "1":

        nome_funcionario = input("Digite o seu nome: ")
        matricula = (input("Digite a sua matricula: "))
        idade = int(input("Digite a sua idade: "))
        sexo = input("Digite o seu sexo: Masculino ou Feminino: ")
        cpf = input("Digite o seu CPF: ")
        salario = float(input("Digite o seu salário: "))
        cadeirante = input("Você é cadeirante: Sim ou Não: ")

        rua = input("Digite o nome da sua rua: ")
        cidade = input("Digite o nome da sua cidade: ")
        estado = input("Digite o nome do seu estado: ")
        cep = input("Digite o seu cep: ")

        endereco = Endereco(rua, cidade, estado, cep)

        funcionario = Funcionario(nome_funcionario, matricula, idade, sexo, cpf, salario, cadeirante, endereco)
        empresa.cadastrar_funcionario(funcionario)
        print("\n Funcionário cadastrado com sucesso.")

    elif opcao == "2":
        matricula = input("\n Digite a matrícula para excluir funcionário: ")

        verif = empresa.excluir_funcionario(matricula)
        if verif == True:
            print("\n Excluído com sucesso.")
        else:
            print("\n Matrícula não encontrada.")

    elif opcao == "3":
        matricula = input("\n Informe a matrícula do funcionário à ter os dados editados: ")

        funcionario = empresa.get_funcionario_por_matricula(matricula)
        print(funcionario)

        escolha = input(""" O que você quer editar: Você tem essas opções:
        
        Nome: 
        Matrícula:
        Idade:
        Sexo:
        CPF: 
        Salário:
        Rua:
        Cidade:
        Estado:
        Cep:

        """)

        if escolha.upper() == "NOME":
            novo_nome = input("Edite seu nome: ")
            empresa.set_funcionario(matricula, novo_nome)
            print("Nome editado com sucesso. ")

        elif escolha.upper() == "MATRÍCULA":
            nova_matricula = input("Edite a sua matrícula: ")
            empresa.set_funcionario(matricula, None, nova_matricula)
            print("Matrícula editada com sucesso. ")
        
        elif escolha.upper() == "IDADE":
            nova_idade = input("Edite a sua idade: ")
            empresa.set_funcionario(matricula, None, None, nova_idade)
            print("Idade editada com sucesso. ")
        
        elif escolha.upper() == "SEXO":
            novo_sexo = input("Edite o seu sexo: ")
            empresa.set_funcionario(matricula, None, None, None, novo_sexo)
            print("Sexo editado com sucesso. ")
        
        elif escolha.upper() == "CPF": 
            novo_cpf = input("Edite seu CPF: ")
            empresa.set_funcionario(matricula, None, None, None, None, novo_cpf)
            print("CPF editado com sucesso. ")
        
        elif escolha.upper() == "SALÁRIO":
            novo_salario = input("Edite o salário: ")
            empresa.set_funcionario(matricula, None, None, None, None, None, novo_salario)
            print("Salário editado com sucesso. ")
        
        elif escolha.upper() == "RUA":
            nova_rua = input("Edite o nome da rua: ")
            empresa.set_funcionario(matricula, None, None, None, None, None, None, nova_rua)
            print("Rua editado com sucesso. ")
        
        elif escolha.upper() == "CIDADE":
            nova_cidade = input("Edite o nome da sua cidade: ")
            empresa.set_funcionario(matricula, None, None, None, None, None, None, None, 
            nova_cidade)
            print("Cidade editado com sucesso. ")
        
        elif escolha.upper() == "ESTADO":
            novo_estado = input("Edite o nome do estado: ")
            empresa.set_funcionario(matricula, None, None, None, None, None, None, None, None, 
            novo_estado)
            print("Estado editado com sucesso. ")
        
        elif escolha.upper() == "CEP":
            novo_cep = input("Edite o seu cep: ")
            empresa.set_funcionario(matricula, None, None, None, None, None, None, None, None, 
            None, novo_cep)
            print("Cep editado com sucesso. ")

    elif opcao == "4":
        matricula = input("\n Informe a matrícula para pesquisar: ")

        funcionario = empresa.get_funcionario_por_matricula(matricula)
        print(funcionario)

    elif opcao == "5":
        cpf = input("\n Informe o CPF para pesquisar: ")

        funcionario = empresa.get_funcionario_por_cpf(cpf)
        print(funcionario)

    elif opcao == "6":
        funcionarios = empresa.get_funcionarios()
        for funcionario in funcionarios:
            print(funcionario)

    elif opcao == "7":
        cidade = input("\n Informe a cidade para pesquisar: ")

        funcionarios = empresa.get_funcionarios_por_cidade(cidade)
        for funcionario in funcionarios:
            print(funcionario)
    
    elif opcao == "8":
        estado = input("\n Informe o estado para pesquisar: ")

        funcionarios = empresa.get_funcionarios_por_estado(estado)
        for funcionario in funcionarios:
            print(funcionario)

    elif opcao == "9":
        salario = float(input("\n Informe um salário para pesquisar: "))

        funcionarios = empresa.get_funcionarios_por_salario_maior_ou_igual(salario)
        for funcionario in funcionarios:
            print(funcionario)
    
    elif opcao == "10":
        salario = float(input("\n Informe um salário para pesquisar: "))
        
        funcionarios = empresa.get_funcionarios_por_salario_menor_ou_igual(salario)
        for funcionario in funcionarios:
            print(funcionario)
    
    elif opcao == "11":

        sexo = input("\n Informe seu sexo para pesquisar: ")
        
        funcionarios = empresa.get_funcionarios_por_sexo(sexo)
        for funcionario in funcionarios:
            print(funcionario)

    elif opcao == "12":
        sexo = input("\n Informe seu sexo para pesquisar: ")
        salario = float(input("\n Informe o salário para pesquisar: "))
        
        funcionarios = empresa.get_funcionarios_por_sexo_e_ganham_mais_x(sexo, salario)
        for funcionario in funcionarios:
            print(funcionario)

    elif opcao == "13":
        estado = input("\n Informe seu estado para pesquisar: ")
        salario1 = float(input("\n Informe o primeiro salário para pesquisar: "))
        salario2 = float(input("\n Informe o segundo salário para pesquisar: "))

        funcionarios = empresa.get_funcionarios_por_estado_e_ganham_entre_x_e_y(estado, salario1, salario2)
        for funcionario in funcionarios:
            print(funcionario)
    
    elif opcao == "14":
        letra = input("\n Digite uma letra para pesquisar: ")

        funcionarios = empresa.get_funcionarios_por_letra(letra)
        for funcionario in funcionarios:
            print(funcionario)
    
    elif opcao == "15":
        sexo = input("\n Informe o seu sexo para pesquisar: ")
        
        funcionarios = empresa.get_funcionario_por_maior_salario(sexo)
    
    elif opcao == "16":
        sexo = input("\n Informe o seu sexo para pesquisar: ")
        
        funcionarios = empresa.get_funcionario_por_menor_salario(sexo)
    
    elif opcao == "17":
        sexo = input("\n informe o seu sexo para pesquisar: ")

        funcionarios = empresa.get_funcionario_por_maior_idade(sexo)

    elif opcao == "18":
        sexo = input("\n Informe o seu sexo para pesquisar: ")
        
        funcionarios = empresa.get_funcionario_por_menor_idade(sexo)

    elif opcao == "19":
        cadeirante = input("\n Você é cadeirante: Sim ou Não ")
        
        funcionarios = empresa.get_funcionarios_cadeirante(cadeirante)
        for funcionario in funcionarios:
            print(funcionario)
    
    elif opcao == "20":
        
        funcionarios = empresa.get_aposentadoria()
    
    elif opcao == "0":
        print("\n Saindo do sistema...")
        break
    
    else:
        print("\n Digite uma opção valida!")
        continue
