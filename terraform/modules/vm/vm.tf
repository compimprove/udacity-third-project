resource "azurerm_network_interface" "main" {
  name                = "${var.application_type}-network-interface"
  location            = var.location
  resource_group_name = var.resource_group_name

  ip_configuration {
    name                          = "internal"
    subnet_id                     = var.subnet_id
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = var.public_ip_address_id
  }
}

resource "azurerm_linux_virtual_machine" "main" {
  name                  = "${var.application_type}-${var.resource_type}"
  location              = var.location
  resource_group_name   = var.resource_group_name
  size                  = "Standard_B1s"
  admin_username        = "adminuser"
  network_interface_ids = [azurerm_network_interface.main.id]
  admin_ssh_key {
    username   = "adminuser"
    public_key = file("./id_rsa.pub")
  }
  os_disk {
    caching              = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }
  source_image_reference {
    publisher = "Canonical"
    offer     = "UbuntuServer"
    sku       = "18.04-LTS"
    version   = "latest"
  }
}

resource "azurerm_virtual_machine_extension" "main" {
  name                       = "OmsAgentForLinux"
  virtual_machine_id         = azurerm_linux_virtual_machine.main.id
  publisher                  = "Microsoft.EnterpriseCloud.Monitoring"
  type                       = "OmsAgentForLinux"
  type_handler_version       = "1.0"
  auto_upgrade_minor_version = true
  
  settings = <<SETTINGS
    {
        "workspaceId": "${var.log_analytics_workspace_id}"
    }
SETTINGS

  protected_settings = <<PROTECTEDSETTINGS
    {
        "workspaceKey": "${var.log_analytics_primary_shared_key}"
    }
PROTECTEDSETTINGS
}
