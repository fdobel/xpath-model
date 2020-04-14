# see https://www.w3.org/TR/1999/REC-xpath-19991116/

# axes

#  descendant-or-self
#  preceding
#  * => all element children
# node tests

# predicates


# node types
# root node
# element nodes
# text nodes
# attribute nodes
# namespace nodes

# Location paths
DOCUMENT_ROOT = "/"

# 2.5 abbreviated syntax
ELEMENT_CHILDREN_ABBREV = "*"
SELF_ABBREV = "."
DESCENDANTS_ABBREV = "//"
# 4.2 String Functions
#Function: string string(object?)
#Function: string concat(string, string, string*)
#Function: boolean starts-with(string, string)
#Function: boolean contains(string, string)
CONTAINS_N = "contains"
def contains_n(a, b):
    return "contains(%s, '%s')" % (a, b)
#Function: string substring-before(string, string)
#Function: string substring-after(string, string)
#Function: string substring(string, number, number?)
#Function: number string-length(string?)
#Function: string normalize-space(string?)
#Function: string translate(string, string, string)

