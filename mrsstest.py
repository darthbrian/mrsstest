import os, datetime
import PyMediaRSS2Gen, PyRSS2Gen
import json

# Read in the JSON file
if not os.path.isfile('MSNIngest.json'):
    # error
    print("ERROR: Unable to find 'MSNIngest.json' file.")
else:
    with open('MSNIngest.json', mode='r', encoding='utf-8') as datajson:
        data = json.load(datajson)

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
                    guid = PyRSS2Gen.Guid(item['uniqueid']),
                    title = item['title'],
                    description = item['description'],
                    pubDate = item['pubdate'],
                    media_content=PyMediaRSS2Gen.MediaContent(
                        url=item['videourl'])
                )
        )

    mediaFeed.write_xml(open("rss2.xml", "w"))
