from babysitter import Babysitter

def test_babysitter_init():
    testSitter = Babysitter()
    assert testSitter.start == 0
    assert testSitter.finish == 0
    assert testSitter.start_to_bed_pay == 12
    assert testSitter.bed_to_mid_pay == 8
    assert testSitter.mid_to_finish_pay == 16
    assert testSitter.bed_time == 10

