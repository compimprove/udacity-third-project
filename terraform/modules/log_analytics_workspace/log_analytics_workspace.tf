data "azurerm_log_analytics_workspace" "main" {
  name = "dinhnt-log-analytics"
  resource_group_name = var.resource_group_name
}