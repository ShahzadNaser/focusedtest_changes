import frappe

def on_submit(doc, method):
    # update parent BOMs
    item_codes = ', '.join(f'"{i.item_code}"' for i in doc.items)
    parent_boms = frappe.db.sql_list(
        """select distinct parent from `tabBOM Item`
        where item_code in ({0}) and parenttype='BOM' order by creation asc""".format(item_codes))
    frappe.enqueue("focusedtest_changes.controller.purchase_order.update_bom_costs",now=True,boms=parent_boms)
    # for bom in parent_boms:
    #     frappe.get_doc("BOM", bom).update_cost(from_child_bom=True)

def update_bom_costs(boms):
    for bom in boms:
        frappe.log_error(title="Updating Bom {}".format(bom), message="Updating Bom {}".format(bom))
        frappe.get_doc("BOM", bom).update_cost(from_child_bom=True)
