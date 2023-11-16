class Game:
    def __init__(self, title):
        self.__ininit = True;
        self.setTitle(title);
        self.__ininit = False;

    def setTitle(self, val):
        #print(f"self.__ininit = {self.__ininit}");
        if (self.__ininit):
            if (type(val) == str and len(val) > 0):
                self.__title = val;
    
    def getTitle(self):
        return "" + self.__title;

    title = property(getTitle, setTitle);

    def results(self):
        return [res for res in Result.all if (res.game == self)];

    def players(self):
        return list(set([res.player for res in Result.all if (res.game == self)]));

    def average_score(self, player):
        scores = [res.score for res in player.results()];
        return float(sum(scores))/len(scores);

class Player:
    def __init__(self, username):
        self.setUsername(username);

    def getUsername(self): return self._username;

    def setUsername(self, val):
        if (type(val) == str and len(val) > 1 and len(val) < 16):
            self._username = val;
    
    username = property(getUsername, setUsername);

    def results(self):
        return [res for res in Result.all if (res.player == self)];

    def all_games_played(self):
        return [res.game for res in Result.all if (res.player == self)];

    def games_played(self):
        return list(set(self.all_games_played()));

    def played_game(self, game):
        return (self in game.players());

    def num_times_played(self, game):
        return sum([1 for res in self.all_games_played() if (res == game)]);

class Result:
    all = [];

    def __init__(self, player, game, score):
        self.__ininit = True;
        self.setPlayer(player);
        self.setGame(game);
        self.setScore(score);
        self.__ininit = False;
        Result.all.append(self);
    
    def getScore(self): return self.__score;

    def setScore(self, val):
        if (self.__ininit):
            if ((type(val) == int or type(val) == float) and (val > 1 or val == 1) and
                (val < 5000 or val == 5000)):
                    self.__score = val;

    score = property(getScore, setScore);

    def setPlayer(self, val):
        if (self.__ininit):
            if (type(val) == Player):
                self.__player = val;

    def getPlayer(self): return self.__player;

    player = property(getPlayer, setPlayer);

    def setGame(self, val):
        if (self.__ininit):
            if (type(val) == Game):
                self.__game = val;

    def getGame(self): return self.__game;

    game = property(getGame, setGame);




#mygame = Game("mytitle");
#print(mygame.__ininit);
#attribute error, but can define one, that is different than it so the title never gets changed
#print("attempting to change the title now!");
#mygame.setTitle("nwtitle");
#mygame.title = "nwtitle";
#print(mygame.title);
#assert(mygame.title == "mytitle");
#print("the title did not change!");
