#!/usr/bin/python
# -*- coding: UTF-8 -*-
from typing import List

class IsValid(object):
	@property
	def From(self) -> str:
		return self.___from
	@property
	def To(self) -> str:
		return self.___to

	@From.setter
	def From(self, aFrom : str):
		self.___from = aFrom
	@To.setter
	def To(self, aTo : str):
		self.___to = aTo

	def __init__(self):
		self.___from : str = None #date
		self.___to : str = None	#date
