# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = [
    'ConfigurationResult',
    'AwaitableConfigurationResult',
    'configuration',
    'configuration_output',
]

@pulumi.output_type
class ConfigurationResult:
    """
    A collection of values returned by Configuration.
    """
    def __init__(__self__, cluster_endpoint=None, cluster_name=None, config_patches=None, docs=None, examples=None, id=None, kubernetes_version=None, machine_configuration=None, machine_secrets=None, machine_type=None, talos_version=None):
        if cluster_endpoint and not isinstance(cluster_endpoint, str):
            raise TypeError("Expected argument 'cluster_endpoint' to be a str")
        pulumi.set(__self__, "cluster_endpoint", cluster_endpoint)
        if cluster_name and not isinstance(cluster_name, str):
            raise TypeError("Expected argument 'cluster_name' to be a str")
        pulumi.set(__self__, "cluster_name", cluster_name)
        if config_patches and not isinstance(config_patches, list):
            raise TypeError("Expected argument 'config_patches' to be a list")
        pulumi.set(__self__, "config_patches", config_patches)
        if docs and not isinstance(docs, bool):
            raise TypeError("Expected argument 'docs' to be a bool")
        pulumi.set(__self__, "docs", docs)
        if examples and not isinstance(examples, bool):
            raise TypeError("Expected argument 'examples' to be a bool")
        pulumi.set(__self__, "examples", examples)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kubernetes_version and not isinstance(kubernetes_version, str):
            raise TypeError("Expected argument 'kubernetes_version' to be a str")
        pulumi.set(__self__, "kubernetes_version", kubernetes_version)
        if machine_configuration and not isinstance(machine_configuration, str):
            raise TypeError("Expected argument 'machine_configuration' to be a str")
        pulumi.set(__self__, "machine_configuration", machine_configuration)
        if machine_secrets and not isinstance(machine_secrets, dict):
            raise TypeError("Expected argument 'machine_secrets' to be a dict")
        pulumi.set(__self__, "machine_secrets", machine_secrets)
        if machine_type and not isinstance(machine_type, str):
            raise TypeError("Expected argument 'machine_type' to be a str")
        pulumi.set(__self__, "machine_type", machine_type)
        if talos_version and not isinstance(talos_version, str):
            raise TypeError("Expected argument 'talos_version' to be a str")
        pulumi.set(__self__, "talos_version", talos_version)

    @property
    @pulumi.getter(name="clusterEndpoint")
    def cluster_endpoint(self) -> str:
        """
        The endpoint of the talos kubernetes cluster
        """
        return pulumi.get(self, "cluster_endpoint")

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> str:
        """
        The name of the talos kubernetes cluster
        """
        return pulumi.get(self, "cluster_name")

    @property
    @pulumi.getter(name="configPatches")
    def config_patches(self) -> Optional[Sequence[str]]:
        """
        The list of config patches to apply to the generated configuration
        """
        return pulumi.get(self, "config_patches")

    @property
    @pulumi.getter
    def docs(self) -> Optional[bool]:
        """
        Whether to generate documentation for the generated configuration
        """
        return pulumi.get(self, "docs")

    @property
    @pulumi.getter
    def examples(self) -> Optional[bool]:
        """
        Whether to generate examples for the generated configuration
        """
        return pulumi.get(self, "examples")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ID of this resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="kubernetesVersion")
    def kubernetes_version(self) -> Optional[str]:
        """
        The version of kubernetes to use
        """
        return pulumi.get(self, "kubernetes_version")

    @property
    @pulumi.getter(name="machineConfiguration")
    def machine_configuration(self) -> str:
        """
        The generated machine configuration
        """
        return pulumi.get(self, "machine_configuration")

    @property
    @pulumi.getter(name="machineSecrets")
    def machine_secrets(self) -> 'outputs.ConfigurationMachineSecretsResult':
        """
        The secrets for the talos cluster
        """
        return pulumi.get(self, "machine_secrets")

    @property
    @pulumi.getter(name="machineType")
    def machine_type(self) -> str:
        """
        The type of machine to generate the configuration for
        """
        return pulumi.get(self, "machine_type")

    @property
    @pulumi.getter(name="talosVersion")
    def talos_version(self) -> Optional[str]:
        """
        The version of talos features to use in generated machine configuration
        """
        return pulumi.get(self, "talos_version")


class AwaitableConfigurationResult(ConfigurationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ConfigurationResult(
            cluster_endpoint=self.cluster_endpoint,
            cluster_name=self.cluster_name,
            config_patches=self.config_patches,
            docs=self.docs,
            examples=self.examples,
            id=self.id,
            kubernetes_version=self.kubernetes_version,
            machine_configuration=self.machine_configuration,
            machine_secrets=self.machine_secrets,
            machine_type=self.machine_type,
            talos_version=self.talos_version)


def configuration(cluster_endpoint: Optional[str] = None,
                  cluster_name: Optional[str] = None,
                  config_patches: Optional[Sequence[str]] = None,
                  docs: Optional[bool] = None,
                  examples: Optional[bool] = None,
                  kubernetes_version: Optional[str] = None,
                  machine_secrets: Optional[pulumi.InputType['ConfigurationMachineSecretsArgs']] = None,
                  machine_type: Optional[str] = None,
                  talos_version: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableConfigurationResult:
    """
    Generate a machine configuration for a node type

    > **Note:** It is recommended to set the optional `talos_version` attribute.
    Otherwise when using a new version of the provider with a new major version of the Talos SDK, new machineconfig features will be enabled by default which could cause unexpected behavior.

    ## Example Usage

    {{tffile "examples/data-sources/talos_machine_configuration/data-source.tf"}}


    :param str cluster_endpoint: The endpoint of the talos kubernetes cluster
    :param str cluster_name: The name of the talos kubernetes cluster
    :param Sequence[str] config_patches: The list of config patches to apply to the generated configuration
    :param bool docs: Whether to generate documentation for the generated configuration
    :param bool examples: Whether to generate examples for the generated configuration
    :param str kubernetes_version: The version of kubernetes to use
    :param pulumi.InputType['ConfigurationMachineSecretsArgs'] machine_secrets: The secrets for the talos cluster
    :param str machine_type: The type of machine to generate the configuration for
    :param str talos_version: The version of talos features to use in generated machine configuration
    """
    __args__ = dict()
    __args__['clusterEndpoint'] = cluster_endpoint
    __args__['clusterName'] = cluster_name
    __args__['configPatches'] = config_patches
    __args__['docs'] = docs
    __args__['examples'] = examples
    __args__['kubernetesVersion'] = kubernetes_version
    __args__['machineSecrets'] = machine_secrets
    __args__['machineType'] = machine_type
    __args__['talosVersion'] = talos_version
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('talos:machine/configuration:Configuration', __args__, opts=opts, typ=ConfigurationResult).value

    return AwaitableConfigurationResult(
        cluster_endpoint=__ret__.cluster_endpoint,
        cluster_name=__ret__.cluster_name,
        config_patches=__ret__.config_patches,
        docs=__ret__.docs,
        examples=__ret__.examples,
        id=__ret__.id,
        kubernetes_version=__ret__.kubernetes_version,
        machine_configuration=__ret__.machine_configuration,
        machine_secrets=__ret__.machine_secrets,
        machine_type=__ret__.machine_type,
        talos_version=__ret__.talos_version)


@_utilities.lift_output_func(configuration)
def configuration_output(cluster_endpoint: Optional[pulumi.Input[str]] = None,
                         cluster_name: Optional[pulumi.Input[str]] = None,
                         config_patches: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                         docs: Optional[pulumi.Input[Optional[bool]]] = None,
                         examples: Optional[pulumi.Input[Optional[bool]]] = None,
                         kubernetes_version: Optional[pulumi.Input[Optional[str]]] = None,
                         machine_secrets: Optional[pulumi.Input[pulumi.InputType['ConfigurationMachineSecretsArgs']]] = None,
                         machine_type: Optional[pulumi.Input[str]] = None,
                         talos_version: Optional[pulumi.Input[Optional[str]]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ConfigurationResult]:
    """
    Generate a machine configuration for a node type

    > **Note:** It is recommended to set the optional `talos_version` attribute.
    Otherwise when using a new version of the provider with a new major version of the Talos SDK, new machineconfig features will be enabled by default which could cause unexpected behavior.

    ## Example Usage

    {{tffile "examples/data-sources/talos_machine_configuration/data-source.tf"}}


    :param str cluster_endpoint: The endpoint of the talos kubernetes cluster
    :param str cluster_name: The name of the talos kubernetes cluster
    :param Sequence[str] config_patches: The list of config patches to apply to the generated configuration
    :param bool docs: Whether to generate documentation for the generated configuration
    :param bool examples: Whether to generate examples for the generated configuration
    :param str kubernetes_version: The version of kubernetes to use
    :param pulumi.InputType['ConfigurationMachineSecretsArgs'] machine_secrets: The secrets for the talos cluster
    :param str machine_type: The type of machine to generate the configuration for
    :param str talos_version: The version of talos features to use in generated machine configuration
    """
    ...
