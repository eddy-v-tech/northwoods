class Babysitter:

    ##
    # Initializes a babysitter:
    #   start: The start time of a shift (initialized to 0 to signify no input yet)
    #   finish: The end time of a shift (initialized to signify no input yet)
    #   start_to_bed_pay: The rate which is paid from the start to bedtime
    #   bed_to_mid_pay: The rate which is paid from bedtime to midnight
    #   mid_to_finish_pay: The rate which is paid from midnight to end of shift
    #   bed_time: The time that is used for the charge calculation
    #
    # Notes:
    #   I took the liberty of setting a default bed time of 10pm but left the code able to handle the 
    #   input of varying bed times for future cases.
    #
    #   In case the rates could also some day change I have used the ones given as a default.
    ##

    def __init__(self, first_init_pay = 12, second_init_pay = 8, third_init_pay = 16, init_bed_time = 10):
        self.start = 0
        self.finish = 0
        self.start_to_bed_pay = first_init_pay
        self.bed_to_mid_pay = second_init_pay
        self.mid_to_finish_pay = third_init_pay
        self.bed_time = init_bed_time

    ##
    # Sets the start time for the babysitter:
    #   
    #
    #
    # Notes:
    #   
    #   
    #
    #   
    ##

    def set_start(self, new_start_time):
        return False

    ##
    # Sets the start time for the babysitter:
    #   
    #
    #
    # Notes:
    #   
    #   
    #
    #   
    ##
    def set_finish(self, new_finish_time):
        return False

    ##
    # Sets the start time for the babysitter:
    #   
    #
    #
    # Notes:
    #   
    #   
    #
    #   
    ##
    def set_bed_time(self, new_bed_time):
        return False

    ##
    # Sets the start time for the babysitter:
    #   
    #
    #
    # Notes:
    #   
    #   
    #
    #   
    ##
    def calculate_nightly_charge(self):
        return False