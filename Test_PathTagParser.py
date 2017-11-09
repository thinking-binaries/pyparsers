# Test_PathTagParser.py  (c) 2014  D.J.Whale
#
# A PathTagParser is a parser that parses tagged data like XML,
# and turns it into a series of "paths", a bit like a directory
# path. Every path is send to the handler function that you provide,
# along with the value at that path. Your handler function can
# then filter out just the data that it needs and process that
# data.
#
# Paths for XML nodes like <record><field><value>A   become:
# /record/field/value/=A
#
# Paths for XML attributes like <record><field id="A">  become:
# /record/field/id=A
#
# Paths for closing tags like <record><field></field>  become:
# /record/field~
#
# Thus you can process data notes and attribute values in a similar
# way if you know their paths through the tags. The tilde (~) marks
# a closing tag, and is sometimes useful to detect the end of a
# whole record of data, when you might want to process that whole
# record in one go.
#
# The underlying TagParser tidies things up for you, so newline
# and space characters around data is removed automatically, so
# what you get passed into your handler is already cleaned up a bit.


import sys
import parsers.PathTagParser as Parser


# use curl URL > cars.xml to get this file.
URL = "http://data.nottinghamtravelwise.org.uk/parking.xml"
FILENAME = "cars.xml"

if len(sys.argv) > 1:
  FILENAME = sys.argv[1]


# This is the function that is called for each tag path in the xml file
def handlePath(path, value):
  print(path + " " + value)


# Enable this if you want the live data fetched every time you run  
#Parser.fetch(URL, FILENAME)


# This is the bit that parses the file and calls your handler
# with a path and a value, for each tag found in the file.

Parser.parse(FILENAME, handler=handlePath)

# END

