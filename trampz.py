import sys, os
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__), '/usr/local/lib/python2.7/dist-packages/bluepy/', 'bluepy')))
import btle

ADDRESS = "78:A5:04:19:58:E1"

conn = btle.Peripheral(ADDRESS)

print(conn)