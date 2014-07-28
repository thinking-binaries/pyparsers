# Demo_CarPark.py  (c) 2014  D.J.Whale
#
# Read the number of cars in all car parks in Nottingham,
# and work out which car park has the most cars in it.
#
# Demonstrates parsing an XML file into paths and values,
# and then using that to perform some other processing.
# The xml file can be read live from the internet by fetching it
# each time you run the program.
#
# or you can manually fetch it like this:
#
# wget -O cars.xml http://data.nottinghamtravelwise.org.uk/parking.xml
#
#
# You can verify the final answer yourself by:
# (1) enabling the print() in the handlePath() function
# (2) Running like this:
#       python Demo_CarPark.py | grep Occupancy/

import sys
import parsers.PathTagParser as PathTagParser

biggest_v = 0
biggest_d = ""
description = ""
 
# This is the function that is called as each tag is processed 
# you can do anything with the data in here.

def handlePath(path, value):
  global description, biggest_v, biggest_d
  #print(path + "=" + value)
  
  if path == "/Parking/Carpark/ShortDescription/":
    description = value
    
  elif path == "/Parking/Carpark/Occupancy/":
    v = int(value)
    if v > biggest_v:
      biggest_v = v
      biggest_d = description
       

# Set up where the data comes from:
URL = "http://data.nottinghamtravelwise.org.uk/parking.xml"
FILENAME = "cars.xml"
#if len(sys.argv) > 1:
#  FILENAME = sys.argv[1]

# Fetch the data live  
PathTagParser.fetch(URL, FILENAME)
  
# Read and process the data
PathTagParser.parse(FILENAME, handler=handlePath)

# Display the final result
print(biggest_d + " has the most cars, with:" + str(biggest_v))

# END

