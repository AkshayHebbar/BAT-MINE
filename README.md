# BAT-MINE

About
--------------------------------
A hobby project to automate BAT rewards mining from Brave Browser

The Program is designed to run for clicking ads to generate rewards of BAT tokens.

Brave provides 0.005 BAT tokens per advertisement in exchange for user attention.

Maximum number of ads which can be monetized per hour is 10.


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
2. Handle Notification Ads
