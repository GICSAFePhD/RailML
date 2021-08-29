#!/usr/bin/python
# -*- coding: UTF-8 -*-
from RailML.Common import tRef, tElementWithIDref
from RailML.Infrastructure import SignalAnnouncement, SignalCatenary, SignalDanger, SignalEtcs, SignalInformation
from RailML.Infrastructure import SignalLevelCrossing, SignalMilepost, SignalSpeed, SignalStopPost, SignalTrainMovement
from RailML.Infrastructure import SignalRadio, SignalVehicleEquipment, SignalConstruction, FunctionalInfrastructureEntity
from typing import List, NewType
Long = NewType("Long", int)

class SignalIS(FunctionalInfrastructureEntity.FunctionalInfrastructureEntity):
	@property
	def IsSwitchable(self) -> Long:
		return self.___isSwitchable
	@property
	def BelongsToParent(self) -> tRef:
		return self.___belongsToParent
	@property
	def BasedOnTemplate(self) -> tRef:
		return self.___basedOnTemplate
	@property
	def SignalAnnouncement(self) -> SignalAnnouncement:
		return self.___isAnnouncementSignal
	@property
	def SignalCatenary(self) -> SignalCatenary:
		return self.___isCatenarySignal
	@property
	def SignalDanger(self) -> SignalDanger:
		return self.___isDangerSignal
	@property
	def SignalEtcs(self) -> SignalEtcs:
		return self.___isEtcsSignal
	@property
	def SignalInformation(self) -> SignalInformation:
		return self.___isInformationSignal
	@property
	def SignalLevelCrossing(self) -> SignalLevelCrossing:
		return self.___isLevelCrossingSignal
	@property
	def SignalMilepost(self) -> SignalMilepost:
		return self.___isMilepost
	@property
	def SignalSpeed(self) -> SignalSpeed:
		return self.___isSpeedSignal
	@property
	def SignalStopPost(self) -> SignalStopPost:
		return self.___isStopPost
	@property
	def SignalTrainMovement(self) -> SignalTrainMovement:
		return self.___isTrainMovementSignal
	@property
	def SignalRadio(self) -> SignalRadio:
		return self.___isTrainRadioSignal
	@property
	def SignalVehicleEquipment(self) -> SignalVehicleEquipment:
		return self.___isVehicleEquipmentSignal
	@property
	def tElementWithIDref(self) -> tElementWithIDref:
		return self.___connectedWithBaliseGroup
	@property
	def SignalConstruction(self) -> SignalConstruction:
		return self.___signalConstruction

	@IsSwitchable.setter
	def IsSwitchable(self, aIsSwitchable : Long):
		self.___isSwitchable = aIsSwitchable
	@BelongsToParent.setter
	def BelongsToParent(self, aBelongsToParent : tRef):
		self.___belongsToParent = aBelongsToParent
	@BasedOnTemplate.setter
	def BasedOnTemplate(self, aBasedOnTemplate : tRef):
		self.___basedOnTemplate = aBasedOnTemplate
	@SignalAnnouncement.setter
	def SignalAnnouncement(self, aSignalAnnouncement : SignalAnnouncement):
		self.___isAnnouncementSignal = aSignalAnnouncement
	@SignalCatenary.setter
	def SignalCatenary(self, aSignalCatenary : SignalCatenary):
		self.___isCatenarySignal = aSignalCatenary
	@SignalDanger.setter
	def SignalDanger(self, aSignalDanger : SignalDanger):
		self.___isDangerSignal = aSignalDanger
	@SignalEtcs.setter
	def SignalEtcs(self, aSignalEtcs : SignalEtcs):
		self.___isEtcsSignal = aSignalEtcs
	@SignalInformation.setter
	def SignalInformation(self, aSignalInformation : SignalInformation):
		self.___isInformationSignal = aSignalInformation
	@SignalLevelCrossing.setter
	def SignalLevelCrossing(self, aSignalLevelCrossing : SignalLevelCrossing):
		self.___isLevelCrossingSignal = aSignalLevelCrossing
	@SignalMilepost.setter
	def SignalMilepost(self, aSignalMilepost : SignalMilepost):
		self.___isMilepost = aSignalMilepost
	@SignalSpeed.setter
	def SignalSpeed(self, aSignalSpeed : SignalSpeed):
		self.___isSpeedSignal = aSignalSpeed
	@SignalStopPost.setter
	def SignalStopPost(self, aSignalStopPost : SignalStopPost):
		self.___isStopPost = aSignalStopPost
	@SignalTrainMovement.setter
	def SignalTrainMovement(self, aSignalTrainMovement : SignalTrainMovement):
		self.___isTrainMovementSignal = aSignalTrainMovement
	@SignalRadio.setter
	def SignalRadio(self, aSignalRadio : SignalRadio):
		self.___isTrainRadioSignal = aSignalRadio
	@SignalVehicleEquipment.setter
	def SignalVehicleEquipment(self, aSignalVehicleEquipment : SignalVehicleEquipment):
		self.___isVehicleEquipmentSignal = aSignalVehicleEquipment
	@tElementWithIDref.setter
	def tElementWithIDref(self, atElementWithIDref : tElementWithIDref):
		self.___connectedWithBaliseGroup = atElementWithIDref
	@SignalConstruction.setter
	def SignalConstruction(self, aSignalConstruction : SignalConstruction):
		self.___signalConstruction = aSignalConstruction
	
	def __init__(self):
		self.___isSwitchable : Long = 0
		"""set TRUE if the signal is able to show several signal aspects, set FALSE if the signal is a static panel that always shows the same signal aspect"""
		self.___belongsToParent : tRef = None
		"""reference to the (one and only) parent signal this signal belongs to"""
		self.___basedOnTemplate : tRef = None
		# @AssociationType Common.tRef
		# @AssociationType Common.tRef
		# """reference to a generic signal"""
		self.___isAnnouncementSignal : SignalAnnouncement = None
		# @AssociationType Infrastructure.SignalAnnouncement
		# @AssociationMultiplicity 0..1
		self.___isCatenarySignal : SignalCatenary = None
		# @AssociationType Infrastructure.SignalCatenary
		# @AssociationMultiplicity 0..1
		# """use this child element to specify the catenary signal/sign in more detail"""
		self.___isDangerSignal : SignalDanger = None
		# @AssociationType Infrastructure.SignalDanger
		# @AssociationMultiplicity 0..1
		self.___isEtcsSignal : SignalEtcs = None
		# @AssociationType Infrastructure.SignalEtcs
		# @AssociationMultiplicity 0..1
		# """use this child element to specify the ETCS signal in more detail"""
		self.___isInformationSignal : SignalInformation = None
		# @AssociationType Infrastructure.SignalInformation
		# @AssociationMultiplicity 0..1
		self.___isLevelCrossingSignal : SignalLevelCrossing = None
		# @AssociationType Infrastructure.SignalLevelCrossing
		# @AssociationMultiplicity 0..1
		# """use this child element to specify the level crossing signal in more detail"""
		self.___isMilepost : SignalMilepost = None
		# @AssociationType Infrastructure.SignalMilepost
		# @AssociationMultiplicity 0..1
		# """use this child element to specify the milepost marker in more detail"""
		self.___isSpeedSignal : SignalSpeed = None
		# @AssociationType Infrastructure.SignalSpeed
		# @AssociationMultiplicity 0..1
		# """use this child element to specify the speed signal in more detail"""
		self.___isStopPost : SignalStopPost = None
		# @AssociationType Infrastructure.SignalStopPost
		# @AssociationMultiplicity 0..1
		# """use this child element to specify the stop post in more detail"""
		self.___isTrainMovementSignal : SignalTrainMovement = None
		# @AssociationType Infrastructure.SignalTrainMovement
		# @AssociationMultiplicity 0..1
		self.___isTrainRadioSignal : SignalRadio = None
		# @AssociationType Infrastructure.SignalRadio
		# @AssociationMultiplicity 0..1
		self.___isVehicleEquipmentSignal : SignalVehicleEquipment = None
		# @AssociationType Infrastructure.SignalVehicleEquipment
		# @AssociationMultiplicity 0..1
		self.___connectedWithBaliseGroup : tElementWithIDref = None
		# @AssociationType Common.tElementWithIDref*
		# @AssociationMultiplicity 0..*
		# """reference to a balise (group) that is connected with this signal"""
		self.___signalConstruction : SignalConstruction = None
		# @AssociationType Infrastructure.SignalConstruction
		# @AssociationMultiplicity 0..1
		# """child element for construction details of the (physical) signal"""