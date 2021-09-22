#!/usr/bin/python
# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod
from RailML.Common import tElementWithIDandName
from typing import List

class OrganizationalUnit(tElementWithIDandName.tElementWithIDandName):
	@property
	def Code(self) -> str:
		return self.___code

	@Code.setter
	def Code(self, aCode : str):
		self.___code = aCode

	def __init__(self):
		super().__init__()
		self.___code : str = None
		"""insert here the matching code from the relevant codelist"""

