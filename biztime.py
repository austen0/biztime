import datetime as dt


def create_date_range(start, end):
  """Returns a list of date objects spanning from the start to end inputs."""
  date_range = [start]
  if start == end:
    return date_range

  range_size = (end - start).days

  last_date = start
  while last_date < end:
    next_date = last_date + dt.timedelta(days=1)
    date_range.append(next_date)
    last_date = next_date

  return date_range

def convert_timedelta(td, unit):
  """Convert timestamp object to int in specified units."""
  td_s = (td.days * 3600 * 24) + td.seconds
  if unit == 's': return td_s
  if unit == 'm': return div_round(td_s, 60)
  if unit == 'h': return div_round(td_s, 3600)
  raise ValueError('unit not recognized: %s' % unit)

def dt_to_date(dt_in):
  """Returns a date object from a datetime object."""
  return dt.date(dt_in.year, dt_in.month, dt_in.day)

def start_of_day(date):
  """Returns a datetime object of 00:00:00am on the input date."""
  return dt.datetime.combine(date, dt.time(0))

def end_of_day(date):
  """Returns a datetime object of 11:59:59pm on the input date."""
  return dt.datetime.combine(date, dt.time(23, 59, 59))

def div_round(dividend, divisor):
  """Divides two ints with proper rounding."""
  return (dividend + divisor // 2) // divisor


class BizTime:

  def __init__(self, conf):
    self.biz_start = conf['biz_start']
    self.biz_end = conf['biz_end']
    self.weekend = conf['weekend']
    self.holidays = conf['holidays']

  def biz_time_from_day(self, start, end):
    """Returns a timedelta between start and end inputs minus non-biz hours."""
    curr_date = dt_to_date(start)
    if curr_date.weekday() in self.weekend or curr_date in self.holidays:
      return dt.timedelta(0)

    biz_start_ = dt.datetime.combine(curr_date, self.biz_start)
    biz_end_ = dt.datetime.combine(curr_date, self.biz_end)
    if start > biz_end_ or end < biz_start_ or start == end:
      return dt.timedelta(0)
    if start < biz_start_:
      start = biz_start_
    if end > biz_end_:
      end = biz_end_

    return end - start

  def diff(self, start, end):
    """Returns timedelta between to dates."""
    biz_time = dt.timedelta(0)

    if end < start:
      raise ValueError(
          'The end date must be equal to or later than the start date.')

    # If start and end times are on same day, immediately calculate and return.
    if dt_to_date(start) == dt_to_date(end):
      return biz_time_from_day(start, end)


    # Get biz hours from partial days at beginning and end of inuput range.
    start_eod = end_of_day(start)
    end_bod = start_of_day(end)
    biz_time += self.biz_time_from_day(start, start_eod)
    biz_time += self.biz_time_from_day(end_bod, end)

    date_range_start = dt_to_date(start) + dt.timedelta(days=1)
    date_range_end = dt_to_date(end) - dt.timedelta(days=1)
    if date_range_start > date_range_end:
      return biz_time

    # Get working hours from full days between start and end dates.
    date_range = create_date_range(date_range_start, date_range_end)
    for date in date_range:
      biz_time += self.biz_time_from_day(start_of_day(date), end_of_day(date))

    return biz_time
