#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Common import tRef
from typing import List

class LocationNetwork(object):
	def setNetworkRef(self, aNetworkRef : tRef):
		self.___networkRef = aNetworkRef

	def getNetworkRef(self) -> tRef:
		return self.___networkRef

	def __init__(self):
		self.___networkRef : tRef = None
		# @AssociationType Common.tRef
		# """reference to a railway topology <network> element"""

