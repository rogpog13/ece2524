#!/usr/bin/env python

from sys import stdin, stdout, stderr
from sys import argv
import sys

string = sys.argv[1]
grade = sys.argv[2]
for line in stdin:
      if line.find(string) > -1:
         line = line[:-3]
         line = line + grade + "\n"       
      print line[:-1]


