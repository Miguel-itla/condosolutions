# Copyright (c) 2023, CondoSolutions and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from datetime import datetime
from frappe.model.document import Document


class Reserve(Document):
    def validate(self):
        self.validate_dates()
        self.validate_numer_of_attendees()
        self.validate_people_limit()
        self.validate_reservation()

    def validate_dates(self):
        if self.from_date > self.to_date:
            frappe.throw(_("From Date cannot be greater than To Date"))

        if self.from_date < frappe.utils.nowdate():
            frappe.throw(_("From Date cannot be less than today"))

        if self.to_date < frappe.utils.nowdate():
            frappe.throw(_("To Date cannot be less than today"))

        if self.from_date == self.to_date:
            start_time = datetime.strptime(self.start_time, "%H:%M:%S").time()
            end_time = datetime.strptime(self.end_time, "%H:%M:%S").time()

            if start_time > end_time:
                frappe.throw(_("Start Time cannot be greater than End Time"))

            if start_time == end_time:
                frappe.throw(_("Start Time cannot be equal to End Time"))

    def validate_numer_of_attendees(self):
        if self.number_of_attendees <= 0:
            frappe.throw(_("Number of Attendees must be greater than zero"))

    def validate_people_limit(self):
        if self.number_of_attendees > self.people_limit:
            frappe.throw(
                _("Number of Attendees cannot be greater than People Limit"))

    def validate_reservation(self):
        # validate if there is a reservation in the same date range and there is no overlap in time
        reservations = frappe.db.sql("""
            Select
                name
            From
                `tabReserve`
            Where
                reserve_area = '{0}'
                and docstatus = 1
                and (
                    (from_date between '{1}' and '{2}')
                    or (to_date between '{1}' and '{2}')
                    or (from_date <= '{1}' and to_date >= '{2}')
                )
                and (
                    (start_time between '{3}' and '{4}')
                    or (end_time between '{3}' and '{4}')
                    or (start_time <= '{3}' and end_time >= '{4}')
                )
        """.format(self.reserve_area, self.from_date, self.to_date, self.start_time, self.end_time), as_dict=True)

        if reservations:
            frappe.throw(
                _("There is already a reservation in the same date range and time range"))
