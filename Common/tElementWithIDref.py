#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tRef
from typing import List

class tElementWithIDref(object):
	"""generic base type, used for inheritance of types deploying references"""
	@property
	def Ref(self) -> tRef:
		return self.___ref
	
	@Ref.setter
	def Ref(self, atRef : tRef):
		self.___ref = atRef

	def __init__(self):
		self.___ref : tRef = None
		# @AssociationType Common.tRef
		# """reference is required because it's the purpose of the element"""