#!/usr/bin/python
# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod
from typing import List

class TimePeriodRule(object):
	__metaclass__ = ABCMeta
	@classmethod
	def setIsNegated(self, aIsNegated : int):	#TODO DEFINED AS LONG
		self.___isNegated = aIsNegated

	@classmethod
	def getIsNegated(self) -> int:	#TODO DEFINED AS LONG
		return self.___isNegated

	@classmethod
	def __init__(self):
		self.___isNegated : int = None	#TODO DEFINED AS LONG

