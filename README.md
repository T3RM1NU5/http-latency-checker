# http-latency-checker
HTTP Latency Checker is a small utility designed to check the status and response time of web servers

## Requirements
**Python 3.2 or higher**

If you receive the error
	Error: This utility requires python 3.2 or higher
run it the program again like this
	python3 http-latency-checker.py

## Usage

By default you only need to supply a URL list file which contains 1 URL perline however you can include a second option to change the output file location.  

```
usage: http-latency-checker.py [-h] [-v] input_file_path [output_file_path]

Check latency of HTTP GET requests

positional arguments:
  input_file_path   List of URLS
  output_file_path  output file path, default output.json

optional arguments:
  -h, --help        show this help message and exit
  -v, --verbose     increase output verbosity
```

## Input File

The user is required to supply an input file that contains a list of URLS like the one bellow

```
http://github.com
termini.me:443
https://gnu.org:80
```

Note HTTP latency checker will by default append http:// to a URL if no scheme was given
An exception is made if the port ends in 443, in this case the scheme is set to https://

## Output File

By default http-latency-checker saves to a json file named output.json. The user can change the output file by including a second positional argument.  Bellow is an example output. 

```
[
    {
        "URL": "https://termini.me",
        "lattency_ms": 1132,
        "size": 3482,
        "status": "reachable",
        "status reason": "HTTP code 200"
    },   
    {
        "URL": "http://foo.bar",
        "latency_ms": null,
        "size": null,
        "status": "unreachable",
        "status reason": "<urlopen error [Errno -2] Name or service not known>"
    }
]
```
