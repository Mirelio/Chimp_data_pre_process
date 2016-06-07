import os
import re

directory='/Users/miriamleon/work/Sandra_data/pre-processed'
#this lists all the files in the given directory.
#Pre-processed is where the inputs (data in mm) are stored and post-processing is where the outputs (data in cm) will be saved to.
#All data points will be divided by 10
dividor = 10

#For each file in the pre-processed directory 
for filename in os.listdir(directory):
    
    in_file = open(directory+'/'+filename, 'r')
    out_name = filename+'_cm'
    #set path to output folder
    outpath = os.path.join("post_processing", out_name)
    #open output file
    out_file = open(outpath, 'w')
    #Regex: if at the beginning of the line (^) there is a digit (\d) or a minus (-)
    data_line = re.compile('^[\d-]')

    #Read each line in the file
    while 1:
        line = in_file.readline()
        if line=="":
            break
        #Find the regex matches
        l = data_line.match(line)
        #If there is a match
        if l:
            #Split the line into a list on the whitespaces
            spl = line.split()
            #Convert the whole list to floats so you can divide
            data_line_numeric = [float(i) for i in spl]
            #Divide each value in the list by 10 (mm -> cm)
            data_line_divided = [x/dividor for x in data_line_numeric]
            #For each item in the new divided list, write it to the new file
            for item in data_line_divided:
                out_file.write("%s " % item)
            #At the end of each list put a new line (so that it retains the same format as input of data data data\n)    
            out_file.write("\n")

            
    in_file.close()
    out_file.close()
    
