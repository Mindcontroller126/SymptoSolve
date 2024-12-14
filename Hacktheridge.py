import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import re

# More detailed symptom-disease mapping with expanded treatments and extra info.
symptom_disease_mapping = {
    # Respiratory Issues
    "fever": {
        "disease": "Flu",
        "treatment": "Rest, drink plenty of fluids, take fever-reducing medications like paracetamol.",
        "info": "Flu is a viral infection that affects the respiratory system. It can be accompanied by body aches and chills."
    },
    "cough": {
        "disease": "Cold",
        "treatment": "Rest, drink warm liquids, use cough syrup, avoid cold air.",
        "info": "A cold is a viral infection of the upper respiratory tract. It commonly causes a runny nose, cough, and sore throat."
    },
    "shortness of breath": {
        "disease": "Asthma",
        "treatment": "Use prescribed inhalers, avoid allergens, maintain a healthy weight.",
        "info": "Asthma is a chronic disease that inflames and narrows the airways, leading to difficulty in breathing."
    },
    "wheezing": {
        "disease": "Chronic Obstructive Pulmonary Disease (COPD)",
        "treatment": "Quit smoking, use prescribed bronchodilators, pulmonary rehabilitation.",
        "info": "COPD is a lung disease that makes it hard to breathe, often caused by long-term exposure to harmful irritants like tobacco smoke."
    },

    # Digestive Issues
    "nausea": {
        "disease": "Gastritis",
        "treatment": "Avoid spicy foods, drink water, take antacids or proton-pump inhibitors.",
        "info": "Gastritis is inflammation of the stomach lining that can lead to nausea, pain, and vomiting."
    },
    "vomiting": {
        "disease": "Gastroenteritis",
        "treatment": "Stay hydrated, eat bland foods, avoid dairy and caffeine, take anti-nausea medications.",
        "info": "Gastroenteritis is the inflammation of the stomach and intestines caused by a viral or bacterial infection."
    },
    "diarrhea": {
        "disease": "Irritable Bowel Syndrome (IBS)",
        "treatment": "Eat a balanced diet, avoid trigger foods, take antispasmodics.",
        "info": "IBS is a common digestive disorder causing symptoms like diarrhea, constipation, and abdominal pain."
    },

    # Cardiovascular Issues
    "chest pain": {
        "disease": "Heart Attack",
        "treatment": "Call emergency services immediately, chew aspirin (if recommended), keep calm.",
        "info": "A heart attack occurs when the blood flow to a part of the heart is blocked. It may be accompanied by sweating and dizziness."
    },
    "palpitations": {
        "disease": "Arrhythmia",
        "treatment": "Take prescribed anti-arrhythmic medication, avoid excessive alcohol and caffeine.",
        "info": "Arrhythmia is an irregular heartbeat. It can cause palpitations, dizziness, and shortness of breath."
    },

    # Neurological Issues
    "headache": {
        "disease": "Migraine",
        "treatment": "Rest in a dark, quiet room, avoid triggers, use over-the-counter pain relief like ibuprofen or prescribed triptans.",
        "info": "Migraine is a severe headache often accompanied by nausea, sensitivity to light, and sometimes visual disturbances."
    },
    "dizziness": {
        "disease": "Vertigo",
        "treatment": "Avoid sudden head movements, perform balance exercises, take prescribed anti-dizziness medications.",
        "info": "Vertigo is the sensation that you or your surroundings are spinning. It is often related to inner ear issues."
    },

    # Skin Conditions
    "rash": {
        "disease": "Eczema",
        "treatment": "Use moisturizing creams, avoid triggers, take prescribed corticosteroids.",
        "info": "Eczema is a condition that causes inflamed, itchy, red skin. It can be triggered by allergens or stress."
    },
    "itching": {
        "disease": "Allergic Reaction",
        "treatment": "Take antihistamines, avoid allergens, use soothing creams.",
        "info": "Itching can be caused by an allergic reaction to foods, pollen, or insect stings. It may also be a symptom of other conditions."
    },

    # Urinary Issues
    "painful urination": {
        "disease": "Urinary Tract Infection (UTI)",
        "treatment": "Drink plenty of fluids, take prescribed antibiotics.",
        "info": "A UTI is an infection of the urinary tract that can cause pain, burning during urination, and frequent urination."
    },
    "blood in my urine": {
        "disease": "Kidney Stones",
        "treatment": "Increase fluid intake, pain management with NSAIDs, may require surgical removal.",
        "info": "Kidney stones are hard deposits of minerals and salts that form in the kidneys, causing intense pain and sometimes bleeding."
    },

    # Endocrine Issues
    "excessive thirst": {
        "disease": "Diabetes",
        "treatment": "Monitor blood sugar, take prescribed insulin or medications, maintain a healthy diet.",
        "info": "Diabetes is a metabolic disorder where the body is unable to regulate blood sugar levels, leading to symptoms like excessive thirst and urination."
    },
    "fatigue": {
        "disease": "Hypothyroidism",
        "treatment": "Take synthetic thyroid hormones as prescribed.",
        "info": "Hypothyroidism occurs when the thyroid gland doesn't produce enough thyroid hormones, leading to fatigue, weight gain, and sensitivity to cold."
    }
}

# Function to detect the disease based on symptoms in a sentence
def diagnose_from_sentence(sentence):
    symptoms = []
    for symptom in symptom_disease_mapping:
        if re.search(r'\b' + re.escape(symptom) + r'\b', sentence.lower()):
            symptoms.append(symptom)
    if not symptoms:
        return ["Sorry, no symptoms matched. Please try again with different symptoms."]
    diagnosis = []
    for symptom in symptoms:
        disease_info = symptom_disease_mapping[symptom]
        diagnosis.append(f"Symptom: '{symptom}'")
        diagnosis.append(f"Possible Disease: {disease_info['disease']}")
        diagnosis.append(f"Treatment: {disease_info['treatment']}")
        diagnosis.append(f"Additional Info: {disease_info['info']}")
    return diagnosis

# Function to display diagnosis results
def display_diagnosis():
    user_input = symptom_entry.get()
    if not user_input.strip():
        messagebox.showerror("Input Error", "Please enter some symptoms.")
        return
    result = diagnose_from_sentence(user_input)
    diagnosis_text.delete(1.0, tk.END)
    diagnosis_text.insert(tk.END, "Diagnosing...\n\n")
    window.after(1000, lambda: update_result(diagnosis_text, result))

def update_result(diagnosis_text, result):
    for line in result:
        diagnosis_text.insert(tk.END, line + "\n")
    diagnosis_text.insert(tk.END, "\nPlease remember, this is just a suggestion. Consult a healthcare professional for an accurate diagnosis.")

# Function to draw a hexagonal pattern
def draw_hexagonal_pattern(canvas, width, height):
    hex_size = 40  # Size of a single hexagon
    dx = 3 ** 0.5 * hex_size  # Horizontal distance between centers
    dy = 1.5 * hex_size  # Vertical distance between centers

    canvas.create_rectangle(0, 0, width, height, fill="#1E2A47", outline="")  # Background fill

    for row in range(int(height / dy) + 2):
        y_offset = row * dy
        for col in range(int(width / dx) + 2):
            x_offset = col * dx
            if row % 2 == 1:
                x_offset += dx / 2
            points = [
                x_offset, y_offset - hex_size / 2,
                x_offset + dx / 2, y_offset,
                x_offset, y_offset + hex_size / 2,
                x_offset - dx / 2, y_offset,
            ]
            canvas.create_polygon(points, outline="black", fill="", width=1)

# Create the main window
window = tk.Tk()
window.title("Symptom Checker Chatbot")
window.geometry("800x600")

# Create a Canvas widget for the background
canvas = tk.Canvas(window, width=800, height=600)
canvas.pack(fill="both", expand=True)
draw_hexagonal_pattern(canvas, 800, 600)

# Add a label with modern styling
label = tk.Label(canvas, text="Enter your symptoms (comma separated):", font=("Times New Roman", 16, "bold"), bg=None, fg="#000000")
label_window = canvas.create_window(400, 50, window=label)

# Create a stylish text entry widget
symptom_entry = tk.Entry(canvas, font=("Times New Roman", 14), width=40, bd=2, relief="solid", fg="#333333", highlightthickness=1, highlightbackground="#5A6D8C", highlightcolor="#5A6D8C")
symptom_entry_window = canvas.create_window(400, 120, window=symptom_entry)

# Create a bold black "Submit Symptoms" button
submit_button = tk.Button(canvas, text="Submit Symptoms", command=display_diagnosis, font=("Times New Roman", 14, "bold"), bg="#000000", fg="#ffffff", bd=3, relief="flat")
submit_button_window = canvas.create_window(400, 180, window=submit_button)

# Add a styled text widget for diagnosis output
diagnosis_text = tk.Text(canvas, font=("Times New Roman", 12), width=58, height=8, wrap=tk.WORD, bg="#f7f7f7", fg="#333333", bd=2, relief="solid", padx=10, pady=10)
diagnosis_text_window = canvas.create_window(400, 350, window=diagnosis_text)

# Start the Tkinter event loop
window.mainloop()
