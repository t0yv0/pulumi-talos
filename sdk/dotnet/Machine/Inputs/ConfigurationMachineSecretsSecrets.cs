// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Talos.Machine.Inputs
{

    public sealed class ConfigurationMachineSecretsSecretsArgs : global::Pulumi.InvokeArgs
    {
        [Input("aescbcEncryptionSecret")]
        private string? _aescbcEncryptionSecret;
        public string? AescbcEncryptionSecret
        {
            get => _aescbcEncryptionSecret;
            set => _aescbcEncryptionSecret = value;
        }

        [Input("bootstrapToken", required: true)]
        private string? _bootstrapToken;
        public string? BootstrapToken
        {
            get => _bootstrapToken;
            set => _bootstrapToken = value;
        }

        [Input("secretboxEncryptionSecret", required: true)]
        private string? _secretboxEncryptionSecret;
        public string? SecretboxEncryptionSecret
        {
            get => _secretboxEncryptionSecret;
            set => _secretboxEncryptionSecret = value;
        }

        public ConfigurationMachineSecretsSecretsArgs()
        {
        }
        public static new ConfigurationMachineSecretsSecretsArgs Empty => new ConfigurationMachineSecretsSecretsArgs();
    }
}
