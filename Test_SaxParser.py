# Test_SaxParser.py  (c) 2014  D.J.Whale
#
# The SAXP interface (simple api for xml processing) is event based
# and needs a separate parser and a handler. This is a small example
# of how you would wire this up.
#
# The other examples in this folder use various helper modules to
# make the processing of XML or other tagged data simpler, as SAX
# still leaves a lot of work up to you to do.

import sys
import xml.sax

class EventHandler(xml.sax.ContentHandler):
  def startElement(self,name,attrs):
    print("start:" + name + " " + str(attrs._attrs))
      
  def characters(self,text):
    print("chars:" + text)
      
  def endElement(self,name):
    print("end:" + name)


FILENAME = "cars.xml"
if len(sys.argv) > 1:
  FILENAME = sys.argv[1]

xml.sax.parse(FILENAME, EventHandler())

# END
