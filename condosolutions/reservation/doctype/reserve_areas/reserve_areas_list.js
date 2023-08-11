
frappe.listview_settings['Reserve Areas'] = {
    add_fields: ["status", "area_type"],

    get_indicator: function (doc) {
        //status indicator
        const status_map = {
            "Active": [__("Active"), "green", "status,=,Active"],
            "On Maintenance": [__("On Maintenance"), "orange", "status,=,On Maintenance"],
            "Inactive": [__("Inactive"), "red", "status,=,Inactive"],
        };

        return status_map[doc.status]

    }
};