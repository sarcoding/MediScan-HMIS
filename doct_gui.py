import tkinter as tk
from tkinter import ttk
import speech_recognition as sr
import asyncio
import websockets
import json
import queue
import threading


data_refresh_rate = 5
token_number = 0
patient_queue = queue.Queue()

def doctor_main():
    async def receive_patient_data(websocket, path):
        global token_number
        
        while True:
            await asyncio.sleep(data_refresh_rate)
            try:
                patient_data = await websocket.recv()
            except websockets.exceptions.ConnectionClosedOK:
                print(" Waiting for a new patient...")
                continue

            patient_data = json.loads(patient_data)

            token_number += 1 

            patient_queue.put((token_number, patient_data))
            name, age, ailment = patient_data['name'], patient_data['age'], patient_data['ailment']
            print(f"Patient {name} registered with Token #{token_number}")
            await asyncio.sleep(1)  


    async def process_patients():
        global waiting_message_printed

        while True:
            if not patient_queue.empty():
                print("New Patients in Queue")
                await asyncio.sleep(2)
            else:
                await asyncio.sleep(1)

    def start_websocket_server():
        asyncio.set_event_loop(asyncio.new_event_loop())
        start_server = websockets.serve(receive_patient_data, "localhost", 8765)
        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_until_complete(process_patients())


    def submit_data():
        diag = diagnosis_combo.get()
        pres = prescription_combo.get()
        """

        diag and pres can be added to the database from here

        """
        token_num, patient_data = patient_queue.get()
        
        name_var.set(patient_data['name'])
        age_var.set(patient_data['age'])
        ailment_var.set(patient_data['ailment'])
        height_var.set(patient_data['height'])
        weight_var.set(patient_data['weight'])
        

    def recognize_speech(entry_var):
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            print("Listening...")
            try:
                audio = recognizer.listen(source)
                text = recognizer.recognize_google(audio)
                entry_var.set(text)
            except sr.UnknownValueError:
                print("Could not understand audio.")
            except sr.RequestError as e:
                print(f"Could not request results; {e}")

    # Create the main window
    root = tk.Tk()
    root.title("Patient Information")

    # Create Labels and Entry widgets for each field
    name_label = tk.Label(root, text="Name:")
    name_label.grid(row=0, column=0)
    name_var = tk.StringVar()
    name_var_lab = tk.Label(root, textvariable=name_var)
    name_var_lab.grid(row=0, column=1)


    age_label = tk.Label(root, text="Age:")
    age_label.grid(row=1, column=0)
    age_var = tk.StringVar()
    age_var_lab = tk.Label(root, textvariable=age_var)
    age_var_lab.grid(row=1, column=1)

    ailment_label = tk.Label(root, text="Ailment:")
    ailment_label.grid(row=2, column=0)
    ailment_var = tk.StringVar()
    ailment_var_lab = tk.Label(root, textvariable=ailment_var)
    ailment_var_lab.grid(row=2, column=1)

    height_label = tk.Label(root, text="Height (cm):")
    height_label.grid(row=3, column=0)
    height_var = tk.StringVar()
    height_var_lab = tk.Label(root, textvariable=height_var)
    height_var_lab.grid(row=3, column=1)

    weight_label = tk.Label(root, text="Weight (kg):")
    weight_label.grid(row=4, column=0)
    weight_var = tk.StringVar()
    weight_var_lab = tk.Label(root, textvariable=weight_var)
    weight_var_lab.grid(row=4, column=1)

    # Diagnosis and Prescription Combo Boxes
    diagnosis_label = tk.Label(root, text="Diagnosis:")
    diagnosis_label.grid(row=5, column=0)
    diagnosis_var = tk.StringVar()
    diagnosis_combo = ttk.Combobox(root, textvariable=diagnosis_var, values=["Diagnosis 1", "Diagnosis 2", "Diagnosis 3"])
    diagnosis_combo.grid(row=5, column=1)

    prescription_label = tk.Label(root, text="Prescription:")
    prescription_label.grid(row=6, column=0)
    prescription_var = tk.StringVar()
    prescription_combo = ttk.Combobox(root, textvariable=prescription_var, values=["Prescription 1", "Prescription 2", "Prescription 3"])
    prescription_combo.grid(row=6, column=1)

    # Microphone Button for Diagnosis and Prescription
    microphone_button_diagnosis = tk.Button(root, text="🎤", command=lambda: recognize_speech(diagnosis_var))
    microphone_button_diagnosis.grid(row=5, column=2)

    microphone_button_prescription = tk.Button(root, text="🎤", command=lambda: recognize_speech(prescription_var))
    microphone_button_prescription.grid(row=6, column=2)

    # Submit button
    submit_button = tk.Button(root, text="Submit", command=submit_data)
    submit_button.grid(row=7, columnspan=2)

    websocket_thread = threading.Thread(target=start_websocket_server)
    websocket_thread.start()
    # Start the Tkinter event loop
    root.mainloop()


if __name__ == "__main__":
    doctor_main()