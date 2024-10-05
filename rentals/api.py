import frappe

@frappe.whitelist()
def get_emoji():
    return "💰"


def get_query_condition_for_vehicle(user):
    return "name = 1"