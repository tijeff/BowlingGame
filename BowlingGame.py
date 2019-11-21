class Game():
    __rolls = [0] * 21
    __current_roll = 0

    def roll(self, pins):
        self.__rolls[self.__current_roll] = pins
        self.__current_roll += 1

    def score(self):
        score = 0
        for i in range(len(self.__rolls)):
            if self.__rolls[i] + self.__rolls[i + 1] == 10: # --> spare
                score += ???
            score += self.__rolls[i]
        return score
