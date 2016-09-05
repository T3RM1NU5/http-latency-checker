#!/usr/bin/env python
import sys

# Version check to warn people trying to run the code on Python 2
if sys.version_info < (3, 2):
    print("Error: This utility requires python 3.2 or higher")
    sys.exit(1)

# Continue importing required libraries
import json
import urllib.request
import time
import urllib.parse
import os.path
import argparse


def main(argv):

    #Parse user arguments
    parser = argparse.ArgumentParser(description='Check latency of HTTP GET requests')
    parser.add_argument('input_file_path',help='List of URL\'S')
    parser.add_argument('output_file_path', nargs='?', default='output.json',
                        help='Optional output file path, default output.json')
    parser.add_argument('-v','--verbose', help='increase output verbosity',
                        action="store_true")

    #If no user arguments are given print help
    if len(sys.argv)==1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()

    output_dic = []  # initialize output list, this list will contain a list of dictionary

    # Check to see if the request input file exist, if not end the program
    if not os.path.exists(args.input_file_path):
        print("Error file {} does not exist".format(args.input_file_path))
        return

    # Intialize line_number used to keep what line of the file we are on
    line_number = 0  # Used to keep track of file line number

    # For every line of the input file, get the content of that line
    with open(args.input_file_path) as urllist:
        for url in urllist:

            # Increment the line number by 1
            line_number += 1

            # Reset values to defaults
            latency_time = 0  # time it takes to perform the get request
            Size = 0  # Size of the requested page
            status = ""  # Status of the requested page
            status_reason = ""  # Reason why the test passed or failed
            start_time = 0  # Holds time before GET request
            latency_time = 0  # Holds time after GET request

            # Remove return character from URL string
            url = url.rstrip()

            # Skip blank lines
            if (len(url) == 0):
                continue

            # Normalize the URL so can be used correctly by URLLIB
            # urllib does not like urls that do not start with a scheme
            # by default we will append http:// url then check for https
            if url[0:4] != 'http':
                url = 'http://' + url
                parsed_url = urllib.parse.urlparse(url)
                # if the port is 443 change the scheme to https
                try:
                    if parsed_url.port == 443:
                        parsed_url = parsed_url._replace(scheme='https')
                        url = parsed_url.geturl()
                # If the URL looks like this http://foo.bar:443h/ it will 
                # trigger a warning that the URL will be considered to be 
                # malformed and result in a non numeric port.
                except:
                    print('\033[93m', "Warning: Malformed URL on line ",
                          line_number, "URL will be unreachable" '\033[0m', "\n")

            # Attempt to connect to the request URL
            try:
                # Set start_time to the current number of seconds since
                # epoch
                start_time = time.time()

                # Perform an HTTP GET request on the requested URL, store the
                # results in url_get
                url_get = urllib.request.urlopen(url, timeout=1)

                # Calculate the time between it took to complete the previous
                # action by subtracting the current time from the start time
                # then convert to milliseconds
                latency_time = round((time.time() - start_time) * 1000)

                # Find the size of requested page
                size = len(url_get.read())

                # Get HTTP Status
                status = "reachable"
                status_reason = str("HTTP code " + str(url_get.code))

            # Handle the various errors that can occur during the GET request
            except Exception as err:
                status = "unreachable"
                status_reason = str(err)
                size = None
                latency_time = None
                pass


            if args.verbose:
                #Print output to standard out
                print("URL: ", url)
                print("Status: ", status)
                print("Status Reason: ", status_reason)

                # Only show latency test info if the initial connection test passed
                if (status == "reachable"):
                    print("Latency: ", latency_time, "Milliseconds")
                    print("Size: ", size, " Bytes")
                print("\n")

            # Store our current test results in a dictionary
            current_test_results = {'URL': url, 'status': status,
                                    "status reason": status_reason, 'latency_ms': latency_time, 'size': size}

            # Append the current test results to the output list
            output_dic.append(current_test_results)

            # close the file handler
            url_get.close()

    # Save the test results to the drive
    with open(args.output_file_path, 'w') as outputfile:
        json.dump(output_dic, outputfile, sort_keys=True, indent=4)

    return 0


if __name__ == "__main__":
    main(sys.argv)
