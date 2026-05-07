"""
SmartStudy AI - Main Application Window
Mô phỏng giao diện dashboard quản lý học tập
"""

import customtkinter as ctk
from tkinter import PhotoImage
from datetime import datetime, timedelta
import calendar

from ui.sidebar import Sidebar
from ui.dashboard import DashboardPage
from ui.schedule import SchedulePage
from ui.tasks import TasksPage
from ui.ai_chat import AIChatPage
from ui.profile import ProfilePage
from ui.widgets import (
    StatCard, CalendarWidget, TaskListWidget, 
    QuickActions, NotificationPanel
)


class SmartStudyApp(ctk.CTk):
    """Main Application Window"""
    
    def __init__(self):
        super().__init__()
        
        # Configure window
        self.title("SmartStudy AI - Quản lý Học tập")
        self.geometry("1400x850")
        self.minsize(1200, 700)
        
        # Configure grid layout (sidebar: content = 1:4)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        
        # Initialize theme colors
        self.primary_color = "#667eea"
        self.secondary_color = "#764ba2"
        self.success_color = "#11998e"
        self.warning_color = "#f59e0b"
        self.danger_color = "#ef4444"
        
        # Initialize data (mock data for demo) - MUST be before create_widgets
        self.init_mock_data()
        
        # Create widgets
        self.create_widgets()
        
        # Show dashboard by default
        self.show_page("dashboard")
    
    def create_widgets(self):
        """Create all widgets in the application"""
        
        # ==================== SIDEBAR ====================
        self.sidebar = Sidebar(self, self)
        
        # ==================== MAIN CONTENT AREA ====================
        # This container will hold all pages
        self.content_container = ctk.CTkFrame(
            self, 
            fg_color="#f8f9fa",
            corner_radius=0
        )
        self.content_container.grid(row=0, column=1, sticky="nsew")
        self.content_container.grid_rowconfigure(0, weight=1)
        self.content_container.grid_columnconfigure(0, weight=1)
        
        # Create pages
        self.pages = {}
        self.pages["dashboard"] = DashboardPage(self.content_container, self)
        self.pages["schedule"] = SchedulePage(self.content_container, self)
        self.pages["tasks"] = TasksPage(self.content_container, self)
        self.pages["ai_chat"] = AIChatPage(self.content_container, self)
        self.pages["profile"] = ProfilePage(self.content_container, self)
        
        # Place all pages at the same position (stacked)
        for page in self.pages.values():
            page.grid(row=0, column=0, sticky="nsew")
    
    def init_mock_data(self):
        """Initialize mock data for demonstration"""
        # Current user info
        self.current_user = {
            "name": "Nguyễn Văn Minh",
            "student_id": "B21DCCN001",
            "email": "minh.nv@example.com",
            "avatar": None,
            "gpa": 3.45,
            "credits_completed": 78,
            "total_credits": 140
        }
        
        # Today's tasks
        self.tasks = [
            {
                "id": 1,
                "title": "Nộp báo cáo nhóm",
                "subject": "Lập trình Python",
                "due_time": "14:00",
                "priority": "high",
                "completed": False
            },
            {
                "id": 2,
                "title": "Ôn tập chương 5",
                "subject": "Cấu trúc dữ liệu",
                "due_time": "18:00",
                "priority": "medium",
                "completed": False
            },
            {
                "id": 3,
                "title": "Hoàn thành quiz online",
                "subject": "Toán rời rạc",
                "due_time": "23:59",
                "priority": "low",
                "completed": False
            }
        ]
        
        # Schedule for current week
        self.schedule = [
            {
                "day": "Thứ 2",
                "date": datetime.now().strftime("%d/%m"),
                "classes": [
                    {"time": "07:00 - 09:30", "name": "Lập trình Python", "room": "A101", "type": "LT"},
                    {"time": "10:00 - 12:00", "name": "Cấu trúc dữ liệu", "room": "B202", "type": "LT"},
                    {"time": "13:00 - 15:30", "name": "Toán rời rạc", "room": "C303", "type": "LT"},
                    {"time": "16:00 - 18:00", "name": "Giải tích", "room": "D404", "type": "LT"}
                ]
            },
            {
                "day": "Thứ 3",
                "date": (datetime.now() + timedelta(days=1)).strftime("%d/%m"),
                "classes": [
                    {"time": "07:00 - 09:30", "name": "Cấu trúc dữ liệu", "room": "C301", "type": "LT"}
                ]
            },
            {
                "day": "Thứ 4",
                "date": (datetime.now() + timedelta(days=2)).strftime("%d/%m"),
                "classes": [
                    {"time": "13:00 - 15:30", "name": "Toán rời rạc", "room": "D102", "type": "LT"},
                    {"time": "16:00 - 18:00", "name": "Tiếng Anh chuyên ngành", "room": "E201", "type": "TH"}
                ]
            },
            {
                "day": "Thứ 5",
                "date": (datetime.now() + timedelta(days=3)).strftime("%d/%m"),
                "classes": [
                    {"time": "07:00 - 09:30", "name": "Mạng máy tính", "room": "F101", "type": "LT"}
                ]
            },
            {
                "day": "Thứ 6",
                "date": (datetime.now() + timedelta(days=4)).strftime("%d/%m"),
                "classes": [
                    {"time": "10:00 - 12:00", "name": "Thực hành mạng", "room": "Lab 1", "type": "TH"},
                    {"time": "13:00 - 15:30", "name": "Giải tích", "room": "G301", "type": "LT"}
                ]
            },
            {
                "day": "Thứ 7",
                "date": (datetime.now() + timedelta(days=5)).strftime("%d/%m"),
                "classes": [
                    {"time": "08:00 - 10:30", "name": "Vật lý đại cương", "room": "H101", "type": "LT"}
                ]
            }
        ]
        
        # Statistics
        self.stats = {
            "gpa": 3.45,
            "attendance_rate": 92,
            "tasks_completed": 28,
            "study_hours": 156,
            "courses": 8,
            "deadlines_this_week": 5,
            "total_periods": 25,
            "study_periods": 20,
            "self_study": 5,
            "completion_rate": 85
        }
        
        # Notifications
        self.notifications = [
            {"icon": "📢", "title": "Thông báo", "content": "Nghỉ học môn Triết học ngày 10/05"},
            {"icon": "📋", "title": "Cập nhật", "content": "Lịch thi giữa kỳ đã được cập nhật"},
            {"icon": "📅", "title": "Nhắc nhở", "content": "Hạn nộp bài tập Python: 12/05"}
        ]
    
    def show_page(self, page_name):
        """Switch to a specific page"""
        # Update sidebar selection
        self.sidebar.set_active(page_name)
        
        # Raise the selected page to the top
        page = self.pages.get(page_name)
        if page:
            page.tkraise()
            
            # Refresh page data if needed
            if hasattr(page, 'refresh'):
                page.refresh()
    
    def get_user_info(self):
        """Get current user information"""
        return self.current_user
    
    def get_tasks(self):
        """Get current tasks"""
        return self.tasks
    
    def get_schedule(self):
        """Get current schedule"""
        return self.schedule
    
    def get_stats(self):
        """Get statistics"""
        return self.stats
    
    def get_notifications(self):
        """Get notifications"""
        return self.notifications


# Run the application
if __name__ == "__main__":
    app = SmartStudyApp()
    app.mainloop()
