# Airline-Flight-Scheduling

Objective:
The	objective	of	this	project	is	to	write	a	program	in	Python	that	will	read	in	a	data	
file	with	all	flights	from	Providence	to	Orlando and	display	information requested	
by	the	user.
The	Statistics:
The	data	file	can	be	found	here:
http://www.cs.uri.edu/~cingiser/csc110/assignments/flights.txt
This	text	file	contains	the	following	information	for	flights	from	Providence	to	
Orlando.		
Airline
The	name	of	the	airline,	which	is	represented	as	a	string.	
Flight	Number
Each	airline	has	a	unique	flight	number	assigned	to	a	particular	flight.		Each	airline	
may	have	more	than	one	flight	scheduled	on	the	same	day	from	Providence	to	
Orlando.
Departure	Time
The	time	of	day	that	the	flight	is	scheduled	to	depart	from	Providence.		Time	is	
represented	in	24	hour	clock	time,	so	14:00	represents	2:00PM.
Arrival	Time
The	time	of	day	that	the	flight	is	scheduled	to	arrive	in	Orlando.
Price
The	cost	of	the	flight.
The	Program:
For	this	assignment,	you	will	present	the	user	with	a	list	of	options	and	you	will	
present	the	results	chosen	by	the	user.		The	program	should	continue	to	run	until	
the	user	chooses	to	quit.		
As	you	can	see	from	the	image,	there	are	7 different	options	offered	to	the	user.		
Here	is	a	brief	description	of	each.
1	– Find	Specific	Flight	
This	option	asks	the	user	to	enter	an	airline	and	a	flight	number,	and	then	displays	
for	the	user	the	information	about	that	flight.		If	the	user	enters	an	airline	or	flight	
number	that	does	not	exist,	the	program	should	let	the	user	know.
2	- Flights	Cheaper	than	a	Specified	Price
This	option	will	ask	the	user	to	specify	a maximum	price	and	then	print	flight	
information	for	each	of	the	flights	whose	price	is	less	than	or	equal	to	that	
maximum.		
3	- Longest Flight
This	option	finds	the	flight	with	the	longest duration.		That	is,	the	flight	with	the	
longest time	difference	between	the	departure	time	and	the	arrival time.
4	- Flights	Arriving Before	a	Specified	Time
This	option	will	provide	the	user	with	a	list	of	flights	that	arrive before a	specified	
time.		Your	program	should	ensure	that	the	time	entered	by	the	user	is	in	a	valid	
time	format.		That	is,	the	user	input	should	be in	the	HH:MM	format	where	HH	is	
between	00	and	24	and	MM	is	between 00	and	60.
5	- Average	Price	of	Flights for	Specified	Airline
This	option	finds	the	average	price of	flights	for	a	given	airline.		The	user	should	be	
prompted	to	enter	an	airline and	then	the	program	should	make	sure	the	user	
chooses	a	correct	option.
6	- Sort	All	Flights	by	Departure	Time and	Write	to	a	New	File
This	option creates	an	output	file,	and	writes	to	the	file	the	flights	sorted	by	
departure	time.		Note	that	you	should	not	change	the	sorting	order	of	the	lists	in	
your	program.		Rather,	you	should	create	a	list	of	indexes	that	you	sort	based	on	the	
order	of	the departure	time.		You	can	use	any	sorting	algorithm	that	you	like.		You	
may	not use	the	python	built-in	sort() function.		
