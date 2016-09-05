# Assumptions 

* All tests should be stored to the JSON, even if the URL can not be contacted

* Results will be stored in JSON file with 5 values 
	* URL: used to store the requested URL
	* Status: contains "reachable" or "unreachable"
	* Status reason: contains the reason why the URL was reachable or unreachable
	* Latency: the time it takes to complete the GET request, is NULL if unreachable
	* Size: The size the request URL, is NULL if unreachable 

* If no scheme was given the default scheme will be HTTP
* If the URL has port 443 and no scheme it will be HTTPS 

* User must define the input file as the first argument
* The output file can optionally be supplied as a second argument 
* If no arguments are given, it will print usage information 
