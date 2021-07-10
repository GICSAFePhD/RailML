#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Common import tRef
from typing import List

class tElementWithIDref(object):
	"""generic base type, used for inheritance of types deploying references"""
	def setRef(self, aRef : tRef):
		self.___ref = aRef

	def getRef(self) -> tRef:
		return self.___ref

	def __init__(self):
		self.___ref : tRef = None
		# @AssociationType Common.tRef
		# """reference is required because it's the purpose of the element"""

