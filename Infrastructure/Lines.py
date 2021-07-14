#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure.Line import Line
from typing import List

class Lines(object):
	def setLine(self, *aLine : Line):
		self._line = aLine

	def getLine(self) -> Line:
		return self._line

	def __init__(self):
		self._line : Line = None
		# @AssociationType Infrastructure.Line*
		# @AssociationMultiplicity 1..*

