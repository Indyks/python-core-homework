import ex1.mapping
from ex1.mapping import RAW_MAPPING, ROLES_TREE


def build_roles_tree(mapping):
    categories = []
    for category_id in mapping["categoryIdsSorted"]:
        category = {
            "id": "category-" + category_id,
            "text": mapping["categories"][category_id]["name"]
        }
        items = []
        for role_id in mapping["categories"][category_id]["roleIds"]:
            items += [{
                "id": role_id,
                "text": mapping["roles"][role_id]["name"]
            }]
        category["items"] = items
        categories.append(category)
    return {"categories": categories}
