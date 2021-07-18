#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
sys.path.append('.')
from RailML.Common import Common
from RailML.Common.ElectrificationSystems import ElectrificationSystems
from RailML.Common.OrganizationalUnits import OrganizationalUnits
from RailML.Common.SpeedProfiles import SpeedProfiles
from RailML.Common.PositioningSystems import PositioningSystems
from RailML.Common.tElementWithID import tElementWithID
from typing import List

class Common(tElementWithID):
	"""This is the top level element for the common model."""

	@property
	def ElectrificationSystems(self) -> ElectrificationSystems:
		return self.___electrificationSystems
	@property
	def OrganizationalUnits(self) -> OrganizationalUnits:
		return self.___organizationalUnits
	@property
	def SpeedProfiles(self) -> SpeedProfiles:
		return self.___speedProfiles
	@property
	def PositioningSystems(self) -> PositioningSystems:
		return self.___positioning

	@ElectrificationSystems.setter
	def ElectrificationSystems(self, aElectrificationSystems : ElectrificationSystems):
		self.___electrificationSystems = aElectrificationSystems
	@OrganizationalUnits.setter
	def OrganizationalUnits(self, aOrganizationalUnits : OrganizationalUnits):
		self.___organizationalUnits = aOrganizationalUnits
	@SpeedProfiles.setter
	def setSpeedProfiles(self, aSpeedProfiles : SpeedProfiles):
		self.___speedProfiles = aSpeedProfiles
	@PositioningSystems.setter
	def PositioningSystems(self, aPositioningSystems : PositioningSystems):
		self.___positioning = aPositioningSystems

	def __init__(self):
		self.___electrificationSystems : ElectrificationSystems = ElectrificationSystems()
		# @AssociationType Common.ElectrificationSystems
		# @AssociationMultiplicity 0..1
		# """container element for all electrificationSystem elements"""
		self.___organizationalUnits : OrganizationalUnits = OrganizationalUnits()
		# @AssociationType Common.OrganizationalUnits
		# @AssociationMultiplicity 0..1
		# """container element for all organizationalUnit elements"""
		self.___speedProfiles : SpeedProfiles = SpeedProfiles()
		# @AssociationType Common.SpeedProfiles
		# @AssociationMultiplicity 0..1
		# """container element for all speedProfile elements"""
		self.___positioning : PositioningSystems = PositioningSystems()
		# @AssociationType Common.PositioningSystems
		# @AssociationMultiplicity 0..1

x = Common()