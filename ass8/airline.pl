/*initializing the airport*/
city(toronto, 50, 60).
city(madrid, 75, 45).
city(barcelona, 40, 30).
city(londan, 75, 80).
city(malaga, 50, 30).
city(valencia, 40, 20).
city(paris, 50, 60).
city(toulouse, 40, 30).

/*printing airports*/
airport(X):-
	city(X, Y, Z),
	printairportdetails(X, Y, Z).

printairportdetails(X, Y, Z):-
   nl,write('City: '),
      write(X),
   nl,write('Airport tax : $'),
      write(Y),
   nl,write('Minminum delay time : '),
      write(Z),
      write('min').
   

	

/*initializing the flights*/
/*AirCanda*/
path(toronto, londan, aircanada, 500, 360).
path(toronto, madrid, aircanada, 900, 480).
path(madrid, barcelona, aircanada, 100, 60).

/*United*/
path(toronto, londan, united, 650, 420).
path(toronto, madrid, united, 950, 540).
path(paris, toulouse, united, 35, 120).

/*Iberia*/
path(toronto, madrid, iberia, 800, 480).
path(madrid, barcelona, iberia, 120, 65).
path(barcelona, londan, iberia, 220, 240).
path(madrid, valencia, iberia, 40, 50).
path(madrid, malaga, iberia, 50, 60).
path(malaga, valencia, iberia, 80, 120).
path(barcelona, valencia, iberia, 110, 75).  

/*printing airports*/
flight(P, Q):-
	path(P, Q, R, S, T),
	printflightdetails(P, Q, R, S, T).

printflightdetails(P, Q, R, S, T):-
   nl,write('Departure City: '),
      write(P),
   nl,write('Arrival City: '),
      write(Q),
   nl,write('Airline Name: '),
      write(R),
   nl,write('Price : $'),
      write(S),
   nl,write('Duration time : '),
      write(T),
      write('min').

isflight(P, Q):-
	path(P, Q,R,S,T),
	printflightdetails(P,Q,R,S,T).

cheapflight(P, Q):-
	path(P, Q, R, S, T),
	(S < 400),
	nl,write('Flight is cheap as price is less than $400.'),
	nl,write('Flight details are:-'),
	printflightdetails(P,Q,R,S,T).

twoflights(A, B):-
	path(A, City,P,Q,R),
	path(City, B,M,N,O),
	nl,write('Flights are available.'),
	printflightdetails(A, City,P,Q,R),
	nl,
	printflightdetails(City, B,M,N,O).

preferflight(P, Q, R, S, T):-
	(cheapflight(P, Q);
	checkaircanada(P,Q,R,S,T)),
	nl,write('FLight can be prefered.').	

checkaircanada(P,Q,R,S,T):-
	path(P,Q,aircanada,S,T),
	printflightdetails(P,Q,R,S,T).

checkunited(P,Q,R,S,T):-
	path(P,Q,united,S,T),
	printflightdetails(P,Q,R,S,T).


unitedandaircanada(A, B):-
	(path(A, B, united,P, Q);
	path(A, B, aircanada,M,N)),
	printflightdetails(A, B, united,P, Q),
	nl,printflightdetails(A, B, aircanada,M, N),
	nl,write('Both united and air canada airlines flights available.').
