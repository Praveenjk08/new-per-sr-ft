import frappe

@frappe.whitelist(allow_guest=True)
def create_contact():

    data = frappe.request.get_json()

    try:

        doc = frappe.get_doc({
            "doctype": "Contact-Us",
            "full_name": data.get("full_name"),
            "email": data.get("email"),
            "phone_number": data.get("phone_number"),
            "service": data.get("service"),
            "message": data.get("message")
        })

        doc.insert(ignore_permissions=True)
        frappe.db.commit()

        return {
            "status": "success",
            "message": "Enquiry Submitted Successfully"
        }

    except frappe.UniqueValidationError:

        return {
            "status": "error",
            "message": "This email is already registered."
        }