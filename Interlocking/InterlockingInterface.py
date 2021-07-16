#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking.tIxlInterfaceLocationTypeList import tIxlInterfaceLocationTypeList
from RailML.Interlocking.EntityILref import EntityILref
from RailML.Interlocking.EntityIL import EntityIL
from typing import List

class InterlockingInterface(EntityIL):
	"""The interface between different interlockings is a special object and differs in the amount of information exchanged between the two.
	If the interlockings are of different type or from different vendor the interface is often made of parallel data exchange and might use relays."""
	def setInterfaceLocation(self, aInterfaceLocation : tIxlInterfaceLocationTypeList):
		self.___interfaceLocation = aInterfaceLocation

	def getInterfaceLocation(self) -> tIxlInterfaceLocationTypeList:
		return self.___interfaceLocation

	def setIsOnCommandSide(self, aIsOnCommandSide : int):	#TODO DEFINED AS LONG
		self.___isOnCommandSide = aIsOnCommandSide

	def getIsOnCommandSide(self) -> int:	#TODO DEFINED AS LONG
		return self.___isOnCommandSide

	def setLastOwnTvdSection(self, aLastOwnTvdSection : EntityILref):
		self._lastOwnTvdSection = aLastOwnTvdSection

	def getLastOwnTvdSection(self) -> EntityILref:
		return self._lastOwnTvdSection

	def setFirstRemoteTvdSection(self, *aFirstRemoteTvdSection : EntityILref):
		self._firstRemoteTvdSection = aFirstRemoteTvdSection

	def getFirstRemoteTvdSection(self) -> EntityILref:
		return self._firstRemoteTvdSection

	def setIncomingRoute(self, *aIncomingRoute : EntityILref):
		self._incomingRoute = aIncomingRoute

	def getIncomingRoute(self) -> EntityILref:
		return self._incomingRoute

	def setOutgoingRoute(self, aOutgoingRoute : EntityILref):
		self._outgoingRoute = aOutgoingRoute

	def getOutgoingRoute(self) -> EntityILref:
		return self._outgoingRoute

	def setHasInterface(self, aHasInterface : EntityILref):
		self._hasInterface = aHasInterface

	def getHasInterface(self) -> EntityILref:
		return self._hasInterface

	def __init__(self):
		self.___interfaceLocation : tIxlInterfaceLocationTypeList = None
		# @AssociationType Interlocking.tIxlInterfaceLocationTypeList
		# """The topology view of interface location determining the extent of information to be exchanged."""
		self.___isOnCommandSide : int = None	#TODO DEFINED AS LONG
		"""True means the related interlocking uses the described commands for output towards the partner. With false it is inverted for the related interlocking."""
		self._lastOwnTvdSection : EntityILref = None
		"""The reference to the last TVD section just before the interface."""
		self._firstRemoteTvdSection : EntityILref = None
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 0..*
		# """The reference to the first TVD section within the other interlocking beyond the interface."""
		self._incomingRoute : EntityILref = None
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 0..*
		# """This is the reference to all routes the interlocking knows that start at the interface location or in rear of it in direction towards the interlocking."""
		self._outgoingRoute : EntityILref = None
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 0..1
		# """This is the reference to all routes the interlocking knows that end at the interface location or in advance of it in direction towards the other interlocking."""
		self._hasInterface : EntityILref = None
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# """This is the reference to the description of the physical interface with commands and messages transmitted."""

