#!/usr/bin/python
import re

def union(x, y):
	union = x.copy()
	for i in y:
		if(i not in x):
			union.append(i)
	union.sort()
	return union

def intersection(x, y):
	inter = []
	for i in y:
		if(i in x):
			inter.append(i)
	inter.sort()
	return inter

