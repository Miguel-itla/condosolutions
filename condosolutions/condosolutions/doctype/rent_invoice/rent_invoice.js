// Copyright (c) 2023, CondoSolutions and contributors
// For license information, please see license.txt

frappe.ui.form.on('Rent Invoice', {
	onload(frm) {
		frm.trigger("toggle_enable_fields");
	},
	// refresh: function(frm) {

	// }

	toggle_enable_fields(frm) {
		// do this fields readonly if status is Paid
		if (frm.doc.status == "Paid") {
			const fields = [
				"tenants",
				"from_date",
				"to_date",
			]

			fields.forEach(function (field) {
				frm.toggle_enable(field, false);
			});
		}
	},

	tenants(frm) {
		frm.trigger("set_rental_agreement");
	},

	set_rental_agreement(frm) {
		if (frm.doc.tenants) {
			frappe.call({
				method: "condosolutions.condosolutions.doctype.rent_invoice.rent_invoice.get_rental_agreement",
				args: {
					tenant: frm.doc.tenants
				},
				callback: function (data) {
					if (!data.message) {
						frappe.msgprint(__("No rental agreement found for this tenant"));
						return;
					} else {
						frm.set_value("rental_agreement", data.message);
						frm.refresh_field("rental_agreement");
					}
				}
			});
		}
	},

});
