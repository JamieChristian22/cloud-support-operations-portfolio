terraform {
  required_providers {
    azurerm = { source = "hashicorp/azurerm", version = "~> 4.0" }
  }
}
provider "azurerm" { features {} }

resource "azurerm_resource_group" "support" {
  name     = "rg-support-lab-eastus"
  location = "East US"
  tags = { environment = "support-lab", owner = "cloud-operations", cost-center = "learning" }
}
