#!/usr/bin/python
# -*- coding: UTF-8 -*-
from typing import List

class External(object):
	def setId(self, aId : str):
		self.___id = aId

	def getId(self) -> str:
		return self.___id

	def setRef(self, aRef : str):
		self.___ref = aRef

	def getRef(self) -> str:
		return self.___ref

	def setDescription(self, aDescription : str):
		self.___description = aDescription

	def getDescription(self) -> str:
		return self.___description

	def __init__(self):
		self.___id : str = None
		"""an external identifier of the element"""
		self.___ref : str = None
		"""a reference to an external element"""
		self.___description : str = None
		"""description of the external identifier or reference, providing basic information about external system"""

