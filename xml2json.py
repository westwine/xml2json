#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import sys
import argparse
import re

parser = argparse.ArgumentParser(description = 'Convert an XML file to JSON.')
parser.add_argument('infile', nargs='?', type = argparse.FileType('rt'), 
                    help = 'xml file name ready to translate',
                    default=sys.stdin)
parser.add_argument('--out', '-o',
                    help = 'output json file name',
                    default='out.json')                   


def xml_element_to_dict(elem):
    "Convert XML Element to a simple dict"
    # inner = dict(elem.attrib)
    inner = {}
    text = elem.text and elem.text.strip()
    if text :
        if text.isdigit() :
            text = int(text, 10)
        elif len(text.split("0x")) > 1 :
            # text = eval(text)
            # text.strip('"')
            text.replace('/"', '')
            
        if inner or len(elem) :
            inner['value'] = text
        else :
            return text

    for child in elem :
        value = xml_element_to_dict(child)
        if child.attrib and 'name' in child.attrib :
            child.tag = child.attrib['name']
        try :
            # add to existing list for this tag
            inner[child.tag].append(value)
        except AttributeError :
            # turn existing entry into a list
            inner[child.tag] = [inner[child.tag], value]
        except KeyError :
            # add a new non-list entry
            inner[child.tag] = value

    return inner

def register_all_namespaces(filename):
    namespaces = dict([node for _, node in ElementTree.iterparse(filename, events=['start-ns'])])
    for ns in namespaces:
        ElementTree.register_namespace(ns, namespaces[ns])

def name_replace(output, dictionary) :
    for key, value in dictionary.items() :
        output = re.sub(r'"%s":'%key, r'"%s":'%value, output)
    return output

def main(args):
    "Dump JSON-from-parsed-XML to stdout"
    # register_all_namespaces(args.infile)
    xml_parser = ElementTree.parse(args.infile)
    root = xml_parser.getroot()
    # json.dump({root.tag : xml_element_to_dict(root)}, sys.stdout, indent=2)
    out = open(args.out, 'w+')
    # json.dump({root.tag : xml_element_to_dict(root)}, out, indent=2)
    output = json.dumps({root.tag : xml_element_to_dict(root)}, indent=2)
    # output = re.sub(r'"0x(.+)"', r'0x\1', output)
    output = name_replace(output, dictionary = {"powerSetting" : "setting"})
    out.write(output)
    print("conversion complete")


if __name__ == '__main__':
    args = parser.parse_args()
    import xml.etree.cElementTree as ElementTree
    main(args)
