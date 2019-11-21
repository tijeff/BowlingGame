class Game():
    __rolls = [0] * 21
    __current_roll = 0

    def roll(self, pins):
        self.__rolls[self.__current_roll] = pins
        self.__current_roll += 1

    def is_spare(self, frame_index):
        return self.__rolls[frame_index] + self.__rolls[frame_index + 1] == 10

    def is_strike(self, roll_index):
        return self.__rolls[roll_index] == 10

    def score(self):
        score = 0
        rool_index = 0
        for _ in range(10):
            if self.is_strike(rool_index):  # strike
                score += 10 + self.__rolls[rool_index+1] + self.__rolls[rool_index+2]
                rool_index += 1
            else:
                frame_score = self.__rolls[rool_index]+self.__rolls[rool_index+1]
                score += frame_score
                if self.is_spare(rool_index):
                    score += self.__rolls[rool_index+2]
                rool_index += 2
        return score
