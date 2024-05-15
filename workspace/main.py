# Folha de pagamento em python
funcionarios = {}
def adicionarFuncionario(): # Ester
    count = 0
    n = int(input("Quantos funcionários deseja adicionar? "))
    while count < n:
        pessoa = []
        matricula = input("Digite a matrícula do funcionário: ")
        nome =  input("Nome do funcioário: ")
        cod_funcao = int(input("Digite o código da função do funcionário: "))
        num_faltas = int(input("Quantidade de faltas no mês: "))
        salarioBruto = float(input("Salário Bruto do funcionário: "))
        pessoa.append(nome)
        pessoa.append(cod_funcao)
        pessoa.append(num_faltas)
        pessoa.append(salarioBruto)
        print(pessoa)
        funcionarios[matricula] = pessoa
        count+=1
    return funcionarios

def removerFuncionario(): # Geovana
    print("")
    
def relatorioFuncionario(relatorio_func): #de um unico funcionario - Ester
   #Matrícula, Nome, Código da Função, Salário Bruto e Salário Líquido de cada funcionário
    print()

def relatorioDosFuncionarios(): #de todos os funcionarios - Natã
    print("")
    
def maiorSalario(): #Infos funcionario com maior salario - Geovana
    print("")
    
def maisFaltas(): #Infos funcionario com mais faltas - Natã
    print("")

print("O que deseja fazer?\n","")
opcao = int(input("1-Adicionar funcionario\n2-Remover funcionario\n3-Ver relatorio do funcionario\n4-Ver relatorios dos funcionarios\n5-Ver o maior salario\n6-Ver funcionario com mais faltas\n"))

if(opcao == 1):
   adicionarFuncionario()
elif(opcao == 2):
   removerFuncionario()
elif(opcao == 3):
   relatorioFuncionario()
elif(opcao == 4):
   relatorioDosFuncionarios()
elif(opcao == 5):
   maiorSalario()
elif(opcao == 6):
   maisFaltas()
else:
   print("Essa opcao não existe")

# Duvidas
# A matricula deve ser int ou string?