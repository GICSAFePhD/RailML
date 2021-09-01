#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import Designator, tElementWithID
from typing import List

class tElementWithIDandDesignator(tElementWithID.tElementWithID):
	@property
	def Designator(self) -> Designator:
		return self.___designator

	@Designator.setter
	def Designator(self, aDesignator : Designator):
		self.___designator = aDesignator

	def create_Designator(self):
		if self.Designator == None:
			self.Designator = []
		self.Designator.append(Designator.Designator())

	def __init__(self):
		super().__init__()
		self.___designator : Designator = None
		# @AssociationType Common.Designator
		# @AssociationMultiplicity 0..1
		# """The designator of the element, which is often a coded identification, e.g. 69W03 for a switch no. 03 in station 69. In case of "private" register use leading underscore."""