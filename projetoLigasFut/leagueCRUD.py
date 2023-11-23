class League:
    def __init__(self, db):
        self.db = db

    def create(self, clubs_list, name):
        query_c = "CREATE (l:League{name: $name})"  # create part of query
        query_m = "MATCH "  # league part of query
        i = 0
        parameters = {"name": name}
        for team_name in clubs_list:
            if i != 0:
                query_m += ", "
            query_m += "(t" + str(i) + ":Team{name: $team_name" + str(i) + "})"
            query_c += ", (t" + str(i) + ")-[:PARTICIPATE]->(l)"
            param_aux = "team_name" + str(i)
            parameters.update({param_aux: team_name})
            i += 1

        query_m += "\n"
        query = query_m + query_c
        self.db.execute_query(query, parameters)

    def delete(self, league_name):
        query = "MATCH (l:League {name: $league_name})" "DETACH DELETE l"
        parameters = {"league_name": league_name}
        self.db.execute_query(query, parameters)

    def read(self, league_name):
        query = "MATCH (l:League{name: $league_name}), (t:Team)-[:PARTICIPATE]->(l:League) RETURN t.name"
        parameters = {"league_name": league_name}
        name = self.db.execute_query(query, parameters)
        return [node["t.name"] for node in name]

    def update(self, name, new_name):
        query = "MATCH (l:League {name: $name})" "SET l.name = $new_name"
        parameters = {"name": name, "new_name": new_name}
        self.db.execute_query(query, parameters)
