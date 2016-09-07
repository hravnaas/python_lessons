import re

def get_matching_words(regex):
 words = ["aimlessness", "assassin", "baby", "beekeeper", "belladonna", "cannonball", "crybaby", "denver", "embraceable",
 "facetious", "flashbulb", "gaslight", "hobgoblin", "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress",
 "millennia", "natural", "obsessive", "paranoia", "queen", "rabble", "reabsorb", "sacrilegious", "schoolroom",
 "tabby", "tabloid", "unbearable", "union", "videotape"]

 return [word for word in words if re.search(regex, word)]

# 1. All words that contain a "v"
print "1:"
print get_matching_words(r"y")

# 2. All words that contain a double-"s"
print "2:"
print get_matching_words(r"ss")

# 3. All words that end with an "e"
print "3:"
print get_matching_words(r'e$')

# 4. All words that contain an "b", any character, then another "b"
print "4:"
print get_matching_words(r"b.b")

# 5. All words that contain an "b", at least one character, then another "b"
print "5:"
print get_matching_words(r"b.+b")

# 6. All words that contain an "b", any number of characters (including zero), then another "b"
print "6:"
print get_matching_words(r"b*b")

# 7. All words that include all five vowels in order
print "7:"
print get_matching_words(r"aeiou")

# 8. All words that only use the letters in "regular expression" (each letter can appear any number of times)
print "8: Not correct"
print get_matching_words(r"[regulaxpsion]")

# 9. All words that contain a double letter
print "9:"
print get_matching_words(r"([a-zA-Z])\1+")