#!/usr/bin/env python2.7
# encoding=utf-8
import ast


class Translator(ast.NodeVisitor):

  def __init__(self):
    self.translation = ""
    return super(Translator, self).__init__()

  def translate(self, stream):
    tree = ast.parse(stream)
    self.visit(tree)
    return self.translation

  def visit_FunctionDef(self, stmt):
    # Acá hacemos la traducción del stmt "def fun (args, kwargs): [stmts, ]"
    return self.generic_visit(stmt)


if __name__ == '__main__':
  import sys
  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument("-f", "--file", action="store", help="File to translate")
  parser.add_argument('infile', nargs='?', type=argparse.FileType('r'),
                      default=sys.stdin, help="Stream to translate") # Support for calling with <, |

  args = parser.parse_args()
  if args.file:
    try:
      args.infile = open(args.file, 'r')
    except IOError:
      error = "Error: can't find file with name %s\n" % (args.file)
      # sys.stderr.write(error)
      sys.exit(error)

  stream = args.infile.read()
  visitor = Translator()
  print visitor.translate(stream)


