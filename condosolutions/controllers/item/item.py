import frappe


def validate(doc, method):
    set_name(doc)


def set_name(doc):
    pass
    # if doc.is_new():
    #     doc.item_code = f"{doc.bloque_manzana}-{doc.no_edificio}-{doc.piso}-{doc.no_apartamento}"
    #     doc.item_name = doc.item_code
    #     doc.save()