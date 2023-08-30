class Professor:
    def __init__(self, nome):
        self.nome = nome

    def ministrarAula(self, assunto):
        print("O professor " + self.nome + " está ministrando uma aula sobre o assunto " + assunto)

class Aluno:
    def __init__(self, nome):
        self.nome = nome
    def presenca(self):
        print("\n O(A) aluno(a) " + self.nome + " está presente.")

class Aula:
    def __init__(self, professor, assunto, alunos):
        self.professor = professor
        self.assunto = assunto
        self.alunos = alunos

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def listar_presenca(self):
        print("Presença na aula sobre o assunto " + self.assunto + " ministrada pelo professor " + self.professor.nome + ":")
        for aluno in self.alunos:
            aluno.presenca()

class Main:
    professor = Professor("Lucas")
    aluno1 = Aluno("Maria")
    aluno2 = Aluno("Pedro")

    aula = Aula(professor, "Programação Orientada a Objetos", [])
    aula.adicionar_aluno(aluno1)
    aula.adicionar_aluno(aluno2)
    print(aula.listar_presenca())
