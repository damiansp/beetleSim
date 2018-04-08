class World:
    def __init__(self, year, month):
        assert month >= 1 and month <= 12, \
            'month must be an integer between 1 and 12'
        self.year = int(year)
        self.month = int(month)

    def __str__(self):
        return ('The world is in year %d, month %d (%s)'
                % (self.year, self.month, self.get_season()))

    def advance_time(self, years, months):
        self.year += years
        self.month += months
        if self.month > 12:
            quotient = self.month / 12
            self.month %= 12
            self.year += quotient

    def get_season(self):
        if self.month < 3 or self.month == 12:
            return 'winter'
        elif self.month < 6:
            return 'spring'
        elif self.month < 9:
            return 'summer'
        return 'fall'
        


# Tests
#world = World(2000, 1)
#print(world)
#world.advance_time(4, 7)
#print(world)
#world.advance_time(2, 11)
#print(world)
#world.advance_time(0, 25)
#print(world)
