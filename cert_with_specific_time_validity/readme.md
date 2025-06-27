# Certificate with specific time and validity checking

Python's datetime supports microseconds but not nanoseconds directly (unless using datetime.timedelta tricks).

X.509 itself limits timestamps to second-level resolution, so even though the Python object carries microseconds, most verifiers will ignore sub-second precision.

X.509 certificates use the following formats:
For dates before the year 2050: UTC Time – YYMMDDHHMMSSZ
For dates from 2050 onward: Generalized Time – YYYYMMDDHHMMSSZ

Here we simulate precision in custom tools, logs, or audits. 
Option to calculate the same for timeformat YYYY-MM-DD_HHmm_ss_ms_ns

