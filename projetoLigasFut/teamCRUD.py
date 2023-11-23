class Team:
    def __init__(self, database):
        self.db = database

    def create(self, name, ano_fund, n_torcedores):  # cria um Time
        query = "CREATE (n:Team {name: $name,  ano_fund: $ano_fund, n_torcedores: $n_torcedores})"
        parameters = {"name": name, "ano_fund": ano_fund, "n_torcedores": n_torcedores}
        self.db.execute_query(query, parameters)

    def read(self, name):  # retorna apenas um Time
        query = "MATCH (t:Team {name: $name}) RETURN t.name,t.ano_fund,t.n_torcedores"
        parameters = {"name": name}
        result = self.db.execute_query(query, parameters)
        return [node for node in result]

    def delete(self, name):  # deleta um Time com base no name
        query = "MATCH (t:Team {name: $name}) DELETE t"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def update(
        self, name, newn_torcedores
    ):  # atualiza a quantidade de torcedores de um time com base no name
        query = "MATCH (t:Team {name: $name}) SET t.n_torcedores = $newn_torcedores"
        parameters = {"name": name, "newn_torcedores": newn_torcedores}
        self.db.execute_query(query, parameters)
