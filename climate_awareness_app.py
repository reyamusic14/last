import tkinter as tk
from tkinter import ttk, messagebox
import requests
from PIL import Image, ImageTk
from io import BytesIO
import json
import os

class ClimateAwarenessApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Climate Change Awareness")
        self.root.geometry("1000x800")
        
        # Set color scheme
        self.colors = {
            "primary": "#4CAF50",
            "secondary": "#45a049",
            "background": "#f8f9fa",
            "text": "#333333"
        }
        
        self.root.configure(bg=self.colors["background"])
        
        self.setup_ui()
        
    def setup_ui(self):
        # Header
        header_frame = tk.Frame(self.root, bg=self.colors["background"])
        header_frame.pack(pady=20)
        
        tk.Label(
            header_frame,
            text="Climate Vision",
            font=("Helvetica", 24, "bold"),
            fg=self.colors["primary"],
            bg=self.colors["background"]
        ).pack()
        
        # Input Section
        input_frame = tk.Frame(self.root, bg=self.colors["background"])
        input_frame.pack(pady=20)
        
        # Location Entry
        tk.Label(
            input_frame,
            text="Location:",
            bg=self.colors["background"],
            fg=self.colors["text"]
        ).pack()
        
        self.location_entry = tk.Entry(input_frame, width=30)
        self.location_entry.pack(pady=5)
        
        # Climate Issue Dropdown
        tk.Label(
            input_frame,
            text="Climate Issue:",
            bg=self.colors["background"],
            fg=self.colors["text"]
        ).pack()
        
        self.issues = [
            "Rising Sea Levels",
            "Deforestation",
            "Air Pollution",
            "Extreme Weather"
        ]
        
        self.issue_var = tk.StringVar()
        self.issue_dropdown = ttk.Combobox(
            input_frame,
            textvariable=self.issue_var,
            values=self.issues,
            width=27
        )
        self.issue_dropdown.pack(pady=5)
        
        # Stats Frame
        stats_frame = tk.Frame(
            self.root,
            bg="white",
            relief="raised",
            bd=1
        )
        stats_frame.pack(pady=20, padx=20, fill="x")
        
        # CO2 Level Display
        co2_frame = tk.Frame(stats_frame, bg="white")
        co2_frame.pack(side="left", expand=True, pady=10)
        
        tk.Label(
            co2_frame,
            text="CO2 Level",
            bg="white",
            fg=self.colors["text"]
        ).pack()
        
        tk.Label(
            co2_frame,
            text="0.0409 mg/m³",
            font=("Helvetica", 12, "bold"),
            bg="white",
            fg=self.colors["primary"]
        ).pack()
        
        # Risk Level Display
        risk_frame = tk.Frame(stats_frame, bg="white")
        risk_frame.pack(side="right", expand=True, pady=10)
        
        tk.Label(
            risk_frame,
            text="Risk Level",
            bg="white",
            fg=self.colors["text"]
        ).pack()
        
        tk.Label(
            risk_frame,
            text="Low",
            font=("Helvetica", 12, "bold"),
            bg="white",
            fg=self.colors["primary"]
        ).pack()
        
        # Generate Button
        generate_btn = tk.Button(
            self.root,
            text="Generate Visualizations",
            bg=self.colors["primary"],
            fg="white",
            command=self.generate_visualizations,
            relief="flat",
            padx=20,
            pady=10
        )
        generate_btn.pack(pady=20)
        
        # Image Display Area
        self.image_frame = tk.Frame(self.root, bg=self.colors["background"])
        self.image_frame.pack(pady=20, expand=True, fill="both")
        
        # Action Buttons
        action_frame = tk.Frame(self.root, bg=self.colors["background"])
        action_frame.pack(pady=20)
        
        tk.Button(
            action_frame,
            text="Save to Gallery",
            bg=self.colors["primary"],
            fg="white",
            command=self.save_to_gallery,
            relief="flat",
            padx=15,
            pady=8
        ).pack(side="left", padx=5)
        
        tk.Button(
            action_frame,
            text="Share",
            bg=self.colors["primary"],
            fg="white",
            command=self.share_image,
            relief="flat",
            padx=15,
            pady=8
        ).pack(side="left", padx=5)

    def generate_visualizations(self):
        location = self.location_entry.get()
        issue = self.issue_var.get()
        
        if not location or not issue:
            messagebox.showwarning("Input Required", "Please enter both location and climate issue.")
            return
            
        # Here you would integrate with AI image generation services
        # For now, we'll show a message
        messagebox.showinfo("Generation", f"Generating visualizations for {issue} in {location}")
        
    def save_to_gallery(self):
        messagebox.showinfo("Save", "Image saved to gallery")
        
    def share_image(self):
        messagebox.showinfo("Share", "Opening sharing options...")

def main():
    root = tk.Tk()
    app = ClimateAwarenessApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()