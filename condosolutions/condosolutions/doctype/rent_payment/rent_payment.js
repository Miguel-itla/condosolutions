// Copyright (c) 2023, CondoSolutions and contributors
// For license information, please see license.txt

frappe.ui.form.on('Rent Payment', {
	onload(frm) {
		frm.trigger("set_payment_date");
		frm.trigger("generate_transaction_id");
	},

	set_payment_date(frm) {
		frm.set_value("payment_date", frappe.datetime.nowdate());
		frm.refresh_field("payment_date");
	},

	generate_transaction_id(frm) {
		if (frm.doc.__islocal) {
			const length = 6;
			const characters = "0123456789";
			let result = "";

			for (let i = 0; i < length; i++) {
				result += characters.charAt(Math.floor(Math.random() * characters.length));
			}

			frm.set_value("transaction_id", result);
			frm.refresh_field("transaction_id");
		}
	},
});
