# PathTagParser.py  10/04/2014  D.J.Whale
#
# Based on ideas from around 2008
# Turn tags into hierarchical paths, for event filtering and processing

import os
from .TagParser import TagParser

def trace(msg):
  print(msg)

def error(msg):
  print("ERROR:" + msg)

    
class PathTagParser(TagParser):
  PATH_SEPARATOR = '/'
  ATTRIBUTE      = '='
  END_TAG        = '~'

  stack = []

  def __init__(self):
    TagParser.__init__(self)

  def topath(self):
    p = ""
    for i in self.stack:
      p = p + self.PATH_SEPARATOR + i
    return p
    
  def tagStart(self, tag, attrs):
    #trace("{" + tag)
    self.stack.append(tag)
    path = self.topath()
    self.handle(path, "") ##NODE/TAG
    if attrs != None:
      for attr in attrs:
        self.handle(path + self.PATH_SEPARATOR + attr + self.ATTRIBUTE, attrs[attr]) ##ATTRIBUTE
    
  def tagEnd(self, tag):
    #trace("}" + tag)
    self.handle(self.topath() + self.END_TAG, "") ##NODE/TAG
    if len(self.stack) > 0:
      top = self.stack[-1]
      if top == tag:
        self.stack.pop()
      else:
        error("MISMATCH: found:" + tag + " stack:" + top)
        self._popto(tag)
    else:
      error("STACK UNDERFLOW")
    
  def _popto(self, tag):
    # search back through stack to see if there is a tag
    for i in range(-1,-(len(self.stack)+1),-1):
      #print(str(i) + "=" + self.stack[i])
      if self.stack[i] == tag:
        #print("found at:" + str(i))
        for j in range(-i):
          popped = self.stack.pop()
          #print("popped:" + str(j) + "=" + popped)
        break
    
  def data(self, data):
    self.handle(self.topath() + self.PATH_SEPARATOR, data) ##DATA

  def setpath(self, path):
    #trace("SETPATH:" + path)
    parts = path.split(self.PATH_SEPARATOR)
    #for p in parts:
    #  trace(p)
    self.stack = parts
    
  # THIS IS THE HANDLER INTERFACE TO OVERRIDE
  def handle(self, path, data):
    if data == None:
      data = ""
    trace(path + "=" + data)


# non object-oriented simple interface

def fetch(url, filename):
  #os.system("wget -O " + filename + " " + url)
  print("warning:wget fetch disabled in PathTagParser")

def parse(filename, handler=None):
  """handler(path, data) must be provided by user"""
  if handler == None:
    # Default handling just prints paths
    p = PathTagParser()
    p.parse(filename)
  else:  
    # Knit up a temporary parser sub class to the user handler
    class MyParser(PathTagParser):
      def __init__(self, handler):
        self.handler = handler
        
      def handle(self, path, data):
        if data == None:
          data = ""
        self.handler(path, data)

    # Call the parser to parse the file, the wrapper class above then
    # dispatches all paths to the user provided function.
    p = MyParser(handler)
    p.parse(filename)
    
#END

  
  
  
  
  
