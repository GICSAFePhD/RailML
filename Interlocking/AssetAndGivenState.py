#!/usr/bin/python
# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod
from RailML.Interlocking.tMustOrShould import tMustOrShould
from RailML.Interlocking.tProving import tProving
#from RailML.Interlocking.Overlap import Overlap	#TODO CIRCULAR!
from RailML.Interlocking.EntityIL import EntityIL
from typing import List

class AssetAndGivenState(EntityIL):
	"""Interlocking model often requires a generic track asset to be in a given state. This base class must be extended and contain a reference to a track asset; signal, section, switch, etc. plus the given status of that element. Eg. (switch_18A, left) or (signal S19, proceed).
	In addition information about the level of state enforcement can be set."""
	__metaclass__ = ABCMeta
	@classmethod
	def setMustOrShould(self, aMustOrShould : tMustOrShould):
		self.___mustOrShould = aMustOrShould

	@classmethod
	def getMustOrShould(self) -> tMustOrShould:
		return self.___mustOrShould

	@classmethod
	def setProving(self, aProving : tProving):
		self.___proving = aProving

	@classmethod
	def getProving(self) -> tProving:
		return self.___proving

	@classmethod
	def setIsNegated(self, aIsNegated : int):	#TODO DEFINED AS long
		self.___isNegated = aIsNegated

	@classmethod
	def getIsNegated(self) -> int:	#TODO DEFINED AS long
		return self.___isNegated

	@classmethod
	def __init__(self):
		self.___mustOrShould : tMustOrShould = None
		# @AssociationType Interlocking.tMustOrShould
		# """level of enforcement"""
		self.___proving : tProving = None
		# @AssociationType Interlocking.tProving
		# """The way the state is proven."""
		self.___isNegated : int = None	#TODO DEFINED AS long
		"""The exclusion of a particular state, i.e. everything else that this one."""
		#self._unnamed_Overlap_ : Overlap = None	#TODO CIRCULAR!

