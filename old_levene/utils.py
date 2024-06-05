import frappe


def onupdate(doc,ev):
    if doc.get('workflow_state'):
        if doc.workflow_state == "Rejected":
            #Check if the last comment on document was created by the current user
            all_comments = frappe.get_all("Comment",{'comment_type':"Comment",'reference_name':doc.name},['name','comment_email'])
            if not all_comments:
                frappe.throw("Please set a reason for rejection")
            else:
                if all_comments[0]['comment_email'] != frappe.session.user:
                    frappe.throw("Please set a reason for rejection")


@frappe.whitelist()
def convert_to_so(doc):
    so_doc = frappe.new_doc("Sales Order")
    po_doc = frappe.get_doc("Purchase Order",doc)
    so_doc.lc_due_date = po_doc.lc_due_date
    so_doc.company = po_doc.company
    so_doc.purchase_order_document = po_doc.name
    for each in po_doc.items:
        so_doc.append('items',each.as_dict())
    return so_doc
    


def before_naming(doc,ev):
    doc.naming_series = frappe.db.get_value("Company",doc.company,'journal_naming_series')