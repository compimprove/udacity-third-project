output "resource_group_name" {
  value = "${data.azurerm_resource_group.main.name}"
}

output "resource_group_id" {
  value = "${data.azurerm_resource_group.main.id}"
}

output "resource_group_location" {
  value = "${data.azurerm_resource_group.main.location}"
}