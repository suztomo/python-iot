# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.cloud.iot import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.iot_v1.services.device_manager.async_client import (
    DeviceManagerAsyncClient,
)
from google.cloud.iot_v1.services.device_manager.client import DeviceManagerClient
from google.cloud.iot_v1.types.device_manager import (
    BindDeviceToGatewayRequest,
    BindDeviceToGatewayResponse,
    CreateDeviceRegistryRequest,
    CreateDeviceRequest,
    DeleteDeviceRegistryRequest,
    DeleteDeviceRequest,
    GatewayListOptions,
    GetDeviceRegistryRequest,
    GetDeviceRequest,
    ListDeviceConfigVersionsRequest,
    ListDeviceConfigVersionsResponse,
    ListDeviceRegistriesRequest,
    ListDeviceRegistriesResponse,
    ListDevicesRequest,
    ListDevicesResponse,
    ListDeviceStatesRequest,
    ListDeviceStatesResponse,
    ModifyCloudToDeviceConfigRequest,
    SendCommandToDeviceRequest,
    SendCommandToDeviceResponse,
    UnbindDeviceFromGatewayRequest,
    UnbindDeviceFromGatewayResponse,
    UpdateDeviceRegistryRequest,
    UpdateDeviceRequest,
)
from google.cloud.iot_v1.types.resources import (
    Device,
    DeviceConfig,
    DeviceCredential,
    DeviceRegistry,
    DeviceState,
    EventNotificationConfig,
    GatewayAuthMethod,
    GatewayConfig,
    GatewayType,
    HttpConfig,
    HttpState,
    LogLevel,
    MqttConfig,
    MqttState,
    PublicKeyCertificate,
    PublicKeyCertificateFormat,
    PublicKeyCredential,
    PublicKeyFormat,
    RegistryCredential,
    StateNotificationConfig,
    X509CertificateDetails,
)

__all__ = (
    "DeviceManagerClient",
    "DeviceManagerAsyncClient",
    "BindDeviceToGatewayRequest",
    "BindDeviceToGatewayResponse",
    "CreateDeviceRegistryRequest",
    "CreateDeviceRequest",
    "DeleteDeviceRegistryRequest",
    "DeleteDeviceRequest",
    "GatewayListOptions",
    "GetDeviceRegistryRequest",
    "GetDeviceRequest",
    "ListDeviceConfigVersionsRequest",
    "ListDeviceConfigVersionsResponse",
    "ListDeviceRegistriesRequest",
    "ListDeviceRegistriesResponse",
    "ListDevicesRequest",
    "ListDevicesResponse",
    "ListDeviceStatesRequest",
    "ListDeviceStatesResponse",
    "ModifyCloudToDeviceConfigRequest",
    "SendCommandToDeviceRequest",
    "SendCommandToDeviceResponse",
    "UnbindDeviceFromGatewayRequest",
    "UnbindDeviceFromGatewayResponse",
    "UpdateDeviceRegistryRequest",
    "UpdateDeviceRequest",
    "Device",
    "DeviceConfig",
    "DeviceCredential",
    "DeviceRegistry",
    "DeviceState",
    "EventNotificationConfig",
    "GatewayConfig",
    "HttpConfig",
    "MqttConfig",
    "PublicKeyCertificate",
    "PublicKeyCredential",
    "RegistryCredential",
    "StateNotificationConfig",
    "X509CertificateDetails",
    "GatewayAuthMethod",
    "GatewayType",
    "HttpState",
    "LogLevel",
    "MqttState",
    "PublicKeyCertificateFormat",
    "PublicKeyFormat",
)
