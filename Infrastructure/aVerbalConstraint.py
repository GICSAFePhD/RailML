#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import UnderCrossing, OverCrossing
from typing import List

class aVerbalConstraint(object):
	@property
	def VerbalConstraint(self) -> str:
		return self.___verbalConstraint
	@property
	def UnderCrossing(self) -> UnderCrossing:
		return self.___unnamed_UnderCrossing_
	@property
	def OverCrossing(self) -> OverCrossing:
		return self.___unnamed_OverCrossing_

	@VerbalConstraint.setter
	def VerbalConstraint(self, aVerbalConstraint : str):
		self.___verbalConstraint = aVerbalConstraint
	@UnderCrossing.setter
	def UnderCrossing(self, aUnderCrossing : UnderCrossing):
		self.___unnamed_UnderCrossing_ = aUnderCrossing
	@OverCrossing.setter
	def OverCrossing(self, aOverCrossing : OverCrossing):
		self.___unnamed_OverCrossing_ = aOverCrossing

	def __init__(self):
		self.___verbalConstraint : str = ""
		"""verbal formulation for any kind of further constraint that applies for using the overCrossing or underCrossing"""
		#self.___unnamed_UnderCrossing_ : UnderCrossing = UnderCrossing.UnderCrossing()	#TODO FIX THIS
		#self.___unnamed_OverCrossing_ : OverCrossing = OverCrossing.OverCrossing()	#TODO FIX THIS

