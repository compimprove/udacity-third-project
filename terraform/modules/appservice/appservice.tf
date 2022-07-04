resource "azurerm_app_service_plan" "main" {
  name                = "${var.application_type}-${var.resource_type}"
  location            = var.location
  resource_group_name = var.resource_group

  sku {
    tier = "Free"
    size = "F1"
  }
}

resource "azurerm_app_service" "main" {
  name                = "${var.application_type}-${var.resource_type}"
  location            = var.location
  resource_group_name = var.resource_group
  app_service_plan_id = azurerm_app_service_plan.main.id

  app_settings = {
    "WEBSITE_RUN_FROM_PACKAGE" = 0
  }
}

resource "azurerm_monitor_action_group" "main" {
  name                = "SendPersonalMail"
  resource_group_name = var.resource_group
  short_name          = "send-mail"

  email_receiver {
    name          = "SendPersonalMail"
    email_address = "compimprove@gmail.com"
  }
}

resource "azurerm_monitor_metric_alert" "main" {
  name                 = "HTTP 2xx More Than 50"
  resource_group_name  = var.resource_group
  description          = "Action will be triggered when HTTP 2xx count is greater than 50."
  scopes               = [azurerm_app_service.main.id]
  enabled              = true
  severity             = 2
  target_resource_type = ""
  criteria {
    metric_namespace       = "Microsoft.Web/sites"
    metric_name            = "Http2xx"
    aggregation            = "Total"
    operator               = "GreaterThan"
    threshold              = 50
    skip_metric_validation = false
    
  }

  action {
    action_group_id = azurerm_monitor_action_group.main.id
  }
}
