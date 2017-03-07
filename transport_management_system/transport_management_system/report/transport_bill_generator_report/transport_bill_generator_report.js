// Copyright (c) 2016, Vishal Dhayagude and contributors
// For license information, please see license.txt

frappe.query_reports["Transport Bill Generator Report"] = {
	"filters": [
        {
            "fieldname":"company",
            "label": __("Company"),
            "fieldtype": "Link",
            "options": "Company",
            "default": frappe.defaults.get_user_default("Company"),
            "reqd": 1
        },
        {
            fieldname: "vehicle",
            label: __("Vehicle"),
            fieldtype: "Link",
            options: "Vehicle"
        },
        {
            fieldname: "from_date",
            label: __("From Date"),
            fieldtype: "Date",
        },
        {
            fieldname:"to_date",
            label: __("To Date"),
            fieldtype: "Date",
            default: get_today()
        },

	]
}
