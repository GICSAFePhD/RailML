#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import Line
from typing import List

class Lines(object):
	@property
	def Line(self) -> Line:
		return self.___line
	
	@Line.setter
	def Line(self, aLine : Line):
		self.___line = aLine

	def __init__(self):
		self.___line : Line = Line.Line()
		# @AssociationType Infrastructure.Line*
		# @AssociationMultiplicity 1..*

