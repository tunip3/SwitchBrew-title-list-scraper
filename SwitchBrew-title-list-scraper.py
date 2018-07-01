"""Test the wikitablescrape script on four articles."""

import os
import shutil

import wikitablescrape

# Delete previous output folder if it exists, then create a new one
try:
    os.remove('TitleID/TitleID.csv')
except:
    pass

wikitablescrape.scrape(
    url="http://switchbrew.org/index.php?title=Title_list/Games",
    output_name="TitleID"
)

print ("done, feel free to exit")
