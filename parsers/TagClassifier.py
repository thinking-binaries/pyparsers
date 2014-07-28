# TagClassifier  10/04/2014  D.J.Whale
#
# Run a file through the classifier to get a dump of
# all the tags it uses, in a helpful indexed form.
# This is useful for "analysing" a data source to see what
# type of data it actually contains.

from .TagParser import TagParser
from .PathTagParser import PathTagParser
import sys

class TagClassifier(PathTagParser):
#class TagClassifier(TagParser):
  pathorder = []
  paths = {}
  
  def __init__(self):
    pass
    
  def handle(self, path, data):
    #print(path + ": " + data)
    if not self.paths.has_key(path):
      self.pathorder.append(path)
      self.paths[path] = [data]
    else:
      self.paths[path].append(data)
      
  def getPaths(self):
    return self.paths
  
  def getPathOrder(self):
    return self.pathorder
 
# non object-oriented test interface

def showPaths(paths, pathOrder):
  pindex = 0
  for path in pathOrder:
    pathdata = paths[path]
    numdata = len(pathdata)
    iindex = 0
    print("[" + str(pindex) + "] " + path + ":" + str(numdata))
    for data in pathdata:
      if data != None:
        tdata = data.strip()
        if len(tdata) > 0:
          print("  [" + str(iindex) + "] " + data)
        iindex += 1
    pindex += 1

def parse(filename):
  c = TagClassifier()
  c.parse(filename)
  
  paths = c.getPaths()
  pathOrder = c.getPathOrder()
  showPaths(paths, pathOrder)
  
#END


