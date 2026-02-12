contact_info ={"Anid": "123-456",
                "Melina": "456-321"
}

Anid_phone = contact_info["Anid"]
print(Anid_phone)

contact_info["Anid"] = "123-123"
print(contact_info)

contact_info["Melina"] = "111-2222"
print(contact_info)


del contact_info["Melina"]

keys = contact_info.keys()
print(keys)

values = contact_info.values()
print(values)

items = contact_info.items()
print(items)


