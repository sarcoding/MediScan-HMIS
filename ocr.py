"""
This file is not integrated directly to the gui yet....
You can check the image provided in the resource folder,
the image recognition and word pattern matching is providing correct answer

"""
import cv2
import pytesseract
from fuzzywuzzy import fuzz
import re

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

path = "resource\sample_image"
def image_to_text(image_path):
    try:
        image = cv2.imread(image_path)

        if image is None:
            raise Exception("Image not loaded successfully.")

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

        text = pytesseract.image_to_string(thresh)
        
        line = text.split('\n')
       ## print(line)
        print("Values detected from the scanned handwritten text:")
        fuzzy_string_matching(line[0], diag=True)
        for i in range(1, len(line)):
            if line[i].strip()=="":
                continue
            fuzzy_string_matching(line[i])

    except Exception as e:
        print(f"An error occurred: {e}")

def fuzzy_string_matching(text, diag=False):
    diogs = ["Hypertension","Diabetes","Respiratory Infections","Malaria","Dengue","Tuberculosis","Gastroenteritis","Typhoid","Chronic Obstructive Pulmonary Disease (COPD)","HIV/AIDS"]
    meds = ["Paracetamol", "Amoxicillin", "Metformin", "Amlodipine", "Ibuprofen", "Aspirin", "Crocin", "Atorvastatin", "Omeprazole", "Losartan", "Ciprofloxacin"]

    if diag:
        similarity_scores_diog = [(diog, fuzz.ratio(text, diog)) for diog in diogs]
        best_match_diog = max(similarity_scores_diog, key=lambda x: x[1])
        print(f"Diagnosis: {best_match_diog[0]} by {best_match_diog[1]}%")
    else:
        similarity_scores_med = [(med, fuzz.ratio(text, med)) for med in meds]
        best_match_med = max(similarity_scores_med, key=lambda x: x[1])
        print(f"Medicine: {best_match_med[0]} by {best_match_med[1]}%")
    
if __name__ == "__main__":
    image_to_text(path+"1.jpg") 
    print("-"*50)
    image_to_text(path+"2.jpg") 
