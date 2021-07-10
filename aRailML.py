#!/usr/bin/python
# -*- coding: UTF-8 -*-
from typing import List

class aRailML(object):
	def setVersion(self, aVersion : str):
		self.___version = aVersion

	def getVersion(self) -> str:
		return self.___version

	def __init__(self):
		self.___version : str = None
		"""the supported railML version should be declared for software compatibility reasons, valid for all subschemas, don't mix railML versions between subschemas in one XML file"""

