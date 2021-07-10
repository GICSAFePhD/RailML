#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Common import tRef
from Infrastructure import SignalAnnouncement
from Infrastructure import SignalCatenary
from Infrastructure import SignalDanger
from Infrastructure import SignalEtcs
from Infrastructure import SignalInformation
from Infrastructure import SignalLevelCrossing
from Infrastructure import SignalMilepost
from Infrastructure import SignalSpeed
from Infrastructure import SignalStopPost
from Infrastructure import SignalTrainMovement
from Infrastructure import SignalRadio
from Infrastructure import SignalVehicleEquipment
from Common import tElementWithIDref
from Infrastructure import SignalConstruction
from Infrastructure import FunctionalInfrastructureEntity
from typing import List

class SignalIS(FunctionalInfrastructureEntity):
	def setIsSwitchable(self, aIsSwitchable : long):
		self.___isSwitchable = aIsSwitchable

	def getIsSwitchable(self) -> long:
		return self.___isSwitchable

	def setBelongsToParent(self, aBelongsToParent : tRef):
		self.___belongsToParent = aBelongsToParent

	def getBelongsToParent(self) -> tRef:
		return self.___belongsToParent

	def setBasedOnTemplate(self, aBasedOnTemplate : tRef):
		self.___basedOnTemplate = aBasedOnTemplate

	def getBasedOnTemplate(self) -> tRef:
		return self.___basedOnTemplate

	def setIsAnnouncementSignal(self, aIsAnnouncementSignal : SignalAnnouncement):
		self._isAnnouncementSignal = aIsAnnouncementSignal

	def getIsAnnouncementSignal(self) -> SignalAnnouncement:
		return self._isAnnouncementSignal

	def setIsCatenarySignal(self, aIsCatenarySignal : SignalCatenary):
		self._isCatenarySignal = aIsCatenarySignal

	def getIsCatenarySignal(self) -> SignalCatenary:
		return self._isCatenarySignal

	def setIsDangerSignal(self, aIsDangerSignal : SignalDanger):
		self._isDangerSignal = aIsDangerSignal

	def getIsDangerSignal(self) -> SignalDanger:
		return self._isDangerSignal

	def setIsEtcsSignal(self, aIsEtcsSignal : SignalEtcs):
		self._isEtcsSignal = aIsEtcsSignal

	def getIsEtcsSignal(self) -> SignalEtcs:
		return self._isEtcsSignal

	def setIsInformationSignal(self, aIsInformationSignal : SignalInformation):
		self._isInformationSignal = aIsInformationSignal

	def getIsInformationSignal(self) -> SignalInformation:
		return self._isInformationSignal

	def setIsLevelCrossingSignal(self, aIsLevelCrossingSignal : SignalLevelCrossing):
		self._isLevelCrossingSignal = aIsLevelCrossingSignal

	def getIsLevelCrossingSignal(self) -> SignalLevelCrossing:
		return self._isLevelCrossingSignal

	def setIsMilepost(self, aIsMilepost : SignalMilepost):
		self._isMilepost = aIsMilepost

	def getIsMilepost(self) -> SignalMilepost:
		return self._isMilepost

	def setIsSpeedSignal(self, aIsSpeedSignal : SignalSpeed):
		self._isSpeedSignal = aIsSpeedSignal

	def getIsSpeedSignal(self) -> SignalSpeed:
		return self._isSpeedSignal

	def setIsStopPost(self, aIsStopPost : SignalStopPost):
		self._isStopPost = aIsStopPost

	def getIsStopPost(self) -> SignalStopPost:
		return self._isStopPost

	def setIsTrainMovementSignal(self, aIsTrainMovementSignal : SignalTrainMovement):
		self._isTrainMovementSignal = aIsTrainMovementSignal

	def getIsTrainMovementSignal(self) -> SignalTrainMovement:
		return self._isTrainMovementSignal

	def setIsTrainRadioSignal(self, aIsTrainRadioSignal : SignalRadio):
		self._isTrainRadioSignal = aIsTrainRadioSignal

	def getIsTrainRadioSignal(self) -> SignalRadio:
		return self._isTrainRadioSignal

	def setIsVehicleEquipmentSignal(self, aIsVehicleEquipmentSignal : SignalVehicleEquipment):
		self._isVehicleEquipmentSignal = aIsVehicleEquipmentSignal

	def getIsVehicleEquipmentSignal(self) -> SignalVehicleEquipment:
		return self._isVehicleEquipmentSignal

	def setConnectedWithBaliseGroup(self, *aConnectedWithBaliseGroup : tElementWithIDref*):
		self._connectedWithBaliseGroup = aConnectedWithBaliseGroup

	def getConnectedWithBaliseGroup(self) -> tElementWithIDref*:
		return self._connectedWithBaliseGroup

	def setSignalConstruction(self, aSignalConstruction : SignalConstruction):
		self._signalConstruction = aSignalConstruction

	def getSignalConstruction(self) -> SignalConstruction:
		return self._signalConstruction

	def __init__(self):
		self.___isSwitchable : long = None
		"""set TRUE if the signal is able to show several signal aspects, set FALSE if the signal is a static panel that always shows the same signal aspect"""
		self.___belongsToParent : tRef = None
		"""reference to the (one and only) parent signal this signal belongs to"""
		self.___basedOnTemplate : tRef = None
		# @AssociationType Common.tRef
		# @AssociationType Common.tRef
		# """reference to a generic signal"""
		self._isAnnouncementSignal : SignalAnnouncement = None
		# @AssociationType Infrastructure.SignalAnnouncement
		# @AssociationMultiplicity 0..1
		self._isCatenarySignal : SignalCatenary = None
		# @AssociationType Infrastructure.SignalCatenary
		# @AssociationMultiplicity 0..1
		# """use this child element to specify the catenary signal/sign in more detail"""
		self._isDangerSignal : SignalDanger = None
		# @AssociationType Infrastructure.SignalDanger
		# @AssociationMultiplicity 0..1
		self._isEtcsSignal : SignalEtcs = None
		# @AssociationType Infrastructure.SignalEtcs
		# @AssociationMultiplicity 0..1
		# """use this child element to specify the ETCS signal in more detail"""
		self._isInformationSignal : SignalInformation = None
		# @AssociationType Infrastructure.SignalInformation
		# @AssociationMultiplicity 0..1
		self._isLevelCrossingSignal : SignalLevelCrossing = None
		# @AssociationType Infrastructure.SignalLevelCrossing
		# @AssociationMultiplicity 0..1
		# """use this child element to specify the level crossing signal in more detail"""
		self._isMilepost : SignalMilepost = None
		# @AssociationType Infrastructure.SignalMilepost
		# @AssociationMultiplicity 0..1
		# """use this child element to specify the milepost marker in more detail"""
		self._isSpeedSignal : SignalSpeed = None
		# @AssociationType Infrastructure.SignalSpeed
		# @AssociationMultiplicity 0..1
		# """use this child element to specify the speed signal in more detail"""
		self._isStopPost : SignalStopPost = None
		# @AssociationType Infrastructure.SignalStopPost
		# @AssociationMultiplicity 0..1
		# """use this child element to specify the stop post in more detail"""
		self._isTrainMovementSignal : SignalTrainMovement = None
		# @AssociationType Infrastructure.SignalTrainMovement
		# @AssociationMultiplicity 0..1
		self._isTrainRadioSignal : SignalRadio = None
		# @AssociationType Infrastructure.SignalRadio
		# @AssociationMultiplicity 0..1
		self._isVehicleEquipmentSignal : SignalVehicleEquipment = None
		# @AssociationType Infrastructure.SignalVehicleEquipment
		# @AssociationMultiplicity 0..1
		self._connectedWithBaliseGroup : tElementWithIDref = None
		# @AssociationType Common.tElementWithIDref*
		# @AssociationMultiplicity 0..*
		# """reference to a balise (group) that is connected with this signal"""
		self._signalConstruction : SignalConstruction = None
		# @AssociationType Infrastructure.SignalConstruction
		# @AssociationMultiplicity 0..1
		# """child element for construction details of the (physical) signal"""

