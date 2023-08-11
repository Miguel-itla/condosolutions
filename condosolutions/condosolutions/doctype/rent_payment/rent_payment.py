# Copyright (c) 2023, CondoSolutions and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document


class RentPayment(Document):
    def on_submit(self):
        self.check_if_has_bank_account()
        self.check_if_the_paid_amount_is_greater_than_the_total_amount()
        self.update_rent_invoice()

    def check_if_has_bank_account(self):
        if not self.bank_account:
            frappe.throw(_("The Customer must have a Bank Account."))

    def check_if_the_paid_amount_is_greater_than_the_total_amount(self):
        if self.payable_amount <= 0:
            frappe.throw(_("The Paid Amount must be greater than zero."))

        if self.payable_amount > self.total_amount or self.payable_amount > self.outstanding_amount:
            frappe.throw(
                _("The Paid Amount must be less than or equal to the Total Amount."))

    def update_rent_invoice(self):
        doctype = "Rent Invoice"
        doc = frappe.get_doc(doctype, self.rent_invoice)

        doc.paid_amount += self.payable_amount
        doc.outstanding_amount -= self.payable_amount

        self.outstanding_amount = self.total_amount - self.payable_amount

        if doc.paid_amount == doc.total_amount:
            doc.outstanding_amount = 0

        if doc.outstanding_amount == 0:
            doc.status = "Paid"

        if doc.outstanding_amount > 0 and doc.outstanding_amount < doc.total_amount:
            doc.status = "Partially Paid"

        if doc.outstanding_amount == doc.total_amount:
            doc.status = "Pending"

        doc.save()
