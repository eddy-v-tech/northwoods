from babysitter import Babysitter
import string_constants

def test_babysitter_init():
    testSitter = Babysitter()

    # Testing initialized values

    assert testSitter.start == None
    assert testSitter.finish == None
    assert testSitter.start_to_bed_pay == 12
    assert testSitter.bed_to_mid_pay == 8
    assert testSitter.mid_to_finish_pay == 16
    assert testSitter.bed_time == 22

def test_invalid_time_input():
    testSitter = Babysitter()

    # Empty inputs are not allowed for start times
    assert testSitter.set_start('') == string_constants.EMPTY_INPUT_ERROR

    # Test that AM or PM is used for time
    assert testSitter.set_start('5:00') == string_constants.MISSING_ENDING_ERROR

    # Non time inputs are not allowed for start times
    assert testSitter.set_start('67PM') == string_constants.INVALID_TIME_FORMAT_ERROR

    # Empty inputs are not allowed for finish times
    assert testSitter.set_finish('') == string_constants.EMPTY_INPUT_ERROR

    # Test that AM or PM is used finish time
    assert testSitter.set_finish('5:00') == string_constants.MISSING_ENDING_ERROR

    # Non time inputs are not allowed for finish times
    assert testSitter.set_finish('67PM') == string_constants.INVALID_TIME_FORMAT_ERROR

    # Empty inputs are not allowed for bed times
    assert testSitter.set_bed_time('') == string_constants.EMPTY_INPUT_ERROR

    # Test that AM or PM is used for bed times
    assert testSitter.set_bed_time('5:00') == string_constants.MISSING_ENDING_ERROR

    # Non time inputs are not allowed for bed times
    assert testSitter.set_bed_time('67PM') == string_constants.INVALID_TIME_FORMAT_ERROR

    # creat a test check for type string input and write code for it

def test_invalid_start_time():
    testSitter = Babysitter()

    # Empty inputs are not allowed for start times
    assert testSitter.set_start('5AM') == string_constants.INVALID_START_TIME_ERROR

def test_valid_start_time():
    testSitter = Babysitter()

    # Test a 6PM start time (18 when converted to 24 hour format)
    assert testSitter.set_start("6:00PM") == string_constants.SUCCESS_STRING
    assert testSitter.start == 18

    # Test a 4PM start time (should auto set to 17 since that is the earliest start)
    assert testSitter.set_start("4PM") == string_constants.SUCCESS_STRING
    assert testSitter.start == 17

    # Test a 6:30 start time to test that fractional times don't count (should be 19)
    assert testSitter.set_start("6:30PM") == string_constants.SUCCESS_STRING
    assert testSitter.start == 19

def test_invalid_finish_time():
    testSitter = Babysitter()

    # Test a 4PM start time (should auto set to 17 since that is the earliest start)
    assert testSitter.set_finish("6AM") == string_constants.FINISH_TIME_AFTER_FIVE_AM_ERROR

    # Test catching finish times before start times
    testSitter.set_start("8PM")
    assert testSitter.set_finish("7PM") == string_constants.FINISH_TIME_BEFORE_START_ERROR

def test_valid_finish_time():
    testSitter = Babysitter()

    # Test a 3AM finish which is within range
    testSitter.set_start("6PM")
    assert testSitter.set_finish("3AM") == string_constants.SUCCESS_STRING

    # Test finishing a full night from both bounds
    testSitter.set_start("5PM")
    assert testSitter.set_finish("4AM") == string_constants.SUCCESS_STRING


def test_invalid_bed_time():
    testSitter = Babysitter()

    # Bed times after midnight are not allowed (could be changed in the future)
    assert testSitter.set_bed_time("3AM") == string_constants.INVALID_BED_TIME_ERROR

    # Bed times before 6 are not allowed (could be changed but before 6 would be at the 5 start time)
    assert testSitter.set_bed_time("4PM") == string_constants.INVALID_BED_TIME_ERROR

def test_valid_bed_time():
    testSitter = Babysitter()

    # Test default bed time which is set to 10PM (22 in 24 hour format)
    assert testSitter.bed_time == 22

    # Test setting bed time at 9PM
    testSitter.set_bed_time("9PM")
    assert testSitter.bed_time == 21


def test_invalid_calculation_scenario():
    testSitter = Babysitter()

    # Test undefined start time

    # Test undefined finish time

    # Test undefined bed time


def test_calculation():
    testSitter = Babysitter()

    # Test undefined start time

    # Test undefined finish time

    # Test undefined bed time

# # 12AM start time?
# edge bed time
# edge start time
# edge finish time
# # Day light savings?
# def test_edge_case():
#     pass