#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Infrastructure.Balises import Balises
from RailML.Infrastructure.Borders import Borders
from RailML.Infrastructure.BufferStops import BufferStops
from RailML.Infrastructure.Crossings import Crossings
from RailML.Infrastructure.DerailersIS import DerailersIS
from RailML.Infrastructure.Electrifications import Electrifications
from RailML.Infrastructure.KeyLocksIS import KeyLocksIS
from RailML.Infrastructure.LevelCrossingsIS import LevelCrossingsIS
from RailML.Infrastructure.Lines import Lines
from RailML.Infrastructure.LoadingGauges import LoadingGauges
from RailML.Infrastructure.OperationalPoints import OperationalPoints
from RailML.Infrastructure.OverCrossings import OverCrossings
from RailML.Infrastructure.Platforms import Platforms
from RailML.Infrastructure.RestrictionAreas import RestrictionAreas
from RailML.Infrastructure.ServiceSections import ServiceSections
from RailML.Infrastructure.SignalsIS import SignalsIS
from RailML.Infrastructure.Speeds import Speeds
from RailML.Infrastructure.StoppingPlaces import StoppingPlaces
from RailML.Infrastructure.SwitchesIS import SwitchesIS
from RailML.Infrastructure.Tracks import Tracks
from RailML.Infrastructure.TrackBeds import TrackBeds
from RailML.Infrastructure.TrackGauges import TrackGauges
from RailML.Infrastructure.TrainDetectionElements import TrainDetectionElements
from RailML.Infrastructure.TrainProtectionElements import TrainProtectionElements
from RailML.Infrastructure.TrainRadios import TrainRadios
from RailML.Infrastructure.UnderCrossings import UnderCrossings
from RailML.Infrastructure.WeightLimits import WeightLimits
from typing import List

class FunctionalInfrastructure(object):
	"""This is the top level element for railML3 functional infrastructure model."""
	def setBalises(self, aBalises : Balises):
		self._balises = aBalises

	def getBalises(self) -> Balises:
		return self._balises

	def setBorders(self, aBorders : Borders):
		self._borders = aBorders

	def getBorders(self) -> Borders:
		return self._borders

	def setBufferStops(self, aBufferStops : BufferStops):
		self._bufferStops = aBufferStops

	def getBufferStops(self) -> BufferStops:
		return self._bufferStops

	def setCrossings(self, aCrossings : Crossings):
		self._crossings = aCrossings

	def getCrossings(self) -> Crossings:
		return self._crossings

	def setDerailersIS(self, aDerailersIS : DerailersIS):
		self._derailersIS = aDerailersIS

	def getDerailersIS(self) -> DerailersIS:
		return self._derailersIS

	def setElectrifications(self, aElectrifications : Electrifications):
		self._electrifications = aElectrifications

	def getElectrifications(self) -> Electrifications:
		return self._electrifications

	def setKeyLocksIS(self, aKeyLocksIS : KeyLocksIS):
		self._keyLocksIS = aKeyLocksIS

	def getKeyLocksIS(self) -> KeyLocksIS:
		return self._keyLocksIS

	def setLevelCrossingsIS(self, aLevelCrossingsIS : LevelCrossingsIS):
		self._levelCrossingsIS = aLevelCrossingsIS

	def getLevelCrossingsIS(self) -> LevelCrossingsIS:
		return self._levelCrossingsIS

	def setLines(self, aLines : Lines):
		self._lines = aLines

	def getLines(self) -> Lines:
		return self._lines

	def setLoadingGauges(self, aLoadingGauges : LoadingGauges):
		self._loadingGauges = aLoadingGauges

	def getLoadingGauges(self) -> LoadingGauges:
		return self._loadingGauges

	def setOperationalPoints(self, aOperationalPoints : OperationalPoints):
		self._operationalPoints = aOperationalPoints

	def getOperationalPoints(self) -> OperationalPoints:
		return self._operationalPoints

	def setOverCrossings(self, aOverCrossings : OverCrossings):
		self._overCrossings = aOverCrossings

	def getOverCrossings(self) -> OverCrossings:
		return self._overCrossings

	def setPlatforms(self, aPlatforms : Platforms):
		self._platforms = aPlatforms

	def getPlatforms(self) -> Platforms:
		return self._platforms

	def setRestrictionAreas(self, aRestrictionAreas : RestrictionAreas):
		self._restrictionAreas = aRestrictionAreas

	def getRestrictionAreas(self) -> RestrictionAreas:
		return self._restrictionAreas

	def setServiceSections(self, aServiceSections : ServiceSections):
		self._serviceSections = aServiceSections

	def getServiceSections(self) -> ServiceSections:
		return self._serviceSections

	def setSignalsIS(self, aSignalsIS : SignalsIS):
		self._signalsIS = aSignalsIS

	def getSignalsIS(self) -> SignalsIS:
		return self._signalsIS

	def setSpeeds(self, aSpeeds : Speeds):
		self._speeds = aSpeeds

	def getSpeeds(self) -> Speeds:
		return self._speeds

	def setStoppingPlaces(self, aStoppingPlaces : StoppingPlaces):
		self._stoppingPlaces = aStoppingPlaces

	def getStoppingPlaces(self) -> StoppingPlaces:
		return self._stoppingPlaces

	def setSwitchesIS(self, aSwitchesIS : SwitchesIS):
		self._switchesIS = aSwitchesIS

	def getSwitchesIS(self) -> SwitchesIS:
		return self._switchesIS

	def setTracks(self, aTracks : Tracks):
		self._tracks = aTracks

	def getTracks(self) -> Tracks:
		return self._tracks

	def setTrackBeds(self, aTrackBeds : TrackBeds):
		self._trackBeds = aTrackBeds

	def getTrackBeds(self) -> TrackBeds:
		return self._trackBeds

	def setTrackGauges(self, aTrackGauges : TrackGauges):
		self._trackGauges = aTrackGauges

	def getTrackGauges(self) -> TrackGauges:
		return self._trackGauges

	def setTrainDetectionElements(self, aTrainDetectionElements : TrainDetectionElements):
		self._trainDetectionElements = aTrainDetectionElements

	def getTrainDetectionElements(self) -> TrainDetectionElements:
		return self._trainDetectionElements

	def setTrainProtectionElements(self, aTrainProtectionElements : TrainProtectionElements):
		self._trainProtectionElements = aTrainProtectionElements

	def getTrainProtectionElements(self) -> TrainProtectionElements:
		return self._trainProtectionElements

	def setTrainRadios(self, aTrainRadios : TrainRadios):
		self._trainRadios = aTrainRadios

	def getTrainRadios(self) -> TrainRadios:
		return self._trainRadios

	def setUnderCrossings(self, aUnderCrossings : UnderCrossings):
		self._underCrossings = aUnderCrossings

	def getUnderCrossings(self) -> UnderCrossings:
		return self._underCrossings

	def setWeightLimits(self, aWeightLimits : WeightLimits):
		self._weightLimits = aWeightLimits

	def getWeightLimits(self) -> WeightLimits:
		return self._weightLimits

	def __init__(self):
		self._balises : Balises = None
		# @AssociationType Infrastructure.Balises
		# @AssociationMultiplicity 0..1
		# """container element for all balise (and balise group) elements"""
		self._borders : Borders = None
		# @AssociationType Infrastructure.Borders
		# @AssociationMultiplicity 0..1
		# """container element for all border elements"""
		self._bufferStops : BufferStops = None
		# @AssociationType Infrastructure.BufferStops
		# @AssociationMultiplicity 0..1
		# """container element for all bufferStop elements"""
		self._crossings : Crossings = None
		# @AssociationType Infrastructure.Crossings
		# @AssociationMultiplicity 0..1
		# """container element for all crossing elements"""
		self._derailersIS : DerailersIS = None
		# @AssociationType Infrastructure.DerailersIS
		# @AssociationMultiplicity 0..1
		# """container element for all derailer elements"""
		self._electrifications : Electrifications = None
		# @AssociationType Infrastructure.Electrifications
		# @AssociationMultiplicity 0..1
		# """container element for all electrification elements incl. electrification system components"""
		self._keyLocksIS : KeyLocksIS = None
		# @AssociationType Infrastructure.KeyLocksIS
		# @AssociationMultiplicity 0..1
		# """container element for all keyLock elements"""
		self._levelCrossingsIS : LevelCrossingsIS = None
		# @AssociationType Infrastructure.LevelCrossingsIS
		# @AssociationMultiplicity 0..1
		# """container element for all levelCrossing elements"""
		self._lines : Lines = None
		# @AssociationType Infrastructure.Lines
		# @AssociationMultiplicity 0..1
		# """container element for all line (section) elements"""
		self._loadingGauges : LoadingGauges = None
		# @AssociationType Infrastructure.LoadingGauges
		# @AssociationMultiplicity 0..1
		# """container element for all loadingGauge elements"""
		self._operationalPoints : OperationalPoints = None
		# @AssociationType Infrastructure.OperationalPoints
		# @AssociationMultiplicity 0..1
		# """container element for all operationalPoint elements"""
		self._overCrossings : OverCrossings = None
		# @AssociationType Infrastructure.OverCrossings
		# @AssociationMultiplicity 0..1
		# """container element for all overCrossing elements"""
		self._platforms : Platforms = None
		# @AssociationType Infrastructure.Platforms
		# @AssociationMultiplicity 0..1
		# """container element for all platform (and platform edge) elements"""
		self._restrictionAreas : RestrictionAreas = None
		# @AssociationType Infrastructure.RestrictionAreas
		# @AssociationMultiplicity 0..1
		# """container element for all restrictionArea elements"""
		self._serviceSections : ServiceSections = None
		# @AssociationType Infrastructure.ServiceSections
		# @AssociationMultiplicity 0..1
		# """container element for all serviceSection elements"""
		self._signalsIS : SignalsIS = None
		# @AssociationType Infrastructure.SignalsIS
		# @AssociationMultiplicity 0..1
		# """container element for all signal (and panel) elements"""
		self._speeds : Speeds = None
		# @AssociationType Infrastructure.Speeds
		# @AssociationMultiplicity 0..1
		# """container element for all line/track speed related elements"""
		self._stoppingPlaces : StoppingPlaces = None
		# @AssociationType Infrastructure.StoppingPlaces
		# @AssociationMultiplicity 0..1
		# """container element for all stoppingPlace elements"""
		self._switchesIS : SwitchesIS = None
		# @AssociationType Infrastructure.SwitchesIS
		# @AssociationMultiplicity 0..1
		# """container element for all switch elements"""
		self._tracks : Tracks = None
		# @AssociationType Infrastructure.Tracks
		# @AssociationMultiplicity 0..1
		# """container element for all track elements"""
		self._trackBeds : TrackBeds = None
		# @AssociationType Infrastructure.TrackBeds
		# @AssociationMultiplicity 0..1
		# """container element for all trackBed elements"""
		self._trackGauges : TrackGauges = None
		# @AssociationType Infrastructure.TrackGauges
		# @AssociationMultiplicity 0..1
		# """container element for all trackGauge elements"""
		self._trainDetectionElements : TrainDetectionElements = None
		# @AssociationType Infrastructure.TrainDetectionElements
		# @AssociationMultiplicity 0..1
		# """container element for all trainDetectionElement elements"""
		self._trainProtectionElements : TrainProtectionElements = None
		# @AssociationType Infrastructure.TrainProtectionElements
		# @AssociationMultiplicity 0..1
		# """container element for all trainProtectionElement elements"""
		self._trainRadios : TrainRadios = None
		# @AssociationType Infrastructure.TrainRadios
		# @AssociationMultiplicity 0..1
		# """container element for all trainRadio elements"""
		self._underCrossings : UnderCrossings = None
		# @AssociationType Infrastructure.UnderCrossings
		# @AssociationMultiplicity 0..1
		# """container element for all underCrossing elements"""
		self._weightLimits : WeightLimits = None
		# @AssociationType Infrastructure.WeightLimits
		# @AssociationMultiplicity 0..1
		# """container element for all weightLimit (axle load, meterload) elements"""

