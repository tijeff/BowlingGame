class Game():
    __rolls = [0] * 21
    __current_roll = 0

    def roll(self, pins):
        self.__rolls[self.__current_roll] = pins
        self.__current_roll += 1

    def score(self):
        score = 0
        for roll in self.__rolls:
            score += roll
        return score
