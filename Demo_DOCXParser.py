import sys
from parsers.PathTagTableParser import PathTagTableParser #the class, not the module
##import re
##from generators import XML
##from dictgen import DictCollector


FILENAME = "../testdata/word/document.xml"
if len(sys.argv) > 1:
  FILENAME = sys.argv[1]


#----- DOCXParser -------------------------------------------------------------

class DOCXParser(PathTagTableParser):

  def __init__(self):
    table = [
      #TESTING
      ##(re.compile("^/w:document/w:body/w:tbl/w:tr/w:tc/w:p/w:r/w:t/$"), self.emitContent),
      ##(re.compile("^/w:document/w:body/w:tbl/w:tr/w:tc/w:p/w:pPr/w:pStyle/w:val$"), self.emitStyle),

      # start of document
      ("/w:document",  self.xmlStart),

      # start of a table cell
      ("/w:document/w:body/w:tbl/w:tr/w:tc", self.tableCellStart),

      # body of a table cell (style if in column 1)
      ("/w:document/w:body/w:tbl/w:tr/w:tc/w:p/w:r/w:t/", self.leftStyle),

      # a right hand column style setter, if in column 2
      ("/w:document/w:body/w:tbl/w:tr/w:tc/w:p/w:pPr/w:pStyle/w:val=", self.setStyle, (DOCXParser.STOP,)),

      # end of a table row
      ("/w:document/w:body/w:tbl/w:tr~", self.tableRowEnd),

      # content
      (PathTagTableParser.EVERYTHING,  self.emitXML)
    ]
    PathTagTableParser.__init__(self, table)
    ##self.xmlgen = XML.XMLGenerator()
    self.styles = []
    self.styleName = None
    self.column = 0

  def xmlStart(self, path, value):
    print("<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>")

  def emit(self, path, value):
    print("%s %s" % (path, value))

  def emitValue(self, path, value):
    print(value)

  def tableCellStart(self, path, value):
    self.column += 1

  def leftStyle(self, path, value):
    if self.column == 1:
      self.styleName = value
      if not value in self.styles:
        self.styles.append(value)

  def setStyle(self, path, value):
    if self.column == 2:
      value = self.styleName
    self.emitXML(path, value)


  def tableRowEnd(self, path, value):
    self.column = 0
    self.styleName = None

  def emitXML(self, path, value):
    pass ## self.xmlgen.emit_xml(path, value)

  def get_styles(self):
    return self.styles


#----- MAIN -------------------------------------------------------------------

if __name__ == "__main__":
  # classify all tags
  #TagClassifier.parse(FILENAME)

  # Read and process the data
  dp = DOCXParser()
  dp.parse(FILENAME)

  # Dump any final stats for xml
  #print('*' * 80)
  #print("STYLESHEET ENTRIES")
  #for s in sorted(dp.get_styles()):
  #  print(s)

# END


