// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package cluster

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Retrieves the kubeconfig for a Talos cluster
func Kubeconfig(ctx *pulumi.Context, args *KubeconfigArgs, opts ...pulumi.InvokeOption) (*KubeconfigResult, error) {
	opts = pkgInvokeDefaultOpts(opts)
	var rv KubeconfigResult
	err := ctx.Invoke("talos:cluster/kubeconfig:Kubeconfig", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking Kubeconfig.
type KubeconfigArgs struct {
	// The client configuration data
	ClientConfiguration KubeconfigClientConfiguration `pulumi:"clientConfiguration"`
	// endpoint to use for the talosclient. if not set, the node value will be used
	Endpoint *string `pulumi:"endpoint"`
	// controlplane node to retrieve the kubeconfig from
	Node     string                 `pulumi:"node"`
	Timeouts map[string]interface{} `pulumi:"timeouts"`
	// Wait for the kubernetes api to be available
	Wait *bool `pulumi:"wait"`
}

// A collection of values returned by Kubeconfig.
type KubeconfigResult struct {
	// The client configuration data
	ClientConfiguration KubeconfigClientConfiguration `pulumi:"clientConfiguration"`
	// endpoint to use for the talosclient. if not set, the node value will be used
	Endpoint string `pulumi:"endpoint"`
	// The ID of this resource.
	Id string `pulumi:"id"`
	// The raw kubeconfig
	KubeconfigRaw string `pulumi:"kubeconfigRaw"`
	// The kubernetes client configuration
	KubernetesClientConfiguration KubeconfigKubernetesClientConfiguration `pulumi:"kubernetesClientConfiguration"`
	// controlplane node to retrieve the kubeconfig from
	Node     string                 `pulumi:"node"`
	Timeouts map[string]interface{} `pulumi:"timeouts"`
	// Wait for the kubernetes api to be available
	Wait *bool `pulumi:"wait"`
}

func KubeconfigOutput(ctx *pulumi.Context, args KubeconfigOutputArgs, opts ...pulumi.InvokeOption) KubeconfigResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (KubeconfigResult, error) {
			args := v.(KubeconfigArgs)
			r, err := Kubeconfig(ctx, &args, opts...)
			var s KubeconfigResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(KubeconfigResultOutput)
}

// A collection of arguments for invoking Kubeconfig.
type KubeconfigOutputArgs struct {
	// The client configuration data
	ClientConfiguration KubeconfigClientConfigurationInput `pulumi:"clientConfiguration"`
	// endpoint to use for the talosclient. if not set, the node value will be used
	Endpoint pulumi.StringPtrInput `pulumi:"endpoint"`
	// controlplane node to retrieve the kubeconfig from
	Node     pulumi.StringInput `pulumi:"node"`
	Timeouts pulumi.MapInput    `pulumi:"timeouts"`
	// Wait for the kubernetes api to be available
	Wait pulumi.BoolPtrInput `pulumi:"wait"`
}

func (KubeconfigOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*KubeconfigArgs)(nil)).Elem()
}

// A collection of values returned by Kubeconfig.
type KubeconfigResultOutput struct{ *pulumi.OutputState }

func (KubeconfigResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*KubeconfigResult)(nil)).Elem()
}

func (o KubeconfigResultOutput) ToKubeconfigResultOutput() KubeconfigResultOutput {
	return o
}

func (o KubeconfigResultOutput) ToKubeconfigResultOutputWithContext(ctx context.Context) KubeconfigResultOutput {
	return o
}

// The client configuration data
func (o KubeconfigResultOutput) ClientConfiguration() KubeconfigClientConfigurationOutput {
	return o.ApplyT(func(v KubeconfigResult) KubeconfigClientConfiguration { return v.ClientConfiguration }).(KubeconfigClientConfigurationOutput)
}

// endpoint to use for the talosclient. if not set, the node value will be used
func (o KubeconfigResultOutput) Endpoint() pulumi.StringOutput {
	return o.ApplyT(func(v KubeconfigResult) string { return v.Endpoint }).(pulumi.StringOutput)
}

// The ID of this resource.
func (o KubeconfigResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v KubeconfigResult) string { return v.Id }).(pulumi.StringOutput)
}

// The raw kubeconfig
func (o KubeconfigResultOutput) KubeconfigRaw() pulumi.StringOutput {
	return o.ApplyT(func(v KubeconfigResult) string { return v.KubeconfigRaw }).(pulumi.StringOutput)
}

// The kubernetes client configuration
func (o KubeconfigResultOutput) KubernetesClientConfiguration() KubeconfigKubernetesClientConfigurationOutput {
	return o.ApplyT(func(v KubeconfigResult) KubeconfigKubernetesClientConfiguration {
		return v.KubernetesClientConfiguration
	}).(KubeconfigKubernetesClientConfigurationOutput)
}

// controlplane node to retrieve the kubeconfig from
func (o KubeconfigResultOutput) Node() pulumi.StringOutput {
	return o.ApplyT(func(v KubeconfigResult) string { return v.Node }).(pulumi.StringOutput)
}

func (o KubeconfigResultOutput) Timeouts() pulumi.MapOutput {
	return o.ApplyT(func(v KubeconfigResult) map[string]interface{} { return v.Timeouts }).(pulumi.MapOutput)
}

// Wait for the kubernetes api to be available
func (o KubeconfigResultOutput) Wait() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v KubeconfigResult) *bool { return v.Wait }).(pulumi.BoolPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(KubeconfigResultOutput{})
}
