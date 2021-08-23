#!/usr/bin/python
# -*- coding: UTF-8 -*-
from typing import List

class PhysicalFacilities(object):
	"""This is the top level element for railML3 physical facilities infrastructure model. It is currently empty, but allows for specific extensions via the any element"""
	@property
	def Unnamed_any(self) -> list:
		return self.___unnamed_any
	
	@Unnamed_any.setter
	def Unnamed_any(self, aUnnamed_any : list):
		self.___unnamed_any = aUnnamed_any

	def __init__(self):
		self.___unnamed_any = None#[]
		"""# @AssociationMultiplicity 0..*"""

