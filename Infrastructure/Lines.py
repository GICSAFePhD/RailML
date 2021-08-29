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

	def create_Line(self):
		if self.Line == None:
			self.Line = []
		self.Line.append(Line.Line())

	def __init__(self):
		self.___line : Line = None
		# @AssociationType Infrastructure.Line*
		# @AssociationMultiplicity 1..*

