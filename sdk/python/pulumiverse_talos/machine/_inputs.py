# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'BootstrapClientConfigurationArgs',
    'ConfigurationApplyClientConfigurationArgs',
    'ConfigurationMachineSecretsArgs',
    'ConfigurationMachineSecretsCertsArgs',
    'ConfigurationMachineSecretsCertsEtcdArgs',
    'ConfigurationMachineSecretsCertsK8sArgs',
    'ConfigurationMachineSecretsCertsK8sAggregatorArgs',
    'ConfigurationMachineSecretsCertsK8sServiceaccountArgs',
    'ConfigurationMachineSecretsCertsOsArgs',
    'ConfigurationMachineSecretsClusterArgs',
    'ConfigurationMachineSecretsSecretsArgs',
    'ConfigurationMachineSecretsTrustdinfoArgs',
    'SecretsClientConfigurationArgs',
    'SecretsMachineSecretsArgs',
    'SecretsMachineSecretsCertsArgs',
    'SecretsMachineSecretsCertsEtcdArgs',
    'SecretsMachineSecretsCertsK8sArgs',
    'SecretsMachineSecretsCertsK8sAggregatorArgs',
    'SecretsMachineSecretsCertsK8sServiceaccountArgs',
    'SecretsMachineSecretsCertsOsArgs',
    'SecretsMachineSecretsClusterArgs',
    'SecretsMachineSecretsSecretsArgs',
    'SecretsMachineSecretsTrustdinfoArgs',
]

@pulumi.input_type
class BootstrapClientConfigurationArgs:
    def __init__(__self__, *,
                 ca_certificate: pulumi.Input[str],
                 client_certificate: pulumi.Input[str],
                 client_key: pulumi.Input[str]):
        """
        :param pulumi.Input[str] ca_certificate: The client CA certificate
        :param pulumi.Input[str] client_certificate: The client certificate
        :param pulumi.Input[str] client_key: The client key
        """
        pulumi.set(__self__, "ca_certificate", ca_certificate)
        pulumi.set(__self__, "client_certificate", client_certificate)
        pulumi.set(__self__, "client_key", client_key)

    @property
    @pulumi.getter(name="caCertificate")
    def ca_certificate(self) -> pulumi.Input[str]:
        """
        The client CA certificate
        """
        return pulumi.get(self, "ca_certificate")

    @ca_certificate.setter
    def ca_certificate(self, value: pulumi.Input[str]):
        pulumi.set(self, "ca_certificate", value)

    @property
    @pulumi.getter(name="clientCertificate")
    def client_certificate(self) -> pulumi.Input[str]:
        """
        The client certificate
        """
        return pulumi.get(self, "client_certificate")

    @client_certificate.setter
    def client_certificate(self, value: pulumi.Input[str]):
        pulumi.set(self, "client_certificate", value)

    @property
    @pulumi.getter(name="clientKey")
    def client_key(self) -> pulumi.Input[str]:
        """
        The client key
        """
        return pulumi.get(self, "client_key")

    @client_key.setter
    def client_key(self, value: pulumi.Input[str]):
        pulumi.set(self, "client_key", value)


@pulumi.input_type
class ConfigurationApplyClientConfigurationArgs:
    def __init__(__self__, *,
                 ca_certificate: pulumi.Input[str],
                 client_certificate: pulumi.Input[str],
                 client_key: pulumi.Input[str]):
        """
        :param pulumi.Input[str] ca_certificate: The client CA certificate
        :param pulumi.Input[str] client_certificate: The client certificate
        :param pulumi.Input[str] client_key: The client key
        """
        pulumi.set(__self__, "ca_certificate", ca_certificate)
        pulumi.set(__self__, "client_certificate", client_certificate)
        pulumi.set(__self__, "client_key", client_key)

    @property
    @pulumi.getter(name="caCertificate")
    def ca_certificate(self) -> pulumi.Input[str]:
        """
        The client CA certificate
        """
        return pulumi.get(self, "ca_certificate")

    @ca_certificate.setter
    def ca_certificate(self, value: pulumi.Input[str]):
        pulumi.set(self, "ca_certificate", value)

    @property
    @pulumi.getter(name="clientCertificate")
    def client_certificate(self) -> pulumi.Input[str]:
        """
        The client certificate
        """
        return pulumi.get(self, "client_certificate")

    @client_certificate.setter
    def client_certificate(self, value: pulumi.Input[str]):
        pulumi.set(self, "client_certificate", value)

    @property
    @pulumi.getter(name="clientKey")
    def client_key(self) -> pulumi.Input[str]:
        """
        The client key
        """
        return pulumi.get(self, "client_key")

    @client_key.setter
    def client_key(self, value: pulumi.Input[str]):
        pulumi.set(self, "client_key", value)


@pulumi.input_type
class ConfigurationMachineSecretsArgs:
    def __init__(__self__, *,
                 certs: 'ConfigurationMachineSecretsCertsArgs',
                 cluster: 'ConfigurationMachineSecretsClusterArgs',
                 secrets: 'ConfigurationMachineSecretsSecretsArgs',
                 trustdinfo: 'ConfigurationMachineSecretsTrustdinfoArgs'):
        """
        :param 'ConfigurationMachineSecretsCertsArgs' certs: The certs for the talos kubernetes cluster
        :param 'ConfigurationMachineSecretsClusterArgs' cluster: The cluster secrets
        :param 'ConfigurationMachineSecretsSecretsArgs' secrets: The secrets for the talos kubernetes cluster
        :param 'ConfigurationMachineSecretsTrustdinfoArgs' trustdinfo: The trustd info for the talos kubernetes cluster
        """
        pulumi.set(__self__, "certs", certs)
        pulumi.set(__self__, "cluster", cluster)
        pulumi.set(__self__, "secrets", secrets)
        pulumi.set(__self__, "trustdinfo", trustdinfo)

    @property
    @pulumi.getter
    def certs(self) -> 'ConfigurationMachineSecretsCertsArgs':
        """
        The certs for the talos kubernetes cluster
        """
        return pulumi.get(self, "certs")

    @certs.setter
    def certs(self, value: 'ConfigurationMachineSecretsCertsArgs'):
        pulumi.set(self, "certs", value)

    @property
    @pulumi.getter
    def cluster(self) -> 'ConfigurationMachineSecretsClusterArgs':
        """
        The cluster secrets
        """
        return pulumi.get(self, "cluster")

    @cluster.setter
    def cluster(self, value: 'ConfigurationMachineSecretsClusterArgs'):
        pulumi.set(self, "cluster", value)

    @property
    @pulumi.getter
    def secrets(self) -> 'ConfigurationMachineSecretsSecretsArgs':
        """
        The secrets for the talos kubernetes cluster
        """
        return pulumi.get(self, "secrets")

    @secrets.setter
    def secrets(self, value: 'ConfigurationMachineSecretsSecretsArgs'):
        pulumi.set(self, "secrets", value)

    @property
    @pulumi.getter
    def trustdinfo(self) -> 'ConfigurationMachineSecretsTrustdinfoArgs':
        """
        The trustd info for the talos kubernetes cluster
        """
        return pulumi.get(self, "trustdinfo")

    @trustdinfo.setter
    def trustdinfo(self, value: 'ConfigurationMachineSecretsTrustdinfoArgs'):
        pulumi.set(self, "trustdinfo", value)


@pulumi.input_type
class ConfigurationMachineSecretsCertsArgs:
    def __init__(__self__, *,
                 etcd: 'ConfigurationMachineSecretsCertsEtcdArgs',
                 k8s: 'ConfigurationMachineSecretsCertsK8sArgs',
                 k8s_aggregator: 'ConfigurationMachineSecretsCertsK8sAggregatorArgs',
                 k8s_serviceaccount: 'ConfigurationMachineSecretsCertsK8sServiceaccountArgs',
                 os: 'ConfigurationMachineSecretsCertsOsArgs'):
        pulumi.set(__self__, "etcd", etcd)
        pulumi.set(__self__, "k8s", k8s)
        pulumi.set(__self__, "k8s_aggregator", k8s_aggregator)
        pulumi.set(__self__, "k8s_serviceaccount", k8s_serviceaccount)
        pulumi.set(__self__, "os", os)

    @property
    @pulumi.getter
    def etcd(self) -> 'ConfigurationMachineSecretsCertsEtcdArgs':
        return pulumi.get(self, "etcd")

    @etcd.setter
    def etcd(self, value: 'ConfigurationMachineSecretsCertsEtcdArgs'):
        pulumi.set(self, "etcd", value)

    @property
    @pulumi.getter
    def k8s(self) -> 'ConfigurationMachineSecretsCertsK8sArgs':
        return pulumi.get(self, "k8s")

    @k8s.setter
    def k8s(self, value: 'ConfigurationMachineSecretsCertsK8sArgs'):
        pulumi.set(self, "k8s", value)

    @property
    @pulumi.getter(name="k8sAggregator")
    def k8s_aggregator(self) -> 'ConfigurationMachineSecretsCertsK8sAggregatorArgs':
        return pulumi.get(self, "k8s_aggregator")

    @k8s_aggregator.setter
    def k8s_aggregator(self, value: 'ConfigurationMachineSecretsCertsK8sAggregatorArgs'):
        pulumi.set(self, "k8s_aggregator", value)

    @property
    @pulumi.getter(name="k8sServiceaccount")
    def k8s_serviceaccount(self) -> 'ConfigurationMachineSecretsCertsK8sServiceaccountArgs':
        return pulumi.get(self, "k8s_serviceaccount")

    @k8s_serviceaccount.setter
    def k8s_serviceaccount(self, value: 'ConfigurationMachineSecretsCertsK8sServiceaccountArgs'):
        pulumi.set(self, "k8s_serviceaccount", value)

    @property
    @pulumi.getter
    def os(self) -> 'ConfigurationMachineSecretsCertsOsArgs':
        return pulumi.get(self, "os")

    @os.setter
    def os(self, value: 'ConfigurationMachineSecretsCertsOsArgs'):
        pulumi.set(self, "os", value)


@pulumi.input_type
class ConfigurationMachineSecretsCertsEtcdArgs:
    def __init__(__self__, *,
                 cert: str,
                 key: str):
        pulumi.set(__self__, "cert", cert)
        pulumi.set(__self__, "key", key)

    @property
    @pulumi.getter
    def cert(self) -> str:
        return pulumi.get(self, "cert")

    @cert.setter
    def cert(self, value: str):
        pulumi.set(self, "cert", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: str):
        pulumi.set(self, "key", value)


@pulumi.input_type
class ConfigurationMachineSecretsCertsK8sArgs:
    def __init__(__self__, *,
                 cert: str,
                 key: str):
        pulumi.set(__self__, "cert", cert)
        pulumi.set(__self__, "key", key)

    @property
    @pulumi.getter
    def cert(self) -> str:
        return pulumi.get(self, "cert")

    @cert.setter
    def cert(self, value: str):
        pulumi.set(self, "cert", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: str):
        pulumi.set(self, "key", value)


@pulumi.input_type
class ConfigurationMachineSecretsCertsK8sAggregatorArgs:
    def __init__(__self__, *,
                 cert: str,
                 key: str):
        pulumi.set(__self__, "cert", cert)
        pulumi.set(__self__, "key", key)

    @property
    @pulumi.getter
    def cert(self) -> str:
        return pulumi.get(self, "cert")

    @cert.setter
    def cert(self, value: str):
        pulumi.set(self, "cert", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: str):
        pulumi.set(self, "key", value)


@pulumi.input_type
class ConfigurationMachineSecretsCertsK8sServiceaccountArgs:
    def __init__(__self__, *,
                 key: str):
        pulumi.set(__self__, "key", key)

    @property
    @pulumi.getter
    def key(self) -> str:
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: str):
        pulumi.set(self, "key", value)


@pulumi.input_type
class ConfigurationMachineSecretsCertsOsArgs:
    def __init__(__self__, *,
                 cert: str,
                 key: str):
        pulumi.set(__self__, "cert", cert)
        pulumi.set(__self__, "key", key)

    @property
    @pulumi.getter
    def cert(self) -> str:
        return pulumi.get(self, "cert")

    @cert.setter
    def cert(self, value: str):
        pulumi.set(self, "cert", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: str):
        pulumi.set(self, "key", value)


@pulumi.input_type
class ConfigurationMachineSecretsClusterArgs:
    def __init__(__self__, *,
                 id: str,
                 secret: str):
        """
        :param str id: The ID of this resource.
        """
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "secret", secret)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ID of this resource.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: str):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def secret(self) -> str:
        return pulumi.get(self, "secret")

    @secret.setter
    def secret(self, value: str):
        pulumi.set(self, "secret", value)


@pulumi.input_type
class ConfigurationMachineSecretsSecretsArgs:
    def __init__(__self__, *,
                 bootstrap_token: str,
                 secretbox_encryption_secret: str,
                 aescbc_encryption_secret: Optional[str] = None):
        pulumi.set(__self__, "bootstrap_token", bootstrap_token)
        pulumi.set(__self__, "secretbox_encryption_secret", secretbox_encryption_secret)
        if aescbc_encryption_secret is not None:
            pulumi.set(__self__, "aescbc_encryption_secret", aescbc_encryption_secret)

    @property
    @pulumi.getter(name="bootstrapToken")
    def bootstrap_token(self) -> str:
        return pulumi.get(self, "bootstrap_token")

    @bootstrap_token.setter
    def bootstrap_token(self, value: str):
        pulumi.set(self, "bootstrap_token", value)

    @property
    @pulumi.getter(name="secretboxEncryptionSecret")
    def secretbox_encryption_secret(self) -> str:
        return pulumi.get(self, "secretbox_encryption_secret")

    @secretbox_encryption_secret.setter
    def secretbox_encryption_secret(self, value: str):
        pulumi.set(self, "secretbox_encryption_secret", value)

    @property
    @pulumi.getter(name="aescbcEncryptionSecret")
    def aescbc_encryption_secret(self) -> Optional[str]:
        return pulumi.get(self, "aescbc_encryption_secret")

    @aescbc_encryption_secret.setter
    def aescbc_encryption_secret(self, value: Optional[str]):
        pulumi.set(self, "aescbc_encryption_secret", value)


@pulumi.input_type
class ConfigurationMachineSecretsTrustdinfoArgs:
    def __init__(__self__, *,
                 token: str):
        pulumi.set(__self__, "token", token)

    @property
    @pulumi.getter
    def token(self) -> str:
        return pulumi.get(self, "token")

    @token.setter
    def token(self, value: str):
        pulumi.set(self, "token", value)


@pulumi.input_type
class SecretsClientConfigurationArgs:
    def __init__(__self__, *,
                 ca_certificate: Optional[pulumi.Input[str]] = None,
                 client_certificate: Optional[pulumi.Input[str]] = None,
                 client_key: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] ca_certificate: The client CA certificate
        :param pulumi.Input[str] client_certificate: The client certificate
        :param pulumi.Input[str] client_key: The client key
        """
        if ca_certificate is not None:
            pulumi.set(__self__, "ca_certificate", ca_certificate)
        if client_certificate is not None:
            pulumi.set(__self__, "client_certificate", client_certificate)
        if client_key is not None:
            pulumi.set(__self__, "client_key", client_key)

    @property
    @pulumi.getter(name="caCertificate")
    def ca_certificate(self) -> Optional[pulumi.Input[str]]:
        """
        The client CA certificate
        """
        return pulumi.get(self, "ca_certificate")

    @ca_certificate.setter
    def ca_certificate(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ca_certificate", value)

    @property
    @pulumi.getter(name="clientCertificate")
    def client_certificate(self) -> Optional[pulumi.Input[str]]:
        """
        The client certificate
        """
        return pulumi.get(self, "client_certificate")

    @client_certificate.setter
    def client_certificate(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "client_certificate", value)

    @property
    @pulumi.getter(name="clientKey")
    def client_key(self) -> Optional[pulumi.Input[str]]:
        """
        The client key
        """
        return pulumi.get(self, "client_key")

    @client_key.setter
    def client_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "client_key", value)


@pulumi.input_type
class SecretsMachineSecretsArgs:
    def __init__(__self__, *,
                 certs: Optional[pulumi.Input['SecretsMachineSecretsCertsArgs']] = None,
                 cluster: Optional[pulumi.Input['SecretsMachineSecretsClusterArgs']] = None,
                 secrets: Optional[pulumi.Input['SecretsMachineSecretsSecretsArgs']] = None,
                 trustdinfo: Optional[pulumi.Input['SecretsMachineSecretsTrustdinfoArgs']] = None):
        """
        :param pulumi.Input['SecretsMachineSecretsClusterArgs'] cluster: The cluster secrets
        :param pulumi.Input['SecretsMachineSecretsSecretsArgs'] secrets: kubernetes cluster secrets
        :param pulumi.Input['SecretsMachineSecretsTrustdinfoArgs'] trustdinfo: trustd secrets
        """
        if certs is not None:
            pulumi.set(__self__, "certs", certs)
        if cluster is not None:
            pulumi.set(__self__, "cluster", cluster)
        if secrets is not None:
            pulumi.set(__self__, "secrets", secrets)
        if trustdinfo is not None:
            pulumi.set(__self__, "trustdinfo", trustdinfo)

    @property
    @pulumi.getter
    def certs(self) -> Optional[pulumi.Input['SecretsMachineSecretsCertsArgs']]:
        return pulumi.get(self, "certs")

    @certs.setter
    def certs(self, value: Optional[pulumi.Input['SecretsMachineSecretsCertsArgs']]):
        pulumi.set(self, "certs", value)

    @property
    @pulumi.getter
    def cluster(self) -> Optional[pulumi.Input['SecretsMachineSecretsClusterArgs']]:
        """
        The cluster secrets
        """
        return pulumi.get(self, "cluster")

    @cluster.setter
    def cluster(self, value: Optional[pulumi.Input['SecretsMachineSecretsClusterArgs']]):
        pulumi.set(self, "cluster", value)

    @property
    @pulumi.getter
    def secrets(self) -> Optional[pulumi.Input['SecretsMachineSecretsSecretsArgs']]:
        """
        kubernetes cluster secrets
        """
        return pulumi.get(self, "secrets")

    @secrets.setter
    def secrets(self, value: Optional[pulumi.Input['SecretsMachineSecretsSecretsArgs']]):
        pulumi.set(self, "secrets", value)

    @property
    @pulumi.getter
    def trustdinfo(self) -> Optional[pulumi.Input['SecretsMachineSecretsTrustdinfoArgs']]:
        """
        trustd secrets
        """
        return pulumi.get(self, "trustdinfo")

    @trustdinfo.setter
    def trustdinfo(self, value: Optional[pulumi.Input['SecretsMachineSecretsTrustdinfoArgs']]):
        pulumi.set(self, "trustdinfo", value)


@pulumi.input_type
class SecretsMachineSecretsCertsArgs:
    def __init__(__self__, *,
                 etcd: Optional[pulumi.Input['SecretsMachineSecretsCertsEtcdArgs']] = None,
                 k8s: Optional[pulumi.Input['SecretsMachineSecretsCertsK8sArgs']] = None,
                 k8s_aggregator: Optional[pulumi.Input['SecretsMachineSecretsCertsK8sAggregatorArgs']] = None,
                 k8s_serviceaccount: Optional[pulumi.Input['SecretsMachineSecretsCertsK8sServiceaccountArgs']] = None,
                 os: Optional[pulumi.Input['SecretsMachineSecretsCertsOsArgs']] = None):
        if etcd is not None:
            pulumi.set(__self__, "etcd", etcd)
        if k8s is not None:
            pulumi.set(__self__, "k8s", k8s)
        if k8s_aggregator is not None:
            pulumi.set(__self__, "k8s_aggregator", k8s_aggregator)
        if k8s_serviceaccount is not None:
            pulumi.set(__self__, "k8s_serviceaccount", k8s_serviceaccount)
        if os is not None:
            pulumi.set(__self__, "os", os)

    @property
    @pulumi.getter
    def etcd(self) -> Optional[pulumi.Input['SecretsMachineSecretsCertsEtcdArgs']]:
        return pulumi.get(self, "etcd")

    @etcd.setter
    def etcd(self, value: Optional[pulumi.Input['SecretsMachineSecretsCertsEtcdArgs']]):
        pulumi.set(self, "etcd", value)

    @property
    @pulumi.getter
    def k8s(self) -> Optional[pulumi.Input['SecretsMachineSecretsCertsK8sArgs']]:
        return pulumi.get(self, "k8s")

    @k8s.setter
    def k8s(self, value: Optional[pulumi.Input['SecretsMachineSecretsCertsK8sArgs']]):
        pulumi.set(self, "k8s", value)

    @property
    @pulumi.getter(name="k8sAggregator")
    def k8s_aggregator(self) -> Optional[pulumi.Input['SecretsMachineSecretsCertsK8sAggregatorArgs']]:
        return pulumi.get(self, "k8s_aggregator")

    @k8s_aggregator.setter
    def k8s_aggregator(self, value: Optional[pulumi.Input['SecretsMachineSecretsCertsK8sAggregatorArgs']]):
        pulumi.set(self, "k8s_aggregator", value)

    @property
    @pulumi.getter(name="k8sServiceaccount")
    def k8s_serviceaccount(self) -> Optional[pulumi.Input['SecretsMachineSecretsCertsK8sServiceaccountArgs']]:
        return pulumi.get(self, "k8s_serviceaccount")

    @k8s_serviceaccount.setter
    def k8s_serviceaccount(self, value: Optional[pulumi.Input['SecretsMachineSecretsCertsK8sServiceaccountArgs']]):
        pulumi.set(self, "k8s_serviceaccount", value)

    @property
    @pulumi.getter
    def os(self) -> Optional[pulumi.Input['SecretsMachineSecretsCertsOsArgs']]:
        return pulumi.get(self, "os")

    @os.setter
    def os(self, value: Optional[pulumi.Input['SecretsMachineSecretsCertsOsArgs']]):
        pulumi.set(self, "os", value)


@pulumi.input_type
class SecretsMachineSecretsCertsEtcdArgs:
    def __init__(__self__, *,
                 cert: Optional[pulumi.Input[str]] = None,
                 key: Optional[pulumi.Input[str]] = None):
        if cert is not None:
            pulumi.set(__self__, "cert", cert)
        if key is not None:
            pulumi.set(__self__, "key", key)

    @property
    @pulumi.getter
    def cert(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "cert")

    @cert.setter
    def cert(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cert", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key", value)


@pulumi.input_type
class SecretsMachineSecretsCertsK8sArgs:
    def __init__(__self__, *,
                 cert: Optional[pulumi.Input[str]] = None,
                 key: Optional[pulumi.Input[str]] = None):
        if cert is not None:
            pulumi.set(__self__, "cert", cert)
        if key is not None:
            pulumi.set(__self__, "key", key)

    @property
    @pulumi.getter
    def cert(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "cert")

    @cert.setter
    def cert(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cert", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key", value)


@pulumi.input_type
class SecretsMachineSecretsCertsK8sAggregatorArgs:
    def __init__(__self__, *,
                 cert: Optional[pulumi.Input[str]] = None,
                 key: Optional[pulumi.Input[str]] = None):
        if cert is not None:
            pulumi.set(__self__, "cert", cert)
        if key is not None:
            pulumi.set(__self__, "key", key)

    @property
    @pulumi.getter
    def cert(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "cert")

    @cert.setter
    def cert(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cert", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key", value)


@pulumi.input_type
class SecretsMachineSecretsCertsK8sServiceaccountArgs:
    def __init__(__self__, *,
                 key: Optional[pulumi.Input[str]] = None):
        if key is not None:
            pulumi.set(__self__, "key", key)

    @property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key", value)


@pulumi.input_type
class SecretsMachineSecretsCertsOsArgs:
    def __init__(__self__, *,
                 cert: Optional[pulumi.Input[str]] = None,
                 key: Optional[pulumi.Input[str]] = None):
        if cert is not None:
            pulumi.set(__self__, "cert", cert)
        if key is not None:
            pulumi.set(__self__, "key", key)

    @property
    @pulumi.getter
    def cert(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "cert")

    @cert.setter
    def cert(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cert", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key", value)


@pulumi.input_type
class SecretsMachineSecretsClusterArgs:
    def __init__(__self__, *,
                 id: Optional[pulumi.Input[str]] = None,
                 secret: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] id: The computed ID of the Talos cluster
        """
        if id is not None:
            pulumi.set(__self__, "id", id)
        if secret is not None:
            pulumi.set(__self__, "secret", secret)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        The computed ID of the Talos cluster
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def secret(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "secret")

    @secret.setter
    def secret(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "secret", value)


@pulumi.input_type
class SecretsMachineSecretsSecretsArgs:
    def __init__(__self__, *,
                 aescbc_encryption_secret: Optional[pulumi.Input[str]] = None,
                 bootstrap_token: Optional[pulumi.Input[str]] = None,
                 secretbox_encryption_secret: Optional[pulumi.Input[str]] = None):
        if aescbc_encryption_secret is not None:
            pulumi.set(__self__, "aescbc_encryption_secret", aescbc_encryption_secret)
        if bootstrap_token is not None:
            pulumi.set(__self__, "bootstrap_token", bootstrap_token)
        if secretbox_encryption_secret is not None:
            pulumi.set(__self__, "secretbox_encryption_secret", secretbox_encryption_secret)

    @property
    @pulumi.getter(name="aescbcEncryptionSecret")
    def aescbc_encryption_secret(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "aescbc_encryption_secret")

    @aescbc_encryption_secret.setter
    def aescbc_encryption_secret(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "aescbc_encryption_secret", value)

    @property
    @pulumi.getter(name="bootstrapToken")
    def bootstrap_token(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "bootstrap_token")

    @bootstrap_token.setter
    def bootstrap_token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "bootstrap_token", value)

    @property
    @pulumi.getter(name="secretboxEncryptionSecret")
    def secretbox_encryption_secret(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "secretbox_encryption_secret")

    @secretbox_encryption_secret.setter
    def secretbox_encryption_secret(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "secretbox_encryption_secret", value)


@pulumi.input_type
class SecretsMachineSecretsTrustdinfoArgs:
    def __init__(__self__, *,
                 token: Optional[pulumi.Input[str]] = None):
        if token is not None:
            pulumi.set(__self__, "token", token)

    @property
    @pulumi.getter
    def token(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "token")

    @token.setter
    def token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "token", value)


