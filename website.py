def CreateBooking(Name,Email,Phone,Date,NRGuests):
	date_components = Date.split('-') #to make string into a list of year,month,day
	print date_components
	year_of_booking = int(date_components[0])	#to split the date of booking into separate numbers to compare with today's date)
	month_of_booking = int(date_components[1])
	day_of_booking = int(date_components[2])
	hour_of_booking= int(date_components[3])	
	minute_of_booking=int(date_components[4])

	#validate that the date inputed is not in the past, check date time library
	import datetime	
	now = datetime.datetime.now()
	if now.year>year_of_booking : 
		print 'Invalid year.' 
	elif now.month>=month_of_booking:#make sure checks only if same year, 1st month in 2019 still valid complared to 9th month in 2018)
		print 'Invalid month'

	#validate the phone number not too short or too long 
	Phone_digits=len(Phone)
	if Phone_digits<10 or Phone_digits>13:
		print 'Invalid number, either too short or too long'

	if int(NRGuests)>20: 
		print 'Unfortunately we cannot take bookings for more than 20 people'


# booking_date = raw_input ('Please input a date in the form YYYY-MM-DD hh-mm')

CreateBooking("Irina", "Irina@test.com", "077777777", "2016-11-01-19-30", '4')
