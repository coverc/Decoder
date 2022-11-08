#Christopher Overcash  800939915#

from ntpath import join
import sys

###INITIALIZE COMMON VARIABLES###
string = "" #String is NULL
decompressed = [] #decompressed result array
table = [] #initialize table
inputFileCommandLine = sys.argv[1] #Sets variable equal to input text file
MAX_TABLE_SIZE = 2 ** int(sys.argv[2]) #sets the max table length as 2^(specified bit length)

###Read the Input###
inputFile = open(inputFileCommandLine, 'r', encoding = 'UTF-16BE') #opens the file with the read mode
input = inputFile.read() #reads the input file

def InitializeTable(table):
###For Loop to Initialize table###
    for x in range(0,255): #table needs 256 numbers
        table.append(chr(x)) #sets the table to include the characters represented from 0 to 256        

def Decoder(input, table, string, decompressed):
###For Loop for actual decoding algorithm###
    for y in range(0,len(input)): #for loop looping from 0 to the length of the input    
        code = ord(input[y]) #code is equal to the input position y (Code is reading each character of the input file)
                         
        if ord(input[y]) >= len(table): #if the unicode of the input at position y is not already in the table 
            newString = string + string[0] #string plus first element of string is equal to the string called newString (newString will be added to the decompressed result array) 
        else: #if the unicode is already in the table
            newString = table[code] #add the corresponding string from the existing table to the newString
    
        decompressed.append(newString) #add the newString to the decompressed result array

        if len(table) < MAX_TABLE_SIZE: #If the table is not yet full add the new element and corresponding code to the table(dictionary)
            table.append(string + newString[0]) #add the new element to the table/dictionary
        string = newString #String is now the newString value for future loops
    y+=1 #increment counter

def PrintCode(decompressed):
    print(''.join(decompressed)) #print the dcompressed result array

def ExportCode(decompressed, inputFile, inputFileCommandLine):
###EXPORTS FILE TO EXTERNAL TXT FILE###
    decompressedFile = inputFileCommandLine.split('.')[0] + '_decoded' + '.txt'
    output = open(decompressedFile, 'w')
    output.write(''.join(decompressed))
    output.close
    inputFile.close

###Call Funtions###
InitializeTable(table) #Function to Initialize Table 0-256
Decoder(input, table, string, decompressed) #Function to decode
PrintCode(decompressed) #Function to Print decompressed code to terminal
ExportCode(decompressed, inputFile, inputFileCommandLine) #Function to Export the Final Code to an txt File