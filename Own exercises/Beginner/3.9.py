class ComputerGame:
    def __init__(self, name: str, publisher: str, year: int):
        self.name = name
        self.publisher = publisher
        self.year = year


class GameWarehouse:
    def __init__(self):
        self.__games = []

    def add_game(self, game:ComputerGame):
        self.__games.append(game)

    def list_games(self):
        return self.__games


class GameMuseum(GameWarehouse):
    def __init__(self):
        super().__init__()

    def list_games(self):
        gamelist = []
        for game in super().list_games():
            if game.year > 1980:
                gamelist.append(game)
                print(game.name)
        return gamelist

    def print(self):
        for game in super().list_games():
            if game.year < 1990:
                print(f"The museum has a collection of games after the year 1990:{game.name, game.publisher}")


museum = GameMuseum()
museum.add_game(ComputerGame("Pacman", "Namco", 1980))
museum.add_game(ComputerGame("GTA 2", "Rockstar", 1999))
museum.add_game(ComputerGame("Bubble Bobble", "Taito", 1986))
museum2 = GameMuseum()
museum2.add_game(ComputerGame("MineCraft", "Mojang", 2011))
museum2.add_game(ComputerGame("Mario", "Nintendo", 1985))


for game in museum.list_games():
    print(game.name)

museum2.print()
