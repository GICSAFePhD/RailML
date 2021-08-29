#!/usr/bin/python
# -*- coding: UTF-8 -*-
from typing import List

class Designator(object):
	@property
	def Register(self) -> str:
		return self.___register
	@property
	def Entry(self) -> str:
		return self.___entry

	@Register.setter
	def Register(self, aRegister : str):
		self.___register = aRegister
	@Entry.setter
	def Entry(self, aEntry : str):
		self.___entry = aEntry

	def __init__(self):
		self.___register : str = ""
		"""name of a register where the designator entry can be found"""
		self.___entry : str = ""
		"""the designator of the element in the specified register"""

