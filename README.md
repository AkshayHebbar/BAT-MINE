# BAT-MINE

About
--------------------------------
Automate BAT rewards from Brave

The Program is set to run in an infinite loop for clicking ads to generate rewards of BAT tokens.

Brave provides 0.005 BAT tokens per advertisement in exchange for user attention.

Maximum number of ads which can be monetized per hour is 5.


Ideal Monetization Calculation
--------------------------------

5 ads * 0.005 BAT = 0.025 BAT per hour

24 hrs * 0.025 BAT = 0.6 BAT per day

7 days * 0.6 BAT = 4.2 BAT per week

4 weeks * 4.2 BAT = 17.64 BAT per month

12 months * 17.64 BAT = 211.68 BAT per year


Possible Issues
--------------------------------

1. Unable to load advertisement page due to caching/ cookie issues
	- Try closing the existing tab and open a new one.
	  Refresh the newly opened tab

2. Browser opening with 0.000 balance
	- Start the browser with the custom configuration.
	  Port and Path of the custom run must be constant
	  Debugconfigutation of selenium must match the browser configuration
	  
3. Stopping the service
	- Currently the program is running in an infinite loop.
	  To close the program kill the process .


Enhancements
---------------------------------
1. Run the program in multiple containers/ pods for increased monetization
2. Handle Notificatino Ads