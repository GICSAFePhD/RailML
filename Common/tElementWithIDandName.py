#!/usr/bin/python
# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod
from Common import Name
from Common import tElementWithID
from typing import List

class tElementWithIDandName(tElementWithID):
	__metaclass__ = ABCMeta
	@classmethod
	def setName(self, *aName : Name*):
		self._name = aName

	@classmethod
	def getName(self) -> Name*:
		return self._name

	@classmethod
	def __init__(self):
		self._name : Name = None
		# @AssociationType Common.Name*
		# @AssociationMultiplicity 0..*

