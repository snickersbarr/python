#!/usr/bin/python

import random
from urllib import urlopen
import sys

WORD_URL = "http://learnpythonthehardway.org/words.txt"
WORDS = []

PHRASES = {
	"class %%%%(%%%%)" :
		"Make a clas named %%%% that is-a %%%%",
	"class %%%%(object):\tdef __init__(self, ***)" :
		"class %%%% has-a __init__ that takes self and *** parameters.",
	"clas %%%%(objecT):\n\t def ***(self, @@@)" :
}