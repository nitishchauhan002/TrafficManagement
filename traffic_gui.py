import tkinter as tk
from tkinter import messagebox
from fpdf import FPDF
import random
from datetime import datetime

# 🚗 Random Vehicle Number Generator
def generate_vehicle_number():
    state_code = random.choice(['BR', 'UP', 'DL', 'MH', 'RJ'])
    rto_code = f"{random.randint(1,99):02d}"
    series = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=2))
    number = f"{random.randint(1000,9999)}"
    return f"{state_code}{rto_code}{series}{number}"

# 💸 PDF Challan Generator
def generate_challan_pdf(vehicle_number, owner_name, speed, fine_amount=500):
    challan_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    file_name = f"Challan_{vehicle_number}.pdf"

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "Traffic Violation Challan", ln=True, align='C')  # 🚨 removed
    pdf.ln(10)

    pdf.set_font("Arial", '', 12)
    pdf.cell(0, 10, f"Date & Time: {challan_time}", ln=True)
    pdf.cell(0, 10, f"Vehicle Number: {vehicle_number}", ln=True)
    pdf.cell(0, 10, f"Owner Name: {owner_name}", ln=True)
    pdf.cell(0, 10, f"Speed Detected: {speed} km/h", ln=True)

    if speed > 60:
        pdf.cell(0, 10, f"Fine Amount: rs{fine_amount}", ln=True)
        pdf.cell(0, 10, "Violation: Speed Limit Exceeded", ln=True)  # 💨 removed
    else:
        pdf.cell(0, 10, "No Violation Detected.", ln=True)

    pdf.output(file_name)
    messagebox.showinfo("✅ Challan Generated", f"PDF Saved: {file_name}")

# 🎬 GUI Setup
def start_gui():
    def animate_lights():
        colors = ['red', 'yellow', 'green']
        for i in range(3):
            canvas.itemconfig(lights[i], fill='gray')
        canvas.itemconfig(lights[current_light[0]], fill=colors[current_light[0]])
        current_light[0] = (current_light[0] + 1) % 3
        window.after(1000, animate_lights)

    def capture_photo():
        messagebox.showinfo("📸 Photo Captured", "Dummy: Vehicle photo saved as 'vehicle_photo.jpg'!")

    def generate_challan():
        speed_text = speed_entry.get().strip()
        if not speed_text.isdigit():
            messagebox.showerror("⚠️ Invalid Input", "Please enter a valid numeric speed!")
            return

        speed = int(speed_text)
        vehicle_number = generate_vehicle_number()
        owner_name = "Rohit Kumar"
        generate_challan_pdf(vehicle_number, owner_name, speed)

    window = tk.Tk()
    window.title("Traffic Management System")
    window.geometry("300x450")
    window.resizable(False, False)

    canvas = tk.Canvas(window, width=200, height=300, bg='black')
    canvas.pack(pady=10)

    lights = [
        canvas.create_oval(50, 20, 150, 120, fill='gray'),
        canvas.create_oval(50, 110, 150, 210, fill='gray'),
        canvas.create_oval(50, 200, 150, 300, fill='gray')
    ]

    current_light = [0]
    animate_lights()

    label = tk.Label(window, text="Enter Vehicle Speed (km/h):", font=('Arial', 10))
    label.pack()

    speed_entry = tk.Entry(window, font=('Arial', 12), justify='center')
    speed_entry.pack(pady=5)

    capture_button = tk.Button(window, text="📸 Capture Photo", bg='lightblue', command=capture_photo)
    capture_button.pack(pady=5)

    challan_button = tk.Button(window, text="rs Generate Challan", bg='lightgreen', command=generate_challan)
    challan_button.pack(pady=5)

    window.mainloop()

# Run GUI
start_gui()
