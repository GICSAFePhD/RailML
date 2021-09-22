#!/usr/bin/python
# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod
from RailML.Common import Name, tElementWithID
from typing import List

class tElementWithIDandName(tElementWithID.tElementWithID):
	@property
	def Name(self) -> Name:
		return self.___name

	@Name.setter
	def Name(self, aName : Name):
		self.___name = aName

	def __init__(self):
		super().__init__()
		self.___name : Name = None
		# @AssociationType Common.Name*
		# @AssociationMultiplicity 0..*

