provider "azurerm" {
  tenant_id       = var.tenant_id
  subscription_id = var.subscription_id
  client_id       = var.client_id
  client_secret   = var.client_secret
  features {}
}
terraform {
  backend "azurerm" {
    storage_account_name = "dinhntterraform"
    container_name       = "terraformcontainer"
    key                  = "dinhntterraform.key"
    access_key           = "qgj0nLg5HQBH3mEf6zlLItsDubEU/qE66ba9l6kXkJjizC5CNVNLB4YwZRM2pDm4nQV/USu5/d1n+AStwCvfmw=="
  }
}
module "resource_group" {
  source         = "../../modules/resource_group"
  resource_group = var.resource_group
}

module "log_analytics_workspace" {
  source              = "../../modules/log_analytics_workspace"
  location = var.location
  resource_group_name = module.resource_group.resource_group_name
}

module "network" {
  source               = "../../modules/network"
  address_space        = var.address_space
  location             = var.location
  virtual_network_name = var.virtual_network_name
  application_type     = var.application_type
  resource_type        = "NET"
  resource_group       = module.resource_group.resource_group_name
  address_prefix_test  = var.address_prefix_test
}

module "nsg-test" {
  source              = "../../modules/networksecuritygroup"
  location            = var.location
  application_type    = var.application_type
  resource_type       = "NSG"
  resource_group      = module.resource_group.resource_group_name
  subnet_id           = module.network.subnet_id_main
  address_prefix_test = var.address_prefix_test
}
module "appservice" {
  source            = "../../modules/appservice"
  location          = var.location
  application_type  = var.application_type
  resource_type     = "AppService"
  resource_group    = module.resource_group.resource_group_name
  resource_group_id = module.resource_group.resource_group_id
}
module "publicip" {
  source           = "../../modules/publicip"
  location         = var.location
  application_type = var.application_type
  resource_type    = "publicip"
  resource_group   = module.resource_group.resource_group_name
}

module "vm" {
  source                           = "../../modules/vm"
  location                         = var.location
  application_type                 = var.application_type
  resource_type                    = "vm"
  resource_group_name              = module.resource_group.resource_group_name
  public_ip_address_id             = module.publicip.public_ip_address_id
  subnet_id                        = module.network.subnet_id_main
  log_analytics_workspace_id       = module.log_analytics_workspace.log_analytics_workspace_id
  log_analytics_primary_shared_key = module.log_analytics_workspace.log_analytics_primary_shared_key
}
