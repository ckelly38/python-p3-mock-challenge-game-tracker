class Game:
    def __init__(self, title):
        self.__ininit = True;
        self.setTitle(title);
        self.__ininit = False;

    def setTitle(self, val):
        #print(f"self.__ininit = {self.__ininit}");
        if (type(val) == str and len(val) > 0):
            if (self.__ininit):
                self._title = val;
            else: raise Exception("title must have at least one character in it!");
        else: raise Exception("title must have at least one character in it!");
    
    def getTitle(self):
        return "" + self._title;

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
        if (type(val) == str and (1 < len(val) and len(val) < 17)):
            self._username = val;
        else: raise Exception("username must have between 2 and 16 characters in it!");
    
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

    @classmethod
    def idxmax(cls, mlist):
        #takes an array and finds the maximum value and then returns a list of all indexes with that value
        mxval = max(mlist);
        return [i for i in range(len(mlist)) if mlist[i] == mxval];

    @classmethod
    def highest_scored(cls, game):
        #get all the results for that game
        #get the scores for corresponding to that game
        #get the index of the max score
        #get the player for that score
        ugps = game.players();
        if (len(ugps) < 1): return None;
        elif (len(ugps) == 1): return ugps[0];
        else:
            gameres = game.results();
            return gameres[cls.idxmax([res.score for res in gameres])[0]].player;

class Result:
    all = [];

    def __init__(self, player, game, score):
        self.__ininit = True;
        self.setPlayer(player);
        self.setGame(game);
        self.setScore(score);
        self.__ininit = False;
        Result.all.append(self);
    
    def getScore(self): return self._score;

    def setScore(self, val):
        if (type(val) == int):
            if (val < 1 or 5000 < val):
                raise Exception("score must be between 1 and 5000 inclusive!");
            elif (self.__ininit):
                self._score = val;
            else: raise Exception("score must be between 1 and 5000 inclusive!");
        else: raise Exception("score must be between 1 and 5000 inclusive!");

    score = property(getScore, setScore);

    def setPlayer(self, val):
        if (type(val) == Player):
            if (self.__ininit):
                self._player = val;
            else: raise Exception("this must be a player, but it was not!");
        else: raise Exception("this must be a player, but it was not!");      

    def getPlayer(self): return self._player;

    player = property(getPlayer, setPlayer);

    def setGame(self, val):
        if (type(val) == Game):
            if (self.__ininit):
                self._game = val;
            else: raise Exception("this must be a game, but it was not!");
        else: raise Exception("this must be a game, but it was not!");  

    def getGame(self): return self._game;

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
