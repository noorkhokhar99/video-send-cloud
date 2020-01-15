

import os, uuid, sys
from azure.storage.blob import BlockBlobService, PublicAccess

#import library
import numpy as np
import cv2
import os
from pathlib import Path
import re
import time

#enter the file name 

print("Enter the File Name:")
file_name = input()
#start recording 
cap = cv2.VideoCapture(0)
#defining the protocol 
fourcc = cv2.VideoWriter_fourcc(*'MP4V')
out = cv2.VideoWriter(str(file_name)+'.mp4', fourcc, 20.0, (640, 480)) 

#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter(str(file_name)+'.avi', fourcc, 60, (320, 240))


#video will record till Q or ESC pressed
while 1:
    ret, img = cap.read()
    out.write(img)
    
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()



def run_sample():
    try:
        # Create the BlockBlockService that is used to call the Blob service for the storage account
        block_blob_service = BlockBlobService(account_name='testvideosurge', account_key=)

        # Create a container called 'quickstartblobs'.
        container_name ='test'
        block_blob_service.create_container(container_name)

        # Set the permission so the blobs are public.
        block_blob_service.set_container_acl(container_name, public_access=PublicAccess.Container)

        # Create a file in Documents to test the upload and download.
        local_path=os.path.abspath(os.path.curdir)
        local_file_name =(str(file_name)+'.mp4')
        full_path_to_file =os.path.join(local_path, local_file_name)

        # Write text to the file.
        #file = open(full_path_to_file,  'w')
        #file.write("Hello, World!")
        #file.close()

        print("Temp file = " + full_path_to_file)
        print("\nUploading to Blob storage as blob" + local_file_name)

        # Upload the created file, use local_file_name for the blob name
        block_blob_service.create_blob_from_path(container_name, local_file_name, full_path_to_file)

        # List the blobs in the container
        print("\nList blobs in the container")
        generator = block_blob_service.list_blobs(container_name)
        for blob in generator:
            print("\t Blob name: " + blob.name)

        # Download the blob(s).
        # Add '_DOWNLOADED' as prefix to '.txt' so you can see both files in Documents.
        full_path_to_file2 = os.path.join(local_path, str.replace(local_file_name ,'.txt', '_DOWNLOADED.txt'))
        print("\nDownloading blob to " + full_path_to_file2)
        block_blob_service.get_blob_to_path(container_name, local_file_name, full_path_to_file2)

        sys.stdout.write("Sample finished running. When you hit <any key>, the sample will be deleted and the sample "
                         "application will exit.")
        sys.stdout.flush()
        input()

        # Clean up resources. This includes the container and the temp files
        #block_blob_service.delete_container(container_name)
      #  os.remove(full_path_to_file)
       # os.remove(full_path_to_file2)
    except Exception as e:
        print(e)


# Main method.
if __name__ == '__main__':
    run_sample()



