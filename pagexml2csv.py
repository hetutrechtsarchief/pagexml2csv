#!/usr/local/bin/python3
import sys,csv,argparse,codecs,re
import xml.etree.ElementTree as ET 

def main(): 
  argparser = argparse.ArgumentParser(description='PageXML TextLines to CSV') 
  argparser.add_argument('infile', default=sys.stdin, type=argparse.FileType('r', encoding="utf-8"), nargs='?')
  argparser.add_argument('outfile', default=sys.stdout, type=argparse.FileType('w', encoding="utf-8"), nargs='?')
  args = argparser.parse_args()

  with args.infile as file:

    xmlstring = file.read()
    xmlstring = re.sub(r'\sxmlns="[^"]+"', '', xmlstring, count=1)
    xml = ET.fromstring(xmlstring) 
    items = []

    for textline in xml.findall("./Page/TextRegion/TextLine"):

      item = {}
      item["id"] = textline.attrib["id"]

      text = textline.find("./TextEquiv/Unicode")
      item["text"] = text.text if text!=None else ""

      coords = textline.find("./Coords")
      item["coords"] = coords.attrib["points"] if coords!=None else ""

      baseline = textline.find("./Baseline")
      item["baseline"] = baseline.attrib["points"] if baseline!=None else ""

      items.append(item)

    writer = csv.DictWriter(args.outfile, fieldnames=["id","text","coords","baseline"], delimiter=',', quoting=csv.QUOTE_ALL, dialect='excel')
    writer.writeheader()
    writer.writerows(items)


if __name__ == "__main__": 
  main() 
