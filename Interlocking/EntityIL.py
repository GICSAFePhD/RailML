#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import anyAttribute
from RailML.Interlocking import tElementWithIDandDesignator
from typing import List

class EntityIL(tElementWithIDandDesignator.tElementWithIDandDesignator):
	"""base type for normal elements in IL providing attributes @id and @name plus the possibility to add an anyAttribute"""
	@property
	def Unnamed_any(self) -> list:
		return self.___unnamed_any_
	@property
	def Unnamed_anyAttribute(self) -> anyAttribute:
		return self.___unnamed_anyAttribute_
	
	@Unnamed_any.setter
	def Unnamed_any(self, aUnnamed_any : list):
		self.___unnamed_any_ = aUnnamed_any
	@Unnamed_anyAttribute.setter
	def Unnamed_anyAttribute(self, aUnnamed_anyAttribute : anyAttribute):
		self.___unnamed_anyAttribute_ = aUnnamed_anyAttribute

	def __init__(self):
		self.___unnamed_any_ = []
		"""# @AssociationMultiplicity 0..*"""
		self.___unnamed_anyAttribute_ : anyAttribute = None

