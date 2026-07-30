from models.funcionario import Funcionario
from models.setor import Setor
from models.fornecedor import Fornecedor

setor1 = Setor(1, "TA")
funcionario1 = Funcionario(1, "Maria", "Dev", 10.00, setor1)

'''
funcionario1.apresentar()
funcionario1.aumentar_salario(20)
funcionario1.trocar_cargo('Dev Senior')
funcionario1.apresentar()
'''

'''
funcionario1.apresentar()
print()
print(funcionario1.nome)
print(funcionario1.salario)
print()
funcionario1.salario = 7000
funcionario1.cargo = "dev S"
funcionario1.apresentar()
    #restrição por encapsulamento != validação

print()
setor1.nome = "Tech"
setor1.apresentar

#parece que estamos acessando o atributo diretamente
#entretanto o python executa o método definido @nome.setter
#permite que ocorra validações

# setor1.nome = "" #devolve erro
funcionario1.aumentar_salario(-500)
funcionario1.apresentar()

'''
fornecedor1 = Fornecedor(1, "T", 123, 1234, "teste.com")
print(fornecedor1.razao_social)











"""
A distinção entre encapsular e validar é um pilar fundamental da Programação Orientada a Objetos, 
pois o encapsulamento, por si só, apenas restringe os canais de acesso e modificação dos atributos. 
A garantia de que um dado é íntegro e condizente com as regras do negócio permanece sob a responsabilidade do desenvolvedor,
que deve programar os critérios de validação. É exatamente por essa razão que métodos modificadores
como set_nome(), set_salario() e set_cargo() tornam-se indispensáveis: 
eles atuam como pontos centralizados de alteração dentro da classe,
o que viabiliza a implementação e a futura manutenção de regras de validação sem
a necessidade de reescrever ou impactar o restante do sistema.
"""

#COMPOSIÇÃO
#funcionario possui um setor
#produto possui um fornecedor
#produto pertence a um setor
#HERANÇA
#Gerente é um funcionario
#Supervisor é um funcionario
#ADM é um funcionario


