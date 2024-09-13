import cv2
import pytesseract
from gtts import gTTS
import os

# Set the path to the Tesseract executable (Windows path)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def capture_and_ocr():
    # Initialize webcam
    cap = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Convert the frame to grayscale for better OCR accuracy
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the captured frame
        cv2.imshow('Frame', frame)

        # Check for key press
        key = cv2.waitKey(1)
        if key == ord('q'):  # Press 'q' to exit the loop
            break
        elif key == ord('f'):  # Press 'f' to perform OCR
            # Perform OCR using Tesseract
            text = pytesseract.image_to_string(gray)

            # Display the OCR result
            print("OCR Result:")
            print(text)

            # Check if there is text to speak
            if text:
                # Convert text to speech
                tts = gTTS(text=text, lang='en')
                tts.save("output.mp3")
                os.system("start output.mp3")  # Windows command to play audio

    # Release the capture
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_and_ocr()
