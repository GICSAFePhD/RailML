#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Interlocking import EntityILref, RouteActivationSection, SwitchAndPosition, RouteEntry, RouteExit, TrackAsset
from typing import List, NewType

Long = NewType("Long", int)
Duration = NewType("Duration", int)

class Route(TrackAsset.TrackAsset):
	"""We define a route as an entry- and exit plus the positions of intermediate switches. If there are no switches in the route, no switch positions can be defined. If one or more switches are encountered en route, either facing or trailing, the positions of these switches must be given. There can be multiple routes from entry to exit depending on the positions of the intermediate switches. The user is free to create different routes with the same entry,exit and same switch positions that differ only by the classifier. This allows one to distinguish for example a traction-route from no-traction-route"""
	@property
	def LocksAutomatically(self) -> Long:
		return self.___locksAutomatically
	@property
	def ProcessingDelay(self) -> Duration:
		return self.___processingDelay
	@property
	def ProceedAspectDelay(self) -> Duration:
		return self.___proceedAspectDelay
	@property
	def SignalClosureDelay(self) -> Duration:
		return self.___signalClosureDelay
	@property
	def ApproachReleaseDelay(self) -> Duration:
		return self.___approachReleaseDelay
	@property
	def HandlesRouteType(self) -> EntityILref:
		return self.___handlesRouteType
	@property
	def RouteActivationSection(self) -> RouteActivationSection:
		return self.___routeActivationSection
	@property
	def FacingSwitchInPosition(self) -> SwitchAndPosition:
		return self.___facingSwitchInPosition
	@property
	def HasTvdSection(self) -> EntityILref:
		return self.___hasTvdSection
	@property
	def RouteEntry(self) -> RouteEntry:
		return self.___routeEntry
	@property
	def HasReleaseGroup(self) -> EntityILref:
		return self.___hasReleaseGroup
	@property
	def SwitchPositionInDepartureTrack(self) -> SwitchAndPosition:
		return self.___switchPositionInDepartureTrack
	@property
	def RouteExit(self) -> RouteExit:
		return self.___routeExit
	@property
	def AdditionalRelation(self) -> EntityILref:
		return self.___additionalRelation

	@LocksAutomatically.setter
	def LocksAutomatically(self, aLocksAutomatically : Long):
		self.___locksAutomatically = aLocksAutomatically
	@ProcessingDelay.setter
	def ProcessingDelay(self, aProcessingDelay : Duration):
		self.___processingDelay = aProcessingDelay
	@ProceedAspectDelay.setter
	def ProceedAspectDelay(self, aProceedAspectDelay : Duration):
		self.___proceedAspectDelay = aProceedAspectDelay
	@SignalClosureDelay.setter
	def SignalClosureDelay(self, aSignalClosureDelay : Duration):
		self.___signalClosureDelay = aSignalClosureDelay
	@ApproachReleaseDelay.setter
	def ApproachReleaseDelay(self, aApproachReleaseDelay : Duration):
		self.___approachReleaseDelay = aApproachReleaseDelay
	@HandlesRouteType.setter
	def HandlesRouteType(self, aHandlesRouteType : EntityILref):	# TODO *aHandlesRouteType
		self.___handlesRouteType = aHandlesRouteType
	@RouteActivationSection.setter
	def RouteActivationSection(self, aRouteActivationSection : RouteActivationSection):	# TODO *aRouteActivationSection
		self.___routeActivationSection = aRouteActivationSection
	@FacingSwitchInPosition.setter
	def FacingSwitchInPosition(self, aFacingSwitchInPosition : SwitchAndPosition): # TODO *aFacingSwitchInPosition
		self.___facingSwitchInPosition = aFacingSwitchInPosition
	@HasTvdSection.setter
	def HasTvdSection(self, aHasTvdSection : EntityILref):	# TODO *aHasTvdSection
		self.___hasTvdSection = aHasTvdSection
	@RouteEntry.setter
	def RouteEntry(self, aRouteEntry : RouteEntry):
		self.___routeEntry = aRouteEntry
	@HasReleaseGroup.setter
	def HasReleaseGroup(self, aHasReleaseGroup : EntityILref):	# TODO *aHasReleaseGroup
		self.___hasReleaseGroup = aHasReleaseGroup
	@SwitchPositionInDepartureTrack.setter
	def SwitchPositionInDepartureTrack(self, aSwitchPositionInDepartureTrack : SwitchAndPosition):	# TODO *aSwitchPositionInDepartureTrack
		self.___switchPositionInDepartureTrack = aSwitchPositionInDepartureTrack
	@RouteExit.setter
	def RouteExit(self, aRouteExit : RouteExit):
		self.___routeExit = aRouteExit
	@AdditionalRelation.setter
	def AdditionalRelation(self, aAdditionalRelation : EntityILref):	# TODO *aAdditionalRelation
		self.___additionalRelation = aAdditionalRelation

	def create_HandlesRouteType(self):
		if self.HandlesRouteType == None:
			self.HandlesRouteType = []
		self.HandlesRouteType.append(EntityILref.EntityILref())
	def create_RouteActivationSection(self):
		if self.RouteActivationSection == None:
			self.RouteActivationSection = []
		self.RouteActivationSection.append(RouteActivationSection.RouteActivationSection())
	def create_FacingSwitchInPosition(self):
		if self.FacingSwitchInPosition == None:
			self.FacingSwitchInPosition = []
		self.FacingSwitchInPosition.append(SwitchAndPosition.SwitchAndPosition())
	def create_HasTvdSection(self):
		if self.HasTvdSection == None:
			self.HasTvdSection = []
		self.HasTvdSection.append(EntityILref.EntityILref())
	def create_RouteEntry(self):
		self.RouteEntry.append(RouteEntry.RouteEntry())
	def create_HasReleaseGroup(self):
		if self.HasReleaseGroup == None:
			self.HasReleaseGroup = []
		self.HasReleaseGroup.append(EntityILref.EntityILref())
	def create_SwitchPositionInDepartureTrack(self):
		if self.SwitchPositionInDepartureTrack == None:
			self.SwitchPositionInDepartureTrack = []
		self.SwitchPositionInDepartureTrack.append(SwitchAndPosition.SwitchAndPosition())
	def create_RouteExit(self):
		self.RouteExit.append(RouteExit.RouteExit())
	def create_AdditionalRelation(self):
		if self.AdditionalRelation == None:
			self.AdditionalRelation = []
		self.AdditionalRelation.append(EntityILref.EntityILref())

	def __init__(self):
		super().__init__()
		self.___locksAutomatically : Long = 0
		"""If true, the interlocking locks this route automatically and immediately after it was cleared. The operator has to intervene if he wishes to call another route. Automatikfahrstrasse in German, trace automatique in French. Note that this functionality is often part of the control system in which case this attribute should be omitted."""
		self.___processingDelay : Duration = 0
		"""The delay in seconds between the moment the interlocking receives the route call and the moment the route the interlocking reports back that the route is locked, i.e. the processing time for setting that route."""
		self.___proceedAspectDelay : Duration = 0
		"""The delay for the signal before it will change from closed to any proceed aspect."""
		self.___signalClosureDelay : Duration = 0
		"""The delay for the signal after the conditions for proceed aspect are removed and the physical closure of the signal."""
		self.___approachReleaseDelay : Duration = 0
		"""The delay between the request from signalman to release an already approached (definitely locked) route and the real release of associated elements of the route."""
		self.___handlesRouteType : EntityILref = EntityILref.EntityILref()
		"""The reference to the IM specific route type. This implies particular characteristics of the route dependent on the IM operational rules."""
		self.___routeActivationSection : RouteActivationSection = RouteActivationSection.RouteActivationSection()
		# @AssociationType Interlocking.RouteActivationSection*
		# @AssociationMultiplicity 0..*
		# """Description of the route activation, i.e. automatic setting or locking when the route entry is approached."""
		self.___facingSwitchInPosition : SwitchAndPosition = SwitchAndPosition.SwitchAndPosition()
		"""The tuple for each facing switch in the running path to unambiguously define the route containing the reference to the switch and its position."""
		self.___hasTvdSection : EntityILref = EntityILref.EntityILref()
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 0..*
		# """The reference to TVD section(s) within the running path of the route."""
		self.___routeEntry : RouteEntry = RouteEntry.RouteEntry()
		# @AssociationType Interlocking.RouteEntry
		# @AssociationMultiplicity 1
		# """Description of the start point of the route. This is normally a signal."""
		self.___hasReleaseGroup : EntityILref = EntityILref.EntityILref()
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 0..*
		# """The references to any partial routes which are to be released together within a group."""
		self.___switchPositionInDepartureTrack : SwitchAndPosition = None
		# @AssociationType Interlocking.SwitchAndPosition*
		# @AssociationMultiplicity 0..*
		# @AssociationType Interlocking.SwitchAndPosition*
		# @AssociationMultiplicity 0..*
		# """The tuple for any switch in the track in rear of the start signal required for this route containing the reference to the switch and its position."""
		self.___routeExit : RouteExit = None
		# @AssociationType Interlocking.RouteExit
		# @AssociationMultiplicity 1
		# """Description of the route destination point. In most cases the route destination is a signal or a buffer stop."""
		self.___additionalRelation : EntityILref = None
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 0..*
		# @AssociationType Interlocking.EntityILref*
		# @AssociationMultiplicity 0..*
		# """reference to any additional relation needed for signalling of this route"""