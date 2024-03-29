# Copyright (c) 2013, Vishal Dhayagude and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import msgprint, _
from frappe.utils import flt

def execute(filters=None):
    if not filters: filters = {}

    columns = get_columns(filters)
    entries = get_entries(filters)
    data = []

    for d in entries:

        data.append([
            d.date, d.challan_number, d.party_information,d.delivery_type,
            d.location,d.rate
        ])

    return columns, data

def get_columns(filters):
    if not filters.get("vehicle"):
        msgprint(_("Please select the Vehicle first"), raise_exception=1)

    return [
        _("Date") + ":Date:80",
        _("Challan Number") + ":Link/Transport Bill Generator:60",
        _("Party Information") + ":Link/Transport Bill Generator:150",
        _("Delivery Type") + ":Link/Transport Bill Generator:130",
        _("Location") + ":Link/Transport Bill Generator:120",
        _("Rate") + ":Int:80"
        ]

def get_entries(filters):
    date_field = "date"
    conditions, values = get_conditions(filters, date_field)
    entries = frappe.db.sql("""
        select
            vt.%s, vt.challan_number, vt.party_information,vt.delivery_type,
            vt.location,vt.rate
        from
            `tabTransport Bill Generator` vt
        where
            vt.vehicle_registration_number = '%s'
            %s order by date
        """ %(date_field, filters["vehicle"],conditions),
            tuple(values),  as_dict=1)

    return entries

def get_conditions(filters, date_field):
    conditions = [""]
    values = []

    if filters.get("from_date"):
        conditions.append("vt.{0}>=%s".format(date_field))
        values.append(filters["from_date"])

    if filters.get("to_date"):
        conditions.append("vt.{0}<=%s".format(date_field))
        values.append(filters["to_date"])

    return " and ".join(conditions), values
