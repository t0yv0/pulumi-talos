// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Talos.Machine.Outputs
{

    [OutputType]
    public sealed class ConfigurationMachineSecretsCertsK8sResult
    {
        public readonly string Cert;
        public readonly string Key;

        [OutputConstructor]
        private ConfigurationMachineSecretsCertsK8sResult(
            string cert,

            string key)
        {
            Cert = cert;
            Key = key;
        }
    }
}
