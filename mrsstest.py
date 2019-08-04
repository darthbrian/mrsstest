
import os, datetime
import PyMediaRSS2Gen, PyRSS2Gen
import json
from bs4 import BeautifulSoup

"""Create an MRSS file using the data gathered from the msningest project

Incoming data is stored in JSON format and is converted to an RSS file.

msningest project is located here: 
    https://github.com/darthbrian/msningest

This project uses both the PyRSS2Gen by Andrew Dalke and PyMediaRSS2Gen
    libraries by Dirk Weise.

PyRSS2Gen - http://www.dalkescientific.com/Python/PyRSS2Gen.html

PyMediaRSS2Gen - https://github.com/wedi/PyMediaRSS2Gen/
"""

# Check to see if the input JSON file exists
if not os.path.isfile('MSNIngest.json'):
    # ERROR: File Not Found
    print("ERROR: Unable to find 'MSNIngest.json' file.")
else:
    # Open the input JSON File
    with open('MSNIngest.json', mode='r', encoding='utf-8') as datajson:
        data = json.load(datajson)

    # Initialize the MediaRSS2Gen object
    mediaFeed = PyMediaRSS2Gen.MediaRSS2(
        title="Media Feed for Alexander Feldmann content",
        link="https://github.com/darthbrian/",
        description="This is a test feed for converting a JSON list of media to a MRSS format."
    )
    mediaFeed.copyright = "Copyright (c) 2019 Two Cool Guys Inc. All Rights Reserved."
    mediaFeed.lastBuildDate = datetime.datetime.now()

    # Need to build the mediaFeed.items list programmatically
    mediaFeed.items = []
    for item in data:
        mediaFeed.items.append(
                PyMediaRSS2Gen.MediaRSSItem(
                    guid = PyRSS2Gen.Guid(item['videourl']),
                    title = item['title'],
                    description = item['description'],
                    pubDate = item['pubdate'],
                    media_content=PyMediaRSS2Gen.MediaContent(
                        url=item['videourl'],type="video/mp4")
                )
        )

    # Write out the XML file
    mediaFeed.write_xml(open("rss2.xml", "w"))


    # Use BeauitfulSoup to make it readable
    bs = BeautifulSoup(open("rss2.xml"), "lxml-xml")
    prettyxml = bs.prettify()

    # Write out the pretty version
    with open('rss2.xml', mode='w', encoding='utf-8') as outfile:
        outfile.write(prettyxml)

