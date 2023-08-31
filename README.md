# MediScan-HMIS
Overview
The Simplified Health Management Information System (HMIS) is a revolutionary solution aimed at simplifying data collection and patient management in government hospitals. The primary goal of this project is to create an intuitive and efficient system that reduces the burden on doctors and healthcare professionals, who often have limited time to learn and interact with complex software due to high patient volumes.

Features
Real-time Patient Data: Seamlessly transmit and display patient information in real-time between the reception and doctor modules.
OCR Integration: Utilize Optical Character Recognition (OCR) to precisely detect and process handwritten prescriptions, enhancing prescription management.
Voice Recognition: Implement speech recognition to enable doctors to effortlessly input diagnoses and prescriptions, reducing manual data entry.
Document Scanner Integration: Doctors can conveniently scan prescription sheets using a document scanner, and the detected prescription details are automatically added to the database.
Queue Management: Efficiently manage patient consultations through a queue data structure, ensuring that doctors can focus on patient care.
Project Structure
main.py: Entry point of the application, orchestrating the integration of various modules.
reception.py: Module for receiving patient data and adding it to the queue.
doctor.py: Module for managing patient consultations, processing the patient queue, and displaying patient details.
doct_gui.py: Graphical user interface for doctors to view patient data and add diagnoses and prescriptions.
ocr.py: Standalone module for Optical Character Recognition (OCR) to enhance prescription processing.
Abha database.csv: A sample database used for testing and prototyping.
Getting Started
Clone the repository to your local machine.
Install the required dependencies using pip install -r requirements.txt.
Run main.py to start the application.
Usage
Receptionists can easily enter patient information through the reception module, reducing manual data entry.
Doctors can view patient data, add diagnoses and prescriptions, and manage appointments via the doctor module.
OCR technology simplifies prescription management by allowing doctors to scan prescription sheets using a document scanner.
WebSocket communication ensures real-time updates across modules, enhancing data accuracy.
Motivation
The primary motivation behind this project is to bridge the gap between the healthcare sector's need for efficient data management and the challenges posed by limited time and software complexity. By combining OCR, speech recognition, and real-time data sharing, we aim to provide healthcare professionals with a user-friendly tool that simplifies their daily tasks.

Contributing
We welcome contributions from the community! If you'd like to enhance the Simplified HMIS project, please follow our contribution guidelines.

License
This project is licensed under the XYZ License - see the LICENSE file for details.
