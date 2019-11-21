class Game():
    __score = 0
    __rolls = [0] * 21
    __current_roll = 0

    def roll(self, pins):
        self.__score += pins
        self.__rolls[self.__current_roll] = pins
        self.__current_roll += 1

    def score(self):
        return self.__score
