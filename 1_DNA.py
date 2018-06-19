sequencia = open("rosalind_dna.txt","r").read()

print sequencia.upper().count("A"),sequencia.upper().count("C"),sequencia.upper().count("G"),sequencia.upper().count("T")

