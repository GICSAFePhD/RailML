#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import SystemAssetConnectedToIL, TrackAssetConnectedToIL,EntityILref, EntityIL
from RailML.Interlocking import InterlockingInterface, SignalPlan, ElementGroup, Configuration
from typing import List

class SignalBox(EntityIL.EntityIL):
	"""The SignalBox (single interlocking) is a vital and fail-safe system. It accepts commands from operation control systems and reads the status of field elements. The interlocking controls a set of track assets and system assets to safely guide and control train movement. This logic reflects the railway rules and regulations.
	IL logic may be implemented in terms of mechanically interlocking bars, relay circuitry or computer programs. 
	This is the master class that must be instantiated for a specific interlocking system that controls a specific yard."""
	@property
	def ControlsSystemAsset(self) -> SystemAssetConnectedToIL:
		return self.___controlsSystemAsset
	@property
	def ControlsTrackAsset(self) -> TrackAssetConnectedToIL:
		return self.___controlsTrackAsset
	@property
	def ControlsRoute(self) -> EntityILref:
		return self.___controlsRoute
	@property
	def ControlsCombinedRoute(self) -> EntityILref:
		return self.___controlsCombinedRoute
	@property
	def ControlsInterface(self) -> InterlockingInterface:
		return self.___controlsInterface
	@property
	def ControlledBy(self) -> EntityILref:
		return self.___controlledBy
	@property
	def ImplementsSignalplan(self) -> SignalPlan:
		return self.___implementsSignalplan
	@property
	def ImplementsElementGroup(self) -> ElementGroup:
		return self.___implementsElementGroup
	@property
	def HasPermissionZone(self) -> EntityILref:
		return self.___hasPermissionZone
	@property
	def HasConflictingRoutes(self) -> EntityILref:
		return self.___hasConflictingRoutes
	@property
	def HasConfiguration(self) -> Configuration:
		return self.___hasConfiguration

	@ControlsSystemAsset.setter
	def ControlsSystemAsset(self, *aControlsSystemAsset : SystemAssetConnectedToIL):
		self.___controlsSystemAsset = aControlsSystemAsset
	@ControlsTrackAsset.setter
	def ControlsTrackAsset(self, *aControlsTrackAsset : TrackAssetConnectedToIL):
		self.___controlsTrackAsset = aControlsTrackAsset
	@ControlsRoute.setter
	def ControlsRoute(self, *aControlsRoute : EntityILref):
		self.___controlsRoute = aControlsRoute
	@ControlsCombinedRoute.setter
	def ControlsCombinedRoute(self, *aControlsCombinedRoute : EntityILref):
		self.___controlsCombinedRoute = aControlsCombinedRoute
	@ControlsInterface.setter
	def ControlsInterface(self, *aControlsInterface : InterlockingInterface):
		self.___controlsInterface = aControlsInterface
	@ControlledBy.setter
	def ControlledBy(self, *aControlledBy : EntityILref):
		self.___controlledBy = aControlledBy
	@ImplementsSignalplan.setter
	def ImplementsSignalplan(self, *aImplementsSignalplan : SignalPlan):
		self.___implementsSignalplan = aImplementsSignalplan
	@ImplementsElementGroup.setter
	def ImplementsElementGroup(self, *aImplementsElementGroup : ElementGroup):
		self.___implementsElementGroup = aImplementsElementGroup
	@HasPermissionZone.setter
	def HasPermissionZone(self, *aHasPermissionZone : EntityILref):
		self.___hasPermissionZone = aHasPermissionZone
	@HasConflictingRoutes.setter
	def HasConflictingRoutes(self, *aHasConflictingRoutes : EntityILref):
		self.___hasConflictingRoutes = aHasConflictingRoutes
	@HasConfiguration.setter
	def HasConfiguration(self, *aHasConfiguration : Configuration):
		self.___hasConfiguration = aHasConfiguration

	def __init__(self):
		self.___controlsSystemAsset : SystemAssetConnectedToIL = SystemAssetConnectedToIL.SystemAssetConnectedToIL()
		# @AssociationType Interlocking.SystemAssetConnectedToIL*
		# @AssociationMultiplicity 0..*
		# """The references to the system assets the interlocking controls"""
		self.___controlsTrackAsset : TrackAssetConnectedToIL = TrackAssetConnectedToIL.TrackAssetConnectedToIL()
		# @AssociationType Interlocking.TrackAssetConnectedToIL*
		# @AssociationMultiplicity 0..*
		# """The interlocking carries a list of (references to) track assets that this interlocking controls. The controlled object has an attribute indicating the Level of Control which is most often �full control�. Track assets that aren't controlled by the interlocking, e.g. field controlled level crossing or open track elements can be tagged with levelOfControl='none'."""
		self.___controlsRoute : EntityILref = EntityILref.EntityILref()
		"""The reference to the routes the interlocking controls"""
		self.___controlsCombinedRoute : EntityILref = EntityILref.EntityILref()
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 0..*
		# """The reference to the combined routes the interlocking controls"""
		self.___controlsInterface : InterlockingInterface = InterlockingInterface.InterlockingInterface()
		# @AssociationType Interlocking.InterlockingInterface*
		# @AssociationMultiplicity 0..*
		# """The references to the interfaces to other interlockings"""
		self.___controlledBy : EntityILref = EntityILref.EntityILref()
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 0..*
		# """The references to the controllers which can control this interlocking"""
		self.___implementsSignalplan : SignalPlan = SignalPlan.SignalPlan()
		# @AssociationType Interlocking.SignalPlan*
		# @AssociationMultiplicity 0..*
		# """The references to the signal plans the interlocking uses"""
		self.___implementsElementGroup : ElementGroup = ElementGroup.ElementGroup()
		# @AssociationType Interlocking.ElementGroup*
		# @AssociationMultiplicity 0..*
		# """The references to the element groups which are configured for this interlocking"""
		self.___hasPermissionZone : EntityILref = EntityILref.EntityILref()
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 0..*
		# """The reference to any permission zone within the area controlled by this interlocking."""
		self.___hasConflictingRoutes : EntityILref = EntityILref.EntityILref()
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 0..*
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 0..*
		# """The references to the conflicting routes the interlocking knows"""
		self.___hasConfiguration : Configuration = Configuration.Configuration()
		# @AssociationType Interlocking.Configuration*
		# @AssociationMultiplicity 0..*
		# """Basic information of the interlocking configuration"""