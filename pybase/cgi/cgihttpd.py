#! /usr/bin/python3


from http.server import CGIHTTPRequestHandler, test


test(CGIHTTPRequestHandler, port=8888)


