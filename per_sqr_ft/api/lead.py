import frappe

@frappe.whitelist(allow_guest=True)
def add_lead(name,email,phone):
    lead=frappe.get_doc({
        "doctype":'CRM Lead',
        "first_name":name,
        "mobile_no":phone,
        "email":email,
    })

    lead.insert(ignore_permissions=True)
    frappe.db.commit()
    message="Lead added successfully"
    return message