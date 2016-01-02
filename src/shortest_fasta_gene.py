from Bio import Entrez
from Bio import SeqIO

def get_genbank_ids(inp):
    return inp.split(" ")

def get_shortest_gene(genbank_ids):
    """Hits the database twice :(
    """
    Entrez.email = "none@example.com"
    # Fetches FASTA strings from the GenBank database
    handle = Entrez.efetch(db='nucleotide', id=genbank_ids, rettype="fasta")
    records = list(SeqIO.parse(handle, "fasta"))
    ids_and_lens = []
    for record in records:
        ids_and_lens.append((record.id.split('|')[3].split('.')[0], len(record.seq)))
    id_with_shortest_gene = min(ids_and_lens, key=lambda x: x[1])[0]
    handle = Entrez.efetch(db='nucleotide', id=id_with_shortest_gene, rettype="fasta")
    print handle.read()

def get_shortest_gene_2(genbank_ids):
    """Hits the database but involves more string manip
    """
    handle = Entrez.efetch(db="nucleotide", id=genbank_ids, rettype="fasta")
    strands = handle.read().split('\n\n')[:-1]
    print min(strands, key=lambda s: sum(len(x) for x in s.split('\n')[1:]))


inp = raw_input()
ids = get_genbank_ids(inp)
get_shortest_gene(ids)
get_shortest_gene_2(ids)
