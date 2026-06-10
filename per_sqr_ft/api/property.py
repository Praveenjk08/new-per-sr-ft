import frappe

@frappe.whitelist(allow_guest=True)
def get_all_projects():

    projects = frappe.get_all(
        "Property Project",
        fields=[
            "name",
            "project_name",
            "status",
            "full_location",
            "bhk",
            "bath",
            "super_built_up_area",
            "thumbnail_image",
            "url"
        ],
        order_by="creation desc"
    )

    return projects


@frappe.whitelist(allow_guest=True)
def get_project_detail(slug):

    project = frappe.get_doc("Property Project", slug)

    return {
        "name": project.project_name,
        "status": project.status,
        "description": project.description,
        "location": project.full_location,
        "bhk": project.bhk,
        "bath": project.bath,
        "floors": project.floors,
        "project_area": project.project_area,
        "builder": project.project_by_builder,
        "super_built_up_area": project.super_built_up_area,
        "thumbnail_image": project.thumbnail_image,
        "gallery_images": project.gallery_images,
        "carousel_images": project.carousel_images
    }


@frappe.whitelist(allow_guest=True)
def get_all_project_by_status(status):
    projects=frappe.get_all("Property Project",
         filters={'status':status},
         fields=[
             "name",
             "project_name",
             "status",
             "full_location",
             "bhk",
             "bath",
             "super_built_up_area",
             "thumbnail_image",
             "url"
         ])

    return projects

@frappe.whitelist(allow_guest=True)
def get_all_details_from_project():

    projects = frappe.get_all(
        "Property Project",
        fields=[
            "name",
            "project_name",
            "status",
            "full_location",
            "bhk",
            "bath",
            "super_built_up_area",
            "thumbnail_image",
            "url",
            "description",
            "floors",
            "project_area",
            "project_by_builder",
            "location_link",
            "project_location_map_embed"

        ]
    )

    final_projects = []

    for project in projects:

        doc = frappe.get_doc(
            "Property Project",
            project["name"]
        )

        # =========================
        # CAROUSEL IMAGES
        # =========================

        project["carousel_images"] = [

            {
                "image": row.image
            }

            for row in doc.carousel_images
        ]

        # =========================
        # GALLERY IMAGES
        # =========================

        project["gallery_images"] = [

            {
                "image": row.images
            }

            for row in doc.gallery_images
        ]

        # =========================
        # PER SQUARE FEET GALLERY
        # =========================

        project["per_square_feet_gallery"] = [

            {
                "image": row.image,
                "alt_text": row.add_alt_text
            }

            for row in doc.per_square_feet_gallery
        ]

        final_projects.append(project)

    return final_projects


# @frappe.whitelist(allow_guest=True)
# def contact_us():
#     contacts=frappe.get_all(
#         "Contact-Us"
#         ,
#         # filters={"service":"Construction Services"},
#         fields=["*"
#             # "full_name",
#             #  "email",
#             # "phone_number",
#             # "message",
#             # "service"
           
            
#         ]
#         ,order_by="service asc"
#     )    

#     return contacts
    

# @frappe.whitelist(allow_guest=True)
# def add_contact():
#     data=frappe.request.get_json()

#     contact=frappe.get_doc({
#         "doctype":"Contact-Us",
#         "full_name":data.get("full_name"),
#         "email":data.get("email"),
#         "phone_number":data.get("phone_number"),
#         "message":data.get("message"),
#         "service":data.get("service"),
#     })

#     contact.insert(ignore_permissions=True)
#     frappe.db.commit()
#     message="recived"
#     return  message

# @frappe.whitelist(allow_guest=True)
# def get_all_contact_by_name(name):
#     contact=frappe.get_all("Contact-Us",
#     filters={"full_name":name},
#     fields=["*"])

#     return contact





@frappe.whitelist(allow_guest=True)
def get_property_types():
    return frappe.get_all(
        "Property Type",
        fields=[
            
            "property_type",
            "property_image"
        ],
        order_by="property_type asc"
    )


   

@frappe.whitelist(allow_guest=True)
def get_projects_by_type(property_type):
    return frappe.get_all(
        "Property Project",
        filters={
            "project_type": property_type
        },
        fields=[
            "name",
            "project_name",
            "status",
            "full_location",
            "bhk",
            "bath",
            "floors",
            "thumbnail_image",
            "description",
            "url"
        ]
    )