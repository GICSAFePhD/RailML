#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking.SystemAssetConnectedToIL import SystemAssetConnectedToIL
from RailML.Interlocking.TrackAssetConnectedToIL import TrackAssetConnectedToIL
from RailML.Interlocking.EntityILref import EntityILref
from RailML.Interlocking.InterlockingInterface import InterlockingInterface
from RailML.Interlocking.SignalPlan import SignalPlan
from RailML.Interlocking.ElementGroup import ElementGroup
from RailML.Interlocking.Configuration import Configuration
from RailML.Interlocking.EntityIL import EntityIL
from typing import List

class SignalBox(EntityIL):
	"""The SignalBox (single interlocking) is a vital and fail-safe system. It accepts commands from operation control systems and reads the status of field elements. The interlocking controls a set of track assets and system assets to safely guide and control train movement. This logic reflects the railway rules and regulations.
	IL logic may be implemented in terms of mechanically interlocking bars, relay circuitry or computer programs. 
	This is the master class that must be instantiated for a specific interlocking system that controls a specific yard."""
	def setControlsSystemAsset(self, *aControlsSystemAsset : SystemAssetConnectedToIL):
		self._controlsSystemAsset = aControlsSystemAsset

	def getControlsSystemAsset(self) -> SystemAssetConnectedToIL:
		return self._controlsSystemAsset

	def setControlsTrackAsset(self, *aControlsTrackAsset : TrackAssetConnectedToIL):
		self._controlsTrackAsset = aControlsTrackAsset

	def getControlsTrackAsset(self) -> TrackAssetConnectedToIL:
		return self._controlsTrackAsset

	def setControlsRoute(self, *aControlsRoute : EntityILref):
		self._controlsRoute = aControlsRoute

	def getControlsRoute(self) -> EntityILref:
		return self._controlsRoute

	def setControlsCombinedRoute(self, *aControlsCombinedRoute : EntityILref):
		self._controlsCombinedRoute = aControlsCombinedRoute

	def getControlsCombinedRoute(self) -> EntityILref:
		return self._controlsCombinedRoute

	def setControlsInterface(self, *aControlsInterface : InterlockingInterface):
		self._controlsInterface = aControlsInterface

	def getControlsInterface(self) -> InterlockingInterface:
		return self._controlsInterface

	def setControlledBy(self, *aControlledBy : EntityILref):
		self._controlledBy = aControlledBy

	def getControlledBy(self) -> EntityILref:
		return self._controlledBy

	def setImplementsSignalplan(self, *aImplementsSignalplan : SignalPlan):
		self._implementsSignalplan = aImplementsSignalplan

	def getImplementsSignalplan(self) -> SignalPlan:
		return self._implementsSignalplan

	def setImplementsElementGroup(self, *aImplementsElementGroup : ElementGroup):
		self._implementsElementGroup = aImplementsElementGroup

	def getImplementsElementGroup(self) -> ElementGroup:
		return self._implementsElementGroup

	def setHasPermissionZone(self, *aHasPermissionZone : EntityILref):
		self._hasPermissionZone = aHasPermissionZone

	def getHasPermissionZone(self) -> EntityILref:
		return self._hasPermissionZone

	def setHasConflictingRoutes(self, *aHasConflictingRoutes : EntityILref):
		self._hasConflictingRoutes = aHasConflictingRoutes

	def getHasConflictingRoutes(self) -> EntityILref:
		return self._hasConflictingRoutes

	def setHasConfiguration(self, *aHasConfiguration : Configuration):
		self._hasConfiguration = aHasConfiguration

	def getHasConfiguration(self) -> Configuration:
		return self._hasConfiguration

	def __init__(self):
		self._controlsSystemAsset : SystemAssetConnectedToIL = None
		# @AssociationType Interlocking.SystemAssetConnectedToIL*
		# @AssociationMultiplicity 0..*
		# """The references to the system assets the interlocking controls"""
		self._controlsTrackAsset : TrackAssetConnectedToIL = None
		# @AssociationType Interlocking.TrackAssetConnectedToIL*
		# @AssociationMultiplicity 0..*
		# """The interlocking carries a list of (references to) track assets that this interlocking controls. The controlled object has an attribute indicating the Level of Control which is most often �full control�. Track assets that aren't controlled by the interlocking, e.g. field controlled level crossing or open track elements can be tagged with levelOfControl='none'."""
		self._controlsRoute : EntityILref = None
		"""The reference to the routes the interlocking controls"""
		self._controlsCombinedRoute : EntityILref = None
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 0..*
		# """The reference to the combined routes the interlocking controls"""
		self._controlsInterface : InterlockingInterface = None
		# @AssociationType Interlocking.InterlockingInterface*
		# @AssociationMultiplicity 0..*
		# """The references to the interfaces to other interlockings"""
		self._controlledBy : EntityILref = None
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 0..*
		# """The references to the controllers which can control this interlocking"""
		self._implementsSignalplan : SignalPlan = None
		# @AssociationType Interlocking.SignalPlan*
		# @AssociationMultiplicity 0..*
		# """The references to the signal plans the interlocking uses"""
		self._implementsElementGroup : ElementGroup = None
		# @AssociationType Interlocking.ElementGroup*
		# @AssociationMultiplicity 0..*
		# """The references to the element groups which are configured for this interlocking"""
		self._hasPermissionZone : EntityILref = None
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 0..*
		# """The reference to any permission zone within the area controlled by this interlocking."""
		self._hasConflictingRoutes : EntityILref = None
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 0..*
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 0..*
		# """The references to the conflicting routes the interlocking knows"""
		self._hasConfiguration : Configuration = None
		# @AssociationType Interlocking.Configuration*
		# @AssociationMultiplicity 0..*
		# """Basic information of the interlocking configuration"""

