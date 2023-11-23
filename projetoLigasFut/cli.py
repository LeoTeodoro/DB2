class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Entre com um comando: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Comando invalido, tente novamente.")


class TeamCLI(SimpleCLI):
    def __init__(self, crud):
        super().__init__()
        self.crud = crud
        self.add_command("create", self.create_team)
        self.add_command("read", self.read_team)
        self.add_command("update", self.update_team)
        self.add_command("delete", self.delete_team)

    def create_team(self):
        print("Criando time")
        name = input("Nome do time: ")
        ano_fund = input("Ano de fundacao do time: ")
        n_torcedores = input("numero de torcedores do time: ")
        try:
            self.crud.create(name, int(ano_fund), n_torcedores)
            print(f"time {name} criado!")
        except Exception as e:
            print(f"Erro ao criar time! {e}")

    def read_team(self):
        print("Lendo time")
        name = input("Nome do time: ")
        try:
            result = self.crud.read(name)
            for i in result:
                print("Nome: ", i["t.name"])
                print("Ano de fundacao: ", i["t.ano_fund"])
                print("n_torcedores: ", i["t.n_torcedores"])
        except Exception as e:
            print(f"Erro ao ler time! {e}")

    def update_team(self):
        print("Atualizando time")
        name = input("Nome do time: ")
        newn_torcedores = input("Novo número de torcedores do time: ")
        try:
            self.crud.update(name, newn_torcedores)
            print("Atualizado!")
        except Exception as e:
            print(f"Erro ao atualizar time! {e}")

    def delete_team(self):
        print("Deletando time")
        name = input("Nome do time: ")
        try:
            self.crud.delete(name)
            print("Deletado!")
        except Exception as e:
            print(f"Erro ao deletar time! {e}")
