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
    public sealed class SecretsMachineSecretsCluster
    {
        /// <summary>
        /// The computed ID of the Talos cluster
        /// </summary>
        public readonly string? Id;
        public readonly string? Secret;

        [OutputConstructor]
        private SecretsMachineSecretsCluster(
            string? id,

            string? secret)
        {
            Id = id;
            Secret = secret;
        }
    }
}
