class Babysitter:

    def __init__(self, first_initial_pay = 12, second_initial_pay = 8, third_initial_pay = 16):
        self.start = 0
        self.finish = 0
        self.start_to_bed_pay = first_initial_pay
        self.bed_to_mid_pay = second_initial_pay
        self.mid_to_finish_pay = third_initial_pay
        self.bed_time = 10

    ## probably shouldn't be after midnight?
    ## will make the assumption that bedtime will be at hour intervals
    def set_bed_time(self, new_bed_time):
        pass

    ## if babysitter shows up late then get the ceiling 
    def set_start(self, new_start_time):
        pass

    ## if the babysitter leaves early get the floor
    def set_finish(self, new_finish_time):
        pass

    ## 5 6 7 8 9 10 11 12 1 2 3 4
    def calculate_nightly_charge(self):
        pass