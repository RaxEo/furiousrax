#Python code to illustrate parsing of XML files 
# importing the required modules
"""
XML parsing in Python
This article focuses on how one can parse a given XML file and extract some useful data out
of it in a structured way.

XML: XML stands for eXtensible Markup Language. It was designed to store and transport data.
It was designed to be both human- and machine-readable.That’s why, the design goals of XML
emphasize simplicity, generality, and usability across the Internet.
The XML file to be parsed in this tutorial is actually a RSS feed.

RSS: RSS(Rich Site Summary, often called Really Simple Syndication) uses a family of
standard web feed formats to publish frequently updated information like blog entries,
news headlines, audio, video. RSS is XML formatted plain text.

The RSS format itself is relatively easy to read both by automated processes and by humans
alike.The RSS processed in this tutorial is the RSS feed of top news stories from a popular
news website. You can check it out here. Our goal is to process this RSS feed (or XML file)
and save it in some other format for future use.
Python Module used: This article will focus on using inbuilt xml module in python for parsing
XML and the main focus will be on the ElementTree XML API of this module.
"""

import csv 
import requests 
import xml.etree.ElementTree as ET 

def loadRSS():
    # url of rss feed 
    url = 'https://www.w3schools.com/xml/simple.xml'

    # creating HTTP response object from given url 
    resp = requests.get(url) 

    # saving the xml file 
    with open('topnewsfeed.xml', 'wb') as f: 
        f.write(resp.content) 
        

def parseXML(xmlfile): 

    # create element tree object 
    tree = ET.parse(xmlfile) 

    # get root element 
    root = tree.getroot() 

    # create empty list for news items 
    newsitems = [] 

    # iterate child elements of item 
    for item in root.findall('./food'):
  
        # empty news dictionary
        news = {}
  
        # iterate child elements of item
        for child in item:
            news[child.tag] = child.text.encode('utf8')
  
        # append news dictionary to news items list
        newsitems.append(news)
      
    # return news items list
    return newsitems


def savetoCSV(newsitems, filename): 

    # specifying the fields for csv file 
    fields = ['name','price', 'description', 'calories'] 

    # writing to csv file 
    with open(filename, 'w') as csvfile: 

        # creating a csv dict writer object 
        writer = csv.DictWriter(csvfile, fieldnames = fields) 

        # writing headers (field names) 
        writer.writeheader() 

        # writing data rows 
        writer.writerows(newsitems) 

    
def main(): 
    # load rss from web to update existing xml file 
    loadRSS() 

    # parse xml file 
    newsitems = parseXML('topnewsfeed.xml') 
    print(newsitems)
    # store news items in a csv file 
    savetoCSV(newsitems, 'topnews.csv') 
    
    
if __name__ == "__main__": 

    # calling main function 
    main() 
