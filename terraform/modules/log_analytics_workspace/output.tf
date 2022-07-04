output "log_analytics_workspace_id" {
  value = "${data.azurerm_log_analytics_workspace.main.workspace_id}"
}

output "log_analytics_primary_shared_key" {
  value = "${data.azurerm_log_analytics_workspace.main.primary_shared_key}"
}