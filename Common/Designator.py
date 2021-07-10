#!/usr/bin/python
# -*- coding: UTF-8 -*-
from typing import List

class Designator(object):
	def setRegister(self, aRegister : str):
		self.___register = aRegister

	def getRegister(self) -> str:
		return self.___register

	def setEntry(self, aEntry : str):
		self.___entry = aEntry

	def getEntry(self) -> str:
		return self.___entry

	def __init__(self):
		self.___register : str = None
		"""name of a register where the designator entry can be found"""
		self.___entry : str = None
		"""the designator of the element in the specified register"""

