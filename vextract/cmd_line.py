doc = """Video Extract.
    <input> can be a video file or a repertory containing video files.
    By default output repertory is the same as the input file.

Usage:
  v-extract.py <input> [--out=<output>] [--sample=<num>]
  
Options:
  --out=<output>    Define an output repertory
  --sample=<num>    Extract <num> sample from the video file 
  -h --help     Show this screen.
"""
import docopt
import os.path
import vextract

def extract():
    arguments = docopt.docopt(doc)
    #print arguments
    INPUT = arguments['<input>']
    OUTPUT = arguments['--out']
    if(arguments['--sample'] == None):
        SAMPLE = None
    else:
        SAMPLE = int(arguments['--sample'])
    
    wearego = True
    #Cleaning path
    INPUT =  os.path.realpath(INPUT)
    if(not os.path.exists(INPUT)):
        print('Error : Input does not exist : {0}'.format(INPUT))
        wearego = False

    if(OUTPUT == None and wearego == True):
        OUTPUT = os.path.dirname(INPUT)
    elif(os.path.exists(OUTPUT)):
        OUTPUT = os.path.realpath(OUTPUT)
    else:
        print('Error : Output does not exist : {0}'.format(OUTPUT))
        wearego = False
   
    if(SAMPLE != None):
        if(not isinstance(SAMPLE,int)):
            wearego = False
            print('Error : Sample has to be an integer strictly superior to 1')
        elif(SAMPLE <= 1):
            wearego = False
            print('Error : Sample has to be an integer strictly superior to 1')
    if(wearego == True):    
        print('INPUT : {0}'.format(INPUT))
        print('OUTPUT : {0}'.format(OUTPUT))
        if(SAMPLE != None):
            print('SAMPLE : {0}'.format(SAMPLE))
        vextract.video_frame2file(INPUT,OUTPUT,SAMPLE)
        
if __name__ == '__main__':
    extract()
        
        