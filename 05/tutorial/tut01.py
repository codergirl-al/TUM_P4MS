from datetime import datetime
def read_datetime():
	dt_str = input("")
	return datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")

def compare_datetimes(dt1, dt2):
	if dt1 < dt2:
		return [dt1.strftime("%Y-%m-%d %H:%M:%S"), dt2.strftime("%Y-%m-%d %H:%M:%S")]
	else:
		return [dt2.strftime("%Y-%m-%d %H:%M:%S"), dt1.strftime("%Y-%m-%d %H:%M:%S")]
	
datetime1 = read_datetime()
datetime2 = read_datetime()
print(compare_datetimes(datetime1, datetime2))