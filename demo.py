import xmltodict
import json
import sys
with open("c642hiv_m030_sensor.xml") as fd :
    d = xmltodict.parse(fd.read())
    with open("demo.json", "w") as jf:
        json.dump(d, jf, indent = 2)
    print("xml to json complete")
    jf.close()


    with open("demo.json", "r") as jf:
        j = json.load(jf)
    xml_new = open("new.xml", "w")
    xml_new.write(xmltodict.unparse(j, pretty = True))
