# PathTagTableParser.py  26/10/2017  D.J.Whale
#
# Based on ideas from around 2008
# A table-configured parser.
# Provide paths (strings or regexps) that map to handlers.

from . import PathTagParser


#----- PathTagTableParser -----------------------------------------------------

class PathTagTableParser():
  EVERYTHING = ""     # global matcher pattern for strings
  STOP       = "stop" # stop processing when rule has fired

  def __init__(self, table=None):
    if table is not None:
      if isinstance(table, dict):
        raise RuntimeError("Must now use a list for the table")
      self.table = table
    else:
      self.table = []

  def parse(self, filename):
    PathTagParser.parse(filename, handler=self.handle)

  def handle(self, path, data):
    # process each tuple in the table list in turn
    # (pattern, handler, optional flags)

    for rule in self.table:
      pattern = rule[0]
      handler = rule[1]
      if len(rule) > 2:
        flags = rule[2]
      else:
        flags = ()

      if pattern == self.EVERYTHING:
        handler(path, data)

      if isinstance(pattern, str):
        if pattern == path:
          handler(path, data)
          if self.STOP in flags:
            ##print("\n\n str ****STOP")
            return

      else: # must be a regexp
        ##print("regexp %s %s" % (pattern.pattern, path))
        result = pattern.match(path)
        if result is not None:
          ##bits = result.group()
          handler(path, data)
          if self.STOP in flags:
            ##print("\n\n re ****STOP")
            return


# non object oriented, module level convenience interface

EVERYTHING = PathTagTableParser.EVERYTHING

def parse(filename, table):
  p = PathTagTableParser(table)
  p.parse(filename)

# END
