#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import TvdSections, SwitchesIL, DerailersIL, MovableCrossings
from RailML.Interlocking import LevelCrossingsIL, Keys, KeyLocksIL, GenericDetectors
from RailML.Interlocking import SignalsIL, ATPdevices, Interfaces, WorkZones
from RailML.Interlocking import LocalOperationAreas, ShuntingZones, PermissionZones
from RailML.Interlocking import RouteReleaseGroupsAhead, RouteReleaseGroupsRear
from RailML.Interlocking import Routes, ConflictingRoutes, RouteRelations
from RailML.Interlocking import CombinedRoutes, Overlaps, DangerPoints
from RailML.Interlocking import DestinationPoints,PowerSuppliesIL, EntityIL
from typing import List

class AssetsForIL(EntityIL.EntityIL):
	"""Container for assets used for operation of interlockings and controllers. They represent a more functional/logical view onto the railway network but depending on the hardware as defined in infrastructure domain.
	Assets in the container are owned by the railway network rather than by individual interlocking systems."""
	@property
	def TvdSections(self) -> TvdSections:
		return self.___tvdSections
	@property
	def SwitchesIL(self) -> SwitchesIL:	#TODO ACA
		return self.___switchesIL
	@property
	def DerailersIL(self) -> DerailersIL:
		return self.___derailersIL
	@property
	def MovableCrossings(self) -> MovableCrossings:
		return self.___movableCrossings
	@property
	def LevelCrossingsIL(self) -> LevelCrossingsIL:
		return self.___levelCrossingsIL
	@property
	def Keys(self) -> Keys:
		return self.___keys
	@property
	def KeyLocksIL(self) -> KeyLocksIL:
		return self.___keyLocksIL
	@property
	def GenericDetectors(self) -> GenericDetectors:
		return self.___genericDetectors
	@property
	def SignalsIL(self) -> SignalsIL:
		return self.___signalsIL
	@property
	def ATPdevices(self) -> ATPdevices:
		return self.___atpDevices
	@property
	def Interfaces(self) -> Interfaces:
		return self.___interfaces
	@property
	def WorkZones(self) -> WorkZones:
		return self.___workZones
	@property
	def LocalOperationAreas(self) -> LocalOperationAreas:
		return self.___localOperationAreas
	@property
	def ShuntingZones(self) -> ShuntingZones:
		return self.___shuntingZones
	@property
	def PermissionZones(self) -> PermissionZones:
		return self.___permissionZones
	@property
	def RouteReleaseGroupsAhead(self) -> RouteReleaseGroupsAhead:
		return self.___routeReleaseGroupsAhead
	@property
	def RouteReleaseGroupsRear(self) -> RouteReleaseGroupsRear:
		return self.___routeReleaseGroupsRear
	@property
	def Routes(self) -> Routes:
		return self.___routes
	@property
	def ConflictingRoutes(self) -> ConflictingRoutes:
		return self.___conflictingRoutes
	@property
	def RouteRelations(self) -> RouteRelations:
		return self.___routeRelations
	@property
	def CombinedRoutes(self) -> CombinedRoutes:
		return self.___combinedRoutes
	@property
	def Overlaps(self) -> Overlaps:
		return self.___overlaps
	@property
	def DangerPoints(self) -> DangerPoints:
		return self.___dangerPoints
	@property
	def DestinationPoints(self) -> DestinationPoints:
		return self.___destinationPoints
	@property
	def PowerSuppliesIL(self) -> PowerSuppliesIL:
		return self.___powerSuppliesIL

	@TvdSections.setter
	def TvdSections(self, aTvdSections : TvdSections):
		self.___tvdSections = aTvdSections
	@SwitchesIL.setter
	def SwitchesIL(self, aSwitchesIL : SwitchesIL):
		self.___switchesIL = aSwitchesIL
	@DerailersIL.setter
	def DerailersIL(self, aDerailersIL : DerailersIL):
		self.___derailersIL = aDerailersIL
	@MovableCrossings.setter
	def MovableCrossings(self, aMovableCrossings : MovableCrossings):
		self.___movableCrossings = aMovableCrossings
	@LevelCrossingsIL.setter
	def LevelCrossingsIL(self, aLevelCrossingsIL : LevelCrossingsIL):
		self.___levelCrossingsIL = aLevelCrossingsIL
	@Keys.setter
	def Keys(self, aKeys : Keys):
		self.___keys = aKeys
	@KeyLocksIL.setter
	def KeyLocksIL(self, aKeyLocksIL : KeyLocksIL):
		self.___keyLocksIL = aKeyLocksIL
	@GenericDetectors.setter
	def GenericDetectors(self, aGenericDetectors : GenericDetectors):
		self.___genericDetectors = aGenericDetectors
	@SignalsIL.setter
	def SignalsIL(self, aSignalsIL : SignalsIL):
		self.___signalsIL = aSignalsIL
	@ATPdevices.setter
	def ATPdevices(self, aATPdevices : ATPdevices):
		self.___atpDevices = aATPdevices
	@Interfaces.setter
	def Interfaces(self, aInterfaces : Interfaces):
		self.___interfaces = aInterfaces
	@WorkZones.setter
	def WorkZones(self, aWorkZones : WorkZones):
		self.___workZones = aWorkZones
	@LocalOperationAreas.setter
	def LocalOperationAreas(self, aLocalOperationAreas : LocalOperationAreas):
		self.___localOperationAreas = aLocalOperationAreas
	@ShuntingZones.setter
	def ShuntingZones(self, aShuntingZones : ShuntingZones):
		self.___shuntingZones = aShuntingZones
	@PermissionZones.setter
	def PermissionZones(self, aPermissionZones : PermissionZones):
		self.___permissionZones = aPermissionZones
	@RouteReleaseGroupsAhead.setter
	def RouteReleaseGroupsAhead(self, aRouteReleaseGroupsAhead : RouteReleaseGroupsAhead):
		self.___routeReleaseGroupsAhead = aRouteReleaseGroupsAhead
	@RouteReleaseGroupsRear.setter
	def RouteReleaseGroupsRear(self, aRouteReleaseGroupsRear : RouteReleaseGroupsRear):
		self.___routeReleaseGroupsRear = aRouteReleaseGroupsRear
	@Routes.setter
	def Routes(self, aRoutes : Routes):
		self.___routes = aRoutes
	@ConflictingRoutes.setter
	def ConflictingRoutes(self, aConflictingRoutes : ConflictingRoutes):
		self.___conflictingRoutes = aConflictingRoutes
	@RouteRelations.setter
	def RouteRelations(self, aRouteRelations : RouteRelations):
		self.___routeRelations = aRouteRelations
	@CombinedRoutes.setter
	def CombinedRoutes(self, aCombinedRoutes : CombinedRoutes):
		self.___combinedRoutes = aCombinedRoutes
	@Overlaps.setter
	def Overlaps(self, aOverlaps : Overlaps):
		self.___overlaps = aOverlaps
	@DangerPoints.setter
	def DangerPoints(self, aDangerPoints : DangerPoints):
		self.___dangerPoints = aDangerPoints
	@DestinationPoints.setter
	def DestinationPoints(self, aDestinationPoints : DestinationPoints):
		self.___destinationPoints = aDestinationPoints
	@PowerSuppliesIL.setter
	def PowerSuppliesIL(self, aPowerSuppliesIL : PowerSuppliesIL):
		self.___powerSuppliesIL = aPowerSuppliesIL

	def __init__(self):
		self.___tvdSections : TvdSections = TvdSections.TvdSections()
		# @AssociationType Interlocking.TvdSections
		# @AssociationMultiplicity 0..1
		# """contains all tvdSection elements"""
		self.___switchesIL : SwitchesIL = SwitchesIL.SwitchesIL()
		# @AssociationType Interlocking.SwitchesIL
		# @AssociationMultiplicity 0..1
		# """contains all MovableElements of type SwitchIL"""
		self.___derailersIL : DerailersIL = DerailersIL.DerailersIL()
		# @AssociationType Interlocking.DerailersIL
		# @AssociationMultiplicity 0..1
		# """contains all MovableElements of type DerailerIL"""
		self.___movableCrossings : MovableCrossings = MovableCrossings.MovableCrossings()
		# @AssociationType Interlocking.MovableCrossings
		# @AssociationMultiplicity 0..1
		# """contains all MovableElements of type MovableCrossing"""
		self.___levelCrossingsIL : LevelCrossingsIL = LevelCrossingsIL.LevelCrossingsIL()
		# @AssociationType Interlocking.LevelCrossingsIL
		# @AssociationMultiplicity 0..1
		# """contains all levelCrossingIL elements"""
		self.___keys : Keys = Keys.Keys()
		# @AssociationType Interlocking.Keys
		# @AssociationMultiplicity 0..1
		# """contains all key elements"""
		self.___keyLocksIL : KeyLocksIL = KeyLocksIL.KeyLocksIL()
		# @AssociationType Interlocking.KeyLocksIL
		# @AssociationMultiplicity 0..1
		# """contains all keyLockIL elements"""
		self.___genericDetectors : GenericDetectors = GenericDetectors.GenericDetectors()
		# @AssociationType Interlocking.GenericDetectors
		# @AssociationMultiplicity 0..1
		# """contains all genericDetector elements"""
		self.___signalsIL : SignalsIL = SignalsIL.SignalsIL()
		# @AssociationType Interlocking.SignalsIL
		# @AssociationMultiplicity 0..1
		# """contains all signalIL elements"""
		self.___atpDevices : ATPdevices = ATPdevices.ATPdevices()
		# @AssociationType Interlocking.ATPdevices
		# @AssociationMultiplicity 0..1
		# """contains all atpDevice elements (not with railML3.1)"""
		self.___interfaces : Interfaces = Interfaces.Interfaces()
		# @AssociationType Interlocking.Interfaces
		# @AssociationMultiplicity 0..1
		# """contains all interface elements"""
		self.___workZones : WorkZones = WorkZones.WorkZones()
		# @AssociationType Interlocking.WorkZones
		# @AssociationMultiplicity 0..1
		# """contains all workZone elements"""
		self.___localOperationAreas : LocalOperationAreas = LocalOperationAreas.LocalOperationAreas()
		# @AssociationType Interlocking.LocalOperationAreas
		# @AssociationMultiplicity 0..1
		# """contains all localOperationArea elements"""
		self.___shuntingZones : ShuntingZones = ShuntingZones.ShuntingZones()
		# @AssociationType Interlocking.ShuntingZones
		# @AssociationMultiplicity 0..1
		# """contains all shuntingZone elements"""
		self.___permissionZones : PermissionZones = PermissionZones.PermissionZones()
		# @AssociationType Interlocking.PermissionZones
		# @AssociationMultiplicity 0..1
		# """contains all permissionZone elements"""
		self.___routeReleaseGroupsAhead : RouteReleaseGroupsAhead = RouteReleaseGroupsAhead.RouteReleaseGroupsAhead()
		# @AssociationType Interlocking.RouteReleaseGroupsAhead
		# @AssociationMultiplicity 0..1
		# """contains all routeReleaseGroupAhead elements"""
		self.___routeReleaseGroupsRear : RouteReleaseGroupsRear = RouteReleaseGroupsRear.RouteReleaseGroupsRear()
		# @AssociationType Interlocking.RouteReleaseGroupsRear
		# @AssociationMultiplicity 0..1
		# """contains all routeReleaseGroupRear elements"""
		self.___routes : Routes = Routes.Routes()
		# @AssociationType Interlocking.Routes
		# @AssociationMultiplicity 0..1
		# """contains all route elements"""
		self.___conflictingRoutes : ConflictingRoutes = ConflictingRoutes.ConflictingRoutes()
		# @AssociationType Interlocking.ConflictingRoutes
		# @AssociationMultiplicity 0..1
		# """contains all conflictingRoute elements"""
		self.___routeRelations : RouteRelations = RouteRelations.RouteRelations()
		# @AssociationType Interlocking.RouteRelations
		# @AssociationMultiplicity 0..1
		# """contains all routeRelation elements"""
		self.___combinedRoutes : CombinedRoutes = CombinedRoutes.CombinedRoutes()
		# @AssociationType Interlocking.CombinedRoutes
		# @AssociationMultiplicity 0..1
		# """contains all combinedRoute elements"""
		self.___overlaps : Overlaps = Overlaps.Overlaps()
		# @AssociationType Interlocking.Overlaps
		# @AssociationMultiplicity 0..1
		# """contains all overlap elements"""
		self.___dangerPoints : DangerPoints = DangerPoints.DangerPoints()
		# @AssociationType Interlocking.DangerPoints
		# @AssociationMultiplicity 0..1
		# """contains all dangerPoints elements"""
		self.___destinationPoints : DestinationPoints = DestinationPoints.DestinationPoints()
		# @AssociationType Interlocking.DestinationPoints
		# @AssociationMultiplicity 0..1
		# """contains all destinationPoint elements"""
		self.___powerSuppliesIL : PowerSuppliesIL = PowerSuppliesIL.PowerSuppliesIL()
		# @AssociationType Interlocking.PowerSuppliesIL
		# @AssociationMultiplicity 0..1
		# """contains all powerSupplyIL elements"""

