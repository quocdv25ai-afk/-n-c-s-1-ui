"""
SmartStudy AI - Schedule Page
Trang xem và quản lý lịch học chi tiết
"""

import customtkinter as ctk
from datetime import datetime, timedelta
import calendar


class SchedulePage(ctk.CTkFrame):
    """Schedule page with weekly and monthly calendar views"""
    
    def __init__(self, parent, app):
        super().__init__(parent)
        
        self.app = app
        self.current_view = "week"
        self.current_date = datetime.now()
        
        # Color palette
        self.colors = {
            "primary": "#667eea",
            "primary_dark": "#5a67d8",
            "secondary": "#38b2ac",
            "accent_pink": "#ed64a6",
            "accent_orange": "#f6ad55",
            "accent_green": "#48bb78",
            "bg_light": "#f0f2f5",
            "bg_card": "#ffffff",
            "text_dark": "#1a202c",
            "text_medium": "#4a5568",
            "text_light": "#a0aec0",
            "border": "#e2e8f0",
            "weekend": "#fff5f5",
            "weekend_accent": "#feb2b2",
        }
        
        self.configure(
            fg_color=self.colors["bg_light"],
            corner_radius=0
        )
        
        self.load_schedule_data()
        self.create_widgets()
    
    def create_widgets(self):
        """Create schedule page widgets"""
        
        # ==================== HEADER ====================
        header = ctk.CTkFrame(
            self,
            fg_color=self.colors["bg_card"],
            height=65,
            corner_radius=0
        )
        header.pack(fill="x")
        header.pack_propagate(False)
        
        # Title
        title_frame = ctk.CTkFrame(header, fg_color="transparent")
        title_frame.pack(side="left", padx=25, pady=15)
        
        ctk.CTkLabel(
            title_frame,
            text="📅",
            font=("Segoe UI Emoji", 24),
            width=40
        ).pack(side="left")
        
        ctk.CTkLabel(
            title_frame,
            text="Lịch học",
            font=ctk.CTkFont(family="Segoe UI", size=20, weight="bold"),
            text_color=self.colors["text_dark"]
        ).pack(side="left", padx=(5, 0))
        
        # ==================== TIME DISPLAY ====================
        time_bar = ctk.CTkFrame(self, fg_color=self.colors["primary"], height=50)
        time_bar.pack(fill="x")
        time_bar.pack_propagate(False)
        
        time_inner = ctk.CTkFrame(time_bar, fg_color="transparent")
        time_inner.pack(pady=10)
        
        self.week_display = ctk.CTkLabel(
            time_inner,
            text=self.get_week_display(),
            font=ctk.CTkFont(family="Segoe UI", size=16, weight="bold"),
            text_color="#ffffff"
        )
        self.week_display.pack()
        
        # ==================== CONTROLS BAR ====================
        controls = ctk.CTkFrame(self, fg_color=self.colors["bg_card"], height=60)
        controls.pack(fill="x")
        controls.pack_propagate(False)
        
        # Left: Week/Month toggle
        toggle_frame = ctk.CTkFrame(controls, fg_color="#e2e8f0", corner_radius=20, height=36)
        toggle_frame.pack(side="left", padx=20, pady=12)
        toggle_frame.pack_propagate(False)
        
        self.week_btn = ctk.CTkButton(
            toggle_frame,
            text="📅 Theo Tuần",
            width=100,
            height=32,
            fg_color=self.colors["primary"],
            hover_color=self.colors["primary_dark"],
            text_color="#ffffff",
            corner_radius=16,
            font=("Segoe UI", 11, "bold"),
            border_width=0,
            command=lambda: self.switch_view("week")
        )
        self.week_btn.pack(side="left", padx=2, pady=2)
        
        self.month_btn = ctk.CTkButton(
            toggle_frame,
            text="📆 Theo Tháng",
            width=100,
            height=32,
            fg_color="transparent",
            hover_color="#d0d5dd",
            text_color=self.colors["text_medium"],
            corner_radius=16,
            font=("Segoe UI", 11),
            border_width=0,
            command=lambda: self.switch_view("month")
        )
        self.month_btn.pack(side="left", padx=2, pady=2)
        
        # Right: Navigation buttons
        nav_frame = ctk.CTkFrame(controls, fg_color="transparent")
        nav_frame.pack(side="right", padx=20, pady=12)
        
        btn_style = {
            "width": 100,
            "height": 36,
            "corner_radius": 8,
        }
        
        prev_btn = ctk.CTkButton(
            nav_frame,
            text="◀ Trước",
            fg_color=self.colors["bg_light"],
            hover_color=self.colors["border"],
            text_color=self.colors["text_medium"],
            font=("Segoe UI", 11),
            command=self.prev_week,
            **btn_style
        )
        prev_btn.pack(side="left", padx=5)
        
        today_btn = ctk.CTkButton(
            nav_frame,
            text="🏠 Tuần này",
            fg_color=self.colors["primary"],
            hover_color=self.colors["primary_dark"],
            text_color="#ffffff",
            font=("Segoe UI", 11, "bold"),
            command=self.go_to_today,
            **btn_style
        )
        today_btn.pack(side="left", padx=5)
        
        next_btn = ctk.CTkButton(
            nav_frame,
            text="Sau ▶",
            fg_color=self.colors["bg_light"],
            hover_color=self.colors["border"],
            text_color=self.colors["text_medium"],
            font=("Segoe UI", 11),
            command=self.next_week,
            **btn_style
        )
        next_btn.pack(side="left", padx=5)
        
        # ==================== SCHEDULE CONTENT ====================
        self.scroll_frame = ctk.CTkScrollableFrame(
            self,
            fg_color="transparent",
            scrollbar_button_color="#d0d5dd",
            scrollbar_fg_color="#e2e8f0"
        )
        self.scroll_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        self.schedule_container = ctk.CTkFrame(self.scroll_frame, fg_color="transparent")
        self.schedule_container.pack(fill="both", expand=True)
        
        self.draw_weekly_schedule()
    
    def load_schedule_data(self):
        """Load schedule data from app"""
        self.schedule = self.app.get_schedule()
    
    def get_week_display(self):
        """Get formatted week display: Tuần 19 [ 04/05 - 10/05/2026 ]"""
        start = self.current_date - timedelta(days=self.current_date.weekday())
        week_num = start.isocalendar()[1]
        end = start + timedelta(days=6)
        return f"Tuần {week_num} [ {start.strftime('%d/%m')} - {end.strftime('%d/%m/%Y')} ]"
    
    def switch_view(self, view):
        """Switch between week and month view"""
        self.current_view = view
        
        if view == "week":
            self.week_btn.configure(
                fg_color=self.colors["primary"],
                text_color="#ffffff",
                font=("Segoe UI", 11, "bold")
            )
            self.month_btn.configure(
                fg_color="transparent",
                text_color=self.colors["text_medium"],
                font=("Segoe UI", 11)
            )
            self.draw_weekly_schedule()
        else:
            self.month_btn.configure(
                fg_color=self.colors["primary"],
                text_color="#ffffff",
                font=("Segoe UI", 11, "bold")
            )
            self.week_btn.configure(
                fg_color="transparent",
                text_color=self.colors["text_medium"],
                font=("Segoe UI", 11)
            )
            self.draw_monthly_schedule()
    
    def draw_weekly_schedule(self):
        """Draw weekly schedule view"""
        for widget in self.schedule_container.winfo_children():
            widget.destroy()
        
        days = [
            {"name": "Thứ 2", "short": "T2", "is_weekend": False},
            {"name": "Thứ 3", "short": "T3", "is_weekend": False},
            {"name": "Thứ 4", "short": "T4", "is_weekend": False},
            {"name": "Thứ 5", "short": "T5", "is_weekend": False},
            {"name": "Thứ 6", "short": "T6", "is_weekend": False},
            {"name": "Thứ 7", "short": "T7", "is_weekend": True},
            {"name": "Chủ nhật", "short": "CN", "is_weekend": True}
        ]
        
        # Container for 7 columns grid (no scroll)
        schedule_frame = ctk.CTkFrame(self.schedule_container, fg_color="transparent")
        schedule_frame.pack(fill="both", expand=True)
        
        # Configure grid columns (equal width for all 7 days)
        for i in range(7):
            schedule_frame.grid_columnconfigure(i, weight=1, uniform="day_col")
        
        # Create each day column
        for day_idx, day_info in enumerate(days):
            self.create_day_column_grid(schedule_frame, day_idx, day_info)
    
    def create_day_column(self, parent, day_idx, day_info):
        """Create a single day column"""
        is_weekend = day_info["is_weekend"]
        accent = self.colors["accent_pink"] if is_weekend else self.colors["primary"]
        is_today = datetime.now().weekday() == day_idx
        
        # Column with fixed width
        col = ctk.CTkFrame(parent, fg_color="transparent", width=200)
        col.pack(side="left", padx=10, fill="y")
        col.pack_propagate(False)
        
        self._create_day_card(col, day_idx, day_info, accent, is_weekend, is_today)
    
    def create_day_column_grid(self, parent, day_idx, day_info):
        """Create a single day column using grid layout"""
        is_weekend = day_info["is_weekend"]
        accent = self.colors["accent_pink"] if is_weekend else self.colors["primary"]
        is_today = datetime.now().weekday() == day_idx
        
        # Column with equal width
        col = ctk.CTkFrame(parent, fg_color="transparent")
        col.grid(row=0, column=day_idx, padx=5, sticky="nsew")
        
        self._create_day_card(col, day_idx, day_info, accent, is_weekend, is_today)
    
    def _create_day_card(self, col, day_idx, day_info, accent, is_weekend, is_today):
        
        # Day card
        card = ctk.CTkFrame(
            col,
            fg_color=self.colors["bg_card"],
            corner_radius=16,
            border_width=1,
            border_color=self.colors["border"] if not is_weekend else "#fbb6ce"
        )
        card.pack(fill="both", expand=True)
        
        # Header with accent color
        header_bg = accent if is_today else ("#fff5f5" if is_weekend else "#f7fafc")
        header = ctk.CTkFrame(card, fg_color=header_bg, corner_radius=16)
        header.pack(fill="x")
        
        # Calculate current date
        current_date = datetime.now() - timedelta(days=datetime.now().weekday() - day_idx)
        
        # Day name - all headers look the same
        header_text = "#ffffff" if is_today else self.colors["text_dark"]
        day_text = f"{day_info['name']} • {current_date.strftime('%d/%m')}"
        if is_today:
            day_text = f"● {day_text}"
        
        ctk.CTkLabel(
            header,
            text=day_text,
            font=ctk.CTkFont(family="Segoe UI", size=12, weight="bold"),
            text_color=header_text
        ).pack(pady=10)
        
        # Divider
        divider = ctk.CTkFrame(card, height=1, fg_color=self.colors["border"])
        divider.pack(fill="x", padx=15, pady=(10, 5))
        
        # Classes container
        classes_container = ctk.CTkFrame(card, fg_color="transparent")
        classes_container.pack(fill="both", expand=True, padx=15, pady=(5, 15))
        
        # Get schedule for this day
        target_day = day_info["name"]
        schedule_for_day = None
        for sched in self.schedule:
            if sched.get("day") == target_day:
                schedule_for_day = sched
                break
        
        # Add classes or empty state
        if schedule_for_day and schedule_for_day.get("classes"):
            for class_info in schedule_for_day["classes"]:
                self.add_class_card(classes_container, class_info, accent)
        else:
            self.add_empty_state(classes_container)
    
    def add_class_card(self, parent, class_info, accent):
        """Add a class card"""
        card = ctk.CTkFrame(
            parent,
            fg_color="#f8f9fa",
            corner_radius=12,
            border_width=1,
            border_color=self.colors["border"]
        )
        card.pack(fill="x", pady=6)
        
        # Left accent bar
        accent_bar = ctk.CTkFrame(card, width=4, fg_color=accent, corner_radius=0)
        accent_bar.place(x=0, y=0, relheight=1)
        
        # Content
        content = ctk.CTkFrame(card, fg_color="transparent")
        content.pack(fill="both", expand=True, padx=(12, 10), pady=10)
        
        # Time with badge
        time_frame = ctk.CTkFrame(content, fg_color="transparent")
        time_frame.pack(fill="x")
        
        ctk.CTkLabel(
            time_frame,
            text=class_info.get("time", ""),
            font=ctk.CTkFont(family="Segoe UI", size=11, weight="bold"),
            text_color=accent
        ).pack(side="left")
        
        # Subject name
        ctk.CTkLabel(
            content,
            text=class_info.get("name", ""),
            font=ctk.CTkFont(family="Segoe UI", size=13, weight="bold"),
            text_color=self.colors["text_dark"],
            wraplength=150,
            anchor="w",
            justify="left"
        ).pack(fill="x", pady=(8, 6))
        
        # Room
        room_frame = ctk.CTkFrame(content, fg_color="#edf2f7", corner_radius=6, height=24)
        room_frame.pack(fill="x")
        room_frame.pack_propagate(False)
        
        room_inner = ctk.CTkFrame(room_frame, fg_color="transparent")
        room_inner.pack(fill="both", expand=True, padx=8)
        
        ctk.CTkLabel(
            room_inner,
            text="📍",
            font=("Segoe UI Emoji", 10)
        ).pack(side="left")
        
        ctk.CTkLabel(
            room_inner,
            text=class_info.get("room", ""),
            font=ctk.CTkFont(family="Segoe UI", size=11),
            text_color=self.colors["text_medium"]
        ).pack(side="left", padx=(4, 0))
    
    def add_empty_state(self, parent):
        """Add empty state message"""
        empty = ctk.CTkFrame(parent, fg_color="transparent")
        empty.pack(fill="both", expand=True)
        
        ctk.CTkLabel(
            empty,
            text="📚",
            font=("Segoe UI Emoji", 24)
        ).pack(pady=(30, 5))
        
        ctk.CTkLabel(
            empty,
            text="Không có lớp học",
            font=ctk.CTkFont(family="Segoe UI", size=11),
            text_color=self.colors["text_light"]
        ).pack()
    
    def draw_monthly_schedule(self):
        """Draw monthly calendar view"""
        for widget in self.schedule_container.winfo_children():
            widget.destroy()
        
        # Month header
        month_header = ctk.CTkFrame(self.schedule_container, fg_color="transparent")
        month_header.pack(fill="x", pady=(0, 20))
        
        ctk.CTkLabel(
            month_header,
            text="🗓️",
            font=("Segoe UI Emoji", 20)
        ).pack(side="left", padx=(0, 10))
        
        ctk.CTkLabel(
            month_header,
            text=self.current_date.strftime("%B %Y"),
            font=ctk.CTkFont(family="Segoe UI", size=18, weight="bold"),
            text_color=self.colors["text_dark"]
        ).pack(side="left")
        
        # Calendar container
        calendar_card = ctk.CTkFrame(
            self.schedule_container,
            fg_color=self.colors["bg_card"],
            corner_radius=16,
            border_width=1,
            border_color=self.colors["border"]
        )
        calendar_card.pack(fill="both", expand=True)
        
        # Day headers
        days_frame = ctk.CTkFrame(calendar_card, fg_color="transparent")
        days_frame.pack(fill="x", padx=20, pady=(20, 10))
        
        days = ["T2", "T3", "T4", "T5", "T6", "T7", "CN"]
        day_colors = [
            self.colors["primary"], self.colors["secondary"], self.colors["accent_green"],
            self.colors["accent_orange"], self.colors["accent_pink"], self.colors["primary_dark"],
            self.colors["text_light"]
        ]
        
        for i, day in enumerate(days):
            ctk.CTkLabel(
                days_frame,
                text=day,
                font=ctk.CTkFont(family="Segoe UI", size=13, weight="bold"),
                text_color=day_colors[i],
                width=60
            ).pack(side="left", padx=10)
        
        # Calendar grid
        grid = ctk.CTkFrame(calendar_card, fg_color="transparent")
        grid.pack(fill="both", expand=True, padx=20, pady=(0, 20))
        
        year = self.current_date.year
        month = self.current_date.month
        
        first_day = datetime(year, month, 1)
        weekday = first_day.weekday()
        
        _, days_in_month = calendar.monthrange(year, month)
        
        day_num = 1
        for week in range(6):
            week_frame = ctk.CTkFrame(grid, fg_color="transparent")
            week_frame.pack(fill="x", pady=5)
            
            for day in range(7):
                cell_num = week * 7 + day
                
                if cell_num < weekday or day_num > days_in_month:
                    placeholder = ctk.CTkFrame(week_frame, fg_color="transparent", height=65, width=60)
                    placeholder.pack(side="left", padx=8)
                    placeholder.pack_propagate(False)
                else:
                    is_today = day_num == datetime.now().day and month == datetime.now().month and year == datetime.now().year
                    self.create_month_cell(week_frame, day_num, is_today)
                    day_num += 1
                    
                    if day_num > days_in_month:
                        break
    
    def create_month_cell(self, parent, day, is_today):
        """Create a month calendar cell"""
        cell = ctk.CTkFrame(
            parent,
            width=60,
            height=65,
            fg_color="#e8eaf6" if is_today else "#f8f9fa",
            corner_radius=12,
            border_width=2 if is_today else 1,
            border_color=self.colors["primary"] if is_today else self.colors["border"]
        )
        cell.pack(side="left", padx=8)
        cell.pack_propagate(False)
        
        ctk.CTkLabel(
            cell,
            text=str(day),
            font=ctk.CTkFont(
                family="Segoe UI",
                size=14,
                weight="bold" if is_today else "normal"
            ),
            text_color=self.colors["primary"] if is_today else self.colors["text_dark"]
        ).place(relx=0.5, rely=0.35, anchor="center")
        
        # Event dot
        if day % 3 == 0:
            ctk.CTkLabel(
                cell,
                text="●",
                font=("Segoe UI", 8),
                text_color=self.colors["primary"]
            ).place(relx=0.5, rely=0.7, anchor="center")
    
    def prev_week(self):
        """Go to previous week"""
        self.current_date -= timedelta(days=7)
        self.week_display.configure(text=self.get_week_display())
        self.draw_weekly_schedule()
    
    def next_week(self):
        """Go to next week"""
        self.current_date += timedelta(days=7)
        self.week_display.configure(text=self.get_week_display())
        self.draw_weekly_schedule()
    
    def go_to_today(self):
        """Go to current week"""
        self.current_date = datetime.now()
        self.week_display.configure(text=self.get_week_display())
        self.draw_weekly_schedule()
    
    def refresh(self):
        """Refresh schedule data"""
        self.load_schedule_data()
        if self.current_view == "week":
            self.draw_weekly_schedule()
        else:
            self.draw_monthly_schedule()
