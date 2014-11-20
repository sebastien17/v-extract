#!python
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
import numpy
import matplotlib
import cv2
import os.path

def capture_information(cap):
    return {'time': cap.get(0),
            'frame': int(cap.get(1)),
            'position': cap.get(2),
            'width': int(cap.get(3)),
            'height': int(cap.get(4)),
            'fps': cap.get(5),
            'fourcc': cap.get(6),
            'frame_total_count': int(cap.get(7)),
            'format': cap.get(8),
            'mode': cap.get(9)
            }
    
def video_processing(video_file, output_directory, sample):
    print('Processing : {0}'.format(video_file))
    cap = cv2.VideoCapture(video_file)
    video_param =  capture_information(cap)
    
    if(sample == None):
        #Print info
        print(video_param)
        
        #Jumping to frame and saving    
        int_frame = 0
        ret, frame = cap.read()
        
        while(ret):
            video_param =  capture_information(cap)
            print(video_param)
            file_name = '{0}_{1}.png'.format(os.path.basename(video_file),int_frame)
            cv2.imwrite(os.path.join(output_directory,file_name),frame)
            int_frame += 1
            ret, frame = cap.read()
    else:
        #Choosing different frames
        frame_list = []
        shift = 1.0/sample
        frame_list.append(shift/2)
        for i in xrange(sample - 1):
            frame_list.append(frame_list[-1] + shift)
        
        #Print info
        print('Frame List :{0}'.format(frame_list))

        #Jumping to frame and saving    
        for int_frame in frame_list:
            cap.set(2, int_frame)
            ret, frame = cap.read()
            video_param =  capture_information(cap)
            print(video_param)
            file_name = '{0}_{1}.png'.format(os.path.basename(video_file),frame_list.index(int_frame))
            cv2.imwrite(os.path.join(output_directory,file_name),frame)

    cap.release()
    cv2.destroyAllWindows()

def main():
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
        video_processing(INPUT,OUTPUT,SAMPLE)
        
if __name__ == '__main__':
        main()
        
        