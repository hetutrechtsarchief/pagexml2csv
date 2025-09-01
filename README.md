# PageXML to CSV 

Simple Python script to extract TextLine data from PageXML files.

For a more complete implementation checkout [py-pagexml](https://omni-us.github.io/pagexml/py-pagexml/): Python wrapper for the PageXML C++ library.
Or [pagexml-tools](https://github.com/knaw-huc/pagexml) by KNAW for PageXML-tools contains functions for parsing and for a range of analysis tasks.


## input
```xml
        
<TextRegion orientation="0.0" id="r2" custom="readingOrder {index:1;}">
    <Coords points="412,512 412,2021 520,2021 520,512"/>
    <TextLine id="r2l2" custom="readingOrder {index:1;}">
        <Coords points="444,688 470,688 496,692 496,619 470,615 444,615"/>
        <Baseline points="444,664 470,664 496,668"/>
        <TextEquiv>
            <Unicode>3 kinderen</Unicode>
        </TextEquiv>
    </TextLine>
```

## output
```csv
"image","id","text","x","y","width","height"
"NL-UtHUA_650_101_000181.jpg","r_1_1l1","Aantal kinderen:",87,327,377,77
...
```
