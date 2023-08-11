# Copyright (c) 2023, CondoSolutions and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class RentInvoice(Document):
    pass


@frappe.whitelist()
def get_rental_agreement(tenant):
    query = frappe.db.sql(f"""
		Select
			name
		From
			`tabRental Agreement`
		Where
			tenant = {tenant!r}
			and docstatus = 1
	""", as_dict=True)

    if query:
        return query[0].name
