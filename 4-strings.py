## Strings

## Strings can be delimited by single or double quotation marks (but the quotes
## have to match):
single_quoted_string = 'data science'
double_quoted_string = "data science"
## Python uses backslashes to encode special characters. For example:
tab_string = "\t"
 # represents the tab character
len(tab_string)
 # is 1
## If you want backslashes as backslashes (which you might in Windows directory
## names or in regular expressions), you can create raw strings using r"":
not_tab_string = r"\t"
 # represents the characters '\' and 't'
len(not_tab_string)
 # is 2
## You can create multiline strings using triple-[double-]-quotes:
multi_line_string = """This is the first line.
and this is the second line
and this is the third line"""
print multi_line_string
