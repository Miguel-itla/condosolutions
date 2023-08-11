// Copyright (c) 2023, CondoSolutions and contributors
// For license information, please see license.txt

frappe.ui.form.on('Reserve', {
	refresh: function (frm) {
		frm.trigger("set_queries");
	},

	set_queries(frm) {
		frm.set_query("reserve_area", function () {
			return {
				filters: {
					"status": "Active",
				}
			};
		});
	},
});
