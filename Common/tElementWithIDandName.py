#!/usr/bin/python
# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod
from RailML.Common import Name, tElementWithID
from typing import List

#class tElementWithIDandName(tElementWithID): #TODO CON ESTA HERENCIA SE ROMPE
class tElementWithIDandName():
	__metaclass__ = ABCMeta
	@classmethod
	def setName(self, aName : Name):
		self._name = aName

	@classmethod
	def getName(self) -> Name:
		return self._name

	@classmethod
	def __init__(self):
		self._name : Name = None
		# @AssociationType Common.Name*
		# @AssociationMultiplicity 0..*

