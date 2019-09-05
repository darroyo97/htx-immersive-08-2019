#this will hold look up function
from contacts import contacts

def lookup(name):
    results = []
    for entry in contacts:
        if name == entry['first_name']:
            results.append(entry)
        elif name == entry['last_name']:
            results.append(entry)
    return results