import tkinter as tk
from tkinter import ttk, messagebox

class BMICalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI Calculator")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        
        # Style configuration
        style = ttk.Style()
        style.configure('TLabel', font=('Arial', 12))
        style.configure('TButton', font=('Arial', 12))
        style.configure('TEntry', font=('Arial', 12))
        
        # Create main frame
        main_frame = ttk.Frame(root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Title
        title_label = ttk.Label(main_frame, text="BMI Calculator", font=('Arial', 20, 'bold'))
        title_label.grid(row=0, column=0, columnspan=2, pady=20)
        
        # Weight input
        ttk.Label(main_frame, text="Weight (kg):").grid(row=1, column=0, pady=10, sticky=tk.W)
        self.weight_var = tk.StringVar()
        self.weight_entry = ttk.Entry(main_frame, textvariable=self.weight_var)
        self.weight_entry.grid(row=1, column=1, pady=10)
        
        # Height input
        ttk.Label(main_frame, text="Height (cm):").grid(row=2, column=0, pady=10, sticky=tk.W)
        self.height_var = tk.StringVar()
        self.height_entry = ttk.Entry(main_frame, textvariable=self.height_var)
        self.height_entry.grid(row=2, column=1, pady=10)
        
        # Calculate button
        calculate_btn = ttk.Button(main_frame, text="Calculate BMI", command=self.calculate_bmi)
        calculate_btn.grid(row=3, column=0, columnspan=2, pady=20)
        
        # Result labels
        self.bmi_label = ttk.Label(main_frame, text="Your BMI: ", font=('Arial', 14))
        self.bmi_label.grid(row=4, column=0, columnspan=2, pady=10)
        
        self.category_label = ttk.Label(main_frame, text="Category: ", font=('Arial', 14))
        self.category_label.grid(row=5, column=0, columnspan=2, pady=10)
        
        # BMI Categories information
        categories_frame = ttk.LabelFrame(main_frame, text="BMI Categories", padding="10")
        categories_frame.grid(row=6, column=0, columnspan=2, pady=20, sticky=(tk.W, tk.E))
        
        categories = [
            "Underweight: < 18.5",
            "Normal weight: 18.5 - 24.9",
            "Overweight: 25 - 29.9",
            "Obese: ≥ 30"
        ]
        
        for i, category in enumerate(categories):
            ttk.Label(categories_frame, text=category).grid(row=i, column=0, sticky=tk.W)
    
    def calculate_bmi(self):
        try:
            weight = float(self.weight_var.get())
            height = float(self.height_var.get()) / 100  # Convert cm to meters
            
            if weight <= 0 or height <= 0:
                raise ValueError
            
            bmi = weight / (height * height)
            category = self.get_bmi_category(bmi)
            
            self.bmi_label.config(text=f"Your BMI: {bmi:.1f}")
            self.category_label.config(text=f"Category: {category}")
            
        except ValueError:
            messagebox.showerror("Error", "Please enter valid weight and height values!")
    
    def get_bmi_category(self, bmi):
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 25:
            return "Normal weight"
        elif 25 <= bmi < 30:
            return "Overweight"
        else:
            return "Obese"

def main():
    root = tk.Tk()
    app = BMICalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()