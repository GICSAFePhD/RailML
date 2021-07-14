#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure.Crossing import Crossing
from typing import List

class Crossings(object):
	def setCrossing(self, *aCrossing : Crossing):
		self._crossing = aCrossing

	def getCrossing(self) -> Crossing:
		return self._crossing

	def __init__(self):
		self._crossing : Crossing = None
		# @AssociationType Infrastructure.Crossing*
		# @AssociationMultiplicity 1..*

