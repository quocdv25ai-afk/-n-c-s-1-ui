"""
SmartStudy AI - Reusable Widgets
Các component UI tái sử dụng
"""

import customtkinter as ctk
from datetime import datetime, timedelta
import calendar


# ==================== STAT CARD ====================

class StatCard(ctk.CTkFrame):
    """Statistics card widget for dashboard"""
    
    def __init__(self, parent, title, value, subtitle="", icon="", color="#667eea", **kwargs):
        super().__init__(parent, **kwargs)
        
        self.configure(
            width=200,
            height=120,
            fg_color="#ffffff",
            corner_radius=16,
            border_width=0
        )
        
        # Icon
        if icon:
            icon_label = ctk.CTkLabel(
                self,
                text=icon,
                font=("Segoe UI Emoji", 28),
                text_color=color
            )
            icon_label.place(x=15, y=15)
        
        # Title
        title_label = ctk.CTkLabel(
            self,
            text=title,
            font=ctk.CTkFont(family="Segoe UI", size=12),
            text_color="#888888",
            anchor="w"
        )
        title_label.place(x=15, y=55)
        
        # Value
        value_label = ctk.CTkLabel(
            self,
            text=str(value),
            font=ctk.CTkFont(family="Segoe UI", size=28, weight="bold"),
            text_color="#333333",
            anchor="w"
        )
        value_label.place(x=15, y=75)
        
        # Subtitle
        if subtitle:
            subtitle_label = ctk.CTkLabel(
                self,
                text=subtitle,
                font=ctk.CTkFont(family="Segoe UI", size=10),
                text_color="#aaaaaa",
                anchor="w"
            )
            subtitle_label.place(x=15, y=105)


# ==================== CALENDAR WIDGET ====================

class CalendarWidget(ctk.CTkFrame):
    """Calendar widget for schedule display"""
    
    def __init__(self, parent, schedule_data=None, **kwargs):
        super().__init__(parent, **kwargs)
        
        self.schedule_data = schedule_data or []
        self.selected_date = datetime.now()
        
        self.configure(
            fg_color="#ffffff",
            corner_radius=16
        )
        
        self.create_widgets()
    
    def create_widgets(self):
        """Create calendar widgets"""
        # Header with month navigation
        header = ctk.CTkFrame(self, fg_color="transparent")
        header.pack(fill="x", padx=20, pady=15)
        
        prev_btn = ctk.CTkButton(
            header,
            text="◀",
            width=35,
            height=35,
            fg_color="#f0f0f0",
            hover_color="#e0e0e0",
            text_color="#333333",
            corner_radius=8,
            command=self.prev_month
        )
        prev_btn.pack(side="left")
        
        month_label = ctk.CTkLabel(
            header,
            text=datetime.now().strftime("%B %Y"),
            font=ctk.CTkFont(family="Segoe UI", size=18, weight="bold"),
            text_color="#333333"
        )
        month_label.pack(side="left", expand=True)
        
        next_btn = ctk.CTkButton(
            header,
            text="▶",
            width=35,
            height=35,
            fg_color="#f0f0f0",
            hover_color="#e0e0e0",
            text_color="#333333",
            corner_radius=8,
            command=self.next_month
        )
        next_btn.pack(side="right")
        
        # Day headers
        days_frame = ctk.CTkFrame(self, fg_color="transparent")
        days_frame.pack(fill="x", padx=20)
        
        days = ["T2", "T3", "T4", "T5", "T6", "T7", "CN"]
        for day in days:
            lbl = ctk.CTkLabel(
                days_frame,
                text=day,
                font=ctk.CTkFont(family="Segoe UI", size=12, weight="bold"),
                text_color="#888888",
                width=45,
                height=30
            )
            lbl.pack(side="left", padx=2)
        
        # Calendar grid
        self.grid_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.grid_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))
        
        self.draw_calendar()
    
    def draw_calendar(self):
        """Draw the calendar grid"""
        # Clear existing widgets
        for widget in self.grid_frame.winfo_children():
            widget.destroy()
        
        # Get current month info
        now = datetime.now()
        first_day = now.replace(day=1)
        month = first_day.month
        year = first_day.year
        
        # Find first day of week (Monday = 0)
        weekday = first_day.weekday()
        
        # Get days in month
        _, days_in_month = calendar.monthrange(year, month)
        
        # Create day cells
        day_num = 1
        for week in range(6):
            for day in range(7):
                cell_num = week * 7 + day
                
                if cell_num < weekday or day_num > days_in_month:
                    # Empty cell
                    placeholder = ctk.CTkFrame(self.grid_frame, fg_color="transparent")
                    placeholder.grid(row=week, column=day, padx=2, pady=2)
                else:
                    # Day cell
                    is_today = day_num == now.day
                    cell = self.create_day_cell(week, day, day_num, is_today)
                    day_num += 1
                    
                    if day_num > days_in_month:
                        break
    
    def create_day_cell(self, row, col, day, is_today):
        """Create a single day cell"""
        cell = ctk.CTkFrame(
            self.grid_frame,
            width=45,
            height=45,
            fg_color=("#e8e8f0" if is_today else "#f5f5f5"),
            corner_radius=10,
            border_width=2 if is_today else 0,
            border_color="#667eea"
        )
        cell.grid(row=row, column=col, padx=2, pady=2)
        cell.grid_propagate(False)
        
        # Day number
        color = "#667eea" if is_today else "#333333"
        lbl = ctk.CTkLabel(
            cell,
            text=str(day),
            font=ctk.CTkFont(family="Segoe UI", size=14, weight="bold" if is_today else "normal"),
            text_color=color
        )
        lbl.place(relx=0.5, rely=0.5, anchor="center")
        
        return cell
    
    def prev_month(self):
        """Go to previous month"""
        pass
    
    def next_month(self):
        """Go to next month"""
        pass


# ==================== TASK LIST WIDGET ====================

class TaskListWidget(ctk.CTkFrame):
    """Task list widget for displaying tasks"""
    
    def __init__(self, parent, tasks=None, on_complete=None, **kwargs):
        super().__init__(parent, **kwargs)
        
        self.tasks = tasks or []
        self.on_complete = on_complete
        
        self.configure(
            fg_color="transparent"
        )
        
        self.create_widgets()
    
    def create_widgets(self):
        """Create task list widgets"""
        for i, task in enumerate(self.tasks):
            self.add_task_item(task)
    
    def add_task_item(self, task):
        """Add a single task item"""
        item_frame = ctk.CTkFrame(
            self,
            fg_color="#ffffff",
            corner_radius=10,
            height=55
        )
        item_frame.pack(fill="x", pady=3)
        item_frame.pack_propagate(False)
        
        # Priority indicator
        priority_colors = {
            "high": "#ef4444",
            "medium": "#f59e0b", 
            "low": "#10b981"
        }
        priority_color = priority_colors.get(task.get("priority", "medium"), "#888888")
        
        indicator = ctk.CTkFrame(
            item_frame,
            width=4,
            fg_color=priority_color,
            corner_radius=2
        )
        indicator.place(x=0, y=8, relheight=0.6)
        
        # Checkbox
        checkbox = ctk.CTkCheckBox(
            item_frame,
            text="",
            width=25,
            fg_color="#667eea",
            hover_color="#764ba2",
            checkbox_width=18,
            checkbox_height=18,
            command=lambda t=task: self.toggle_task(t)
        )
        checkbox.place(x=12, y=18)
        
        # Task info
        title_label = ctk.CTkLabel(
            item_frame,
            text=task.get("title", ""),
            font=ctk.CTkFont(family="Segoe UI", size=12, weight="bold"),
            text_color="#333333",
            anchor="w"
        )
        title_label.place(x=45, y=10)
        
        subject_label = ctk.CTkLabel(
            item_frame,
            text=task.get("subject", ""),
            font=ctk.CTkFont(family="Segoe UI", size=10),
            text_color="#888888",
            anchor="w"
        )
        subject_label.place(x=45, y=28)
        
        # Due time
        due_label = ctk.CTkLabel(
            item_frame,
            text=f"⏰ {task.get('due_time', '')}",
            font=ctk.CTkFont(family="Segoe UI", size=10),
            text_color="#666666"
        )
        due_label.place(relx=0.98, y=20, anchor="e")
    
    def toggle_task(self, task):
        """Toggle task completion"""
        if self.on_complete:
            self.on_complete(task)


# ==================== WEEK CALENDAR GRID ====================

class WeekCalendarGrid(ctk.CTkFrame):
    """Week calendar grid widget - displays week schedule in a grid format"""
    
    def __init__(self, parent, schedule=None, start_offset=0, **kwargs):
        super().__init__(parent, **kwargs)
        
        self.schedule = schedule or []
        self.start_offset = start_offset
        
        self.configure(
            fg_color="transparent"
        )
        
        self.create_widgets()
    
    def create_widgets(self):
        """Create the week calendar grid"""
        # Day headers
        days_frame = ctk.CTkFrame(self, fg_color="transparent")
        days_frame.pack(fill="x", pady=(0, 10))
        
        days = ["Thứ 2", "Thứ 3", "Thứ 4", "Thứ 5", "Thứ 6", "Thứ 7", "CN"]
        
        for i, day in enumerate(days):
            day_frame = ctk.CTkFrame(
                days_frame,
                fg_color="#f0f0f0" if i < 5 else "#fff5e6",
                corner_radius=8,
                width=120,
                height=40
            )
            day_frame.grid(row=0, column=i, padx=4, sticky="ew")
            day_frame.pack_propagate(False)
            
            day_label = ctk.CTkLabel(
                day_frame,
                text=day,
                font=ctk.CTkFont(family="Segoe UI", size=12, weight="bold"),
                text_color="#333333" if i < 5 else "#b37400"
            )
            day_label.place(relx=0.5, rely=0.5, anchor="center")
        
        # Configure equal widths
        days_frame.grid_columnconfigure((0,1,2,3,4,5,6), weight=1)
        
        # Time slots
        time_slots = ["07:00", "09:00", "11:00", "13:00", "15:00", "17:00", "19:00"]
        
        for slot_idx, time in enumerate(time_slots):
            slot_frame = ctk.CTkFrame(self, fg_color="transparent")
            slot_frame.pack(fill="x", pady=2)
            
            # Time label
            time_label = ctk.CTkLabel(
                slot_frame,
                text=time,
                font=ctk.CTkFont(family="Segoe UI", size=10),
                text_color="#888888",
                width=45
            )
            time_label.pack(side="left", padx=(0, 5))
            
            # Day columns
            for day_idx in range(7):
                cell = ctk.CTkFrame(
                    slot_frame,
                    fg_color="#fafafa" if day_idx < 5 else "#fffcf5",
                    corner_radius=6,
                    height=50
                )
                cell.pack(side="left", fill="both", expand=True, padx=2)
                cell.pack_propagate(False)
                
                # Add classes if match
                self.add_class_to_cell(cell, day_idx, time)
    
    def add_class_to_cell(self, cell, day_idx, time_slot):
        """Add class information to the cell if there's a class at this time"""
        # Map schedule to this view
        class_colors = {
            "Lập trình Python": "#667eea",
            "Thực hành Python": "#667eea",
            "Cấu trúc dữ liệu": "#11998e",
            "Toán rời rạc": "#f59e0b",
            "Mạng máy tính": "#ef4444",
            "Thực hành mạng": "#ef4444",
            "Tiếng Anh chuyên ngành": "#8b5cf6",
            "Giải tích": "#10b981",
            "Vật lý đại cương": "#ec4899"
        }
        
        class_types = {
            "Lập trình Python": "LT",
            "Thực hành Python": "TH",
            "Cấu trúc dữ liệu": "LT",
            "Toán rời rạc": "LT",
            "Mạng máy tính": "LT",
            "Thực hành mạng": "TH",
            "Tiếng Anh chuyên ngành": "TH",
            "Giải tích": "LT",
            "Vật lý đại cương": "LT"
        }
        
        # Demo classes
        demo_schedule = [
            {"day": 0, "start": "07:00", "name": "Lập trình Python", "room": "A101", "type": "LT"},
            {"day": 0, "start": "10:00", "name": "Thực hành Python", "room": "B202", "type": "TH"},
            {"day": 1, "start": "07:00", "name": "Cấu trúc dữ liệu", "room": "C301", "type": "LT"},
            {"day": 2, "start": "13:00", "name": "Toán rời rạc", "room": "D102", "type": "LT"},
            {"day": 2, "start": "16:00", "name": "Tiếng Anh chuyên ngành", "room": "E201", "type": "TH"},
            {"day": 3, "start": "07:00", "name": "Mạng máy tính", "room": "F101", "type": "LT"},
            {"day": 4, "start": "10:00", "name": "Thực hành mạng", "room": "Lab 1", "type": "TH"},
            {"day": 4, "start": "13:00", "name": "Giải tích", "room": "G301", "type": "LT"},
            {"day": 5, "start": "08:00", "name": "Vật lý đại cương", "room": "H101", "type": "LT"},
        ]
        
        for cls in demo_schedule:
            if cls["day"] == day_idx and cls["start"] == time_slot:
                color = class_colors.get(cls["name"], "#667eea")
                
                class_card = ctk.CTkFrame(
                    cell,
                    fg_color=color,
                    corner_radius=5,
                    height=45
                )
                class_card.place(relx=0, rely=0, relwidth=1, relheight=1)
                
                type_badge = ctk.CTkLabel(
                    class_card,
                    text=cls["type"],
                    font=ctk.CTkFont(family="Segoe UI", size=8, weight="bold"),
                    text_color="#ffffff",
                    fg_color="#4a5bd8",
                    corner_radius=3,
                    width=22,
                    height=14
                )
                type_badge.place(x=3, y=3)
                
                name_label = ctk.CTkLabel(
                    class_card,
                    text=cls["name"],
                    font=ctk.CTkFont(family="Segoe UI", size=9, weight="bold"),
                    text_color="#ffffff"
                )
                name_label.place(relx=0.5, rely=0.35, anchor="center")
                
                room_label = ctk.CTkLabel(
                    class_card,
                    text=f"📍 {cls['room']}",
                    font=ctk.CTkFont(family="Segoe UI", size=8),
                    text_color="#e0e0ff"
                )
                room_label.place(relx=0.5, rely=0.7, anchor="center")
                
                break
    
    def update_week(self, offset):
        """Update the calendar when navigating weeks"""
        # For demo, just refresh the display
        pass


# ==================== TODO LIST WIDGET ====================

class TodoListWidget(ctk.CTkFrame):
    """Todo list widget with task items"""
    
    def __init__(self, parent, tasks=None, on_complete=None, **kwargs):
        super().__init__(parent, **kwargs)
        
        self.tasks = tasks or []
        self.on_complete = on_complete
        
        self.configure(
            fg_color="transparent"
        )
        
        self.create_widgets()
    
    def create_widgets(self):
        """Create todo list"""
        for task in self.tasks:
            self.add_todo_item(task)
    
    def add_todo_item(self, task):
        """Add a single todo item"""
        item_frame = ctk.CTkFrame(
            self,
            fg_color="#f8f9fa",
            corner_radius=10,
            height=70
        )
        item_frame.pack(fill="x", pady=5)
        item_frame.pack_propagate(False)
        
        # Priority color indicator
        priority_colors = {
            "high": "#ef4444",
            "medium": "#f59e0b", 
            "low": "#10b981"
        }
        priority_color = priority_colors.get(task.get("priority", "medium"), "#888888")
        
        indicator = ctk.CTkFrame(
            item_frame,
            width=4,
            fg_color=priority_color,
            corner_radius=2
        )
        indicator.place(x=0, y=10, relheight=0.7)
        
        # Checkbox
        checkbox = ctk.CTkCheckBox(
            item_frame,
            text="",
            width=28,
            height=28,
            fg_color="#667eea",
            hover_color="#5a6fd6",
            checkbox_width=22,
            checkbox_height=22,
            corner_radius=6,
            command=lambda t=task: self.toggle_task(t)
        )
        checkbox.place(x=15, y=21)
        
        # Task info
        info_frame = ctk.CTkFrame(item_frame, fg_color="transparent")
        info_frame.place(x=50, y=12, relwidth=0.65, relheight=1)
        
        title_label = ctk.CTkLabel(
            info_frame,
            text=task.get("title", ""),
            font=ctk.CTkFont(family="Segoe UI", size=13, weight="bold"),
            text_color="#333333",
            anchor="w"
        )
        title_label.pack(anchor="w")
        
        subject_label = ctk.CTkLabel(
            info_frame,
            text=task.get("subject", ""),
            font=ctk.CTkFont(family="Segoe UI", size=10),
            text_color="#888888",
            anchor="w"
        )
        subject_label.pack(anchor="w")
        
        # Due time with icon
        due_frame = ctk.CTkFrame(item_frame, fg_color="transparent")
        due_frame.place(relx=1, x=-10, y=0, relheight=1)
        
        due_label = ctk.CTkLabel(
            due_frame,
            text=f"⏰ {task.get('due_time', '')}",
            font=ctk.CTkFont(family="Segoe UI", size=10),
            text_color="#666666"
        )
        due_label.place(relx=1, rely=0.5, anchor="center", x=-5)
    
    def toggle_task(self, task):
        """Toggle task completion"""
        if self.on_complete:
            self.on_complete(task)


# ==================== QUICK ACTIONS ====================

class QuickActions(ctk.CTkFrame):
    """Quick actions widget"""
    
    def __init__(self, parent, actions=None, **kwargs):
        super().__init__(parent, **kwargs)
        
        self.actions = actions or [
            {"icon": "➕", "label": "Thêm Task", "color": "#667eea"},
            {"icon": "📅", "label": "Xem Lịch", "color": "#11998e"},
            {"icon": "📚", "label": "Học tập", "color": "#f59e0b"},
            {"icon": "💬", "label": "Chat AI", "color": "#764ba2"}
        ]
        
        self.configure(
            fg_color="#ffffff",
            corner_radius=16
        )
        
        self.create_widgets()
    
    def create_widgets(self):
        """Create quick action buttons"""
        # Title
        title = ctk.CTkLabel(
            self,
            text="Thao tác nhanh",
            font=ctk.CTkFont(family="Segoe UI", size=14, weight="bold"),
            text_color="#333333"
        )
        title.pack(anchor="w", padx=20, pady=(15, 10))
        
        # Buttons frame
        buttons_frame = ctk.CTkFrame(self, fg_color="transparent")
        buttons_frame.pack(fill="x", padx=15, pady=(0, 15))
        
        for i, action in enumerate(self.actions):
            btn = ctk.CTkButton(
                buttons_frame,
                text=f"{action['icon']}\n{action['label']}",
                width=70,
                height=70,
                fg_color=action["color"],
                hover_color=action["color"],
                text_color="#ffffff",
                font=ctk.CTkFont(family="Segoe UI", size=10),
                corner_radius=12,
                compound="top"
            )
            btn.grid(row=0, column=i, padx=5)


# ==================== NOTIFICATION PANEL ====================

class NotificationPanel(ctk.CTkFrame):
    """Notification panel widget"""
    
    def __init__(self, parent, notifications=None, **kwargs):
        super().__init__(parent, **kwargs)
        
        self.notifications = notifications or [
            {"icon": "📢", "title": "Nhắc nhở", "content": "Bài tập Python hết hạn trong 2 ngày"},
            {"icon": "📢", "title": "Thông báo", "content": "Lịch thi giữa kỳ đã được cập nhật"},
            {"icon": "📢", "title": "Sự kiện", "content": "Workshop AI vào thứ 7 tuần này"}
        ]
        
        self.configure(
            fg_color="#ffffff",
            corner_radius=16
        )
        
        self.create_widgets()
    
    def create_widgets(self):
        """Create notification items"""
        # Title
        title = ctk.CTkLabel(
            self,
            text="Thông báo",
            font=ctk.CTkFont(family="Segoe UI", size=14, weight="bold"),
            text_color="#333333"
        )
        title.pack(anchor="w", padx=20, pady=(15, 10))
        
        # Notifications list
        for notif in self.notifications:
            self.add_notification_item(notif)
    
    def add_notification_item(self, notif):
        """Add a single notification item"""
        item = ctk.CTkFrame(
            self,
            fg_color="#f8f9fa",
            corner_radius=10,
            height=60
        )
        item.pack(fill="x", padx=15, pady=3)
        item.pack_propagate(False)
        
        # Icon
        icon_lbl = ctk.CTkLabel(
            item,
            text=notif.get("icon", "📢"),
            font=("Segoe UI Emoji", 18)
        )
        icon_lbl.place(x=10, y=20)
        
        # Content
        content_frame = ctk.CTkFrame(item, fg_color="transparent")
        content_frame.place(x=45, y=8, relwidth=0.85, relheight=1)
        
        title_lbl = ctk.CTkLabel(
            content_frame,
            text=notif.get("title", ""),
            font=ctk.CTkFont(family="Segoe UI", size=12, weight="bold"),
            text_color="#333333",
            anchor="w"
        )
        title_lbl.pack(anchor="w")
        
        content_lbl = ctk.CTkLabel(
            content_frame,
            text=notif.get("content", ""),
            font=ctk.CTkFont(family="Segoe UI", size=10),
            text_color="#888888",
            anchor="w"
        )
        content_lbl.pack(anchor="w")


# ==================== PROGRESS RING ====================

class ProgressRing(ctk.CTkFrame):
    """Circular progress indicator"""
    
    def __init__(self, parent, value=0, size=100, **kwargs):
        super().__init__(parent, **kwargs)
        
        self.value = value
        self.size = size
        
        self.configure(
            width=size,
            height=size,
            fg_color="transparent"
        )
        
        self.create_widgets()
    
    def create_widgets(self):
        """Create progress ring"""
        # Background circle
        bg_label = ctk.CTkLabel(
            self,
            text="",
            width=self.size,
            height=self.size,
            fg_color="#e8e8e8",
            corner_radius=self.size//2
        )
        bg_label.place(relx=0.5, rely=0.5, anchor="center")
        
        # Progress indicator (using label with text for simplicity)
        progress = ctk.CTkLabel(
            self,
            text=f"{self.value}%",
            font=ctk.CTkFont(family="Segoe UI", size=20, weight="bold"),
            text_color="#667eea"
        )
        progress.place(relx=0.5, rely=0.5, anchor="center")
        
        # Label
        label = ctk.CTkLabel(
            self,
            text="Hoàn thành",
            font=ctk.CTkFont(family="Segoe UI", size=10),
            text_color="#888888"
        )
        label.place(relx=0.5, rely=0.75, anchor="center")


# ==================== MOTIVATIONAL QUOTE ====================

class MotivationalQuote(ctk.CTkFrame):
    """Daily motivational quote widget"""
    
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        
        self.quotes = [
            ("Học tập là chìa khóa mở cửa tương lai", "📚"),
            ("Kiến thức là sức mạnh, học hỏi là ánh sáng", "💡"),
            ("Mỗi ngày tiến bộ, mỗi ngày thành công", "🎯"),
            ("Thất bại là mẹ thành công, đừng sợ sai lầm", "🌟"),
            ("Chỉ cần kiên trì, thành công sẽ đến", "🏆"),
            ("Học một lần, dùng cả đời", "🧠"),
            ("Tri thức không có giới hạn", "🚀"),
            ("Nỗ lực hôm nay, thành quả ngày mai", "⏳")
        ]
        
        self.configure(
            fg_color="#ffffff",
            corner_radius=16
        )
        
        self.create_widgets()
    
    def create_widgets(self):
        """Create quote widget"""
        # Gradient-like background effect using layered frames
        bg_frame = ctk.CTkFrame(
            self,
            fg_color="#667eea",
            corner_radius=16
        )
        bg_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
        
        # Quote content
        import random
        quote, icon = random.choice(self.quotes)
        
        icon_label = ctk.CTkLabel(
            self,
            text=icon,
            font=("Segoe UI Emoji", 30),
            text_color="#ffffff"
        )
        icon_label.place(relx=0.5, rely=0.2, anchor="center")
        
        quote_label = ctk.CTkLabel(
            self,
            text=f'"{quote}"',
            font=ctk.CTkFont(family="Segoe UI", size=13, weight="bold"),
            text_color="#ffffff",
            wraplength=250,
            justify="center"
        )
        quote_label.place(relx=0.5, rely=0.55, anchor="center")
        
        # Author/source
        author_label = ctk.CTkLabel(
            self,
            text="— SmartStudy AI",
            font=ctk.CTkFont(family="Segoe UI", size=10),
            text_color="#ffffff",
            text_color_disabled="#ffffff"
        )
        author_label.place(relx=0.5, rely=0.8, anchor="center")


# ==================== STUDY STREAK ====================

class StudyStreak(ctk.CTkFrame):
    """Study streak counter widget"""
    
    def __init__(self, parent, days=7, **kwargs):
        super().__init__(parent, **kwargs)
        
        self.days = days
        
        self.configure(
            fg_color="#ffffff",
            corner_radius=16
        )
        
        self.create_widgets()
    
    def create_widgets(self):
        """Create streak widget"""
        # Title
        title = ctk.CTkLabel(
            self,
            text="🔥 Chuỗi học tập",
            font=ctk.CTkFont(family="Segoe UI", size=14, weight="bold"),
            text_color="#333333"
        )
        title.pack(anchor="w", padx=20, pady=(15, 5))
        
        # Streak number
        streak_label = ctk.CTkLabel(
            self,
            text=f"{self.days}",
            font=ctk.CTkFont(family="Segoe UI", size=36, weight="bold"),
            text_color="#f59e0b"
        )
        streak_label.pack(anchor="w", padx=20, pady=(0, 5))
        
        # Streak description
        desc_label = ctk.CTkLabel(
            self,
            text="ngày học liên tiếp",
            font=ctk.CTkFont(family="Segoe UI", size=11),
            text_color="#888888"
        )
        desc_label.pack(anchor="w", padx=20, pady=(0, 10))
        
        # Week visualization
        week_frame = ctk.CTkFrame(self, fg_color="transparent")
        week_frame.pack(fill="x", padx=20, pady=(0, 15))
        
        days_labels = ["T2", "T3", "T4", "T5", "T6", "T7", "CN"]
        today = datetime.now().weekday()
        
        for i in range(7):
            day_frame = ctk.CTkFrame(
                week_frame,
                width=30,
                height=35,
                fg_color="#f0f0f0",
                corner_radius=8
            )
            day_frame.grid(row=0, column=i, padx=3)
            day_frame.grid_propagate(False)
            
            # Check if this day has activity (last 7 days including today)
            has_activity = i <= today and i >= max(0, today - 6 + self.days)
            color = "#10b981" if has_activity else "#e8e8e8"
            text_color = "#ffffff" if has_activity else "#aaaaaa"
            
            day_frame.configure(fg_color=color)
            
            lbl = ctk.CTkLabel(
                day_frame,
                text=days_labels[i],
                font=ctk.CTkFont(family="Segoe UI", size=10, weight="bold"),
                text_color=text_color
            )
            lbl.place(relx=0.5, rely=0.5, anchor="center")


# ==================== SUBJECT PROGRESS ====================

class SubjectProgress(ctk.CTkFrame):
    """Subject progress tracking widget"""
    
    def __init__(self, parent, subjects=None, **kwargs):
        super().__init__(parent, **kwargs)
        
        self.subjects = subjects or [
            {"name": "Lập trình Python", "progress": 75, "color": "#667eea"},
            {"name": "Cấu trúc dữ liệu", "progress": 60, "color": "#11998e"},
            {"name": "Toán rời rạc", "progress": 85, "color": "#f59e0b"},
            {"name": "Mạng máy tính", "progress": 45, "color": "#ef4444"}
        ]
        
        self.configure(
            fg_color="#ffffff",
            corner_radius=16
        )
        
        self.create_widgets()
    
    def create_widgets(self):
        """Create subject progress widget"""
        # Title
        title = ctk.CTkLabel(
            self,
            text="📖 Tiến độ môn học",
            font=ctk.CTkFont(family="Segoe UI", size=14, weight="bold"),
            text_color="#333333"
        )
        title.pack(anchor="w", padx=20, pady=(15, 10))
        
        # Subject list
        for subject in self.subjects:
            self.add_subject_item(subject)
    
    def add_subject_item(self, subject):
        """Add a subject progress item"""
        item_frame = ctk.CTkFrame(self, fg_color="transparent")
        item_frame.pack(fill="x", padx=20, pady=5)
        
        # Subject name
        name_label = ctk.CTkLabel(
            item_frame,
            text=subject["name"],
            font=ctk.CTkFont(family="Segoe UI", size=11),
            text_color="#333333",
            anchor="w"
        )
        name_label.pack(anchor="w")
        
        # Progress bar
        bar_frame = ctk.CTkFrame(item_frame, fg_color="#e8e8e8", height=8, corner_radius=4)
        bar_frame.pack(fill="x", pady=(3, 0))
        bar_frame.pack_propagate(False)
        
        progress_fill = ctk.CTkFrame(
            bar_frame,
            fg_color=subject["color"],
            corner_radius=4
        )
        progress_fill.place(x=0, y=0, relheight=1, relwidth=subject["progress"] / 100)
        
        # Progress percentage
        percent_label = ctk.CTkLabel(
            item_frame,
            text=f"{subject['progress']}%",
            font=ctk.CTkFont(family="Segoe UI", size=9),
            text_color="#888888"
        )
        percent_label.pack(anchor="e")


# ==================== QUICK STATS ROW ====================

class QuickStatsRow(ctk.CTkFrame):
    """Quick stats row with mini cards"""
    
    def __init__(self, parent, stats=None, **kwargs):
        super().__init__(parent, **kwargs)
        
        self.configure(
            fg_color="transparent"
        )
        
        self.create_widgets(stats or {})
    
    def create_widgets(self, stats):
        """Create quick stats"""
        quick_stats = [
            {"icon": "⏱️", "value": f"{stats.get('study_today', 4)}h", "label": "Học hôm nay", "color": "#667eea"},
            {"icon": "📝", "value": str(stats.get('tasks_done', 3)), "label": "Task hoàn thành", "color": "#11998e"},
            {"icon": "🎯", "value": f"{stats.get('focus_rate', 85)}%", "label": "Tập trung", "color": "#f59e0b"},
            {"icon": "☕", "value": str(stats.get('break_taken', 2)), "label": "Nghỉ ngơi", "color": "#10b981"}
        ]
        
        for stat in quick_stats:
            self.add_mini_stat(stat)


# ==================== MINI STAT CARD ====================

class MiniStatCard(ctk.CTkFrame):
    """Mini stat card for inline display"""
    
    def __init__(self, parent, icon, value, label, color="#667eea", **kwargs):
        super().__init__(parent, **kwargs)
        
        self.configure(
            fg_color="#ffffff",
            corner_radius=12,
            width=100,
            height=70
        )
        
        self.create_widgets(icon, value, label, color)
    
    def create_widgets(self, icon, value, label, color):
        """Create mini stat"""
        icon_label = ctk.CTkLabel(
            self,
            text=icon,
            font=("Segoe UI Emoji", 18),
            text_color=color
        )
        icon_label.place(x=12, y=10)
        
        value_label = ctk.CTkLabel(
            self,
            text=value,
            font=ctk.CTkFont(family="Segoe UI", size=18, weight="bold"),
            text_color="#333333"
        )
        value_label.place(x=12, y=35)
        
        label_label = ctk.CTkLabel(
            self,
            text=label,
            font=ctk.CTkFont(family="Segoe UI", size=9),
            text_color="#888888"
        )
        label_label.place(x=12, y=52)


# ==================== ENHANCED PROGRESS RING ====================

class EnhancedProgressRing(ctk.CTkFrame):
    """Enhanced circular progress ring with stats"""
    
    def __init__(self, parent, value=0, label="Hoàn thành", size=120, color="#667eea", **kwargs):
        super().__init__(parent, **kwargs)
        
        self.value = value
        self.label_text = label
        self.size = size
        self.color = color
        
        self.configure(
            fg_color="#ffffff",
            corner_radius=16,
            width=160,
            height=160
        )
        
        self.create_widgets()
    
    def create_widgets(self):
        """Create enhanced progress ring"""
        # Main container
        container = ctk.CTkFrame(self, fg_color="transparent")
        container.place(relx=0.5, rely=0.5, anchor="center")
        
        # Circular progress visualization using stacked frames
        outer_size = self.size
        inner_size = outer_size - 20
        
        # Background circle
        bg_circle = ctk.CTkFrame(
            container,
            width=outer_size,
            height=outer_size,
            fg_color="#e8e8e8",
            corner_radius=outer_size // 2
        )
        bg_circle.pack()
        bg_circle.pack_propagate(False)
        
        # Progress indicator using a progress bar
        progress_bar = ctk.CTkProgressBar(
            container,
            width=inner_size,
            height=12,
            progress_color=self.color,
            fg_color="#e8e8e8",
            corner_radius=6
        )
        progress_bar.pack(pady=(30, 5))
        progress_bar.set(self.value / 100)
        
        # Value display
        value_label = ctk.CTkLabel(
            container,
            text=f"{self.value}%",
            font=ctk.CTkFont(family="Segoe UI", size=28, weight="bold"),
            text_color=self.color
        )
        value_label.pack()
        
        # Label
        label_label = ctk.CTkLabel(
            container,
            text=self.label_text,
            font=ctk.CTkFont(family="Segoe UI", size=11),
            text_color="#888888"
        )
        label_label.pack()


# ==================== WEEKLY SCHEDULE CARD ====================

class WeeklyScheduleCard(ctk.CTkFrame):
    """Weekly schedule display card"""
    
    def __init__(self, parent, schedule=None, **kwargs):
        super().__init__(parent, **kwargs)
        
        self.schedule = schedule or []
        
        self.configure(
            fg_color="#ffffff",
            corner_radius=16
        )
        
        self.create_widgets()
    
    def create_widgets(self):
        """Create schedule card widgets"""
        # Title with icon
        title_frame = ctk.CTkFrame(self, fg_color="transparent")
        title_frame.pack(fill="x", padx=15, pady=(12, 8))
        
        title_icon = ctk.CTkLabel(
            title_frame,
            text="📅",
            font=("Segoe UI Emoji", 14)
        )
        title_icon.pack(side="left")
        
        title = ctk.CTkLabel(
            self,
            text="Lịch học tuần",
            font=ctk.CTkFont(family="Segoe UI", size=13, weight="bold"),
            text_color="#333333"
        )
        title.place(x=30, y=2)
        
        # Schedule scrollable frame
        scroll_frame = ctk.CTkScrollableFrame(
            self,
            fg_color="transparent",
            scrollbar_button_color="#e0e0e0",
            height=350
        )
        scroll_frame.pack(fill="both", expand=True, padx=15, pady=(0, 15))
        
        # Add schedule items
        for day_data in self.schedule:
            self.add_day_item(scroll_frame, day_data)
    
    def add_day_item(self, parent, day_data):
        """Add a single day item"""
        # Day header with highlight for today
        day_frame = ctk.CTkFrame(parent, fg_color="transparent")
        day_frame.pack(fill="x", pady=(10, 5))
        
        # Check if this is today
        today_str = datetime.now().strftime("%d/%m")
        is_today = day_data.get('date', '') == today_str
        
        day_color = "#10b981" if is_today else "#667eea"
        day_bg = "#e8f5e9" if is_today else "transparent"
        
        if is_today:
            day_label = ctk.CTkLabel(
                day_frame,
                text=f"📍 {day_data.get('day', '')} - {day_data.get('date', '')} (Hôm nay)",
                font=ctk.CTkFont(family="Segoe UI", size=13, weight="bold"),
                text_color=day_color
            )
        else:
            day_label = ctk.CTkLabel(
                day_frame,
                text=f"{day_data.get('day', '')} - {day_data.get('date', '')}",
                font=ctk.CTkFont(family="Segoe UI", size=13, weight="bold"),
                text_color=day_color
            )
        day_label.pack(anchor="w")
        
        # Classes
        for class_info in day_data.get("classes", []):
            self.add_class_item(day_frame, class_info, is_today)
    
    def add_class_item(self, parent, class_info, highlight=False):
        """Add a single class item"""
        bg_color = "#f0fdf4" if highlight else "#f8f9fa"
        
        class_frame = ctk.CTkFrame(
            parent,
            fg_color=bg_color,
            corner_radius=10,
            height=50
        )
        class_frame.pack(fill="x", pady=3, padx=(0, 0))
        class_frame.pack_propagate(False)
        
        # Time with icon
        time_icon = ctk.CTkLabel(
            class_frame,
            text="🕐",
            font=("Segoe UI Emoji", 10),
            text_color="#667eea"
        )
        time_icon.place(x=10, y=10)
        
        time_label = ctk.CTkLabel(
            class_frame,
            text=class_info.get("time", ""),
            font=ctk.CTkFont(family="Segoe UI", size=11),
            text_color="#667eea"
        )
        time_label.place(x=30, y=10)
        
        # Class name
        name_label = ctk.CTkLabel(
            class_frame,
            text=class_info.get("name", ""),
            font=ctk.CTkFont(family="Segoe UI", size=12, weight="bold"),
            text_color="#333333"
        )
        name_label.place(x=30, y=28)
        
        # Room
        room_label = ctk.CTkLabel(
            class_frame,
            text=f"📍 {class_info.get('room', '')}",
            font=ctk.CTkFont(family="Segoe UI", size=10),
            text_color="#888888"
        )
        room_label.place(x=250, y=10)
        
        # Type badge
        type_text = class_info.get("type", "LT")
        type_color = "#667eea" if type_text == "LT" else "#11998e"
        type_badge = ctk.CTkLabel(
            class_frame,
            text=type_text,
            font=ctk.CTkFont(family="Segoe UI", size=10, weight="bold"),
            text_color="#ffffff",
            fg_color=type_color,
            width=30,
            height=20,
            corner_radius=5
        )
        type_badge.place(x=310, y=15)
