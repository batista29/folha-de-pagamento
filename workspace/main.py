# Folha de pagamento em python
funcionarios = {}
def lerDados():
    matricula = input("Digite a matrícula do funcionário: ")
    nome =  input("Nome do funcioário: ")
    cod_funcao = int(input("Digite o código da função do funcionário: "))
    num_faltas = int(input("Quantidade de faltas no mês: "))
    salarioBruto = float(input("Salário Bruto do funcionário: "))
    return matricula,nome,cod_funcao,num_faltas,salarioBruto
def adicionarFuncionario(matricula,nome,cod_funcao,num_faltas,salarioBruto): # Ester
    pessoa = []
    pessoa.append(nome)
    pessoa.append(cod_funcao)
    pessoa.append(num_faltas)
    pessoa.append(salarioBruto)
    print(pessoa)
    funcionarios[matricula] = pessoa
    #return funcionarios

def removerFuncionario(): # Geovana
    print("")
    
def relatorioFuncionario(funcionarios,matricula): #de um unico funcionario - Ester
   #Matrícula, Nome, Código da Função, Salário Bruto e Salário Líquido de cada funcionário
    salario_liquido = 0
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

def relatorioDosFuncionarios(): #de todos os funcionarios - Natã
    print("")
    
def maiorSalario(): #Infos funcionario com maior salario - Geovana
    print("")
    
def maisFaltas(): #Infos funcionario com mais faltas - Natã
    print("")

print("O que deseja fazer?\n","")
opcao = int(input("1-Adicionar funcionario\n2-Remover funcionario\n3-Ver relatorio do funcionario\n4-Ver relatorios dos funcionarios\n5-Ver o maior salario\n6-Ver funcionario com mais faltas\n"))
while opcao !=0:
    
    if(opcao == 1):
        matricula,nome,cod_funcao,num_faltas,salarioBruto = lerDados()
        adicionarFuncionario(matricula,nome,cod_funcao,num_faltas,salarioBruto)
    elif(opcao == 2):
        removerFuncionario(funcionarios,matricula)
    elif(opcao == 3):
        matricula = input("Por Favor digite nº da matricula do funcionário que deseja ver relatório: ")
        relatorioFuncionario(funcionarios,matricula)

    elif(opcao == 4):
        funcionarios = adicionarFuncionario()
        relatorioDosFuncionarios()
    elif(opcao == 5):
        maiorSalario()
    elif(opcao == 6):
        maisFaltas()
    else:
        print("Essa opcao não existe!")
    print("O que deseja fazer?\n","")
    opcao = int(input("1-Adicionar funcionario\n2-Remover funcionario\n3-Ver relatorio do funcionario\n4-Ver relatorios dos funcionarios\n5-Ver o maior salario\n6-Ver funcionario com mais faltas\n"))
# Duvidas
# A matricula deve ser int ou string?
#posso armazenar mais dados ou precisa ser somente os dados listados?
# como funciona o salário bruto?