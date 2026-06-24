# 
import frappe

@frappe.whitelist(allow_guest=True)
def add_lead(name, email, phone):

    # Empty field validations
    if not name:
        frappe.throw("Name is required")

    if not email:
        frappe.throw("Email is required")

    if not phone:
        frappe.throw("Phone number is required")

    # Check duplicate email
    if frappe.db.exists("CRM Lead", {"email": email}):
        frappe.throw("Email already exists")

    # Check duplicate phone
    if frappe.db.exists("CRM Lead", {"mobile_no": phone}):
        frappe.throw("Phone number already exists")

    lead = frappe.get_doc({
        "doctype": "CRM Lead",
        "first_name": name,
        "email": email,
        "mobile_no": phone,
         "source": "Website"
    })

    lead.insert(ignore_permissions=True)
    frappe.db.commit()

    return "Lead added successfully"