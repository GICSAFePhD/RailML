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
	def SwitchesIL(self) -> SwitchesIL:	
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

	def create_TvdSections(self):
		if self.TvdSections == None:
			self.TvdSections = []
		self.TvdSections.append(TvdSections.TvdSections())
	def create_SwitchesIL(self):
		if self.SwitchesIL == None:
			self.SwitchesIL = []
		self.SwitchesIL.append(SwitchesIL.SwitchesIL())
	def create_DerailersIL(self):
		if self.DerailersIL == None:
			self.DerailersIL = []
		self.DerailersIL.append(DerailersIL.DerailersIL())
	def create_MovableCrossings(self):
		if self.MovableCrossings == None:
			self.MovableCrossings = []
		self.MovableCrossings.append(MovableCrossings.MovableCrossings())
	def create_LevelCrossingsIL(self):
		if self.LevelCrossingsIL == None:
			self.LevelCrossingsIL = []
		self.LevelCrossingsIL.append(LevelCrossingsIL.LevelCrossingsIL())
	def create_Keys(self):
		if self.Keys == None:
			self.Keys = []
		self.Keys.append(Keys.Keys())
	def create_KeyLocksIL(self):
		if self.KeyLocksIL == None:
			self.KeyLocksIL = []
		self.KeyLocksIL.append(KeyLocksIL.KeyLocksIL())
	def create_GenericDetectors(self):
		if self.GenericDetectors == None:
			self.GenericDetectors = []
		self.GenericDetectors.append(GenericDetectors.GenericDetectors())
	def create_SignalsIL(self):
		if self.SignalsIL == None:
			self.SignalsIL = []
		self.SignalsIL.append(SignalsIL.SignalsIL())
	def create_ATPdevices(self):
		if self.ATPdevices == None:
			self.ATPdevices = []
		self.ATPdevices.append(ATPdevices.ATPdevices())
	def create_Interfaces(self):
		if self.Interfaces == None:
			self.Interfaces = []
		self.Interfaces.append(Interfaces.Interfaces())
	def create_WorkZones(self):
		if self.WorkZones == None:
			self.WorkZones = []
		self.WorkZones.append(WorkZones.WorkZones())
	def create_LocalOperationAreas(self):
		if self.LocalOperationAreas == None:
			self.LocalOperationAreas = []
		self.LocalOperationAreas.append(LocalOperationAreas.LocalOperationAreas())
	def create_ShuntingZones(self):
		if self.ShuntingZones == None:
			self.ShuntingZones = []
		self.ShuntingZones.append(ShuntingZones.ShuntingZones())
	def create_PermissionZones(self):
		if self.PermissionZones == None:
			self.PermissionZones = []
		self.PermissionZones.append(PermissionZones.PermissionZones())
	def create_RouteReleaseGroupsAhead(self):
		if self.RouteReleaseGroupsAhead == None:
			self.RouteReleaseGroupsAhead = []
		self.RouteReleaseGroupsAhead.append(RouteReleaseGroupsAhead.RouteReleaseGroupsAhead())
	def create_RouteReleaseGroupsRear(self):
		if self.RouteReleaseGroupsRear == None:
			self.RouteReleaseGroupsRear = []
		self.RouteReleaseGroupsRear.append(RouteReleaseGroupsRear.RouteReleaseGroupsRear())
	def create_Routes(self):
		if self.Routes == None:
			self.Routes = []
		self.Routes.append(Routes.Routes())
	def create_ConflictingRoutes(self):
		if self.ConflictingRoutes == None:
			self.ConflictingRoutes = []
		self.ConflictingRoutes.append(ConflictingRoutes.ConflictingRoutes())
	def create_RouteRelations(self):
		if self.RouteRelations == None:
			self.RouteRelations = []
		self.RouteRelations.append(RouteRelations.RouteRelations())	
	def create_CombinedRoutes(self):
		if self.CombinedRoutes == None:
			self.CombinedRoutes = []
		self.CombinedRoutes.append(CombinedRoutes.CombinedRoutes())
	def create_Overlaps(self):
		if self.Overlaps == None:
			self.Overlaps = []
		self.Overlaps.append(Overlaps.Overlaps())
	def create_DangerPoints(self):
		if self.DangerPoints == None:
			self.DangerPoints = []
		self.DangerPoints.append(DangerPoints.DangerPoints())
	def create_DestinationPoints(self):
		if self.DestinationPoints == None:
			self.DestinationPoints = []
		self.DestinationPoints.append(DestinationPoints.DestinationPoints())
	def create_PowerSuppliesIL(self):
		if self.PowerSuppliesIL == None:
			self.PowerSuppliesIL = []
		self.PowerSuppliesIL.append(PowerSuppliesIL.PowerSuppliesIL())

	def __init__(self):
		self.___tvdSections : TvdSections = None
		# @AssociationType Interlocking.TvdSections
		# @AssociationMultiplicity 0..1
		# """contains all tvdSection elements"""
		self.___switchesIL : SwitchesIL = None
		# @AssociationType Interlocking.SwitchesIL
		# @AssociationMultiplicity 0..1
		# """contains all MovableElements of type SwitchIL"""
		self.___derailersIL : DerailersIL = None
		# @AssociationType Interlocking.DerailersIL
		# @AssociationMultiplicity 0..1
		# """contains all MovableElements of type DerailerIL"""
		self.___movableCrossings : MovableCrossings = None
		# @AssociationType Interlocking.MovableCrossings
		# @AssociationMultiplicity 0..1
		# """contains all MovableElements of type MovableCrossing"""
		self.___levelCrossingsIL : LevelCrossingsIL = None
		# @AssociationType Interlocking.LevelCrossingsIL
		# @AssociationMultiplicity 0..1
		# """contains all levelCrossingIL elements"""
		self.___keys : Keys = None
		# @AssociationType Interlocking.Keys
		# @AssociationMultiplicity 0..1
		# """contains all key elements"""
		self.___keyLocksIL : KeyLocksIL = None
		# @AssociationType Interlocking.KeyLocksIL
		# @AssociationMultiplicity 0..1
		# """contains all keyLockIL elements"""
		self.___genericDetectors : GenericDetectors = None
		# @AssociationType Interlocking.GenericDetectors
		# @AssociationMultiplicity 0..1
		# """contains all genericDetector elements"""
		self.___signalsIL : SignalsIL = None
		# @AssociationType Interlocking.SignalsIL
		# @AssociationMultiplicity 0..1
		# """contains all signalIL elements"""
		self.___atpDevices : ATPdevices = None
		# @AssociationType Interlocking.ATPdevices
		# @AssociationMultiplicity 0..1
		# """contains all atpDevice elements (not with railML3.1)"""
		self.___interfaces : Interfaces = None
		# @AssociationType Interlocking.Interfaces
		# @AssociationMultiplicity 0..1
		# """contains all interface elements"""
		self.___workZones : WorkZones = None
		# @AssociationType Interlocking.WorkZones
		# @AssociationMultiplicity 0..1
		# """contains all workZone elements"""
		self.___localOperationAreas : LocalOperationAreas = None
		# @AssociationType Interlocking.LocalOperationAreas
		# @AssociationMultiplicity 0..1
		# """contains all localOperationArea elements"""
		self.___shuntingZones : ShuntingZones = None
		# @AssociationType Interlocking.ShuntingZones
		# @AssociationMultiplicity 0..1
		# """contains all shuntingZone elements"""
		self.___permissionZones : PermissionZones = None
		# @AssociationType Interlocking.PermissionZones
		# @AssociationMultiplicity 0..1
		# """contains all permissionZone elements"""
		self.___routeReleaseGroupsAhead : RouteReleaseGroupsAhead = None
		# @AssociationType Interlocking.RouteReleaseGroupsAhead
		# @AssociationMultiplicity 0..1
		# """contains all routeReleaseGroupAhead elements"""
		self.___routeReleaseGroupsRear : RouteReleaseGroupsRear = None
		# @AssociationType Interlocking.RouteReleaseGroupsRear
		# @AssociationMultiplicity 0..1
		# """contains all routeReleaseGroupRear elements"""
		self.___routes : Routes = None
		# @AssociationType Interlocking.Routes
		# @AssociationMultiplicity 0..1
		# """contains all route elements"""
		self.___conflictingRoutes : ConflictingRoutes = None
		# @AssociationType Interlocking.ConflictingRoutes
		# @AssociationMultiplicity 0..1
		# """contains all conflictingRoute elements"""
		self.___routeRelations : RouteRelations = None
		# @AssociationType Interlocking.RouteRelations
		# @AssociationMultiplicity 0..1
		# """contains all routeRelation elements"""
		self.___combinedRoutes : CombinedRoutes = None
		# @AssociationType Interlocking.CombinedRoutes
		# @AssociationMultiplicity 0..1
		# """contains all combinedRoute elements"""
		self.___overlaps : Overlaps = None
		# @AssociationType Interlocking.Overlaps
		# @AssociationMultiplicity 0..1
		# """contains all overlap elements"""
		self.___dangerPoints : DangerPoints = None
		# @AssociationType Interlocking.DangerPoints
		# @AssociationMultiplicity 0..1
		# """contains all dangerPoints elements"""
		self.___destinationPoints : DestinationPoints = None
		# @AssociationType Interlocking.DestinationPoints
		# @AssociationMultiplicity 0..1
		# """contains all destinationPoint elements"""
		self.___powerSuppliesIL : PowerSuppliesIL = None
		# @AssociationType Interlocking.PowerSuppliesIL
		# @AssociationMultiplicity 0..1
		# """contains all powerSupplyIL elements"""