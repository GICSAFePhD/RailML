#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure import Balises, Borders, BufferStops, Crossings, DerailersIS, Electrifications, KeyLocksIS, LevelCrossingsIS, Lines
from RailML.Infrastructure import LoadingGauges, OperationalPoints, OverCrossings, Platforms, RestrictionAreas, ServiceSections, SignalsIS
from RailML.Infrastructure import Speeds, StoppingPlaces, SwitchesIS, Tracks, TrackBeds, TrackGauges, TrainDetectionElements, TrainProtectionElements
from RailML.Infrastructure import TrainRadios, UnderCrossings, WeightLimits
from typing import List

class FunctionalInfrastructure(object):
	"""This is the top level element for railML3 functional infrastructure model."""
	@property
	def Balises(self) -> Balises:
		return self.___balises
	@property
	def Borders(self) -> Borders:
		return self.___borders
	@property
	def BufferStops(self) -> BufferStops:
		return self.___bufferStops
	@property
	def Crossings(self) -> Crossings:
		return self.___crossings
	@property
	def DerailersIS(self) -> DerailersIS:
		return self.___derailersIS
	@property
	def Electrifications(self) -> Electrifications:
		return self.___electrifications
	@property
	def KeyLocksIS(self) -> KeyLocksIS:
		return self.___keyLocksIS
	@property
	def LevelCrossingsIS(self) -> LevelCrossingsIS:
		return self.___levelCrossingsIS
	@property
	def Lines(self) -> Lines:
		return self.___lines
	@property
	def LoadingGauges(self) -> LoadingGauges:
		return self.___loadingGauges
	@property
	def OperationalPoints(self) -> OperationalPoints:
		return self.___operationalPoints
	@property
	def OverCrossings(self) -> OverCrossings:
		return self.___overCrossings
	@property
	def Platforms(self) -> Platforms:
		return self.___platforms
	@property
	def RestrictionAreas(self) -> RestrictionAreas:
		return self.___restrictionAreas
	@property
	def ServiceSections(self) -> ServiceSections:
		return self.___serviceSections
	@property
	def SignalsIS(self) -> SignalsIS:
		return self.___signalsIS
	@property
	def Speeds(self) -> Speeds:
		return self.___speeds
	@property
	def StoppingPlaces(self) -> StoppingPlaces:
		return self.___stoppingPlaces
	@property
	def SwitchesIS(self) -> SwitchesIS:
		return self.___switchesIS
	@property
	def Tracks(self) -> Tracks:
		return self.___tracks
	@property
	def TrackBeds(self) -> TrackBeds:
		return self.___trackBeds
	@property
	def TrackGauges(self) -> TrackGauges:
		return self.___trackGauges
	@property
	def TrainDetectionElements(self) -> TrainDetectionElements:
		return self.___trainDetectionElements
	@property
	def TrainProtectionElements(self) -> TrainProtectionElements:
		return self.___trainProtectionElements
	@property
	def TrainRadios(self) -> TrainRadios:
		return self.___trainRadios
	@property
	def UnderCrossings(self) -> UnderCrossings:
		return self.___underCrossings
	@property
	def WeightLimits(self) -> WeightLimits:
		return self.___weightLimits

	Balises.setter
	def Balises(self, aBalises : Balises):
		self.___balises = aBalises
	Borders.setter
	def Borders(self, aBorders : Borders):
		self.___borders = aBorders
	BufferStops.setter
	def BufferStops(self, aBufferStops : BufferStops):
		self.___bufferStops = aBufferStops
	Crossings.setter
	def Crossings(self, aCrossings : Crossings):
		self.___crossings = aCrossings
	DerailersIS.setter
	def DerailersIS(self, aDerailersIS : DerailersIS):
		self.___derailersIS = aDerailersIS
	Electrifications.setter
	def Electrifications(self, aElectrifications : Electrifications):
		self.___electrifications = aElectrifications
	KeyLocksIS.setter
	def KeyLocksIS(self, aKeyLocksIS : KeyLocksIS):
		self.___keyLocksIS = aKeyLocksIS
	LevelCrossingsIS.setter
	def LevelCrossingsIS(self, aLevelCrossingsIS : LevelCrossingsIS):
		self.___levelCrossingsIS = aLevelCrossingsIS
	Lines.setter
	def Lines(self, aLines : Lines):
		self.___lines = aLines
	LoadingGauges.setter
	def LoadingGauges(self, aLoadingGauges : LoadingGauges):
		self.___loadingGauges = aLoadingGauges
	OperationalPoints.setter
	def OperationalPoints(self, aOperationalPoints : OperationalPoints):
		self.___operationalPoints = aOperationalPoints
	OverCrossings.setter
	def OverCrossings(self, aOverCrossings : OverCrossings):
		self.___overCrossings = aOverCrossings
	Platforms.setter
	def Platforms(self, aPlatforms : Platforms):
		self.___platforms = aPlatforms
	RestrictionAreas.setter
	def RestrictionAreas(self, aRestrictionAreas : RestrictionAreas):
		self.___restrictionAreas = aRestrictionAreas
	ServiceSections.setter
	def ServiceSections(self, aServiceSections : ServiceSections):
		self.___serviceSections = aServiceSections
	SignalsIS.setter
	def SignalsIS(self, aSignalsIS : SignalsIS):
		self.___signalsIS = aSignalsIS
	Speeds.setter
	def Speeds(self, aSpeeds : Speeds):
		self.___speeds = aSpeeds
	StoppingPlaces.setter
	def StoppingPlaces(self, aStoppingPlaces : StoppingPlaces):
		self.___stoppingPlaces = aStoppingPlaces
	SwitchesIS.setter
	def SwitchesIS(self, aSwitchesIS : SwitchesIS):
		self.___switchesIS = aSwitchesIS
	Tracks.setter
	def Tracks(self, aTracks : Tracks):
		self.___tracks = aTracks
	TrackBeds.setter
	def TrackBeds(self, aTrackBeds : TrackBeds):
		self.___trackBeds = aTrackBeds
	TrackGauges.setter
	def TrackGauges(self, aTrackGauges : TrackGauges):
		self.___trackGauges = aTrackGauges
	TrainDetectionElements.setter
	def TrainDetectionElements(self, aTrainDetectionElements : TrainDetectionElements):
		self.___trainDetectionElements = aTrainDetectionElements
	TrainProtectionElements.setter
	def TrainProtectionElements(self, aTrainProtectionElements : TrainProtectionElements):
		self.___trainProtectionElements = aTrainProtectionElements
	TrainRadios.setter
	def TrainRadios(self, aTrainRadios : TrainRadios):
		self.___trainRadios = aTrainRadios
	UnderCrossings.setter
	def UnderCrossings(self, aUnderCrossings : UnderCrossings):
		self.___underCrossings = aUnderCrossings
	WeightLimits.setter
	def WeightLimits(self, aWeightLimits : WeightLimits):
		self.___weightLimits = aWeightLimits


	def __init__(self):
		self.___balises : Balises = Balises.Balises()
		# @AssociationType Infrastructure.Balises
		# @AssociationMultiplicity 0..1
		# """container element for all balise (and balise group) elements"""
		self.___borders : Borders = Borders.Borders()
		# @AssociationType Infrastructure.Borders
		# @AssociationMultiplicity 0..1
		# """container element for all border elements"""
		self.___bufferStops : BufferStops = BufferStops.BufferStops()
		# @AssociationType Infrastructure.BufferStops
		# @AssociationMultiplicity 0..1
		# """container element for all bufferStop elements"""
		self.___crossings : Crossings = Crossings.Crossings()
		# @AssociationType Infrastructure.Crossings
		# @AssociationMultiplicity 0..1
		# """container element for all crossing elements"""
		self.___derailersIS : DerailersIS = DerailersIS.DerailersIS()
		# @AssociationType Infrastructure.DerailersIS
		# @AssociationMultiplicity 0..1
		# """container element for all derailer elements"""
		self.___electrifications : Electrifications = Electrifications.Electrifications()
		# @AssociationType Infrastructure.Electrifications
		# @AssociationMultiplicity 0..1
		# """container element for all electrification elements incl. electrification system components"""
		self.___keyLocksIS : KeyLocksIS = KeyLocksIS.KeyLocksIS()
		# @AssociationType Infrastructure.KeyLocksIS
		# @AssociationMultiplicity 0..1
		# """container element for all keyLock elements"""
		self.___levelCrossingsIS : LevelCrossingsIS = LevelCrossingsIS.LevelCrossingsIS()
		# @AssociationType Infrastructure.LevelCrossingsIS
		# @AssociationMultiplicity 0..1
		# """container element for all levelCrossing elements"""
		self.___lines : Lines = Lines.Lines()
		# @AssociationType Infrastructure.Lines
		# @AssociationMultiplicity 0..1
		# """container element for all line (section) elements"""
		self.___loadingGauges : LoadingGauges = LoadingGauges.LoadingGauges()
		# @AssociationType Infrastructure.LoadingGauges
		# @AssociationMultiplicity 0..1
		# """container element for all loadingGauge elements"""
		self.___operationalPoints : OperationalPoints = OperationalPoints.OperationalPoints()
		# @AssociationType Infrastructure.OperationalPoints
		# @AssociationMultiplicity 0..1
		# """container element for all operationalPoint elements"""
		self.___overCrossings : OverCrossings = OverCrossings.OverCrossings()
		# @AssociationType Infrastructure.OverCrossings
		# @AssociationMultiplicity 0..1
		# """container element for all overCrossing elements"""
		self.___platforms : Platforms = Platforms.Platforms()
		# @AssociationType Infrastructure.Platforms
		# @AssociationMultiplicity 0..1
		# """container element for all platform (and platform edge) elements"""
		self.___restrictionAreas : RestrictionAreas = RestrictionAreas.RestrictionAreas()
		# @AssociationType Infrastructure.RestrictionAreas
		# @AssociationMultiplicity 0..1
		# """container element for all restrictionArea elements"""
		self.___serviceSections : ServiceSections = ServiceSections.ServiceSections()
		# @AssociationType Infrastructure.ServiceSections
		# @AssociationMultiplicity 0..1
		# """container element for all serviceSection elements"""
		self.___signalsIS : SignalsIS = SignalsIS.SignalsIS()
		# @AssociationType Infrastructure.SignalsIS
		# @AssociationMultiplicity 0..1
		# """container element for all signal (and panel) elements"""
		self.___speeds : Speeds = Speeds.Speeds()
		# @AssociationType Infrastructure.Speeds
		# @AssociationMultiplicity 0..1
		# """container element for all line/track speed related elements"""
		self.___stoppingPlaces : StoppingPlaces = StoppingPlaces.StoppingPlaces()
		# @AssociationType Infrastructure.StoppingPlaces
		# @AssociationMultiplicity 0..1
		# """container element for all stoppingPlace elements"""
		self.___switchesIS : SwitchesIS = SwitchesIS.SwitchesIS()
		# @AssociationType Infrastructure.SwitchesIS
		# @AssociationMultiplicity 0..1
		# """container element for all switch elements"""
		self.___tracks : Tracks = Tracks.Tracks()
		# @AssociationType Infrastructure.Tracks
		# @AssociationMultiplicity 0..1
		# """container element for all track elements"""
		self.___trackBeds : TrackBeds = TrackBeds.TrackBeds()
		# @AssociationType Infrastructure.TrackBeds
		# @AssociationMultiplicity 0..1
		# """container element for all trackBed elements"""
		self.___trackGauges : TrackGauges = TrackGauges.TrackGauges()
		# @AssociationType Infrastructure.TrackGauges
		# @AssociationMultiplicity 0..1
		# """container element for all trackGauge elements"""
		self.___trainDetectionElements : TrainDetectionElements = TrainDetectionElements.TrainDetectionElements()
		# @AssociationType Infrastructure.TrainDetectionElements
		# @AssociationMultiplicity 0..1
		# """container element for all trainDetectionElement elements"""
		self.___trainProtectionElements : TrainProtectionElements = TrainProtectionElements.TrainProtectionElements()
		# @AssociationType Infrastructure.TrainProtectionElements
		# @AssociationMultiplicity 0..1
		# """container element for all trainProtectionElement elements"""
		self.___trainRadios : TrainRadios = TrainRadios.TrainRadios()
		# @AssociationType Infrastructure.TrainRadios
		# @AssociationMultiplicity 0..1
		# """container element for all trainRadio elements"""
		self.___underCrossings : UnderCrossings = UnderCrossings.UnderCrossings()
		# @AssociationType Infrastructure.UnderCrossings
		# @AssociationMultiplicity 0..1
		# """container element for all underCrossing elements"""
		self.___weightLimits : WeightLimits = WeightLimits.WeightLimits()
		# @AssociationType Infrastructure.WeightLimits
		# @AssociationMultiplicity 0..1
		# """container element for all weightLimit (axle load, meterload) elements"""

