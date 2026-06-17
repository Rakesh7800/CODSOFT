import cv2

def execute_facial_scan(image_source, save_destination='scanned_output.jpg'):
    classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt2.xml')
    
    source_img = cv2.imread(image_source)
    if source_img is None:
        print("Error: Invalid image source path provided.")
        return
        
    monochrome_frame = cv2.cvtColor(source_img, cv2.COLOR_BGR2GRAY)
    identified_regions = classifier.detectMultiScale(monochrome_frame, scaleFactor=1.08, minNeighbors=6)
    
    print(f"Scan Completed: Detected {len(identified_regions)} facial structures.")
    
    for (px, py, width, height) in identified_regions:
        cv2.rectangle(source_img, (px, py), (px + width, py + height), (0, 255, 0), 3)
        
    cv2.imwrite(save_destination, source_img)
    print(f"Processed image successfully exported to {save_destination}")

# execute_facial_scan('input_portrait.jpg') 

