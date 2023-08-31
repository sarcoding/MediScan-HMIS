import asyncio
import websockets
import json
from extract import search

async def add_new_patient(abha_no, height, weight):
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        try:
            name, age, ailment = search(abha_no)
            patient_data = {
                "name": name,
                "age": int(age),
                "ailment": ailment,
                "height": height,
                "weight": weight
            }

            await websocket.send(json.dumps(patient_data))
            print("Patient data sent successfully.")

        except Exception as e:
            print(f"Error: {e}")
            print("Wrong Abha No.")

if __name__ == "__main__":
    while True:
        aNo = int(input("Enter patient's Abha No.: "))
        height = float(input("Enter patient's height (in cm): "))
        weight = float(input("Enter patient's weight (in kg): "))

        asyncio.get_event_loop().run_until_complete(add_new_patient(aNo, height, weight))
