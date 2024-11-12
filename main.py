class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.__salario = salario

    def obter_salario(self):
        """Método para obter o salário do funcionário."""
        return self.__salario

    def aumentar_salario(self, percentual):
        """Método para aumentar o salário com base em um percentual."""
        if percentual > 0:
            self.__salario += self.__salario * (percentual / 100)
        else:
            print("O percentual de aumento deve ser positivo.")

class Gerente(Funcionario):
    def __init__(self, nome, cargo, salario, bonus):
        super().__init__(nome, cargo, salario)
        self.bonus = bonus

    def obter_salario(self):
        """Retorna o salário total do gerente, incluindo o bônus."""
        return super().obter_salario() + self.bonus



#funcionário
funcionario = Funcionario("Ailton", "Analista", 1200)
print(f"Salário inicial do Funcionário: R${funcionario.obter_salario():.2f}")
funcionario.aumentar_salario(20)
print(f"Salário após aumento do Funcionário: R${funcionario.obter_salario():.2f}")

#gerente
gerente = Gerente("Ana", "Gerente de Projetos", 4500, 1500)
print(f"\nSalário inicial do Gerente (com bônus): R${gerente.obter_salario():.2f}")
gerente.aumentar_salario(30)
print(f"Salário após aumento do Gerente (com bônus): R${gerente.obter_salario():.2f}")
