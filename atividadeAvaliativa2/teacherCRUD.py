class TeacherCRUD:
    def __init__(self, database):
        self.db = database

    def create(self, name, ano_nasc, cpf):  # cria um Teacher
        query = "CREATE (n:Teacher {name: $name,  ano_nasc: $ano_nasc, cpf: $cpf})"
        parameters = {"name": name, "ano_nasc": ano_nasc, "cpf": cpf}
        self.db.execute_query(query, parameters)

    def read(self, name):  # retorna apenas um Teacher
        query = "MATCH (t:Teacher {name: $name}) RETURN t.name,t.ano_nasc,t.cpf"
        parameters = {"name": name}
        result = self.db.execute_query(query, parameters)
        return [node for node in result]

    def delete(self, name):  # deleta Teacher com base no name
        query = "MATCH (t:Teacher {name: $name}) DELETE t"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def update(self, name, newCpf):  # atualiza cpf com base no name
        query = "MATCH (t:Teacher {name: $name}) SET t.cpf = $newCpf"
        parameters = {"name": name, "newCpf": newCpf}
        self.db.execute_query(query, parameters)
