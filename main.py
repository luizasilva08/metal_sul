from models.funcionario import funcionario

from models.funcionario import funcionario

funcionario1 = funcionario("carlos silva", "11111111111", "operador CNC", 4500)
funcionario2 = funcionario("mariana souza", "22222222222", "analista de qualidade", 5200)
funcionario3 = funcionario("joao pereira", "33333333333", "supervisor de producao", 6800)

print(funcionario1.nome, funcionario1.cpf, funcionario1.cargo, funcionario1.salario)
print(funcionario2.nome, funcionario2.cpf, funcionario2.cargo, funcionario2.salario)
print(funcionario3.nome, funcionario3.cpf, funcionario3.cargo, funcionario3.salario)