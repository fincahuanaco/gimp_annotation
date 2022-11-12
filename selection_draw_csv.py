from gimpfu import *
import csv
def process(image,layer):


    # Indicates that the process has started.
    gimp.progress_init("Reading CSV...")
    
    try:

        unname=image.filename.split(".")  #filename.....ext
        
        csvname="".join(unname[:len(unname)-1])+".csv"  #filename....csv

        # Open file.
        f = None
        f = open(csvname,"r")  #for append
        reader = csv.reader(f)
        if(f is None):
            gimp.message("The CSV file could not be created.")
        else :
            drw = pdb.gimp_image_active_drawable(image)
            pdb.gimp_context_set_foreground((255, 0,0))  #red
            pdb.gimp_context_set_brush('Circle (01)')
            pdb.gimp_context_set_brush_size(10)
            for row in reader:
               y1, x1, h, w = row[0],row[1],row[2],row[3]
               y1, x1, h, w=int(y1),int(x1),int(h),int(w)
               y2=y1+h
               x2=x1+w
               ctrlPoints = [x1,y1,x1,y2,x2,y2,x2,y1,x1,y1]   
               pdb.gimp_paintbrush_default(drw,len(ctrlPoints),ctrlPoints)
            f.close()            
        
    except Exception as err:
        gimp.message("Unexpected error: " + str(err)) #Dialog with error
    
register(
    "python_fu_selection_draw_csv",  #id
    "Selection in CSV",  #title
    "Draw rectangles selection from CSV file.",  #Info
    "fincahuanaco",  #Author
    "Open source (BSD 3-clause license)",
    "2022",
    "<Image>/Filters/Annotation/Selection draw CSV",
    "*",
    [], #No parameters 
    [],
    process)

main()

