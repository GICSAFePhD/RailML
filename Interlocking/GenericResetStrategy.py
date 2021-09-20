#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import tGenericResetStrategyList, EntityIL
from typing import List

class GenericResetStrategy(EntityIL.EntityIL):
	"""Used by TVD section reset strategy that the IM regulates. E.g. reset by sweep allowed, manual reset allowed. Note that the IM can apply different reset strategies to sections. Absence of a strategy implies that reset is not possible."""
	@property
	def tGenericResetStrategyList(self) -> tGenericResetStrategyList:
		return self.___resetStrategy
	
	@tGenericResetStrategyList.setter
	def tGenericResetStrategyList(self, atGenericResetStrategyList : tGenericResetStrategyList):
		self.___resetStrategy = atGenericResetStrategyList

	def __init__(self):
		super().__init__()
		self.___resetStrategy : tGenericResetStrategyList = None
		# @AssociationType Interlocking.tGenericResetStrategyList
		# """The classification of the reset strategy."""

