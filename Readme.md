This is the simple script which I made during the duration of [Kiwi's Prague Hackatron](http://www.travelhackatron.cz) in summer 2017.  

#### Script idea ####
I would like to find cheapest return ticket between 2 airports (exp. PRG - JFK), in range from 3 to 14 days in
period of following next 9 months.

#### Installation ####
This is Python 2 script. Just change directory to script location and run it through Python command. It is necessary to 
open the script and manually change desired parameters. These parameters are:
* flyFrom - departure airport ITA code exp. 'PRG' for Prague
* flyTo - arrival airport ITA code exp. 'POA' for Palermo
* dateFrom - search period start date in form day/month/year exp. '30/06/2017'
* dateTo - search period end date in form day/month/year exp. '30/04/2018'
* days - list of day periods exp. [5, 10, 18] 

#### Ideas for improvement ####
* Possibility to set script arguments (departure, destination, one way etc.)
* Make argument check at start:
    * Check if dates are correct
    * Check if airport codes are valid ITA airport codes 
* In case of failure during the requesting URL from the URLlist, all info should be flushed/saved. Change structure and 
save every record immediately to file
* To implement option for selecting flights only in certain days of the week
* Loop this script over list of destination
* Multithreading
* Order csv from the cheapest to most expensive in the end 
* Output of script in form of HTML(Bootstrap) report
* Output statistics into console (exp. start time of the procedure, end time of the procedure, number of requests, cheapest flight etc.)

