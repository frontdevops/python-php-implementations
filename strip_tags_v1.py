import re

"""Compile regex for best performance"""
pattern = re.compile('<[^<]+?>')

def strip_tags(html):
  """
  Variant 1 with regex
  """
  return pattern.sub('', html)

