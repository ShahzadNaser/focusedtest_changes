from . import __version__ as app_version

app_name = "focusedtest_changes"
app_title = "Focusedtest Changes"
app_publisher = "Shahzad Naser"
app_description = "focusedtest_changes"
app_email = "shahzadnaser1122@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/focusedtest_changes/css/focusedtest_changes.css"
# app_include_js = "/assets/focusedtest_changes/js/focusedtest_changes.js"

# include js, css files in header of web template
# web_include_css = "/assets/focusedtest_changes/css/focusedtest_changes.css"
# web_include_js = "/assets/focusedtest_changes/js/focusedtest_changes.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "focusedtest_changes/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
    "BOM" : "public/js/bom.js"
}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "focusedtest_changes.utils.jinja_methods",
#	"filters": "focusedtest_changes.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "focusedtest_changes.install.before_install"
# after_install = "focusedtest_changes.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "focusedtest_changes.uninstall.before_uninstall"
# after_uninstall = "focusedtest_changes.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "focusedtest_changes.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

override_doctype_class = {
	"BOM": "focusedtest_changes.controller.bom.BOMCUSTOM"
}

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Purchase Order": {
		"on_submit": "focusedtest_changes.controller.purchase_order.on_submit"
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"focusedtest_changes.tasks.all"
#	],
#	"daily": [
#		"focusedtest_changes.tasks.daily"
#	],
#	"hourly": [
#		"focusedtest_changes.tasks.hourly"
#	],
#	"weekly": [
#		"focusedtest_changes.tasks.weekly"
#	],
#	"monthly": [
#		"focusedtest_changes.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "focusedtest_changes.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "focusedtest_changes.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "focusedtest_changes.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"focusedtest_changes.auth.validate"
# ]
