# Test_TagParser.py  (c) 2014  D.J.Whale
#
# A TagParser is a helper for SAXP (Simple Api For XML Processing)
# that makes it much easier to use for beginners.
# Just call the parse() method to parse a file.
#
# See other test and demo programs in this folder to find out
# how to actually process data using a TagParser

import sys
import parsers.TagParser as TagParser

FILENAME = "cars.xml"
if len(sys.argv) > 1:
  FILENAME = sys.argv[1]
  
TagParser.parse(FILENAME)

# END
