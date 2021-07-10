#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Common import tElementWithID
from typing import List

class tElementWithIDandCode(tElementWithID):
	def setCode(self, aCode : str):
		self.___code = aCode

	def getCode(self) -> str:
		return self.___code

	def __init__(self):
		self.___code : str = None

