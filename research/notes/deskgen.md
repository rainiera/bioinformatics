
DESKGEN
    for designing CRISPR experiments

score guide RNAs for knock-outs and knock-ins
automatically insert guides into the correct locations of any CRIPSR vector
generate an assembly strategy to clone it up

repositories
experiments
    login

    knock-in/knock-out
    input gene name or ID from Ensembl
    CDC20
        top or forward strand gene with four known transcript variants
            two of which have consensus coding sequences
        exons in black
        untranslated regions in grey
        introns as lines
        sequence level view retains this information, below

        to get the best chance of knockout, disrupt all variants by targeting an exon conserved across multiple variants
        drag master play head to the region where the exon is conserved throughout multiple transcripts
        targeting three variants at the same time

        type a location for fine-tuned genome browsing

        Deskgen finds and scores every possible guide with the NGG-PAM sequence
            lollipop - a guide, number has an on-target scoring activity using the ?dench-root? scoring system
            summary of all guides
            MIT Zhang tool looks for crispr design and analysis
            
