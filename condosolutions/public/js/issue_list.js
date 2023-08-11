

frappe.listview_settings["Issue"] = {
    add_fields: ["issue_state"],

    get_indicator(doc) {
        if (doc.issue_state == "Open") {
            return [__("Open"), "orange", "issue_state,=,Open"];
        }
    },
};
