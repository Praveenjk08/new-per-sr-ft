import frappe

@frappe.whitelist(allow_guest=True)
def get_gallery_images():

    images = frappe.get_all(
        "Gallery Page",
        filters={"is_active": 1},
        fields=[
           "title",
            "category",
            "image",
            "order_by"
        ],
        order_by="order_by asc"
    )

    return images