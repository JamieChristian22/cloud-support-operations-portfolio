terraform {
  required_providers {
    google = { source = "hashicorp/google", version = "~> 6.0" }
  }
}
provider "google" {
  project = "northstar-support-lab-2026"
  region  = "us-east1"
}

resource "google_storage_bucket" "support" {
  name                        = "northstar-multicloud-gcp-2026"
  location                    = "US-EAST1"
  uniform_bucket_level_access = true
  labels = { environment = "support-lab", owner = "cloud-operations", cost_center = "learning" }
}
