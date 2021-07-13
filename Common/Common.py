#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common.ElectrificationSystems import ElectrificationSystems
from RailML.Common.OrganizationalUnits import OrganizationalUnits
from RailML.Common.SpeedProfiles import SpeedProfiles
from RailML.Common.PositioningSystems import PositioningSystems
from RailML.Common.tElementWithID import tElementWithID
from typing import List

class Common(tElementWithID):
	"""This is the top level element for the common model."""
	def setElectrificationSystems(self, aElectrificationSystems : ElectrificationSystems):
		self.___electrificationSystems = aElectrificationSystems

	def getElectrificationSystems(self) -> ElectrificationSystems:
		return self.___electrificationSystems

	def setOrganizationalUnits(self, aOrganizationalUnits : OrganizationalUnits):
		self.___organizationalUnits = aOrganizationalUnits

	def getOrganizationalUnits(self) -> OrganizationalUnits:
		return self.___organizationalUnits

	def setSpeedProfiles(self, aSpeedProfiles : SpeedProfiles):
		self.___speedProfiles = aSpeedProfiles

	def getSpeedProfiles(self) -> SpeedProfiles:
		return self.___speedProfiles

	def setPositioning(self, aPositioning : PositioningSystems):
		self.___positioning = aPositioning

	def getPositioning(self) -> PositioningSystems:
		return self.___positioning

	def __init__(self):
		self.___electrificationSystems : ElectrificationSystems = None
		# @AssociationType Common.ElectrificationSystems
		# @AssociationMultiplicity 0..1
		# """container element for all electrificationSystem elements"""
		self.___organizationalUnits : OrganizationalUnits = None
		# @AssociationType Common.OrganizationalUnits
		# @AssociationMultiplicity 0..1
		# """container element for all organizationalUnit elements"""
		self.___speedProfiles : SpeedProfiles = None
		# @AssociationType Common.SpeedProfiles
		# @AssociationMultiplicity 0..1
		# """container element for all speedProfile elements"""
		self.___positioning : PositioningSystems = None
		# @AssociationType Common.PositioningSystems
		# @AssociationMultiplicity 0..1

