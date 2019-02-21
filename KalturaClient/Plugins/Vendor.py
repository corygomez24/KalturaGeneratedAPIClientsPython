# ===================================================================================================
#                           _  __     _ _
#                          | |/ /__ _| | |_ _  _ _ _ __ _
#                          | ' </ _` | |  _| || | '_/ _` |
#                          |_|\_\__,_|_|\__|\_,_|_| \__,_|
#
# This file is part of the Kaltura Collaborative Media Suite which allows users
# to do with audio, video, and animation what Wiki platfroms allow them to do with
# text.
#
# Copyright (C) 2006-2019  Kaltura Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http:#www.gnu.org/licenses/>.
#
# @ignore
# ===================================================================================================
# @package Kaltura
# @subpackage Client
from __future__ import absolute_import

from .Core import *
from ..Base import (
    getXmlNodeBool,
    getXmlNodeFloat,
    getXmlNodeInt,
    getXmlNodeText,
    KalturaClientPlugin,
    KalturaEnumsFactory,
    KalturaObjectBase,
    KalturaObjectFactory,
    KalturaParams,
    KalturaServiceBase,
)

########## enums ##########
########## classes ##########
########## services ##########

# @package Kaltura
# @subpackage Client
class KalturaZoomVendorService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def deAuthorization(self):
        kparams = KalturaParams()
        self.client.queueServiceActionCall("vendor_zoomvendor", "deAuthorization", "None", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeText(resultNode)

    def fetchRegistrationPage(self, tokensData, iv):
        kparams = KalturaParams()
        kparams.addStringIfDefined("tokensData", tokensData)
        kparams.addStringIfDefined("iv", iv)
        self.client.queueServiceActionCall("vendor_zoomvendor", "fetchRegistrationPage", "None", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def oauthValidation(self):
        kparams = KalturaParams()
        self.client.queueServiceActionCall("vendor_zoomvendor", "oauthValidation", "None", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeText(resultNode)

    def recordingComplete(self):
        kparams = KalturaParams()
        self.client.queueServiceActionCall("vendor_zoomvendor", "recordingComplete", "None", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def submitRegistration(self, defaultUserId, zoomCategory, accountId, enableRecordingUpload, createUserIfNotExist):
        kparams = KalturaParams()
        kparams.addStringIfDefined("defaultUserId", defaultUserId)
        kparams.addStringIfDefined("zoomCategory", zoomCategory)
        kparams.addStringIfDefined("accountId", accountId)
        kparams.addBoolIfDefined("enableRecordingUpload", enableRecordingUpload);
        kparams.addBoolIfDefined("createUserIfNotExist", createUserIfNotExist);
        self.client.queueServiceActionCall("vendor_zoomvendor", "submitRegistration", "None", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeText(resultNode)

########## main ##########
class KalturaVendorClientPlugin(KalturaClientPlugin):
    # KalturaVendorClientPlugin
    instance = None

    # @return KalturaVendorClientPlugin
    @staticmethod
    def get():
        if KalturaVendorClientPlugin.instance == None:
            KalturaVendorClientPlugin.instance = KalturaVendorClientPlugin()
        return KalturaVendorClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
            'zoomVendor': KalturaZoomVendorService,
        }

    def getEnums(self):
        return {
        }

    def getTypes(self):
        return {
        }

    # @return string
    def getName(self):
        return 'vendor'

