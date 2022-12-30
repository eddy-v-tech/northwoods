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

    # Test that anything that is not a string is not permitted
    assert testSitter.set_start(67) == string_constants.INVALID_TYPE_INPUT_ERROR

    # Empty inputs are not allowed for finish times
    assert testSitter.set_finish('') == string_constants.EMPTY_INPUT_ERROR

    # Test that AM or PM is used finish time
    assert testSitter.set_finish('5:00') == string_constants.MISSING_ENDING_ERROR

    # Non time inputs are not allowed for finish times
    assert testSitter.set_finish('67PM') == string_constants.INVALID_TIME_FORMAT_ERROR

    # Test that anything that is not a string is not permitted
    assert testSitter.set_finish(67) == string_constants.INVALID_TYPE_INPUT_ERROR

    # Empty inputs are not allowed for bed times
    assert testSitter.set_bed_time('') == string_constants.EMPTY_INPUT_ERROR

    # Test that AM or PM is used for bed times
    assert testSitter.set_bed_time('5:00') == string_constants.MISSING_ENDING_ERROR

    # Non time inputs are not allowed for bed times
    assert testSitter.set_bed_time('67PM') == string_constants.INVALID_TIME_FORMAT_ERROR

    # Test that anything that is not a string is not permitted
    assert testSitter.set_bed_time(67) == string_constants.INVALID_TYPE_INPUT_ERROR

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
    assert testSitter.set_bed_time("4AM") == string_constants.INVALID_BED_TIME_ERROR

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

    # Test undefined start time is handled
    testSitter.start = None
    assert testSitter.calculate_nightly_charge() == string_constants.NO_START_TIME_SET_ERROR

    # Test undefined finish time is handled
    testSitter.finish = None
    assert testSitter.calculate_nightly_charge() == string_constants.NO_START_TIME_SET_ERROR

    # Test undefined bed time is handled
    testSitter.bed_time = None
    assert testSitter.calculate_nightly_charge() == string_constants.NO_START_TIME_SET_ERROR


def test_calculation():
    testSitter = Babysitter()

    # Test a 1 hour shift before bed time should be $12 (using default bed time of 10PM)
    testSitter.set_start("5PM")
    testSitter.set_finish("6PM")
    assert testSitter.calculate_nightly_charge() == 12


    # Test a 7 hour shift that includes all rates (2*12+3*8+2*16 = $80)
    testSitter.set_start("7PM")
    testSitter.set_finish("2AM")
    testSitter.set_bed_time("9PM")
    assert testSitter.calculate_nightly_charge() == 80

    # Test a 2 hour shift that includes just bed time and before midnight (2*8 = 16)
    testSitter.set_start("9PM")
    testSitter.set_finish("11PM")
    testSitter.set_bed_time("9PM")
    assert testSitter.calculate_nightly_charge() == 16

    # Test a 2 hour shift that includes just after midnight hours (16*2=32)
    testSitter.set_start("1AM")
    testSitter.set_finish("3AM")
    assert testSitter.calculate_nightly_charge() == 32


# Might have to come back to this one since I took care of some of what I thought would be edge cases already
# def test_edge_case():
#     pass