#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking.EntityILref import EntityILref
from RailML.Interlocking.RouteActivationSection import RouteActivationSection
from RailML.Interlocking.SwitchAndPosition import SwitchAndPosition
from RailML.Interlocking.RouteEntry import RouteEntry
from RailML.Interlocking.RouteExit import RouteExit
from RailML.Interlocking.TrackAsset import TrackAsset
from typing import List

class Route(TrackAsset):
	"""We define a route as an entry- and exit plus the positions of intermediate switches. If there are no switches in the route, no switch positions can be defined. If one or more switches are encountered en route, either facing or trailing, the positions of these switches must be given. There can be multiple routes from entry to exit depending on the positions of the intermediate switches. The user is free to create different routes with the same entry,exit and same switch positions that differ only by the classifier. This allows one to distinguish for example a traction-route from no-traction-route"""
	def setLocksAutomatically(self, aLocksAutomatically : int):	#TODO DEFINED AS LONG
		self.___locksAutomatically = aLocksAutomatically

	def getLocksAutomatically(self) -> int:	#TODO DEFINED AS LONG
		return self.___locksAutomatically

	def setProcessingDelay(self, aProcessingDelay : int):	#TODO DEFINED AS duration
		self.___processingDelay = aProcessingDelay

	def getProcessingDelay(self) -> int:	#TODO DEFINED AS duration
		return self.___processingDelay

	def setProceedAspectDelay(self, aProceedAspectDelay : int):	#TODO DEFINED AS duration
		self.___proceedAspectDelay = aProceedAspectDelay

	def getProceedAspectDelay(self) -> int:	#TODO DEFINED AS duration
		return self.___proceedAspectDelay

	def setSignalClosureDelay(self, aSignalClosureDelay : int):	#TODO DEFINED AS duration
		self.___signalClosureDelay = aSignalClosureDelay

	def getSignalClosureDelay(self) -> int:	#TODO DEFINED AS duration
		return self.___signalClosureDelay

	def setApproachReleaseDelay(self, aApproachReleaseDelay : int):	#TODO DEFINED AS duration
		self.___approachReleaseDelay = aApproachReleaseDelay

	def getApproachReleaseDelay(self) -> int:	#TODO DEFINED AS duration
		return self.___approachReleaseDelay

	def setHandlesRouteType(self, *aHandlesRouteType : EntityILref):
		self._handlesRouteType = aHandlesRouteType

	def getHandlesRouteType(self) -> EntityILref:
		return self._handlesRouteType

	def setRouteActivationSection(self, *aRouteActivationSection : RouteActivationSection):
		self._routeActivationSection = aRouteActivationSection

	def getRouteActivationSection(self) -> RouteActivationSection:
		return self._routeActivationSection

	def setFacingSwitchInPosition(self, *aFacingSwitchInPosition : SwitchAndPosition):
		self._facingSwitchInPosition = aFacingSwitchInPosition

	def getFacingSwitchInPosition(self) -> SwitchAndPosition:
		return self._facingSwitchInPosition

	def setHasTvdSection(self, *aHasTvdSection : EntityILref):
		self._hasTvdSection = aHasTvdSection

	def getHasTvdSection(self) -> EntityILref:
		return self._hasTvdSection

	def setRouteEntry(self, aRouteEntry : RouteEntry):
		self._routeEntry = aRouteEntry

	def getRouteEntry(self) -> RouteEntry:
		return self._routeEntry

	def setHasReleaseGroup(self, *aHasReleaseGroup : EntityILref):
		self._hasReleaseGroup = aHasReleaseGroup

	def getHasReleaseGroup(self) -> EntityILref:
		return self._hasReleaseGroup

	def setSwitchPositionInDepartureTrack(self, *aSwitchPositionInDepartureTrack : SwitchAndPosition):
		self._switchPositionInDepartureTrack = aSwitchPositionInDepartureTrack

	def getSwitchPositionInDepartureTrack(self) -> SwitchAndPosition:
		return self._switchPositionInDepartureTrack

	def setRouteExit(self, aRouteExit : RouteExit):
		self._routeExit = aRouteExit

	def getRouteExit(self) -> RouteExit:
		return self._routeExit

	def setAdditionalRelation(self, *aAdditionalRelation : EntityILref):
		self._additionalRelation = aAdditionalRelation

	def getAdditionalRelation(self) -> EntityILref:
		return self._additionalRelation

	def __init__(self):
		self.___locksAutomatically : int = None	#TODO DEFINED AS LONG
		"""If true, the interlocking locks this route automatically and immediately after it was cleared. The operator has to intervene if he wishes to call another route. Automatikfahrstrasse in German, trace automatique in French. Note that this functionality is often part of the control system in which case this attribute should be omitted."""
		self.___processingDelay : int = None	#TODO DEFINED AS duration
		"""The delay in seconds between the moment the interlocking receives the route call and the moment the route the interlocking reports back that the route is locked, i.e. the processing time for setting that route."""
		self.___proceedAspectDelay : int = None	#TODO DEFINED AS duration
		"""The delay for the signal before it will change from closed to any proceed aspect."""
		self.___signalClosureDelay : int = None	#TODO DEFINED AS duration
		"""The delay for the signal after the conditions for proceed aspect are removed and the physical closure of the signal."""
		self.___approachReleaseDelay : int = None	#TODO DEFINED AS duration
		"""The delay between the request from signalman to release an already approached (definitely locked) route and the real release of associated elements of the route."""
		self._handlesRouteType : EntityILref = None
		"""The reference to the IM specific route type. This implies particular characteristics of the route dependent on the IM operational rules."""
		self._routeActivationSection : RouteActivationSection = None
		# @AssociationType Interlocking.RouteActivationSection*
		# @AssociationMultiplicity 0..*
		# """Description of the route activation, i.e. automatic setting or locking when the route entry is approached."""
		self._facingSwitchInPosition : SwitchAndPosition = None
		"""The tuple for each facing switch in the running path to unambiguously define the route containing the reference to the switch and its position."""
		self._hasTvdSection : EntityILref = None
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 0..*
		# """The reference to TVD section(s) within the running path of the route."""
		self._routeEntry : RouteEntry = None
		# @AssociationType Interlocking.RouteEntry
		# @AssociationMultiplicity 1
		# """Description of the start point of the route. This is normally a signal."""
		self._hasReleaseGroup : EntityILref = None
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 0..*
		# """The references to any partial routes which are to be released together within a group."""
		self._switchPositionInDepartureTrack : SwitchAndPosition = None
		# @AssociationType Interlocking.SwitchAndPosition*
		# @AssociationMultiplicity 0..*
		# @AssociationType Interlocking.SwitchAndPosition*
		# @AssociationMultiplicity 0..*
		# """The tuple for any switch in the track in rear of the start signal required for this route containing the reference to the switch and its position."""
		self._routeExit : RouteExit = None
		# @AssociationType Interlocking.RouteExit
		# @AssociationMultiplicity 1
		# """Description of the route destination point. In most cases the route destination is a signal or a buffer stop."""
		self._additionalRelation : EntityILref = None
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 0..*
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 0..*
		# """reference to any additional relation needed for signalling of this route"""

