#!/bin/bash

while true; do
	{ echo -ne "HTTP/1.1 200 OK\r\nContent-Length: 12\r\n\r\nWelcome!"; } | nc -l -p 8080
done
