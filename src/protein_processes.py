from Bio import ExPASy
from Bio import SwissProt

def get_biological_processes(uniprot_id):
    handle = ExPASy.get_sprot_raw(uniprot_id)
    record = SwissProt.read(handle)
    return record

record = get_biological_processes('P53449')
# print vars(record)
# for attr_name, attr in zip(vars(record), map(lambda x: getattr(record, x), vars(record))):
#     print attr_name + "\n"
#     print str(attr) + "\n\n\n"
# # print record.features

for reference in record.cross_references:
    if reference[0] == "GO":
        if reference[2].startswith("P:"):
            print reference[2][2:]

print "\n"
print "\n".join([reference[2][2:] for reference in record.cross_references if "P:" in reference[2]])
