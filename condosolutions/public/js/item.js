
frappe.ui.form.on("Item", {
    refresh(frm) {

    },

    block(frm) {
        frm.trigger("set_item_code");
    },

    building(frm) {
        frm.trigger("set_item_code");
    },

    floor(frm) {
        frm.trigger("set_item_code");
    },

    apartment(frm) {
        frm.trigger("set_item_code");
    },

    set_item_code(frm) {
        const { doc } = frm;

        doc.item_code = `${doc.block}${doc.building}${doc.floor}${doc.apartment}`;
        frm.refresh_field("item_code");
    }
});