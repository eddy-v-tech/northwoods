from babysitter import Babysitter
import string_constants

def test_babysitter_init():
    testSitter = Babysitter()
    assert testSitter.start == 0
    assert testSitter.finish == 0
    assert testSitter.start_to_bed_pay == 12
    assert testSitter.bed_to_mid_pay == 8
    assert testSitter.mid_to_finish_pay == 16
    assert testSitter.bed_time == 10

def test_invalid_start_times():
    testSitter = Babysitter()

    # Empty inputs are not allowed for start times
    assert testSitter.set_start('') == string_constants.EMPTY_INPUT_ERROR
    # Test that AM or PM is used for time
    assert testSitter.set_start('5:00') == string_constants.MISSING_ENDING_ERROR
    # Empty inputs are not allowed for start times
    assert testSitter.set_start('67PM') == string_constants.INVALID_TIME_FORMAT
    # Empty inputs are not allowed for start times
    assert testSitter.set_start('5AM') == string_constants.INVALID_START_TIME_ERROR

def test_invalid_finish_time():
    pass

def test_invalid_bed_time():
    pass
