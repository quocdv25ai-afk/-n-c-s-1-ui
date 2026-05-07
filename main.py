"""
SmartStudy AI - Student Learning Management Application
Main Entry Point

Tác giả phần giao diện: [Tên sinh viên]
"""

import sys
import os

# Thêm thư mục hiện tại vào path để import được app.py
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import customtkinter as ctk

# Import trực tiếp từ app.py
from app import SmartStudyApp


def main():
    """Main entry point for the application"""
    # Set appearance mode
    ctk.set_appearance_mode("light")  # Options: "dark", "light", "system"
    
    # Set default color theme  
    ctk.set_default_color_theme("blue")  # Options: "blue", "green", "dark-blue", "purple"
    
    # Create and run application
    app = SmartStudyApp()
    app.mainloop()


if __name__ == "__main__":
    main()
