data "azurerm_log_analytics_workspace" "main" {
  name                = "my-log-analytics"
  resource_group_name = var.resource_group_name
  # location            = var.location
  # retention_in_days   = 30
  # sku                 = "PerGB2018"
}
