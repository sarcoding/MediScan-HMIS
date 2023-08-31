## MediScan-HMIS

### Overview
MediScan-HMIS is a revolutionary solution aimed at simplifying data collection and patient management in government hospitals. The primary goal of this project is to create an intuitive and efficient system that reduces the burden on doctors and healthcare professionals, who often have limited time to learn and interact with complex software due to high patient volumes.

<!--![MediScan-HMIS Screenshot](link_to_screenshot.png)-->


### Features
**Real-time Patient Data:** Seamlessly transmit and display patient information in real-time between the reception and doctor modules.

**OCR Integration:** Utilize Optical Character Recognition (OCR) to precisely detect and process handwritten prescriptions, enhancing prescription management.

**Voice Recognition:** Implement speech recognition to enable doctors to effortlessly input diagnoses and prescriptions, reducing manual data entry.

**Document Scanner Integration:** Doctors can conveniently scan prescription sheets using a document scanner, and the detected prescription details are automatically added to the database.

**Queue Management:** Efficiently manage patient consultations through a queue data structure, ensuring that doctors can focus on patient care.


### Project Structure
- **main.py:** Entry point of the application, orchestrating the integration of various modules.
- **reception.py:** Module for receiving patient data and adding it to the queue.
- **doctor.py:** Module for managing patient consultations, processing the patient queue, and displaying patient details.
- **doct_gui.py:** Graphical user interface for doctors to view patient data and add diagnoses and prescriptions.
- **ocr.py:** Standalone module for Optical Character Recognition (OCR) to enhance prescription processing.
- **Abha database.csv:** A sample database used for testing and prototyping.


### Getting Started
1. Clone the repository to your local machine.

   ```shell
   git clone https://github.com/your-username/MediScan-HMIS.git
2. Install the required dependencies using `pip install -r requirements.txt`.
   + For tesseract: `https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-5.3.1.20230401.exe`
3. Run `main.py` to start the application.


### Future Plans
We have exciting plans to further improve the HMIS by integrating Optical Character Recognition (OCR) directly into the graphical user interface (GUI). This enhancement will streamline prescription management for doctors, allowing them to scan and process handwritten prescriptions seamlessly within the application. By combining OCR technology with our user-friendly GUI, we aim to make the healthcare data management experience even more efficient and intuitive for healthcare professionals.

Stay tuned for this upcoming feature that will elevate the functionality of the HMIS!
