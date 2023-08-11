import frappe


def set_overdue_to_rent_invoice():
    rent_invoices = frappe.db.sql("""
        Select
            name
        From
            `tabRent Invoice`
        Where
            payment_date < CURDATE()
            And outstanding_amount > 0
    """, as_dict=True)

    for rent_invoice in rent_invoices:
        doc = frappe.get_doc("Rent Invoice", rent_invoice.name)
        doc.status = "Overdue"
        # late_payment_fee is a percentage
        doc.total_charges = doc.outstanding_amount * \
            (doc.late_payment_fee / 100)

        doc.total_amount = doc.outstanding_amount + doc.total_charges
        doc.db_update()
