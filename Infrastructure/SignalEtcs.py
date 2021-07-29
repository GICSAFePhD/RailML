#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import SignalX
from typing import List

class SignalEtcs(SignalX.SignalX):
	@property
	def Version(self) -> str:
		return self.___srsVersion
	
	@Version.setter
	def Version(self, aVersion : str):
		self.___srsVersion = aVersion

	def __init__(self):
		self.___srsVersion : str = ""
		"""Version of ETCS language (SRS edition) installed"""

