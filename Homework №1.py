while True:
    print("Enter command")
    command_name = input()
    if command_name == 'exit':
        print("Good luck")
        break
    print("Enter sequence")
    sequence = input()
    sequence = list(sequence)
# так и не придумала, как проверить правильность букв. Красиво не получается :(    
    true_nucl = ['A', 'T', 'G', 'C', 'a', 't', 'g', 'c']
    for nucl in sequence:
        if nucl not in true_nucl:
            print("Try again!")
        else:
            continue
    
    
    def transcribe(sequence):
        nucl_transcribe = {'A':'U', 'T':'A', 'G':'C', 'C':'G', 'a':'u', 't':'a', 'g':'c', 'c':'g'}
        seq_transcribe = []
        seq_transcribe_join = []
        for nucl in sequence:
            seq_transcribe.append(nucl_transcribe[nucl])
            seq_transcribe_join = ''.join(seq_transcribe)
        print(seq_transcribe_join)
     
    
    def reverse(sequence):
        reverse_seq = []
        reverse_seq = sequence[::-1]
        reverse_seq = ''.join(reverse_seq)
        print(reverse_seq)
     
    def complement(sequence):
        nucl_complement = {'A':'T', 'T':'A', 'G':'C', 'C':'G', 'a':'t', 't':'a', 'g':'c', 'c':'g'}
        seq_complement = []
        seq_complement_join = []
        for nucl in sequence:
            seq_complement.append(nucl_complement[nucl])
            seq_complement_join = ''.join(seq_complement)
        print(seq_complement_join)      
      
    def reverse_complement(sequence):
        nucl_complement = {'A':'T', 'T':'A', 'G':'C', 'C':'G', 'a':'t', 't':'a', 'g':'c', 'c':'g'}
        seq_complement = []
        seq_rev_complement = []
        seq_rev_complement_join = []
        for nucl in sequence:
            seq_complement.append(nucl_complement[nucl])
            seq_rev_complement = seq_complement[::-1]
            seq_rev_complement_join= ''.join(seq_rev_complement)        
        print(seq_rev_complement_join)
       
    if command_name == 'transcribe':
        transcribe(sequence)
    elif command_name == 'reverse':
        reverse(sequence)
    elif command_name == 'complement':
        complement(sequence)
    elif command_name == 'reverse complement':
        reverse_complement(sequence)
