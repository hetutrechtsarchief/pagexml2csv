#!/usr/bin/env python3
import sys,csv,argparse,codecs,re
import xml.etree.ElementTree as ET 

tags = []

def main(): 
  writer = csv.DictWriter(sys.stdout, fieldnames=["image","id","text","x","y","width","height"], quoting=csv.QUOTE_NONNUMERIC)
  writer.writeheader()
    
  for filename in sys.argv[1:]:
    with open(filename) as file:

      xmlstring = file.read()
      xmlstring = re.sub(r'\sxmlns="[^"]+"', '', xmlstring, count=1)
      xml = ET.fromstring(xmlstring) 
      items = []

      image = xml.find("Page").attrib["imageFilename"]

      for textline in xml.findall('.//TextLine'):

        item = {}

        item["id"] = textline.attrib["id"]

        item["image"] = image

        text = textline.find("./TextEquiv/Unicode")
        item["text"] = text.text if text!=None else ""

        coords = textline.find("./Coords")
        coords = coords.attrib["points"] if coords!=None else ""

        # split by space and comma
        coords = [coord.split(",") for coord in coords.split(" ")]

        # cast to int
        coords = [(int(float(a)), int(float(b))) for a,b in coords]

        # Usage example:
        bounds = BoundingBox(coords)

        item["x"] = bounds.minx
        item["y"] = bounds.miny
        item["width"] = bounds.width
        item["height"] = bounds.height

        writer.writerow(item)

class BoundingBox(object):
    """
    A 2D bounding box
    """
    def __init__(self, points):
        if len(points) == 0:
            raise ValueError("Can't compute bounding box of empty list")
        self.minx, self.miny = float("inf"), float("inf")
        self.maxx, self.maxy = float("-inf"), float("-inf")
        for x, y in points:
            self.minx = min(x,self.minx)
            self.maxx = max(x,self.maxx)
            self.miny = min(y,self.miny)
            self.maxy = max(y,self.maxy)

    @property
    def width(self):
        return self.maxx - self.minx
    @property
    def height(self):
        return self.maxy - self.miny
    def __repr__(self):
        return "BoundingBox(minX={}, minY={}, maxX={}, maxY={})".format(
            self.minx, self.miny, self.maxx, self.maxy)


if __name__ == "__main__": 
  main() 
