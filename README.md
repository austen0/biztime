# biztime

`biztime` is a is a utility for calculating the total time between given
dates/times, while omitting non-working hours, weekends, and holidays as
configured by the user. Includes additional helper functions for interacting
with various `datetime` objects.

## Installation

**COMING SOON** ~~Install and update using pip:~~

~~`sudo pip install biztime`~~

## Reference

### BizTime Class Functions

<pre>
BizTime()<b>.time_diff</b>(<i>start, end</i>)
	Returns a datetime.timedelta object representing the number of working hours
	between the start and end time.
	&nbsp;
	Arg Types:
		start - datetime.time
		end   - datetime.time
	&nbsp;
BizTime()<b>.date_diff</b>(<i>start, end</i>)
	Returns a datetime.timedelta object representing the number of working hours
	between the start and end time, having omitted weekends and holidays.
	&nbsp;
	Arg Types:
		start - datetime.datetime
		end   - datetime.datetime
	&nbsp;
BizTime()<b>.is_biz_day</b>(<i>date</i>)
	Returns a bool indicating whether the given date is a weekend or holiday per
	the users' config.
	&nbsp;
	Arg Types:
		date - datetime.date
	&nbsp;
</pre>

### Helper Functions

<pre>
<b>create_date_range</b>(<i>start, stop</i>)
	Returns a list of datetime.date objects for all dates between the given start
	and end dates (inclusive).
	&nbsp;
	Arg Types:
		start - datetime.date
		end   - datetime.date
	&nbsp;
<b>convert_timedelta</b>(<i>td, unit</i>)
	Returns an int value representation of the given timedelta in the specified
	units.
	&nbsp;
	Arg Types:
		td   - datetime.timedelta
		unit - string ('s', 'm', or 'h')
	&nbsp;
<b>dt_to_date</b>(<i>dt_in</i>)
	Returns a datetime.date object from a given datetime object.
	&nbsp;
	Arg Types:
		dt_in   - datetime.datetime
	&nbsp;
<b>dt_to_time</b>(<i>dt_in</i>)
	Returns a datetime.time object from a given datetime object.
	&nbsp;
	Arg Types:
		dt_in   - datetime.datetime
	&nbsp;
</pre>
