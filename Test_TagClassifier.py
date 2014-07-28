# Test_TagClassifier.py  (c) 2014  D.J.Whale
#
# A TagClassifier scans any XML or tagged file and creates
# a useful indexed dump of data that it finds. This is a
# useful way to see the structure and content of a tagged
# file like XML in a more human readable form, especially
# useful if you are about to write a program that processes
# that data.

import sys
import parsers.TagClassifier as TagClassifier
  
# SIMPLE TEST HARNESS

FILENAME = "cars.xml"
if len(sys.argv) > 1:
  FILENAME = sys.argv[1]
  
TagClassifier.parse(FILENAME)
  
#END
