#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking.tGenericResetStrategyList import tGenericResetStrategyList
from RailML.Interlocking.EntityIL import EntityIL
from typing import List

class GenericResetStrategy(EntityIL):
	"""Used by TVD section reset strategy that the IM regulates. E.g. reset by sweep allowed, manual reset allowed. Note that the IM can apply different reset strategies to sections. Absence of a strategy implies that reset is not possible."""
	def setResetStrategy(self, aResetStrategy : tGenericResetStrategyList):
		self.___resetStrategy = aResetStrategy

	def getResetStrategy(self) -> tGenericResetStrategyList:
		return self.___resetStrategy

	def __init__(self):
		self.___resetStrategy : tGenericResetStrategyList = None
		# @AssociationType Interlocking.tGenericResetStrategyList
		# """The classification of the reset strategy."""

