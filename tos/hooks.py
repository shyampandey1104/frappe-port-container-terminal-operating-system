# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "tos"
app_title = "Frappe Port Container Terminal Operating System"
app_publisher = "Shyamkumar Pandey"
app_description = "Frappe Port Container Terminal Operating System for Frappe and ERPNext"
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = "/assets/tos/css/tos.bundle.css"
app_include_js = "/assets/tos/js/tos.bundle.js"

# Document Events
# ---------------
doc_events = {
    "DocType Event": {
        "on_submit": "tos.engine.on_document_submit",
        "on_cancel": "tos.engine.on_document_cancel"
    }
}

# Scheduled Tasks
# ---------------
scheduler_events = {
    "daily": [
        "tos.engine.daily_scheduled_sync"
    ]
}
