# Folha de pagamento em python
funcionarios = {}

def lerDados():
    matricula = int(input("Digite a matrícula do funcionário: "))
    nome =  input("Nome do funcioário: ")
    cod_funcao = int(input("Digite o código da função do funcionário: "))
    num_faltas = int(input("Quantidade de faltas no mês: "))
    if cod_funcao == 101:
        sal_fixo = 1500
        valor_venda = int(input("Digite o valor de vendas no mês:"))
        comissao = valor_venda*0.09 
        desc_faltas = (sal_fixo/30)*num_faltas
        salarioBruto = (sal_fixo+comissao)- desc_faltas
    elif cod_funcao == 102:
        sal_fixo = float(input("Salário do funcionário (R$ 2150 - 6950): "))
        while sal_fixo < 2150 or sal_fixo > 6950:
            print("Faixa salarial é de R$2150 a R$6950")
            sal_fixo = float(input("Salário do funcionário (R$ 2150 - 6950): "))
        salarioBruto = sal_fixo
        
    return matricula,nome,cod_funcao,num_faltas,salarioBruto

def adicionarFuncionario(matricula,nome,cod_funcao,num_faltas,salarioBruto): # Ester
    pessoa = []
    pessoa.append(nome)
    pessoa.append(cod_funcao)
    pessoa.append(num_faltas)
    pessoa.append(salarioBruto)
    
    funcionarios[matricula] = pessoa
    #return funcionarios

def removerFuncionario(funcionarios): #Geovana
    excluir = input("Digite a matricula do funcionario que deseja remover: ")
    if excluir in funcionarios:
        del funcionarios[excluir]
        print(f"Funcionário com matrícula {excluir} removido com sucesso.")
    else:
        print(f"Funcionário com matrícula {excluir} não encontrado.")

def relatorioFuncionario(funcionarios,matricula): #de um unico funcionario - Ester
   #Matrícula, Nome, Código da Função, Salário Bruto e Salário Líquido de cada funcionário
    salario_liquido = 0

    print(funcionarios)
    print("\nRelatório do Funcionário\n")
    print("Nº matrícula: "+matricula)
    print("Nome: "+ funcionarios[matricula][0])
    if funcionarios[matricula][1] == 101:
        funcao = "Vendedor"
    elif funcionarios[matricula][1] == 102:
        funcao = "Administrativo"
    print(f"Código da Função: {funcionarios[matricula][1]} - {funcao}")
    print(f"Quantidade de faltas no mês: {funcionarios[matricula][2]}")
    print(f"Salário Bruto: {funcionarios[matricula][3]}")
    print(f"Salário Líquido:  {salario_liquido}")

def relatorioDosFuncionarios(funcionarios): #de todos os funcionarios - Natã

    for matricula in (funcionarios.keys()):
        #verificar se a formula esta correta
        salario_descontado = funcionarios[matricula][3]-(((funcionarios[matricula][3])/30)*funcionarios[matricula][2])

        if (funcionarios[matricula][3] <= 2259.2):
            salario_liquido = salario_descontado
        elif(2259.21 <= funcionarios[matricula][3] <= 2828.65):
            salario_liquido = salario_descontado-(salario_descontado*0.075)
        elif(2828.66 <= funcionarios[matricula][3] <= 3751.05):
            salario_liquido = salario_descontado-(salario_descontado*0.15)
        elif(3751.06 <= funcionarios[matricula][3] <= 4664.68):
            salario_liquido = salario_descontado-(salario_descontado*0.225)
        else:
            salario_liquido = salario_descontado-(salario_descontado*0.275)

        print("\nMatricula: ", matricula,",Nome: ", funcionarios[matricula][0], ",Código da função: ", funcionarios[matricula][1], ",Faltas: ", funcionarios[matricula][2], ",Salário bruto: ", funcionarios[matricula][3],",Salário liquido: ",salario_liquido,"\n")

def maiorSalario(funcionarios): #Infos funcionario com maior salario - Geovana
    maior_salario = 0

    for matricula in (funcionarios.keys()):
        if (funcionarios[matricula][3] > maior_salario):
            maior_salario = funcionarios[matricula][3]
            matriculafuncionario = matricula

    print(f"Matricula: {matriculafuncionario}, {funcionarios[matriculafuncionario][0]}, Código da função: {funcionarios[matriculafuncionario][1]}, Faltas: {funcionarios[matriculafuncionario][2]}, Salário bruto: {funcionarios[matriculafuncionario][3]} ")
            
    
def maisFaltas(funcionarios): #Infos funcionario com mais faltas - Natã
    mais_faltas = 0

    for matricula in (funcionarios.keys()):
        if(mais_faltas < funcionarios[matricula][2]):
            mais_faltas = funcionarios[matricula][2]
            matricula_func = matricula

    print("Matricula: ", matricula_func,"\nNome: ", funcionarios[matricula_func][0], ", Código da função: ", funcionarios[matricula_func][1], ", Faltas: ", funcionarios[matricula_func][2], ", Salário bruto: ", funcionarios[matricula_func][3],"\n")

print("O que deseja fazer?\n","")
opcao = int(input("1-Adicionar funcionario\n2-Remover funcionario\n3-Ver relatorio do funcionario\n4-Ver relatorios dos funcionarios\n5-Ver o maior salario\n6-Ver funcionario com mais faltas\n"))

while opcao !=0:
    if(opcao == 1):
        matricula,nome,cod_funcao,num_faltas,salarioBruto = lerDados()
        adicionarFuncionario(matricula,nome,cod_funcao,num_faltas,salarioBruto)
    elif(opcao == 2):
        removerFuncionario(funcionarios)
    elif(opcao == 3):
        matricula = input("Por Favor digite nº da matricula do funcionário que deseja ver relatório: ")
        relatorioFuncionario(funcionarios,matricula)
    elif(opcao == 4):
        relatorioDosFuncionarios(funcionarios)
    elif(opcao == 5):
        maiorSalario(funcionarios)
    elif(opcao == 6):
        maisFaltas(funcionarios)
    else:
        print("Essa opcao não existe!")
        
    opcao = int(input("O que deseja fazer?\n\n1-Adicionar funcionario\n2-Remover funcionario\n3-Ver relatorio do funcionario\n4-Ver relatorios dos funcionarios\n5-Ver o maior salario\n6-Ver funcionario com mais faltas\n"))

# Duvidas
# A matricula deve ser int ou string?
# como calcular a comissão de venda dos vendedores?   
#posso armazenar mais dados ou precisa ser somente os dados listados?
# como funciona o salário bruto?
