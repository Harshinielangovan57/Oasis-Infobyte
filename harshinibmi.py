import tkinter as tk
from tkinter import messagebox

# Function to calculate BMI and show result
def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get()) / 100
        
        bmi = weight / (height ** 2)
        bmi = round(bmi, 2)

        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obesity"

        result_label.config(text=f"BMI: {bmi}\nCategory: {category}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers for weight and height.")

root = tk.Tk()
root.title("BMI Calculator")

label_weight = tk.Label(root, text="Enter your weight (kg):")
label_weight.pack(pady=10)
entry_weight = tk.Entry(root)
entry_weight.pack()

label_height = tk.Label(root, text="Enter your height (cm):")
label_height.pack(pady=10)
entry_height = tk.Entry(root)
entry_height.pack()

calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.pack(pady=20)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=20)

# Start the main event loop
root.mainloop()

