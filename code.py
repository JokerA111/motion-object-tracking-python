banner ="""                     
                          Motion Detection and Tracking System
                                  :-=+####%%%%%%####*+=-.                                 
                           .-=*#**==-:.             .:-=+*#*+-:                           
                        -*%#+-                              :=*%#=:                       
                    :=##=:                                      :-*#+-                    
                  +@#=                                              -*@*.                 
               -*%=.                                                   -#%=               
             :%#:                                                        .*@=             
           :%#:                                                            .+%=           
          +%:         :              ....:::::::::...              :.         #%:         
        =@*       -*%*.         .....:.. .: .. ..  .:.....          =%#=.      =%*        
       +@:    :.=@@%:        ...   :.    :  ..  ..   .:.   ...        +@@#.-.    #%       
      *#   .*#.#@@*.      ..:.   ..     :   ..   :.    ..   .:..       =@@#.+%:   +%:     
    .%%    %@ +@*.=:    .:     .::..   ..   ..    :   ..:::.    .:     +.=@* *@-   +@-    
   .%#  -.#@* =-+@+   ..       :     ..:..+#==%%*.::.     ..      ..   :@#-=::@@:-  =@-   
   *#  ++ @@:+%@#-   :.       :       :.  *#:.=@@. :       ..       :.  .+@@*:#@+ %  -%.  
  -@  -@+ @*@@=:   .:        :        :     .-%#:  :.       :        ..   .=#@*@= @#  *#  
 .@=  #@* %#-:+-   :...     ..        :     .+     ..       .:     .....  :*-:*@::@@. :@= 
 *@   %@@ =:%@*   :     ....:..      ..     .:      :      ..::...     ..  +@@=-:+@@:  *@ 
.@* . *@@ +@@*   ..        .:    ....:......@@=.....:....    .:         :   =@@#.+@@.. :@-
=@: # .@#+@@::   :         :.        .      :-      :         :         ..  :.#@@=@+ *. #*
*%. @= *#@#.-*  ..         :         :     .::.     :         ..         :  :# =@*%  %- +#
%# .@@..@+ =@-  :.         :         :  -:=%@@@*:-: :         ..         :   @# :@= *@- -%
@#  %@@.= +@%   :..........:........:=#@#   #%:  -@%+:........::.........:   =@%.= *@@: -%
%#  =@@# =@@:   :.         : :==+*#%@@@@:  -++-.  #@@@@%*+==- ..         :    %@% +@@%  -%
#%   +@@-#@* +  ..         :-@@@@@@@@@@%    *%    =@@@@@@@@@@*..         :  .-=@@.@@%.. +#
+@:.* :@#*@:.@.  :         :*@@@@@@@@@@@.   @@=   *@@@@@@@@@@@-         .:  #+ %@=@+ := #*
.@+ @#:.#%% *@=  :.        :%@@@@@@@@@@@*  .@@+  :@@@@@@@@@@@@=         :  :@@ +@%- +@:.@-
 #@ -@@+ -# %@+   :       .=@@@@@@@@@@@@@- .@@* .@@@@@@@@@@@@@#..      ..  =@@:=* -@@# +@ 
 .@= :%@@+..@@* - .......  =@@@@@@@@@@@@@@-:@@*.%@@@@@@@@@@@@@%   ...... ..*@@-.-%@@= .@+ 
  =%   =@@@=*@# =%..:      @@@@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@:     .. +% #@@-%@@#.  *#  
   ##  :.+%@+%@ .@%  :    .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-    :. +@+ @@+@@*-.. -@.  
   .@* -#- :+*@= #@#  ..  -@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+  ..  =@@.-@#*- :++ :@=   
    :@* :%@*- .+::@@* : :.=@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#.:..::@@# +: .+@@+ -@*    
     .#*  -#@@%*=.+@@=-#=.*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@% :*+.@@#.-+#@@@+. -@=     
       #%.  :*@@@@#+%@:-@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@#.%@**@@@@#=   =@:      
        +@=  :::-=*##%%-:%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+.#@##*+=:::  :#%.       
         .##. :##+=::::-: -#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%= .-::::-+*#:  +@=         
           =%+. .=*%@@@@@@@%%%%#*%@@@@@@@@@@@@@@@@@@@@@@@+*%%%%@@@@@@@@#+:  =%*           
             =%+    ..:-=--:.  -+%@@@@@@@@@@@@@@@@@@@@@@@*=.  :--=--:..   =@*.            
              .+%#:  -+**+**#%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#**++*+=: .+%+.              
                 :#%+:  :=+***+=-%@@@@@@@@@@@@@@@@@@@@@@@=-+****=-.  =#%=                 
                   .-*#+-.       @@@@@@@@@@@@@@@@@@@@@@@@-       :=##=:                   
                       :+%%+-   .@@@@@@@@@@@@@@@@@@@@@@@@+   :=#%*=                       
                          .-=*#*#@@@@@@@@@@@@@@@@@@@@@@@@%*#*+-.                          
                                 :-=+*##%%%@@@@%%%%#*+==:.                                
                               
                                 Cyber Wing Gold Campus

"""

# Define functions for motion tracking and object detection
def motion_tracking():
    # Your motion tracking code here
    import cv2
    import numpy as np
    import torch
    from IPython.display import display, clear_output
    import time

    # Re-import YOLOv5 in case it wasn't imported earlier
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

    # Initialize webcam
    cap = cv2.VideoCapture(0)

    # Set webcam frame dimensions (optional)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    # Loop to capture frames and run object detection
    try:
        while True:
            ret, frame = cap.read()  # Capture a frame from the webcam
            if not ret:
                break

            # Convert BGR to RGB (YOLOv5 expects RGB input)
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Run YOLOv5 object detection
            results = model(frame_rgb)

            # Get the annotated frame with detections
            annotated_frame = np.squeeze(results.render())  # Render results to image

            # Display the frame with detections
            clear_output(wait=True)  # Clear the output to update the video feed
            cv2.imshow("YOLOv5 Webcam", cv2.cvtColor(annotated_frame, cv2.COLOR_RGB2BGR))

            # Check if 'q' is pressed to exit the loop
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    except KeyboardInterrupt:
        pass

    # Release the webcam and close any open windows
    cap.release()
    cv2.destroyAllWindows()

    print("Running motion tracking...")  # This line should be aligned with the function definition
 
def object_detection():
    # Your object detection code here
    import cv2
    import mediapipe as mp
    import numpy as np

    cap = cv2.VideoCapture(0)
    ws, hs = 1280, 720
    cap.set(3, ws)
    cap.set(4, hs)

    if not cap.isOpened():
        print("Camera couldn't Access!!!")
        exit()

    mp_face_detection = mp.solutions.face_detection
    mp_drawing = mp.solutions.drawing_utils

    while True:
        success, img = cap.read()

        if not success:
            print("Failed to read frame from the camera!")
            break

        # Convert the image to RGB
        rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        # Detect faces in the image
        with mp_face_detection.FaceDetection(min_detection_confidence=0.5) as face_detection:
            results = face_detection.process(rgb_img)
            
            if results.detections:
                for detection in results.detections:
                    ih, iw, _ = img.shape
                    bbox = int(detection.location_data.relative_bounding_box.xmin * iw), \
                           int(detection.location_data.relative_bounding_box.ymin * ih), \
                           int(detection.location_data.relative_bounding_box.width * iw), \
                           int(detection.location_data.relative_bounding_box.height * ih)

                    # Draw bounding box
                    cv2.rectangle(img, bbox, (255, 0, 255), 2)

                    # Calculate forehead position
                    forehead_x = bbox[0] + bbox[2] // 2
                    forehead_y = bbox[1]

                    # Draw a large red dot on the forehead
                    cv2.circle(img, (forehead_x, forehead_y), 10, (0, 0, 255), -1)

        cv2.imshow("Image", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    print("Running object detection...")  # This line should be aligned with the function definition

# Display the banner
print(banner)
# Prompt the user to choose an option
print("Choose an option:")
print("1. Motion Tracking")
print("2. Object Detection")

# Get user input for the option
option = input("Enter your choice: ")
# Execute the corresponding functionality based on the user's choice
if option == '1':
    motion_tracking()
elif option == '2':
    object_detection()
else:
    print("Invalid option!")
