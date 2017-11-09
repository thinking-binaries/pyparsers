# Test_PathTagParser.py  (c) 2014  D.J.Whale
#
# A PathTagParser that is table driven.


import sys
import parsers.PathTagTableParser as Parser
import re


URL = "http://data.nottinghamtravelwise.org.uk/parking.xml"
FILENAME = "cars.xml"

if len(sys.argv) > 1:
  FILENAME = sys.argv[1]


# This is the bit that parses the file and calls your handler
# with a path and a value, for each tag found in the file.

def emit(path, value):
  print("%s %s" % (path, value))

Parser.parse(FILENAME, [
  #(Parser.EVERYTHING,            emit),
  #("/Parking/Carpark/ShortDescription/",     emit),
  #("/Parking/Carpark/OccupancyPercentage/",  emit),
  (re.compile("^/Parking/.*$"),              emit)
])

# END

