#!/usr/bin/python
# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod
from RailML.Interlocking import tMustOrShould, tProving, EntityIL
#from RailML.Interlocking.Overlap import Overlap	#TODO CIRCULAR!
from typing import List, NewType

Long = NewType("Long", int)

class AssetAndGivenState(EntityIL.EntityIL):
	"""Interlocking model often requires a generic track asset to be in a given state. This base class must be extended and contain a reference to a track asset; signal, section, switch, etc. plus the given status of that element. Eg. (switch_18A, left) or (signal S19, proceed).
	In addition information about the level of state enforcement can be set."""
	@property
	def MustOrShould(self) -> tMustOrShould:
		return self.___mustOrShould
	@property
	def Proving(self) -> tProving:
		return self.___proving
	@property
	def IsNegated(self) -> Long:
		return self.___isNegated

	@MustOrShould.setter
	def MustOrShould(self, aMustOrShould : tMustOrShould):
		self.___mustOrShould = aMustOrShould
	@Proving.setter
	def Proving(self, aProving : tProving):
		self.___proving = aProving
	@IsNegated.setter
	def IsNegated(self, aIsNegated : Long):
		self.___isNegated = aIsNegated

	def __init__(self):
		super().__init__()
		self.___mustOrShould : tMustOrShould = None
		# @AssociationType Interlocking.tMustOrShould
		# """level of enforcement"""
		self.___proving : tProving = None
		# @AssociationType Interlocking.tProving
		# """The way the state is proven."""
		self.___isNegated : Long = None
		"""The exclusion of a particular state, i.e. everything else that this one."""
		#self._unnamed_Overlap_ : Overlap = None	#TODO CIRCULAR!