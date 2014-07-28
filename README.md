pyparsers
=========

Python Parsers for XML and other tagged data formats


Here is a collection of parsers that can be used to parse various
file formats - for example if you want to read and process live
data sets from the internet.


Most of this is work in progress, but the XML parser is the most
mature of the pieces of code. Try out the CarPark demo first
to show how you can easily fetch live data from an external
data source on the internet, and perform some processing on that
data.


The parsers in this package use a technique I developed many years
ago to simplify parsing structured data, called "path parsing".
This turns each collection of tags into a path a bit like a
directory path, so the xml tags <record> then <field> then <value>
would have a path of /record/field/value/


These paths are then fed with their associated values into a single
function that you provide, which can choose which paths to process
and which paths to filter out. It's a very powerful technique that
I have built many products using.


I will add more documentation, more examples, and more parsers
over the coming weeks, so do follow this repo and look out for
new code as I test and document it. (I've got more code in the
wings, but I've only released in public form the parts that I think
are most useful to other people at this stage).


David Whale
@whaleygeek
July 2014

