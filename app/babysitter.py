import string_constants

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

    def __init__(self, first_init_pay = 12, second_init_pay = 8, third_init_pay = 16, init_bed_time = 22):
        self.start = None
        self.finish = None
        self.start_to_bed_pay = first_init_pay
        self.bed_to_mid_pay = second_init_pay
        self.mid_to_finish_pay = third_init_pay
        self.bed_time = init_bed_time
    
    ##
    # Converts the inputs that the program takes to be used later by the set methods
    #
    # Notes:
    #   I know the objective is to show TDD and this time conversion might be overkill for the project
    #   but there were a few unknowns in the product description that I just wanted to account for. 
    #
    #   In the real world I would just ask more questions to make sure I am creating the right program for
    #   the end user, but for now I'm just having fun being a little meticulous on the input.
    ##

    def convert_time(self, timeString):
        
        returnInfo = {
            'hour' : None,
            'minutes' : None,
            'ending' : None,
            'error' : None,
        }

        if len(timeString.replace(" ", "")) == 0:
            returnInfo['error'] = string_constants.EMPTY_INPUT_ERROR
            return returnInfo 
        
        ending = timeString.replace(" ", "")[-2:].upper()
        
        if 'PM' not in timeString and 'AM' not in timeString:
            returnInfo['error'] = string_constants.MISSING_ENDING_ERROR
            return returnInfo

        if ending != 'PM' and ending != 'AM':
            returnInfo['error'] = string_constants.MISSING_ENDING_ERROR
            return returnInfo

        if ':' in timeString:

            hour = timeString.split(':')[0].replace(" ", "")
            if len(hour) > 2 or len(hour) < 1 or not hour.isnumeric() or int(hour) > 12:
                returnInfo['error'] = string_constants.INVALID_TIME_FORMAT_ERROR
                return returnInfo
            else:
                hour = int(hour)
                if ending == 'PM':
                    hour += 12
                

            minutes = timeString.split(':')[1][:-2].replace(" ", "")
            if len(minutes) != 2 or not minutes.isnumeric() or int(minutes) >= 60:
                returnInfo['error'] = string_constants.INVALID_TIME_FORMAT_ERROR
                return returnInfo
            else:
                minutes = int(minutes)

            returnInfo['hour'] = hour
            returnInfo['minutes'] = minutes
            returnInfo['ending'] = ending
        
        else:
            hour = timeString[:-2]
            if len(hour) > 2 or len(hour) < 1 or not hour.isnumeric() or int(hour) > 12:
                returnInfo['error'] = string_constants.INVALID_TIME_FORMAT_ERROR
                return returnInfo
            else:
                hour = int(hour)
                if ending == 'PM':
                    hour += 12

            returnInfo['hour'] = hour
            returnInfo['ending'] = ending
        
        return returnInfo



    ##
    # Sets the start time for the babysitter:
    #
    #   The babysitter can arrive at any time, but will not start being paid until 5:00 PM.
    #
    #   While abnormal the baby sitter will be allowed to start at any time before 4:00 AM since
    #   constraints were not given but will assume a babysitty cannot come before 6:00 AM
    #   
    #   The method will accept a string to parse in the format of 1:00 AM or 1 AM anything else should
    #   raise an error and let the user know that they need to use the correct format.
    #
    #   The string will be converted to a 24 hour format time int so 1 AM would be 1 and 5 PM would be 17.
    #
    # Notes:
    #
    #   It might be a little counterintuitive to have the conversion set this way, but that is how it goes
    #   in the real world with 24 hour format so I will leave it this way
    #
    #   The time should probably be it's own object since I have properties coming through and could be
    #   confusing for a future programmer as to what is and is not coming through from the convert_time
    #   dictionary I am returning.
    #   
    ##

    def set_start(self, new_start_time):
        time = self.convert_time(new_start_time)
        if time['error'] != None:
            return time['error']
        
        else:
            if (6 >= time['hour'] >= 4):
                return string_constants.INVALID_START_TIME_ERROR

            elif time['minutes'] != None and time['minutes'] > 0:
                self.start = time['hour'] + 1
                print(string_constants.MINUTES_AFTER_WARNING)
                
            elif time['hour'] < 17:
                self.start = 17

            else:
                self.start = time['hour']
            
        return string_constants.SUCCESS_STRING

    ##
    # Sets the finish time for the babysitter:
    #   The babysitter stops getting paid at 4AM and must leave by then.
    #
    #   Have to check and make sure a time before the start is not entered.
    #
    #   The conversion of time has to be checked as 5PM (17:00) is earlier than 3AM (3:00)
    #
    # Notes:
    #   I left some of the constraints open to be changed later such as how strict that 5AM 
    #   must-leave-by time as I can see how some assumptions I've made could be misinterpretations
    #   of the requirements
    #
    ##
    def set_finish(self, new_finish_time):
        time = self.convert_time(new_finish_time)
        if time['error'] != None:
            return time['error']
        
        else:
            if (16 >= time['hour'] >= 5):
                return string_constants.FINISH_TIME_AFTER_FIVE_AM_ERROR

            elif time['minutes'] != None and time['minutes'] > 0:
                temp_finish = time['hour'] - 1
                if temp_finish >= 17 and self.start >= 16 and self.start > temp_finish:
                    return string_constants.FINISH_TIME_BEFORE_START_ERROR
                elif temp_finish <= 4 and self.start <= 4 and temp_finish < self.start:
                    return string_constants.FINISH_TIME_BEFORE_START_ERROR

                else:
                    self.finish = temp_finish
                print(string_constants.MINUTES_AFTER_WARNING)
            
            else:
                if time['hour'] >= 17 and self.start >= 16 and self.start > time['hour']:
                    return string_constants.FINISH_TIME_BEFORE_START_ERROR
                elif time['hour'] <= 4 and self.start <= 4 and time['hour'] < self.start:
                    return string_constants.FINISH_TIME_BEFORE_START_ERROR
                else:
                    self.finish = time['hour']
                
            
        return string_constants.SUCCESS_STRING

    ##
    # Sets the bed time for the babysitter/kids:
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
        time = self.convert_time(new_bed_time)
        if time['error'] != None:
            return time['error']

    ##
    # Calculates the amount to charge for the babysitting:
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