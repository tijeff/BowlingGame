class Game():
    __rolls = [0] * 21
    __current_roll = 0

    def roll(self, pins):
        self.__rolls[self.__current_roll] = pins
        self.__current_roll += 1

    def score(self):
        score = 0
        rool_index = 0
        for _ in range(10):
            score += self.__rolls[rool_index]+self.__rolls[rool_index+1]
            rool_index += 2
        return score
