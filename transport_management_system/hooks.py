# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "transport_management_system"
app_title = "Transport Management System"
app_publisher = "Vishal Dhayagude"
app_description = "Provide transportation solution for your business need."
app_icon = "fa fa-truck"
app_color = "blue"
app_email = "vishaldhayagude09@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/transport_management_system/css/transport_management_system.css"
# app_include_js = "/assets/transport_management_system/js/transport_management_system.js"
app_include_js = [
    "/assets/transport_management_system/js/transport_management_system.js",
    "https://maps.googleapis.com/maps/api/js?v=3.exp&sensor=false&libraries=places"
]
# include js, css files in header of web template
web_include_css = "/assets/transport_management_system/css/transport_management_system.css"
web_include_js = "/assets/transport_management_system/js/transport_management_system.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "transport_management_system.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "transport_management_system.install.before_install"
# after_install = "transport_management_system.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "transport_management_system.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"transport_management_system.tasks.all"
# 	],
# 	"daily": [
# 		"transport_management_system.tasks.daily"
# 	],
# 	"hourly": [
# 		"transport_management_system.tasks.hourly"
# 	],
# 	"weekly": [
# 		"transport_management_system.tasks.weekly"
# 	]
# 	"monthly": [
# 		"transport_management_system.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "transport_management_system.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "transport_management_system.event.get_events"
# }
fixtures = [ {"dt": "Custom Field", "filters":[["name", "in", [
                    'Lead-company_website', 'Lead-source_city_address', 'Lead-destination_city_address',
                    'Lead-section_break_centres','Lead-number_of_item','Lead-weight',
                    'Lead-last_name', 'Lead-first_name',
                    ]]]},"Property Setter"]
