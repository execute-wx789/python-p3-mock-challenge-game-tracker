import statistics

class Game:
    def __init__(self, title):
        if isinstance(title, str):
            self.title = title
            

    def results(self):
        return [result for result in Result.all if result.game == self]

    def players(self):
        return list({result.player for result in Result.all if result.game == self})

    def average_score(self, player):
        return statistics.mean([result.score for result in player.results() if result.game is self])
    
    def __setattr__(cls,name,value):
        if hasattr(cls,"title"):
            pass
        else:
            super().__setattr__(name,value)

class Player:
    def __init__(self, username):
        if isinstance(username, str):
            if 2 < len(username) or len(username) < 16:
                self.username = username

    def results(self):
        return [result for result in Result.all if result.player == self]

    def games_played(self):
        return list(set([result.game for result in Result.all if result.player == self]))

    def played_game(self, game, games_played=games_played):
        return game in games_played(self)

    def num_times_played(self, game, results=results):
        return len([games for games in results(self) if games.game == game])

    def __setattr__(cls,name,value):
        if hasattr(cls,"username"):
            if isinstance(value, str):
                if 2 <= len(value) and len(value) <= 16:
                    print(value)
                    super().__setattr__(name,value)
                else:
                    print("To long/short")
            else:
                print("Isn't string")
        else:
            super().__setattr__(name,value)

class Result:
    all = []
    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)

    def __setattr__(cls,name,value):
        if hasattr(cls,"score"):
            pass
        else:
            super().__setattr__(name,value)