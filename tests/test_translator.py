from datetime import datetime

from freezegun import freeze_time

from ferda_time_translator.translator import (
    get_current_ferda_time,
    get_ferda_time,
)


def time_to_datetime(time: str) -> datetime:
    return datetime.strptime(time, "%H:%M")


# flake8: noqa: E501
def test_get_ferda_time():
    # fmt: off
    assert get_ferda_time(time_to_datetime("00:00")) == "midnight snack"
    assert get_ferda_time(time_to_datetime("00:25")) == "midnight snack"
    assert get_ferda_time(time_to_datetime("01:45")) == "2nd dinner"
    assert get_ferda_time(time_to_datetime("02:30")) == "unironic, actual dinner"
    assert get_ferda_time(time_to_datetime("05:00")) == "pre-pre-breakfast (eaten during sleep)"
    assert get_ferda_time(time_to_datetime("05:45")) == "1st snack (still asleep)"
    assert get_ferda_time(time_to_datetime("06:30")) == "Musaharati / Breakfast Barbaque / Musahūr"
    assert get_ferda_time(time_to_datetime("07:15")) == "pre-breakfast"
    assert get_ferda_time(time_to_datetime("07:50")) == "breakfast"
    assert get_ferda_time(time_to_datetime("09:00")) == "brunch"
    assert get_ferda_time(time_to_datetime("10:00")) == "2nd breakfast / zweites Frühstück"
    assert get_ferda_time(time_to_datetime("10:45")) == "bruncher"
    assert get_ferda_time(time_to_datetime("11:11")) == "Elevenses"
    assert get_ferda_time(time_to_datetime("11:45")) == "suncher"
    assert get_ferda_time(time_to_datetime("11:55")) == "suncher"
    assert get_ferda_time(time_to_datetime("12:05")) == "pre-lunch"
    assert get_ferda_time(time_to_datetime("12:40")) == "ironic post-ironic unironic krabby patty bruncher"
    assert get_ferda_time(time_to_datetime("13:20")) == "lunch (just a snack)"
    assert get_ferda_time(time_to_datetime("14:05")) == "post lunch"
    assert get_ferda_time(time_to_datetime("15:00")) == "Tiffin"
    assert get_ferda_time(time_to_datetime("15:30")) == "post-ironic post-modernist post-lunch"
    assert get_ferda_time(time_to_datetime("16:15")) == "pre-linner (2nd snack)"
    assert get_ferda_time(time_to_datetime("17:00")) == "pina colada OR pre modernist mezcal shot"
    assert get_ferda_time(time_to_datetime("17:15")) == "second post ironic unironic pre ironic breakfast"
    assert get_ferda_time(time_to_datetime("18:22")) == "linner"
    assert get_ferda_time(time_to_datetime("19:00")) == "dunch"
    assert get_ferda_time(time_to_datetime("20:15")) == "dinner (if you're post-modernist, add Jiggs)"
    assert get_ferda_time(time_to_datetime("21:10")) == "supper (~2nd suncher)"
    assert get_ferda_time(time_to_datetime("22:10")) == "Siu Yeh"
    assert get_ferda_time(time_to_datetime("23:00")) == "ler"
    assert get_ferda_time(time_to_datetime("23:42")) == "post-linner"
    assert get_ferda_time(time_to_datetime("23:52")) == "a krabby patty"
    # fmt: on


def test_get_current_ferda_time():
    with freeze_time("2020-09-10 00:00"):
        assert get_current_ferda_time() == "midnight snack"
    with freeze_time("2020-09-10 00:25"):
        assert get_current_ferda_time() == "midnight snack"
