import requests
import json
import argparse
import socket

if __name__ == "__main__":

    parser = argparse.ArgumentParser() # to use on command line
    parser.add_argument("-i", "--ipaddress", help="IP address to track") # args on terminal
    args = parser.parse_args() # to get the args from the terminal
    ip = args.ipaddress #to get the ip

    url = "http://ip-api.com/json/"+ip # free api to get the location

    response = requests.get(url) # to get the request

    data = json.loads(response.content) # to convert the json data

    print(data)

