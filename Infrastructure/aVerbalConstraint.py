#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Infrastructure import UnderCrossing
from Infrastructure import OverCrossing
from typing import List

class aVerbalConstraint(object):
	def setVerbalConstraint(self, aVerbalConstraint : str):
		self.___verbalConstraint = aVerbalConstraint

	def getVerbalConstraint(self) -> str:
		return self.___verbalConstraint

	def __init__(self):
		self.___verbalConstraint : str = None
		"""verbal formulation for any kind of further constraint that applies for using the overCrossing or underCrossing"""
		self._unnamed_UnderCrossing_ : UnderCrossing = None
		self._unnamed_OverCrossing_ : OverCrossing = None

