import biztime
import unittest
from datetime import date, datetime, time, timedelta


class TestHelperFunctions(unittest.TestCase):

  def test_div_round_RoundsUp(self):
    self.assertEqual(biztime.div_round(5, 2), 3)
    self.assertEqual(biztime.div_round(5, 3), 2)

  def test_div_round_RoundsDown(self):
    self.assertEqual(biztime.div_round(1, 3), 0)
    self.assertEqual(biztime.div_round(5, 4), 1)

  def test_div_round_NoRound(self):
    self.assertEqual(biztime.div_round(4, 2), 2)
    self.assertEqual(biztime.div_round(0, 2), 0)

  def test_div_round_DivideByZeroRaisesError(self):
    with self.assertRaises(ZeroDivisionError):
      biztime.div_round(1, 0)


class TestBizTime(unittest.TestCase):

  def setUp(self):
    self.bt_blank = biztime.BizTime({
      'biz_start': time(0, 0),
      'biz_end': time(23, 59, 59),
    })
    self.bt_basic = biztime.BizTime({
      'biz_start': time(9, 0),
      'biz_end': time(17, 0),
      'weekend': [5, 6],
      'holidays': [
        date(2018, 12, 24),
        date(2018, 12, 25),
        date(2019, 1, 1),
      ]
    })

  def test_is_biz_day_weekendReturnsFalse(self):
    self.assertFalse(self.bt_basic.is_biz_day(date(2018, 12, 9)))

  def test_is_biz_day_holidayReturnsFalse(self):
    self.assertFalse(self.bt_basic.is_biz_day(date(2018, 12, 25)))

  def test_time_diff_invalidInputsRaisesError(self):
    with self.assertRaises(TypeError):
      self.bt_blank.time_diff(
          datetime(2018, 1, 1, 8, 0, 0), datetime(2018, 1, 2, 8, 0, 0))
    with self.assertRaises(ValueError):
      self.bt_blank.time_diff(time(8, 0, 0), time(3, 0, 0))

  def test_time_diff_validInputReturnsTimedelta(self):
    test_cases = [
      [time(0, 0, 0), time(8, 0, 0), timedelta(hours=8)],
      [time(10, 23, 0), time(15, 11, 0), timedelta(hours=4, minutes=48)],
    ]
    for t in test_cases:
      self.assertEqual(self.bt_blank.time_diff(t[0], t[1]), t[2])

  def test_date_diff_invalidInputsRaisesError(self):
    with self.assertRaises(TypeError):
      self.bt_blank.date_diff(time(8, 0, 0), time(10, 0, 0))
    with self.assertRaises(ValueError):
      self.bt_blank.date_diff(
          datetime(2018, 1, 2, 8, 0, 0), datetime(2018, 1, 1, 8, 0, 0))

  def test_date_diff_validInputReturnsTimedelta_fullWorkWeek(self):
    self.assertEqual(
        self.bt_basic.date_diff(
            datetime(2018, 12, 9, 8, 0, 0),
            datetime(2018, 12, 15, 8, 0, 0)
        ),
        timedelta(hours=40)
    )


if __name__ == '__main__':
  unittest.main(verbosity=2)
