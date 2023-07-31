# xml2json
Convert XML to JSON with Python 3 and ElementTree

# Usage
```
$ ./xml2json.py -h
usage: xml2json.py [-h] [--out OUT] [infile]

Convert an XML file to JSON.

positional arguments:
  infile             xml file name ready to translate

optional arguments:
  -h, --help         show this help message and exit
  --out OUT, -o OUT  output json file name
```

# Examples
```sh
# without json file name
./xml2json.py sample_input.xml

# with json file name
./xml2json.py sample_input.xml out.json
```

# Conversion logic
Each element gets converted into an object of the form: 
`{tagName : {children} }`
`{tagName : text}`
## Note
namespace management is done by string substitution
# xml2json
