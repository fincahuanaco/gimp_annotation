from gimpfu import *
import csv
def process(image,layer):


    # Indicates that the process has started.
    gimp.progress_init("Creating CSV...")
    
    try:

        unname=image.filename.split(".")  #filename.....ext
        
        csvname="".join(unname[:len(unname)-1])+".csv"  #filename....csv

        # Open file.
        f = None
        f = open(csvname,"a+")  #for append
        writer = csv.writer(f)
        if(f is None):
            gimp.message("The CSV file could not be created.")
        else :
            non_empty, x1, y1, x2, y2 = pdb.gimp_selection_bounds(image)
            pdb.gimp_selection_none(image)  #unslect
            writer.writerow([y1,x1,(y2-y1),(x2-x1)])
            f.close()            
        
    except Exception as err:
        gimp.message("Unexpected error: " + str(err)) #Dialog with error
    
register(
    "python_fu_selection_selection_csv",  #id
    "Selection in CSV",  #title
    "Save rectangle selection into a CSV file.",  #Info
    "fincahuanaco",  #Author
    "Open source (BSD 3-clause license)",
    "2022",
    "<Image>/Filters/Annotation/Selection to CSV",
    "*",
    [], #No parameters 
    [],
    process)

main()

