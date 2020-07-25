from Queue import PriorityQueue

HUFFMAN_CODE=PriorityQueue()
TOTAL_BITS={}
FREQUENCY_PQ=PriorityQueue()

#Each Node created in Huffman Tree is an object of Character 
class Character:
    def __init__(self, left,right,frequency):
        self.left = left
        self.right = right
        self.frequency = frequency


#Creating the initial list of characters and their frequencies
def find_frequency():   
    total_characters=0
    filename="WomenOfBelgium.txt"
    frequency_dict={}
    VISITED=[]
    with open(filename, 'r') as file:
            for line in file:
                for word in line.split('\n'):
                    for letter in word:
                        if ord(letter) >=32 and ord(letter) <=127:
                            total_characters=total_characters+1
                            
                            if letter not in VISITED:
                                VISITED.append(letter)

                                frequency_dict[letter]=1
                            else:
                                frequency_dict[letter]=frequency_dict[letter]+1                                                                 
    for character,frequency in frequency_dict.items():
        FREQUENCY_PQ.put((frequency,character))
    return total_characters    
        
#Huffman code as taught in class
def huffman_code_tree():
    for i in range(1,FREQUENCY_PQ.qsize()):
        x=FREQUENCY_PQ.get()
        y=FREQUENCY_PQ.get()
        z=Character(x,y,x[0]+y[0])
        FREQUENCY_PQ.put((z.frequency,z))   

#Recursive code to traverse the tree and create code for each character
def generate_code(node,code):
    if not isinstance(node,Character): 
        HUFFMAN_CODE.put((len(code),node,code)) 
        return
    generate_code(node.right[1],code+'1')
    generate_code(node.left[1],code+'0')    
        
#Print code for each character
def show_output():
    total_number_of_bits=0
    while not HUFFMAN_CODE.empty():
        node=HUFFMAN_CODE.get()
#         total_number_of_bits=total_number_of_bits+node[0]
        print(node[1] + ': ' +node[2])    
        TOTAL_BITS.update({node[1]:node[0]})
    filename="WomenOfBelgium.txt"
    with open(filename, 'r') as file:
            for line in file:
                for word in line.split('\n'):
                    for letter in word:
                        if ord(letter) >=32 and ord(letter) <=127:  
                            total_number_of_bits=total_number_of_bits+TOTAL_BITS[letter]
    return total_number_of_bits   


        
total_characters=find_frequency() 
huffman_code_tree()
generate_code(FREQUENCY_PQ.get()[1],'')
total_number_of_bits=show_output()
print("Total number of bits in huffman code: "+str(total_number_of_bits))
print("Total number of bits in fixed code: "+str(total_characters*7))
print("Bits saved: "+str((total_characters*7)-total_number_of_bits))