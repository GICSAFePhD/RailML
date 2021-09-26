#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import anyAttribute, tElementWithIDref
from typing import List

class EntityILref(tElementWithIDref.tElementWithIDref):
	"""base type for referring elements in other parts of the schema providing just attribute @ref plus the possibility to add an anyAttribute"""
	
	''' 
	@property
	def Unnamed_anyAttribute(self) -> anyAttribute:
		return self.___unnamed_anyAttribute_
	
	@Unnamed_anyAttribute.setter
	def Unnamed_anyAttribute(self, aUnnamed_anyAttribute : anyAttribute):
		self.___unnamed_anyAttribute_ = aUnnamed_anyAttribute '''

	def __init__(self):
		super().__init__()
		#self.___unnamed_anyAttribute_ : anyAttribute = None #TODO SOLVE THIS!