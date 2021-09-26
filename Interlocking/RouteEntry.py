#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import EntityILref
from RailML.Interlocking import EntityIL
from typing import List

class RouteEntry(EntityIL.EntityIL):
	"""The route entry is normally a (virtual) signal."""
	@property
	def RefersTo(self) -> EntityILref:
		return self.___refersTo
	@property
	def NonReplacement(self) -> EntityILref:
		return self.___nonReplacement

	@RefersTo.setter
	def RefersTo(self, aRefersTo : EntityILref):	# TODO *RefersTo
		self.___refersTo = aRefersTo
	@NonReplacement.setter
	def NonReplacement(self, aNonReplacement : EntityILref):
		self.___nonReplacement = aNonReplacement

	def __init__(self):
		super().__init__()
		self.___refersTo : EntityILref = None
		"""The reference to the track asset representing the start point of the route. In most cases this is a signal."""
		self.___nonReplacement : EntityILref = None
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# """The reference to any TVD section in advance to the start signal which sequential occupation will not cause the signal closure."""