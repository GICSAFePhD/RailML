#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking.TvdSections import TvdSections
from RailML.Interlocking.SwitchesIL import SwitchesIL
from RailML.Interlocking.DerailersIL import DerailersIL
from RailML.Interlocking.MovableCrossings import MovableCrossings
from RailML.Interlocking.LevelCrossingsIL import LevelCrossingsIL
from RailML.Interlocking.Keys import Keys
from RailML.Interlocking.KeyLocksIL import KeyLocksIL
from RailML.Interlocking.GenericDetectors import GenericDetectors
from RailML.Interlocking.SignalsIL import SignalsIL
from RailML.Interlocking.ATPdevices import ATPdevices
from RailML.Interlocking.Interfaces import Interfaces
from RailML.Interlocking.WorkZones import WorkZones
from RailML.Interlocking.LocalOperationAreas import LocalOperationAreas
from RailML.Interlocking.ShuntingZones import ShuntingZones
from RailML.Interlocking.PermissionZones import PermissionZones
from RailML.Interlocking.RouteReleaseGroupsAhead import RouteReleaseGroupsAhead
from RailML.Interlocking.RouteReleaseGroupsRear import RouteReleaseGroupsRear
from RailML.Interlocking.Routes import Routes
from RailML.Interlocking.ConflictingRoutes import ConflictingRoutes
from RailML.Interlocking.RouteRelations import RouteRelations
from RailML.Interlocking.CombinedRoutes import CombinedRoutes
from RailML.Interlocking.Overlaps import Overlaps
from RailML.Interlocking.DangerPoints import DangerPoints
from RailML.Interlocking.DestinationPoints import DestinationPoints
from RailML.Interlocking.PowerSuppliesIL import PowerSuppliesIL
from RailML.Interlocking.EntityIL import EntityIL
from typing import List

class AssetsForIL(EntityIL):
	"""Container for assets used for operation of interlockings and controllers. They represent a more functional/logical view onto the railway network but depending on the hardware as defined in infrastructure domain.
	Assets in the container are owned by the railway network rather than by individual interlocking systems."""
	def setTvdSections(self, aTvdSections : TvdSections):
		self._tvdSections = aTvdSections

	def getTvdSections(self) -> TvdSections:
		return self._tvdSections

	def setSwitchesIL(self, aSwitchesIL : SwitchesIL):
		self._switchesIL = aSwitchesIL

	def getSwitchesIL(self) -> SwitchesIL:
		return self._switchesIL

	def setDerailersIL(self, aDerailersIL : DerailersIL):
		self._derailersIL = aDerailersIL

	def getDerailersIL(self) -> DerailersIL:
		return self._derailersIL

	def setMovableCrossings(self, aMovableCrossings : MovableCrossings):
		self._movableCrossings = aMovableCrossings

	def getMovableCrossings(self) -> MovableCrossings:
		return self._movableCrossings

	def setLevelCrossingsIL(self, aLevelCrossingsIL : LevelCrossingsIL):
		self._levelCrossingsIL = aLevelCrossingsIL

	def getLevelCrossingsIL(self) -> LevelCrossingsIL:
		return self._levelCrossingsIL

	def setKeys(self, aKeys : Keys):
		self._keys = aKeys

	def getKeys(self) -> Keys:
		return self._keys

	def setKeyLocksIL(self, aKeyLocksIL : KeyLocksIL):
		self._keyLocksIL = aKeyLocksIL

	def getKeyLocksIL(self) -> KeyLocksIL:
		return self._keyLocksIL

	def setGenericDetectors(self, aGenericDetectors : GenericDetectors):
		self._genericDetectors = aGenericDetectors

	def getGenericDetectors(self) -> GenericDetectors:
		return self._genericDetectors

	def setSignalsIL(self, aSignalsIL : SignalsIL):
		self._signalsIL = aSignalsIL

	def getSignalsIL(self) -> SignalsIL:
		return self._signalsIL

	def setAtpDevices(self, aAtpDevices : ATPdevices):
		self._atpDevices = aAtpDevices

	def getAtpDevices(self) -> ATPdevices:
		return self._atpDevices

	def setInterfaces(self, aInterfaces : Interfaces):
		self._interfaces = aInterfaces

	def getInterfaces(self) -> Interfaces:
		return self._interfaces

	def setWorkZones(self, aWorkZones : WorkZones):
		self._workZones = aWorkZones

	def getWorkZones(self) -> WorkZones:
		return self._workZones

	def setLocalOperationAreas(self, aLocalOperationAreas : LocalOperationAreas):
		self._localOperationAreas = aLocalOperationAreas

	def getLocalOperationAreas(self) -> LocalOperationAreas:
		return self._localOperationAreas

	def setShuntingZones(self, aShuntingZones : ShuntingZones):
		self._shuntingZones = aShuntingZones

	def getShuntingZones(self) -> ShuntingZones:
		return self._shuntingZones

	def setPermissionZones(self, aPermissionZones : PermissionZones):
		self._permissionZones = aPermissionZones

	def getPermissionZones(self) -> PermissionZones:
		return self._permissionZones

	def setRouteReleaseGroupsAhead(self, aRouteReleaseGroupsAhead : RouteReleaseGroupsAhead):
		self._routeReleaseGroupsAhead = aRouteReleaseGroupsAhead

	def getRouteReleaseGroupsAhead(self) -> RouteReleaseGroupsAhead:
		return self._routeReleaseGroupsAhead

	def setRouteReleaseGroupsRear(self, aRouteReleaseGroupsRear : RouteReleaseGroupsRear):
		self._routeReleaseGroupsRear = aRouteReleaseGroupsRear

	def getRouteReleaseGroupsRear(self) -> RouteReleaseGroupsRear:
		return self._routeReleaseGroupsRear

	def setRoutes(self, aRoutes : Routes):
		self._routes = aRoutes

	def getRoutes(self) -> Routes:
		return self._routes

	def setConflictingRoutes(self, aConflictingRoutes : ConflictingRoutes):
		self._conflictingRoutes = aConflictingRoutes

	def getConflictingRoutes(self) -> ConflictingRoutes:
		return self._conflictingRoutes

	def setRouteRelations(self, aRouteRelations : RouteRelations):
		self._routeRelations = aRouteRelations

	def getRouteRelations(self) -> RouteRelations:
		return self._routeRelations

	def setCombinedRoutes(self, aCombinedRoutes : CombinedRoutes):
		self._combinedRoutes = aCombinedRoutes

	def getCombinedRoutes(self) -> CombinedRoutes:
		return self._combinedRoutes

	def setOverlaps(self, aOverlaps : Overlaps):
		self._overlaps = aOverlaps

	def getOverlaps(self) -> Overlaps:
		return self._overlaps

	def setDangerPoints(self, aDangerPoints : DangerPoints):
		self._dangerPoints = aDangerPoints

	def getDangerPoints(self) -> DangerPoints:
		return self._dangerPoints

	def setDestinationPoints(self, aDestinationPoints : DestinationPoints):
		self._destinationPoints = aDestinationPoints

	def getDestinationPoints(self) -> DestinationPoints:
		return self._destinationPoints

	def setPowerSuppliesIL(self, aPowerSuppliesIL : PowerSuppliesIL):
		self._powerSuppliesIL = aPowerSuppliesIL

	def getPowerSuppliesIL(self) -> PowerSuppliesIL:
		return self._powerSuppliesIL

	def __init__(self):
		self._tvdSections : TvdSections = None
		# @AssociationType Interlocking.TvdSections
		# @AssociationMultiplicity 0..1
		# """contains all tvdSection elements"""
		self._switchesIL : SwitchesIL = None
		# @AssociationType Interlocking.SwitchesIL
		# @AssociationMultiplicity 0..1
		# """contains all MovableElements of type SwitchIL"""
		self._derailersIL : DerailersIL = None
		# @AssociationType Interlocking.DerailersIL
		# @AssociationMultiplicity 0..1
		# """contains all MovableElements of type DerailerIL"""
		self._movableCrossings : MovableCrossings = None
		# @AssociationType Interlocking.MovableCrossings
		# @AssociationMultiplicity 0..1
		# """contains all MovableElements of type MovableCrossing"""
		self._levelCrossingsIL : LevelCrossingsIL = None
		# @AssociationType Interlocking.LevelCrossingsIL
		# @AssociationMultiplicity 0..1
		# """contains all levelCrossingIL elements"""
		self._keys : Keys = None
		# @AssociationType Interlocking.Keys
		# @AssociationMultiplicity 0..1
		# """contains all key elements"""
		self._keyLocksIL : KeyLocksIL = None
		# @AssociationType Interlocking.KeyLocksIL
		# @AssociationMultiplicity 0..1
		# """contains all keyLockIL elements"""
		self._genericDetectors : GenericDetectors = None
		# @AssociationType Interlocking.GenericDetectors
		# @AssociationMultiplicity 0..1
		# """contains all genericDetector elements"""
		self._signalsIL : SignalsIL = None
		# @AssociationType Interlocking.SignalsIL
		# @AssociationMultiplicity 0..1
		# """contains all signalIL elements"""
		self._atpDevices : ATPdevices = None
		# @AssociationType Interlocking.ATPdevices
		# @AssociationMultiplicity 0..1
		# """contains all atpDevice elements (not with railML3.1)"""
		self._interfaces : Interfaces = None
		# @AssociationType Interlocking.Interfaces
		# @AssociationMultiplicity 0..1
		# """contains all interface elements"""
		self._workZones : WorkZones = None
		# @AssociationType Interlocking.WorkZones
		# @AssociationMultiplicity 0..1
		# """contains all workZone elements"""
		self._localOperationAreas : LocalOperationAreas = None
		# @AssociationType Interlocking.LocalOperationAreas
		# @AssociationMultiplicity 0..1
		# """contains all localOperationArea elements"""
		self._shuntingZones : ShuntingZones = None
		# @AssociationType Interlocking.ShuntingZones
		# @AssociationMultiplicity 0..1
		# """contains all shuntingZone elements"""
		self._permissionZones : PermissionZones = None
		# @AssociationType Interlocking.PermissionZones
		# @AssociationMultiplicity 0..1
		# """contains all permissionZone elements"""
		self._routeReleaseGroupsAhead : RouteReleaseGroupsAhead = None
		# @AssociationType Interlocking.RouteReleaseGroupsAhead
		# @AssociationMultiplicity 0..1
		# """contains all routeReleaseGroupAhead elements"""
		self._routeReleaseGroupsRear : RouteReleaseGroupsRear = None
		# @AssociationType Interlocking.RouteReleaseGroupsRear
		# @AssociationMultiplicity 0..1
		# """contains all routeReleaseGroupRear elements"""
		self._routes : Routes = None
		# @AssociationType Interlocking.Routes
		# @AssociationMultiplicity 0..1
		# """contains all route elements"""
		self._conflictingRoutes : ConflictingRoutes = None
		# @AssociationType Interlocking.ConflictingRoutes
		# @AssociationMultiplicity 0..1
		# """contains all conflictingRoute elements"""
		self._routeRelations : RouteRelations = None
		# @AssociationType Interlocking.RouteRelations
		# @AssociationMultiplicity 0..1
		# """contains all routeRelation elements"""
		self._combinedRoutes : CombinedRoutes = None
		# @AssociationType Interlocking.CombinedRoutes
		# @AssociationMultiplicity 0..1
		# """contains all combinedRoute elements"""
		self._overlaps : Overlaps = None
		# @AssociationType Interlocking.Overlaps
		# @AssociationMultiplicity 0..1
		# """contains all overlap elements"""
		self._dangerPoints : DangerPoints = None
		# @AssociationType Interlocking.DangerPoints
		# @AssociationMultiplicity 0..1
		# """contains all dangerPoints elements"""
		self._destinationPoints : DestinationPoints = None
		# @AssociationType Interlocking.DestinationPoints
		# @AssociationMultiplicity 0..1
		# """contains all destinationPoint elements"""
		self._powerSuppliesIL : PowerSuppliesIL = None
		# @AssociationType Interlocking.PowerSuppliesIL
		# @AssociationMultiplicity 0..1
		# """contains all powerSupplyIL elements"""

