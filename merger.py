'''
Created on Dec 6, 2015

@author: amnon
'''

import sys
import os

def usage():
    print 'Usage: merger [root-search]', 
    

class Dir:
    """ holds information about specific directory"""
    def __init__(self, subdir, dirs, files, tree):
        self.set(subdir, dirs, files, tree)

    def set(self, root, dirs, files, tree):
        self.full_name = os.path.abspath(root).rstrip(os.sep)
        self.short_name = os.path.basename(self.full_name)
        self.dirs = dirs[:]
        self.files = files[:]
        self.parent =  os.path.dirname(self.full_name)
        if self.parent not in tree:
            self.parent = None
        tree[self.full_name] = self

    def pr(self):
        print self.full_name, self.short_name, self.dep

    def lst(self):
        print "root", self.full_name
        print "files:"
        for f in self.files:
            print f
        print "dirs:"
        for d in self.dirs:
            print d
        
    def contain(self, d):
        """ check if a directory contains directory"""
        return False
    
if len(sys.argv) < 2:
    usage()
    exit()

def build_tree(root, tree):
    for subdir, dirs, files in os.walk(root):
        Dir(subdir, dirs, files, tree)

tree = {}
build_tree(sys.argv[1], tree)

tree[tree.keys()[4]].lst()