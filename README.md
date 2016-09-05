# http-latency-checker
HTTP Latency Checker is a small utility designed to check the status and response time of web servers

## Requirements
	Python 3.1 or higher 

## Usage

By default you only need to supply a URL list file which contains 1 URL perline however you can include a second option to change the output file location

	python ./http-latency-checker.py urllist [output.json] 

HTTP Latency checker will by default append http:// to a URL if no scheme was given
An exception is made if the port ends in 443, in this case the scheme is set to https://

## Output 

The output format is a .json that looks similar to bellow

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
