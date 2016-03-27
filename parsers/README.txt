Notes about the internal architecture of these parsers:

These parsers are designed to be stream based and interchangeable.


STREAM BASED

By being stream based, the memory requirements required to process an arbitrarily
large stream of data are limited to the maximum depth of a single hierarchy.
i.e. if you have a hierarchy of ONE/TWO/THREE and 1 record, or 1 billion records,
the memory overhead for the 1 record and 1 billion record versions of the data
are identical. This means that parsing can scale to any number of records.


INTERCHANGEABLE

The 'path' abstraction used here, builds up a string path that describes the
hierarchy as a single string. The root character / marks the start of the hierarchy.
The first tag or attribute under that follows the root, and nested tags or attributes
follow that, again separated by a path separator character.

So, if you have an XML file with a <REC> tag, and inside that a <NAME> tag, and inside
that a TYPE attribute, your path will be: /REC/NAME/TYPE

Paths are also symetrical, so you can sense entry into a path and exit from a path
should you wish to run code at the top and tail of particular structures, e.g.

/REC/NAME/    <- perform entry processing here
/REC/NAME/~   <- perform exit processing here.

Paths and any values are passed into a user supplied handler function,
and you can choose to filter and handle those paths and their associated values
any way you want.


TOOLS

There are additional tools you may find useful

Classifier - run this over any data source to get a dump of unique paths and counts.
Useful for classifying an existing data source before writing your application code.

Handler - a generic handler that takes a table of paths, with functions to call


ARCHITECTURE

The internal architecture of this code is likely to change significantly, due
to the requirement to be able to transparrently parse XML, HTML and JSON using
the same path based structure. Much of the innovations that I have in my
(currently closed source) PHP and Java implementations need to be rationalised
into this codebase. The plan is that any heirarchical data source could be
parsed with a specific parser, and offered to the application as a series of
path handler callbacks.

In doing this, I propose that each parser will be developed as a standalone
entity in another repo, and the code for the runtime parser imported into
this repo and wrapped with the path parser concept.


HERITAGE

I had the original idea for path parsers in around 2000, when I was writing a lot
of XML parsers for webapps, and realised that there was always a lot of mucky
wiring up code that seemed to be mostly the same. 

Around 2010 I developed the idea into it's first standalone form inside a PHP web application for parsing large streams of XML data from a Web API. That code is not (yet) open sourced.

Around 2012 I developed some Java based versions that parsed XML and also JSON.

Around 2014 when doing some research for a 'live data' chapter in my book,
I found the Nottingham Car Parks XML data feed, and decided this would be a useful
scheme to port to Python, and open sourced some demo code in this Repo which
still stands today. I never used this in my book in the end.

In 2016 when looking at the weather station feeds that Jim Darby at Oracle has
started to publish from the Raspberry Pi weather station code, I decided it might
be worth porting my Java based JSON parsers into Python, as a way to process large
streams of JSON weather data efficiently in Python.

David Whale
@whaleygeek
March 2016


