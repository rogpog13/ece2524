#!/usr/bin/env python

def change_grade(argv):

   string = argv[1]
   grade = argv[2]
   for line in stdin:
       if line.find(string) > -1:
          line = line[:-3]
          line = line + grade + "\n"       
   print line[:-1]
   return


if __name__='__main__'
   from sys import stdin, stdout, stderr
   from sys import argv
   import sys

   change_grade(argv)
stdout.write('Done')
