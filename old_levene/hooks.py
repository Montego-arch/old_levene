from . import __version__ as app_version

app_name = "old_levene"
app_title = "Old Levene"
app_publisher = "Montego"
app_description = "old app for levene"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "mmanuelmiles@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/old_levene/css/old_levene.css"
# app_include_js = "/assets/old_levene/js/old_levene.js"

# include js, css files in header of web template
# web_include_css = "/assets/old_levene/css/old_levene.css"
# web_include_js = "/assets/old_levene/js/old_levene.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "old_levene/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {"Purchase Order" : "public/js/po.js"}
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

# Installation
# ------------

# before_install = "old_levene.install.before_install"
# after_install = "old_levene.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "old_levene.uninstall.before_uninstall"
# after_uninstall = "old_levene.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "old_levene.notifications.get_notification_config"

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

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Journal Entry": {
		"before_naming": "old_levene.utils.before_naming"
	},
	"Purchase Order": {
		"on_update": "old_levene.utils.onupdate",
	},
	"Purchase Invoice": {
		"on_update": "old_levene.utils.onupdate",
	},
	"Sales Order": {
		"on_update": "old_levene.utils.onupdate",
	},
	"Sales Invoice": {
		"on_update": "old_levene.utils.onupdate",
	},
	"Purchase Receipt": {
		"on_update": "old_levene.utils.onupdate",
	},
	"Delivery Note": {
		"on_update": "old_levene.utils.onupdate",
	},
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"old_levene.tasks.all"
#	],
#	"daily": [
#		"old_levene.tasks.daily"
#	],
#	"hourly": [
#		"old_levene.tasks.hourly"
#	],
#	"weekly": [
#		"old_levene.tasks.weekly"
#	]
#	"monthly": [
#		"old_levene.tasks.monthly"
#	]
# }

# Testing
# -------

# before_tests = "old_levene.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "old_levene.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "old_levene.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Request Events
# ----------------
# before_request = ["old_levene.utils.before_request"]
# after_request = ["old_levene.utils.after_request"]

# Job Events
# ----------
# before_job = ["old_levene.utils.before_job"]
# after_job = ["old_levene.utils.after_job"]

# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"old_levene.auth.validate"
# ]

