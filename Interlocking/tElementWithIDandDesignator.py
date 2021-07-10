#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Common import Designator
from Common import tElementWithID
from typing import List

class tElementWithIDandDesignator(tElementWithID):
	def setDesignator(self, aDesignator : Designator):
		self._designator = aDesignator

	def getDesignator(self) -> Designator:
		return self._designator

	def __init__(self):
		self._designator : Designator = None
		# @AssociationType Common.Designator
		# @AssociationMultiplicity 0..1
		# """The designator of the element, which is often a coded identification, e.g. 69W03 for a switch no. 03 in station 69. In case of "private" register use leading underscore."""

