import xml.etree.ElementTree as ET
from collections import OrderedDict

# 1. LRUCache Provider
class LRUCache:
    def __init__(self, capacity=128):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return None
        self.cache.move_to_end(key) 
        return self.cache[key]
    
    def set(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

    def has(self, key):
        return key in self.cache
    
# 2. SSML Parser: converts SSML string to XML node tree
def parseSSML(ssml_input):
    try:
        root = ET.fromstring(ssml_input)
        return root
    except ET.ParseError as e:
        raise ValueError(f"Invalid SSML format: {e}")

# 3. SSML Node to Text
def ssmlNodeToText(node):
    text = node.text or ""
    for child in node:
        text += ssmlNodeToText(child)
        if child.tail:
            text += child.tail
    return text.strip()

# ------- Sample usage ----------
if __name__ == "__main__":
    # LRUCache Test

    #import textwrap 

    cache = LRUCache(capacity=2)
    cache.set("a", 1)
    cache.set("b", 2)
    print("Get 'a' :", cache.get("a"))
    cache.set("c",3)
    print("has 'b':", cache.has("b"))

    ssml_string = '<speak>Hello,this is <emphasis level="strong">SSML</emphasis>!</speak>'
    ssml_tree = parseSSML(ssml_string)
    plain_text = ssmlNodeToText(ssml_tree)
    print("Extracted Text:", plain_text)