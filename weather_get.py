from weather_fetch import Fetch

class Get(Fetch):
    def __init__(self, cur_temp, ):
        super().__init__(self.cur_temp, self.cur_symbol, self.next_six_temp, self.next_six_symbol)