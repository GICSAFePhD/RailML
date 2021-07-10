#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Infrastructure import SignalX
from typing import List

class SignalEtcs(SignalX):
	def setSrsVersion(self, aSrsVersion : str):
		self.___srsVersion = aSrsVersion

	def getSrsVersion(self) -> str:
		return self.___srsVersion

	def __init__(self):
		self.___srsVersion : str = None
		"""Version of ETCS language (SRS edition) installed"""

