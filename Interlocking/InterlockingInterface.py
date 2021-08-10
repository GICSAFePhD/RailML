#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import tIxlInterfaceLocationTypeList, EntityILref, EntityIL
from typing import List, NewType
Long = NewType("Long", int)

class InterlockingInterface(EntityIL.EntityIL):
	"""The interface between different interlockings is a special object and differs in the amount of information exchanged between the two.
	If the interlockings are of different type or from different vendor the interface is often made of parallel data exchange and might use relays."""
	@property
	def InterfaceLocation(self) -> tIxlInterfaceLocationTypeList:
		return self.___interfaceLocation
	@property
	def IsOnCommandSide(self) -> Long:
		return self.___isOnCommandSide
	@property
	def LastOwnTvdSection(self) -> EntityILref:
		return self.___lastOwnTvdSection
	@property
	def FirstRemoteTvdSection(self) -> EntityILref:
		return self.___firstRemoteTvdSection
	@property
	def IncomingRoute(self) -> EntityILref:
		return self.___incomingRoute
	@property
	def OutgoingRoute(self) -> EntityILref:
		return self.___outgoingRoute
	@property
	def HasInterface(self) -> EntityILref:
		return self.___hasInterface

	@InterfaceLocation.setter
	def InterfaceLocation(self, aInterfaceLocation : tIxlInterfaceLocationTypeList):
		self.___interfaceLocation = aInterfaceLocation
	@IsOnCommandSide.setter
	def IsOnCommandSide(self, aIsOnCommandSide : Long):
		self.___isOnCommandSide = aIsOnCommandSide
	@LastOwnTvdSection.setter
	def LastOwnTvdSection(self, aLastOwnTvdSection : EntityILref):
		self.___lastOwnTvdSection = aLastOwnTvdSection
	@FirstRemoteTvdSection.setter
	def FirstRemoteTvdSection(self, *aFirstRemoteTvdSection : EntityILref):
		self.___firstRemoteTvdSection = aFirstRemoteTvdSection
	@IncomingRoute.setter
	def IncomingRoute(self, *aIncomingRoute : EntityILref):
		self.___incomingRoute = aIncomingRoute
	@OutgoingRoute.setter
	def OutgoingRoute(self, aOutgoingRoute : EntityILref):
		self.___outgoingRoute = aOutgoingRoute
	@HasInterface.setter
	def HasInterface(self, aHasInterface : EntityILref):
		self.___hasInterface = aHasInterface

	def __init__(self):
		self.___interfaceLocation : tIxlInterfaceLocationTypeList = tIxlInterfaceLocationTypeList.tIxlInterfaceLocationTypeList()
		# @AssociationType Interlocking.tIxlInterfaceLocationTypeList
		# """The topology view of interface location determining the extent of information to be exchanged."""
		self.___isOnCommandSide : Long = 0
		"""True means the related interlocking uses the described commands for output towards the partner. With false it is inverted for the related interlocking."""
		self.___lastOwnTvdSection : EntityILref = EntityILref.EntityILref()
		"""The reference to the last TVD section just before the interface."""
		self.___firstRemoteTvdSection : EntityILref = EntityILref.EntityILref()
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 0..*
		# """The reference to the first TVD section within the other interlocking beyond the interface."""
		self.___incomingRoute : EntityILref = EntityILref.EntityILref()
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 0..*
		# """This is the reference to all routes the interlocking knows that start at the interface location or in rear of it in direction towards the interlocking."""
		self.___outgoingRoute : EntityILref = EntityILref.EntityILref()
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 0..1
		# """This is the reference to all routes the interlocking knows that end at the interface location or in advance of it in direction towards the other interlocking."""
		self.___hasInterface : EntityILref = EntityILref.EntityILref()
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# @AssociationType Interlocking.EntityILref
		# @AssociationMultiplicity 1
		# """This is the reference to the description of the physical interface with commands and messages transmitted."""