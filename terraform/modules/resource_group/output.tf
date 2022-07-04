output "resource_group_name" {
  value = "${data.azurerm_resource_group.main.name}"
}

output "resource_group_id" {
  value = "${data.azurerm_resource_group.main.id}"
}