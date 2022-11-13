#!/usr/bin/python
# -*- coding: UTF-8 -*-
from typing import List

class External(object):
	@property
	def Id(self) -> str:
		return self.___id
	@property
	def Ref(self) -> str:
		return self.___ref
	@property
	def Description(self) -> str:
		return self.___description

	@Id.setter
	def Id(self, aId : str):
		self.___id = aId
	@Ref.setter
	def Ref(self, aRef : str):
		self.___ref = aRef
	@Description.setter
	def Description(self, aDescription : str):
		self.___description = aDescription

	def __init__(self):
		self.___id : str = None
		"""an external identifier of the element"""
		self.___ref : str = None
		"""a reference to an external element"""
		self.___description : str = None
		"""description of the external identifier or reference, providing basic information about external system"""