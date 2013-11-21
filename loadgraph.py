#!/usr/bin/python
# loadgraph.py

import os
import sys
import numpy as np
import argparse

def loadgraph(fn):
  """
  Load a numpy-saved graph from disk

  @param fn: the file path and name of the saved graph
  @return: the loaded sparse csc scipy matrix
  """
  assert os.path.exists(fn), "The specified file path: %s does not exist" % str(fn)
  return np.load(fn).item()  

def test(fn):
  g = loadgraph(fn)
  (a,b) = g.shape
  for x in range(a):
    line = str(x) +  ' "' + str(x) + '" '
    l = len(line)
    for y in range(x,b):
      z = g[x,y]
      if z != 0:
        line += str(y) + ' '
    if l < len(line):
      print line
  print "Printing graph sample ...\n", g[0:a,0:a].todense()

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Read Numpy-saved graph from file")
  parser.add_argument("filename", action="store", help="File name of graph")
  
  result = parser.parse_args()
  test(result.filename)
