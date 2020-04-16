


from lark import Lark, Transformer

l = Lark('''
        ?start: location_path
                      
            location_path: relative_location_path | absolute_location_path
            absolute_location_path: "/" | "/" relative_location_path | abbreviated_absolute_location_path 
            relative_location_path: step | relative_location_path "/" step 
            step: axis_specifier node_test predicate* | abbreviated_step 
            axis_specifier: AXIS_NAME "::" | abbreviated_axis_specifier
            abbreviated_axis_specifier: "@"?
                
            string : WORD
                        
            AXIS_NAME: "ancestor" | "ancestor-or-self" | "attribute" | "child" | "descendant-or-self" 
                    | "descendant" | "following" | "following-sibling" | "namespace"	
                    | "parent" | "preceding" | "preceding-sibling" | "self"
                    
            node_test: NAME_TEST | NODE_TYPE "(" ")" 
            NODE_TYPE: "comment" | "text" | "processing-instruction" | "node"
            NAME_TEST: "*" | Q_NAME | NAME ":" "*"	
            
            
            abbreviated_absolute_location_path: "//" relative_location_path	
            abbreviated_relative_location_path: relative_location_path "//" step	
            abbreviated_step: "." | ".."
            
            predicate: "[" predicate_expr "]"	
            predicate_expr: expr
            
            number: digits ("." digits?)? | "." digits -> number
            digits: SIGNED_NUMBER -> number
            
            literal: "' WORD '"
            variable_reference: "$" Q_NAME
            Q_NAME: UNPREFIXED_NAME // | PrefixedName
            
            UNPREFIXED_NAME: NAME
            
            function_call: function_name "(" ( argument ( "," argument )* )? ")"
            function_name: Q_NAME
            argument: expr
             
            expr: union_expr //or_expr
            primary_expr: variable_reference | "(" expr ")" | literal | number | function_call
            
            or_expr: union_expr | or_expr "or" or_expr
            //and_expr: equality_expr | and_expr "and" equality_expr
            //equality_expr: relational_expr | equality_expr "=" relational_expr | equality_expr "!=" relational_expr
            //relational_expr: additive_expr | relational_expr "<" additive_expr | relational_expr ">" additive_expr 
            //            | relational_expr "<=" additive_expr | relational_expr ">=" additive_expr
            //additive_expr: multiplicative_expr | additive_expr "+" multiplicative_expr | additive_expr "-" multiplicative_expr
            //multiplicative_expr: unary_expr	 | multiplicative_expr MULTIPLY_OPERATOR unary_expr 
            //            | multiplicative_expr "div" unary_expr | multiplicative_expr "mod" unary_expr
            //unary_expr: union_expr | "-" unary_expr
            
            union_expr: path_expr | union_expr "|" path_expr
            path_expr: location_path | filter_expr | filter_expr "/" relative_location_path | filter_expr "//" relative_location_path
            filter_expr: primary_expr | filter_expr predicate	
            //...
            MULTIPLY_OPERATOR: "*"	
            
            NAME: NAME_START_CHAR NAME_CHAR*
            NAME_CHAR: NAME_START_CHAR | "-" | "." | "0".."9" | "#xB7" //| [#x0300-#x036F] | [#x203F-#x2040]
            NAME_START_CHAR: ":" 
                        | "A".."Z" | "_" | "a".."z" 
                        //| "#xC0".."#xD6" | "#xD8".."#xF6" 
                        //| "#xF8".."#x2FF" | "#x370".."#x37D" | "#x37F".."#x1FFF" 
                        // | [#x200C-#x200D] | [#x2070-#x218F] | [#x2C00-#x2FEF] | [#x3001-#xD7FF] | [#xF900-#xFDCF] | [#xFDF0-#xFFFD] | [#x10000-#xEFFFF]	
            %import common.ESCAPED_STRING
            %import common.SIGNED_NUMBER
            %import common.WS
            %import common.LETTER
            %import common.WORD
            
            %ignore WS
         ''', ambiguity="explicit", lexer='dynamic_complete')#, parser="lalr", lexer="contextual")

class Step:
    def __init__(self, node, axis="@"):
        self.node = node
        self.axis = axis

    def __str__(self):
        return "<Step %s>" % self.node
class Slash:
    pass
class DoubleSlash:
    pass

class XPathParser(Transformer):

    def __init__(self):
        self.literals = []
        self.functions = []
        self.nodes = []
        self.steps = []

    def location_path(self, args):
        return args[0]

    def abbreviated_axis_specifier(self, args):
        return ""

    def NAME_TEST(self, args):
        return args

    def node_test(self, args):
        # print(args)
        return args[0]  # args[0]

    def absolute_location_path(self, args):
        parsed = args[0]
        first = parsed[0]
        if isinstance(first, Slash):
            parsed[0] = DoubleSlash()
            return parsed

        return [Slash()] + args[0]

    def abbreviated_absolute_location_path(self, args):
        return [Slash()] + args[0]

    def relative_location_path(self, args):
        # print(args)
        if len(args) <= 1: # should only be 1
            return [args[0]]
        if len(args) == 2:
            return args[0] + [Slash(), args[1]]

    def step(self, args):
        nodename = str(args[1])
        self.steps.append(args[0])
        self.nodes.append(nodename)
        self.steps.append(Step(nodename, axis=args[0]))
        step = Step(nodename, axis=args[0])
        #print(self.steps)
        # print("s", len(args), args)
        return step


xp = '/descendant-or-self::node()/nodename_2'
print(xp)
p = l.parse(xp)
# print(XPathParser().transform(p).pretty())
for a in XPathParser().transform(p):
    print(a)
print("-----")


xp = "//nodenamex/self::*[/nodenamey | nodenamez]"
print(xp)
p = l.parse(xp)
# print(XPathParser().transform(p).pretty())
for a in XPathParser().transform(p):
    print(a)
print("-----")

print("---")
print(xp)
xp = 'descendant-or-self::node()'
p = l.parse(xp)
for a in XPathParser().transform(p):
    print(a)
print("-----")
