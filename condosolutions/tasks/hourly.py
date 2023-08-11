import frappe


def set_active_to_reservation_status():
    reservations = frappe.db.sql("""
        Select
            name
        From
            `tabReserve`
        Where
            docstatus = 1
            and from_date = CURDATE()
            and start_time <= CURTIME()
    """, as_dict=True)

    for reservation in reservations:
        doc = frappe.get_doc("Reserve", reservation.name)
        doc.reservation_status = "Active"
        doc.db_update()


def set_expired_to_reservation_status():
    reservations = frappe.db.sql("""
        Select
            name
        From
            `tabReserve`
        Where
            docstatus = 1
            and (from_date < CURDATE() or 
            (from_date = CURDATE() and start_time < CURTIME()))
            and reservation_status = "Active"
    """, as_dict=True)

    for reservation in reservations:
        doc = frappe.get_doc("Reserve", reservation.name)
        doc.reservation_status = "Expired"
        doc.db_update()