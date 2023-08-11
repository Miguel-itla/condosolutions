
frappe.listview_settings["Rent Invoice"] = {
    add_fields: ["status"],
    get_indicator: function (doc) {
        if (doc.status == "Paid") {
            return [__("Paid"), "green", "status,=,Paid"];
        }

        if (doc.status == "Pending") {
            return [__("Pending"), "orange", "status,=,Pending"];
        }

        if (doc.status == "Overdue") {
            return [__("Overdue"), "red", "status,=,Overdue"];
        }

        if (doc.status == "Cancelled") {
            return [__("Cancelled"), "grey", "status,=,Cancelled"];
        }

        if (doc.status == "Partially Paid") {
            return [__("Partially Paid"), "yellow", "status,=,Partially Paid"];
        }
    },
};