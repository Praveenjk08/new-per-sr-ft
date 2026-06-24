import frappe

@frappe.whitelist(allow_guest=True)
def subscribe_newsletter(email):

    if not email:
        frappe.throw("Email is required")

    if frappe.db.exists("Newsletter Subscriber", {"email": email}):
        frappe.throw("This email is already subscribed")

    doc = frappe.get_doc({
        "doctype": "Newsletter Subscriber",
        "email": email
    })

    doc.insert(ignore_permissions=True)
    frappe.db.commit()

    return "Thank you for subscribing!"