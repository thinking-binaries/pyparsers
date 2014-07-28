# TagParser.py  10/04/2014  D.J.Whale
#
# A Tag Parser that uses a SAX based xml event parser.
# Note that the parser and the event handler are wrapped into
# a single class, which makes it easier to explain and use to
# beginners. Attributes and values are passed as strings, maps,
# lists, which is not as efficient and flexible as the standard
# SAX Impl interfaces, but it is simpler to explain and understand,
# especially to children.

import xml.sax

def trace(msg):
  print(msg)

def error(msg):
  print("ERROR:" + msg)


class TagParser:
  
  def parse(self, inFileName):
    #trace("parse:" + inFileName)
    class EventHandler(xml.sax.ContentHandler):
      def __init__(self, parent):
        self.parent = parent
        self.databuffer = None

      def flushdata(self):
        if self.databuffer != None:
          #trace("flushdata")
          # we have some chars collected, notify our client
          buf = self.databuffer.strip()
          if len(buf) > 0:
            self.parent.data(buf)
          self.databuffer = None
                
      def startElement(self, name, attrs):
        #trace("start:" + name)
        self.flushdata()
        attrmap = None # default if no attrs
        count = attrs.getLength()
        if count > 0:
          attrmap = {}
          for attrname in attrs.getNames():
            attrvalue = attrs.get(attrname)
            attrmap[attrname] = attrvalue
        self.parent.tagStart(name, attrmap)
        
      def characters(self, text):
        #trace("chars:" + text)
        if self.databuffer == None:
          self.databuffer = text
        else:
          self.databuffer += text
        
      def endElement(self, name):
        #trace("end:" + name)
        self.flushdata()
        self.parent.tagEnd(name)

    xml.sax.parse(inFileName, EventHandler(self))

    
  # THIS IS THE SAXP INTERFACE TO OVERRIDE
  def tagStart(self, tag, attr):
    trace("tagstart:" + tag)
    if attr != None:
      trace("  attrs:" + str(attr))
    
  def tagEnd(self, tag):
    trace("tagend:" + tag)
    
  def data(self, data):
    trace("data:" + data)


# non object-oriented test interface

def parse(filename):
  """Just prints what it finds"""
  p = TagParser()
  p.parse(filename)  
       
  
#END

  
  
  
  
  
