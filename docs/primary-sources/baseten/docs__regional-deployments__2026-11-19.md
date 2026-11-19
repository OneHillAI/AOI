doc_type: docs
entity: baseten
source_url: https://docs.baseten.co/deployment/regional-deployments (markdown at .../regional-deployments.md)
document_effective_date: not stamped
retrieval_date: 2026-11-19
exists: yes
retrieved: true
tag: publisher
read_by: code session (curl on the .md rendering)

## What changed against the 2026-09-20 baseline
The baseline recorded "No published list of specific region names was found" and coded eu_region_available unknown. The live docs now carry a "Regional deployments" page with a published region table that includes the European Union, selectable per deployment by CLI or API. The "Regional environments" page (still "require initial configuration by Baseten") is unchanged in substance.

## Governing text (VERBATIM)
"Regional deployments restrict every replica in a deployment to a specific Baseten region. You can select the region through the Baseten dashboard, Baseten CLI, or Management API."

"Your organization's compliance policy defines the regions where its deployments may run. A deployment region adds a narrower constraint for one deployment. It cannot expand the regions allowed by the compliance policy."

"Global is the default when neither a deployment region nor a compliance policy limits placement. Baseten can place replicas in any region where the requested compute is available."

Constraints: "One region per deployment. All replicas run in the selected region."; "Region selection is not a capacity reservation."; "GPU deployments only. Regional selection is supported for deployments on GPU instance types. Deployments on shared CPU instance types can't select a region."; "Models only. Regional selection applies to model deployments. Chains and training jobs can't select a region."

Available regions table:
| Region slug | Location |
| us | United States |
| eu | European Union |
"Need a region that isn't listed? Contact support."

Deploy: "baseten model push --region eu"; REST: set the region field in the deployment payload sent to POST /v1/prepare_model_upload.

Regional endpoint: https://model-{model_id}-region-{region_slug}.api.baseten.co/predict

## Related pages read the same day
- docs.baseten.co/deployment/regional-environments: "Regional environments require initial configuration by Baseten. Contact support to confirm availability for the region you need and configure regional restrictions for your environments." (unchanged)
- docs.baseten.co/inference/model-apis/overview.md, "Regions and compliance": "Model APIs use a shared endpoint, and the regions serving a model can change. If your workloads must stay in specific regions, contact support to confirm model availability and enable a Model APIs compliance policy." "The policy restricts which deployments can serve your requests. Availability depends on the model having capacity in an allowed region." So Model APIs residency is support-enabled, not self-serve.
- docs.baseten.co/hosting-options/overview.md: "Baseten operates the control plane for every option. The location, ownership, and tenancy of the workload plane change." (the control plane is not stated to be region-pinned). Hosting options named: Baseten Cloud, Single-tenant ("An isolated VPC in Baseten Cloud", Enterprise, custom pricing), Self-hosted (Enterprise, custom pricing), Hybrid.
- docs.baseten.co/observability/security.md: compliance policy "Region: the geographic regions where your workloads can run. The policy can't be overridden".
