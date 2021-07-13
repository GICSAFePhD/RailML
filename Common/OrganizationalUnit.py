#!/usr/bin/python
# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod
from RailML.Common.tElementWithIDandName import tElementWithIDandName
from typing import List

class OrganizationalUnit(tElementWithIDandName):
	__metaclass__ = ABCMeta
	@classmethod
	def setCode(self, aCode : str):
		self.___code = aCode

	@classmethod
	def getCode(self) -> str:
		return self.___code

	@classmethod
	def __init__(self):
		self.___code : str = None
		"""insert here the matching code from the relevant codelist"""

