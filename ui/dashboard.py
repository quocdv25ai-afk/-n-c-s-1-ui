"""
SmartStudy AI - Dashboard Page
Thiết kế nâng cấp đồ họa với bố cục scrollable
"""

import customtkinter as ctk
from datetime import datetime, timedelta


class DashboardPage(ctk.CTkFrame):
    """Dashboard page - Trang chủ chính với đồ họa cao cấp"""
    
    def __init__(self, parent, app):
        super().__init__(parent)
        
        self.app = app
        
        # Configure frame
        self.configure(fg_color="#f0f4f8")
        
        self.create_widgets()
    
    def create_widgets(self):
        """Create all dashboard widgets"""
        
        # ==================== 1. HEADER BAR ====================
        self.create_header()
        
        # ==================== MAIN CONTENT (SCROLLABLE) ====================
        self.scroll_frame = ctk.CTkScrollableFrame(
            self,
            fg_color="transparent",
            scrollbar_button_color="#e2e8f0",
            scrollbar_fg_color="#cbd5e1"
        )
        self.scroll_frame.pack(fill="both", expand=True, padx=0, pady=0)
        
        content = ctk.CTkFrame(self.scroll_frame, fg_color="transparent")
        content.pack(fill="both", expand=True, padx=25, pady=20)
        
        # Left column (65%) - Schedule, Tasks, AI
        left_col = ctk.CTkFrame(content, fg_color="transparent")
        left_col.pack(side="left", fill="both", expand=True, padx=(0, 20))
        
        # Right column (35%) - Stats, Suggestions, Notifications
        right_col = ctk.CTkFrame(content, fg_color="transparent")
        right_col.pack(side="right", fill="both", expand=True)
        
        # ==================== 2. LỜI CHÀO ====================
        self.create_greeting(left_col)
        
        # ==================== 4. LỊCH HỌC THEO TUẦN ====================
        self.create_weekly_schedule(left_col)
        
        # ==================== 5. VIỆC CẦN LÀM HÔM NAY (SCROLLABLE) ====================
        self.create_today_tasks(left_col)
        
        # ==================== 7. AI ASSISTANT BUTTON ====================
        self.create_ai_button(left_col)
        
        # ==================== 3. THỐNG KÊ TUẦN ====================
        self.create_weekly_stats(right_col)
        
        # ==================== 6. GỢI Ý LỊCH HỌC THÔNG MINH ====================
        self.create_smart_suggestion(right_col)
        
        # ==================== 8. THÔNG BÁO (SCROLLABLE) ====================
        self.create_notifications(right_col)
    
    def create_header(self):
        """1. Header với Search, Bell, Settings - Thiết kế nâng cấp"""
        header = ctk.CTkFrame(self, fg_color="#ffffff", height=70)
        header.pack(fill="x", padx=0, pady=0)
        header.pack_propagate(False)
        
        # Bottom border effect
        border = ctk.CTkFrame(header, fg_color="#e2e8f0", height=2)
        border.pack(fill="x", side="bottom")
        
        header_inner = ctk.CTkFrame(header, fg_color="transparent")
        header_inner.pack(fill="both", expand=True, padx=25)
        
        # Logo with gradient background
        logo_frame = ctk.CTkFrame(header_inner, fg_color="transparent")
        logo_frame.pack(side="left", pady=12)
        
        logo_bg = ctk.CTkFrame(logo_frame, fg_color="#6366f1", corner_radius=10, width=44, height=44)
        logo_bg.pack(side="left")
        logo_bg.pack_propagate(False)
        
        logo = ctk.CTkLabel(
            logo_bg,
            text="📚",
            font=("Segoe UI Emoji", 26)
        )
        logo.place(relx=0.5, rely=0.5, anchor="center")
        
        title = ctk.CTkLabel(
            logo_frame,
            text="SmartStudy AI",
            font=ctk.CTkFont(family="Segoe UI", size=20, weight="bold"),
            text_color="#1e293b"
        )
        title.pack(side="left", padx=(12, 0))
        
        # Search bar (center) - modern design
        search_frame = ctk.CTkFrame(header_inner, fg_color="#f1f5f9", corner_radius=25, width=380, height=46)
        search_frame.pack(side="left", padx=40, pady=12)
        search_frame.pack_propagate(False)
        
        # Search icon with brighter appearance
        search_icon = ctk.CTkLabel(
            search_frame,
            text="🔍",
            font=("Segoe UI Emoji", 18),
            text_color="#64748b"
        )
        search_icon.place(x=15, y=12)
        
        search_entry = ctk.CTkEntry(
            search_frame,
            placeholder_text="Tìm kiếm nhanh...",
            fg_color="transparent",
            border_width=0,
            font=ctk.CTkFont(family="Segoe UI", size=14),
            text_color="#64748b"
        )
        search_entry.place(x=42, y=12, relwidth=0.8)
        
        # Right buttons
        btn_frame = ctk.CTkFrame(header_inner, fg_color="transparent")
        btn_frame.pack(side="right", pady=12)
        
        # Bell notification button with badge
        bell_btn = ctk.CTkButton(
            btn_frame,
            text="🔔",
            font=("Segoe UI Emoji", 24),
            fg_color="#f1f5f9",
            hover_color="#e2e8f0",
            text_color="#475569",
            width=46,
            height=46,
            corner_radius=23
        )
        bell_btn.pack(side="left", padx=(0, 10))
        
        # Settings button
        settings_btn = ctk.CTkButton(
            btn_frame,
            text="⚙️",
            font=("Segoe UI Emoji", 24),
            fg_color="#f1f5f9",
            hover_color="#e2e8f0",
            text_color="#475569",
            width=46,
            height=46,
            corner_radius=23
        )
        settings_btn.pack(side="left")
    
    def create_greeting(self, parent):
        """2. Lời chào ngắn gọn theo thời gian - Thiết kế gradient"""
        greeting_card = ctk.CTkFrame(parent, fg_color="#6366f1", corner_radius=16)
        greeting_card.pack(fill="x", pady=(0, 15))
        
        inner = ctk.CTkFrame(greeting_card, fg_color="transparent")
        inner.pack(fill="x", padx=25, pady=20)
        
        hour = datetime.now().hour
        if hour < 12:
            greeting = "Chào buổi sáng"
            emoji = "🌅"
        elif hour < 18:
            greeting = "Chào buổi chiều"
            emoji = "☀️"
        else:
            greeting = "Chào buổi tối"
            emoji = "🌙"
        
        user_name = self.app.get_user_info().get("name", "Bạn")
        
        greeting_label = ctk.CTkLabel(
            inner,
            text=f"{emoji} {greeting}, {user_name}!",
            font=ctk.CTkFont(family="Segoe UI", size=22, weight="bold"),
            text_color="#ffffff",
            anchor="w"
        )
        greeting_label.pack(anchor="w")
        
        date_label = ctk.CTkLabel(
            inner,
            text=datetime.now().strftime("%d/%m/%Y • %A"),
            font=ctk.CTkFont(family="Segoe UI", size=13),
            text_color="#c7d2fe",
            anchor="w"
        )
        date_label.pack(anchor="w", pady=(5, 0))
    
    def create_weekly_stats(self, parent):
        """3. Thống kê tuần - Thiết kế card với icon nền màu"""
        stats_card = ctk.CTkFrame(parent, fg_color="#ffffff", corner_radius=16)
        stats_card.pack(fill="x", pady=(0, 15))
        
        inner = ctk.CTkFrame(stats_card, fg_color="transparent")
        inner.pack(fill="x", padx=15, pady=12)
        
        # Title with icon
        title_frame = ctk.CTkFrame(inner, fg_color="transparent")
        title_frame.pack(fill="x", pady=(0, 12))
        
        icon_lbl = ctk.CTkLabel(
            title_frame,
            text="📊",
            font=("Segoe UI Emoji", 22)
        )
        icon_lbl.pack(side="left")
        
        title = ctk.CTkLabel(
            title_frame,
            text="Thống kê tuần",
            font=ctk.CTkFont(family="Segoe UI", size=15, weight="bold"),
            text_color="#1e293b"
        )
        title.pack(side="left", padx=(8, 0))
        
        # Stats grid - 2x2 with colored icons
        stats = self.app.get_stats()
        
        stats_items = [
            {"icon": "📚", "label": "Tổng tiết", "value": str(stats.get('total_periods', 25)), "bg": "#dbeafe"},
            {"icon": "🎓", "label": "Tiết học", "value": str(stats.get('study_periods', 20)), "bg": "#dcfce7"},
            {"icon": "📖", "label": "Tự học", "value": str(stats.get('self_study', 5)), "bg": "#fef3c7"},
            {"icon": "✅", "label": "Hoàn thành", "value": f"{stats.get('completion_rate', 85)}%", "bg": "#f3e8ff"},
        ]
        
        # Create 2x2 grid using pack
        top_row = ctk.CTkFrame(inner, fg_color="transparent")
        top_row.pack(fill="x", pady=(0, 5))
        
        bottom_row = ctk.CTkFrame(inner, fg_color="transparent")
        bottom_row.pack(fill="x")
        
        rows = [top_row, bottom_row]
        
        for i, stat in enumerate(stats_items):
            row_frame = rows[i // 2]
            
            stat_frame = ctk.CTkFrame(row_frame, fg_color="#f8fafc", corner_radius=12)
            stat_frame.pack(side="left", fill="both", expand=True, padx=3)
            
            stat_inner = ctk.CTkFrame(stat_frame, fg_color="transparent")
            stat_inner.pack(padx=10, pady=10)
            
            # Icon with colored background
            icon_bg = ctk.CTkFrame(stat_inner, fg_color=stat["bg"], corner_radius=8, width=36, height=36)
            icon_bg.pack()
            icon_bg.pack_propagate(False)
            
            icon_lbl = ctk.CTkLabel(
                icon_bg,
                text=stat["icon"],
                font=("Segoe UI Emoji", 20)
            )
            icon_lbl.place(relx=0.5, rely=0.5, anchor="center")
            
            val_lbl = ctk.CTkLabel(
                stat_inner,
                text=stat["value"],
                font=ctk.CTkFont(family="Segoe UI", size=20, weight="bold"),
                text_color="#1e293b"
            )
            val_lbl.pack(pady=(5, 0))
            
            lbl_lbl = ctk.CTkLabel(
                stat_inner,
                text=stat["label"],
                font=ctk.CTkFont(family="Segoe UI", size=11),
                text_color="#94a3b8"
            )
            lbl_lbl.pack()
    
    def create_weekly_schedule(self, parent):
        """4. Lịch học theo tuần - Thiết kế card đẹp"""
        schedule_card = ctk.CTkFrame(parent, fg_color="#ffffff", corner_radius=16)
        schedule_card.pack(fill="both", expand=True, pady=(0, 15))
        
        inner = ctk.CTkFrame(schedule_card, fg_color="transparent")
        inner.pack(fill="both", expand=True, padx=15, pady=12)
        
        # Title with icon
        title_frame = ctk.CTkFrame(inner, fg_color="transparent")
        title_frame.pack(fill="x", pady=(0, 10))
        
        icon_lbl = ctk.CTkLabel(
            title_frame,
            text="📅",
            font=("Segoe UI Emoji", 24)
        )
        icon_lbl.pack(side="left")
        
        title = ctk.CTkLabel(
            title_frame,
            text="Lịch học tuần này",
            font=ctk.CTkFont(family="Segoe UI", size=17, weight="bold"),
            text_color="#1e293b"
        )
        title.pack(side="left", padx=(10, 0))
        
        # Week navigation arrows
        nav_frame = ctk.CTkFrame(inner, fg_color="transparent")
        nav_frame.pack(fill="x", pady=(0, 10))
        
        prev_btn = ctk.CTkButton(
            nav_frame,
            text="◀",
            font=("Segoe UI", 14),
            fg_color="#f1f5f9",
            hover_color="#e2e8f0",
            text_color="#64748b",
            width=35,
            height=30,
            corner_radius=8
        )
        prev_btn.pack(side="left")
        
        week_label = ctk.CTkLabel(
            nav_frame,
            text="Tuần 18 • 05/05 - 11/05",
            font=ctk.CTkFont(family="Segoe UI", size=12),
            text_color="#64748b"
        )
        week_label.pack(side="left", padx=15)
        
        next_btn = ctk.CTkButton(
            nav_frame,
            text="▶",
            font=("Segoe UI", 14),
            fg_color="#f1f5f9",
            hover_color="#e2e8f0",
            text_color="#64748b",
            width=35,
            height=30,
            corner_radius=8
        )
        next_btn.pack(side="left")
        
        # Schedule content
        schedule = self.app.get_schedule()
        self.create_schedule_content(inner, schedule)
    
    def create_schedule_content(self, parent, schedule):
        """Tạo nội dung lịch học chi tiết"""
        scroll_frame = ctk.CTkScrollableFrame(
            parent,
            fg_color="transparent",
            scrollbar_button_color="#e2e8f0",
            scrollbar_fg_color="#cbd5e1",
            height=280
        )
        scroll_frame.pack(fill="both", expand=True, pady=(0, 5))
        
        today_str = datetime.now().strftime("%d/%m")
        
        for day_data in schedule:
            # Day header
            day_frame = ctk.CTkFrame(scroll_frame, fg_color="transparent")
            day_frame.pack(fill="x", pady=(10, 5))
            
            is_today = day_data.get('date', '') == today_str
            day_color = "#10b981" if is_today else "#6366f1"
            day_text = f"{day_data.get('day', '')} - {day_data.get('date', '')}"
            if is_today:
                day_text += " (Hôm nay)"
            
            day_label = ctk.CTkLabel(
                day_frame,
                text=f"{'📍' if is_today else '📌'} {day_text}",
                font=ctk.CTkFont(family="Segoe UI", size=13, weight="bold"),
                text_color=day_color,
                anchor="w"
            )
            day_label.pack(anchor="w")
            
            # Classes for this day
            for class_info in day_data.get("classes", []):
                self.create_class_item(scroll_frame, class_info, is_today)
    
    def create_class_item(self, parent, class_info, highlight=False):
        """Tạo item lớp học với thiết kế đẹp"""
        if highlight:
            bg_color = "#ecfdf5"
            border_color = "#10b981"
            icon_bg = "#d1fae5"
        else:
            bg_color = "#f8fafc"
            border_color = "#e2e8f0"
            icon_bg = "#f1f5f9"
        
        class_frame = ctk.CTkFrame(
            parent,
            fg_color=bg_color,
            border_color=border_color,
            border_width=1 if highlight else 0,
            corner_radius=10
        )
        class_frame.pack(fill="x", pady=3)
        
        inner = ctk.CTkFrame(class_frame, fg_color="transparent")
        inner.pack(fill="x", padx=12, pady=10)
        
        # Left side - time and subject
        left_frame = ctk.CTkFrame(inner, fg_color="transparent")
        left_frame.pack(side="left", fill="x", expand=True)
        
        # Time with icon
        time_lbl = ctk.CTkLabel(
            left_frame,
            text=f"🕐 {class_info.get('time', '07:00 - 09:00')}",
            font=ctk.CTkFont(family="Segoe UI", size=13),
            text_color="#64748b",
            anchor="w"
        )
        time_lbl.pack(anchor="w")
        
        # Subject with colored dot
        subject_lbl = ctk.CTkLabel(
            left_frame,
            text=f"● {class_info.get('name', class_info.get('subject', 'Môn học'))}",
            font=ctk.CTkFont(family="Segoe UI", size=14, weight="bold"),
            text_color="#1e293b",
            anchor="w"
        )
        subject_lbl.pack(anchor="w", pady=(3, 0))
        
        # Location
        loc_lbl = ctk.CTkLabel(
            left_frame,
            text=f"📍 {class_info.get('room', class_info.get('location', 'Phòng học'))}",
            font=ctk.CTkFont(family="Segoe UI", size=12),
            text_color="#94a3b8",
            anchor="w"
        )
        loc_lbl.pack(anchor="w")
        
        # Type badge
        class_type = class_info.get('type', 'LT')
        type_colors = {"LT": "#dbeafe", "TH": "#dcfce7"}
        type_text_colors = {"LT": "#1d4ed8", "TH": "#15803d"}
        
        type_bg = ctk.CTkFrame(inner, fg_color=type_colors.get(class_type, "#f1f5f9"), corner_radius=6)
        type_bg.pack(side="right", padx=(10, 0))
        
        type_lbl = ctk.CTkLabel(
            type_bg,
            text=class_type,
            font=ctk.CTkFont(family="Segoe UI", size=10, weight="bold"),
            text_color=type_text_colors.get(class_type, "#64748b")
        )
        type_lbl.pack(padx=8, pady=4)
    
    def create_today_tasks(self, parent):
        """5. Việc cần làm hôm nay - SCROLLABLE"""
        tasks_card = ctk.CTkFrame(parent, fg_color="#ffffff", corner_radius=16)
        tasks_card.pack(fill="x", pady=(0, 15))
        
        inner = ctk.CTkFrame(tasks_card, fg_color="transparent")
        inner.pack(fill="x", padx=15, pady=12)
        
        # Title with icon
        title_frame = ctk.CTkFrame(inner, fg_color="transparent")
        title_frame.pack(fill="x", pady=(0, 8))
        
        icon_lbl = ctk.CTkLabel(
            title_frame,
            text="📋",
            font=("Segoe UI Emoji", 22)
        )
        icon_lbl.pack(side="left")
        
        title = ctk.CTkLabel(
            title_frame,
            text="Việc cần làm hôm nay",
            font=ctk.CTkFont(family="Segoe UI", size=15, weight="bold"),
            text_color="#1e293b"
        )
        title.pack(side="left", padx=(8, 0))
        
        # Task count badge
        tasks = self.app.get_tasks()
        count = len(tasks) if tasks else 0
        
        count_bg = ctk.CTkFrame(title_frame, fg_color="#fee2e2", corner_radius=10)
        count_bg.pack(side="right")
        
        count_lbl = ctk.CTkLabel(
            count_bg,
            text=f"{count} việc",
            font=ctk.CTkFont(family="Segoe UI", size=11, weight="bold"),
            text_color="#dc2626"
        )
        count_lbl.pack(padx=10, pady=3)
        
        # Scrollable tasks list
        scroll_frame = ctk.CTkScrollableFrame(
            inner,
            fg_color="transparent",
            scrollbar_button_color="#e2e8f0",
            scrollbar_fg_color="#cbd5e1",
            height=150
        )
        scroll_frame.pack(fill="x", pady=(5, 0))
        
        if not tasks or len(tasks) == 0:
            # Empty state
            empty_frame = ctk.CTkFrame(scroll_frame, fg_color="#f0fdf4", corner_radius=10)
            empty_frame.pack(fill="x", pady=5)
            
            empty_lbl = ctk.CTkLabel(
                empty_frame,
                text="✨ Không có việc cần làm hôm nay!\nHãy tận hưởng ngày nghỉ.",
                font=ctk.CTkFont(family="Segoe UI", size=12),
                text_color="#10b981",
                justify="center"
            )
            empty_lbl.pack(padx=15, pady=15)
        else:
            # Task items
            for task in tasks:
                self.create_task_item(scroll_frame, task)
    
    def create_task_item(self, parent, task):
        """Tạo item công việc với thiết kế đẹp"""
        priority = task.get("priority", "medium")
        
        # Priority colors
        priority_colors = {
            "high": {"bg": "#fef2f2", "border": "#fca5a5", "badge": "#ef4444"},
            "medium": {"bg": "#fffbeb", "border": "#fcd34d", "badge": "#f59e0b"},
            "low": {"bg": "#f0fdf4", "border": "#86efac", "badge": "#10b981"}
        }
        
        colors = priority_colors.get(priority, priority_colors["medium"])
        
        task_frame = ctk.CTkFrame(
            parent,
            fg_color=colors["bg"],
            border_color=colors["border"],
            border_width=1,
            corner_radius=10
        )
        task_frame.pack(fill="x", pady=4)
        
        inner = ctk.CTkFrame(task_frame, fg_color="transparent")
        inner.pack(fill="x", padx=12, pady=10)
        
        # Checkbox area
        checkbox = ctk.CTkCheckBox(
            inner,
            text="",
            checkbox_width=22,
            checkbox_height=22,
            corner_radius=6,
            fg_color=colors["badge"],
            hover_color=colors["badge"]
        )
        checkbox.pack(side="left", padx=(0, 12))
        
        # Task content
        content_frame = ctk.CTkFrame(inner, fg_color="transparent")
        content_frame.pack(side="left", fill="x", expand=True)
        
        task_lbl = ctk.CTkLabel(
            content_frame,
            text=task.get("title", "Công việc"),
            font=ctk.CTkFont(family="Segoe UI", size=13, weight="bold"),
            text_color="#1e293b",
            anchor="w"
        )
        task_lbl.pack(anchor="w")
        
        # Subject and due time
        sub_lbl = ctk.CTkLabel(
            content_frame,
            text=task.get("subject", ""),
            font=ctk.CTkFont(family="Segoe UI", size=11),
            text_color="#64748b",
            anchor="w"
        )
        sub_lbl.pack(anchor="w")
        
        # Priority badge
        priority_lbl = ctk.CTkLabel(
            inner,
            text=task.get("due_time", ""),
            font=ctk.CTkFont(family="Segoe UI", size=11),
            text_color="#94a3b8"
        )
        priority_lbl.pack(side="right")
    
    def create_smart_suggestion(self, parent):
        """6. Gợi ý lịch học thông minh - Thiết kế gradient đẹp"""
        suggestion_card = ctk.CTkFrame(parent, fg_color="#ffffff", corner_radius=16)
        suggestion_card.pack(fill="x", pady=(0, 15))
        
        inner = ctk.CTkFrame(suggestion_card, fg_color="transparent")
        inner.pack(fill="x", padx=15, pady=12)
        
        # Icon + Title
        header_frame = ctk.CTkFrame(inner, fg_color="transparent")
        header_frame.pack(fill="x", pady=(0, 10))
        
        icon_bg = ctk.CTkFrame(header_frame, fg_color="#fef3c7", corner_radius=10, width=40, height=40)
        icon_bg.pack(side="left")
        icon_bg.pack_propagate(False)
        
        icon_lbl = ctk.CTkLabel(
            icon_bg,
            text="💡",
            font=("Segoe UI Emoji", 24)
        )
        icon_lbl.place(relx=0.5, rely=0.5, anchor="center")
        
        title = ctk.CTkLabel(
            header_frame,
            text="Gợi ý thông minh",
            font=ctk.CTkFont(family="Segoe UI", size=15, weight="bold"),
            text_color="#1e293b"
        )
        title.pack(side="left", padx=(10, 0))
        
        # Suggestion text with icon
        suggestion_frame = ctk.CTkFrame(inner, fg_color="#f8fafc", corner_radius=10)
        suggestion_frame.pack(fill="x", pady=(0, 10))
        
        suggest_inner = ctk.CTkFrame(suggestion_frame, fg_color="transparent")
        suggest_inner.pack(fill="x", padx=12, pady=10)
        
        suggest_lbl = ctk.CTkLabel(
            suggest_inner,
            text="🔮 Bạn có 2 khoảng trống vào thứ 4.\nGợi ý: Học Toán cao cấp lúc 14:00",
            font=ctk.CTkFont(family="Segoe UI", size=12),
            text_color="#475569",
            anchor="w",
            justify="left"
        )
        suggest_lbl.pack(anchor="w")
        
        # View button
        view_btn = ctk.CTkButton(
            inner,
            text="Xem gợi ý →",
            font=ctk.CTkFont(family="Segoe UI", size=13, weight="bold"),
            fg_color="#6366f1",
            hover_color="#4f46e5",
            text_color="#ffffff",
            height=38,
            corner_radius=10
        )
        view_btn.pack(fill="x")
    
    def create_ai_button(self, parent):
        """7. Nút AI Assistant - Gradient đẹp"""
        ai_card = ctk.CTkFrame(parent, fg_color="#6366f1", corner_radius=16)
        ai_card.pack(fill="x", pady=(0, 15))
        
        inner = ctk.CTkFrame(ai_card, fg_color="transparent")
        inner.pack(fill="x", padx=20, pady=15)
        
        # Icon with glow effect
        icon_bg = ctk.CTkFrame(
            inner,
            fg_color="#a5b4fc",
            corner_radius=30,
            width=60,
            height=60
        )
        icon_bg.pack(side="left", padx=(0, 15))
        icon_bg.pack_propagate(False)
        
        icon_lbl = ctk.CTkLabel(
            icon_bg,
            text="🤖",
            font=("Segoe UI Emoji", 36)
        )
        icon_lbl.place(relx=0.5, rely=0.5, anchor="center")
        
        # Text
        text_frame = ctk.CTkFrame(inner, fg_color="transparent")
        text_frame.pack(side="left")
        
        ai_title = ctk.CTkLabel(
            text_frame,
            text="AI Assistant",
            font=ctk.CTkFont(family="Segoe UI", size=18, weight="bold"),
            text_color="#ffffff",
            anchor="w"
        )
        ai_title.pack(anchor="w")
        
        ai_desc = ctk.CTkLabel(
            text_frame,
            text="Hỏi đáp, gợi ý học tập thông minh",
            font=ctk.CTkFont(family="Segoe UI", size=12),
            text_color="#c7d2fe",
            anchor="w"
        )
        ai_desc.pack(anchor="w")
        
        # Arrow button
        arrow_btn = ctk.CTkButton(
            inner,
            text="→",
            font=ctk.CTkFont(family="Segoe UI", size=24, weight="bold"),
            fg_color="#a5b4fc",
            hover_color="#818cf8",
            text_color="#ffffff",
            width=50,
            height=50,
            corner_radius=25
        )
        arrow_btn.pack(side="right")
    
    def create_notifications(self, parent):
        """8. Thông báo - SCROLLABLE"""
        notif_card = ctk.CTkFrame(parent, fg_color="#ffffff", corner_radius=16)
        notif_card.pack(fill="x")
        
        inner = ctk.CTkFrame(notif_card, fg_color="transparent")
        inner.pack(fill="x", padx=15, pady=12)
        
        # Title with icon and badge
        title_frame = ctk.CTkFrame(inner, fg_color="transparent")
        title_frame.pack(fill="x", pady=(0, 10))
        
        icon_lbl = ctk.CTkLabel(
            title_frame,
            text="🔔",
            font=("Segoe UI Emoji", 22)
        )
        icon_lbl.pack(side="left")
        
        title = ctk.CTkLabel(
            title_frame,
            text="Thông báo",
            font=ctk.CTkFont(family="Segoe UI", size=15, weight="bold"),
            text_color="#1e293b"
        )
        title.pack(side="left", padx=(8, 0))
        
        # Count badge
        count_bg = ctk.CTkFrame(title_frame, fg_color="#fee2e2", corner_radius=10)
        count_bg.pack(side="right")
        
        count_lbl = ctk.CTkLabel(
            count_bg,
            text="3",
            font=ctk.CTkFont(family="Segoe UI", size=11, weight="bold"),
            text_color="#dc2626"
        )
        count_lbl.pack(padx=8, pady=3)
        
        # Scrollable notifications list
        scroll_frame = ctk.CTkScrollableFrame(
            inner,
            fg_color="transparent",
            scrollbar_button_color="#e2e8f0",
            scrollbar_fg_color="#cbd5e1",
            height=200
        )
        scroll_frame.pack(fill="x", pady=(5, 0))
        
        # Notification items
        notifications = self.app.get_notifications()
        
        if not notifications or len(notifications) == 0:
            notifications = [
                {"icon": "📢", "title": "Thông báo", "content": "Nghỉ học môn Triết học ngày 10/05", "type": "warning"},
                {"icon": "📋", "title": "Cập nhật", "content": "Lịch thi giữa kỳ đã được cập nhật", "type": "info"},
                {"icon": "📅", "title": "Nhắc nhở", "content": "Hạn nộp bài tập Python: 12/05", "type": "reminder"}
            ]
        
        for notif in notifications:
            self.create_notification_item(scroll_frame, notif)
    
    def create_notification_item(self, parent, notif):
        """Tạo item thông báo với thiết kế đẹp"""
        notif_type = notif.get("type", "info")
        
        # Type-based colors
        type_colors = {
            "warning": {"bg": "#fffbeb", "border": "#fcd34d", "icon_bg": "#fef3c7"},
            "info": {"bg": "#eff6ff", "border": "#93c5fd", "icon_bg": "#dbeafe"},
            "reminder": {"bg": "#f0fdf4", "border": "#86efac", "icon_bg": "#dcfce7"}
        }
        
        colors = type_colors.get(notif_type, type_colors["info"])
        
        notif_frame = ctk.CTkFrame(
            parent,
            fg_color=colors["bg"],
            border_color=colors["border"],
            border_width=1,
            corner_radius=10
        )
        notif_frame.pack(fill="x", pady=4)
        
        inner = ctk.CTkFrame(notif_frame, fg_color="transparent")
        inner.pack(fill="x", padx=12, pady=10)
        
        # Icon with colored background
        icon_bg = ctk.CTkFrame(inner, fg_color=colors["icon_bg"], corner_radius=8, width=36, height=36)
        icon_bg.pack(side="left", padx=(0, 10))
        icon_bg.pack_propagate(False)
        
        icon_lbl = ctk.CTkLabel(
            icon_bg,
            text=notif.get("icon", "📢"),
            font=("Segoe UI Emoji", 20)
        )
        icon_lbl.place(relx=0.5, rely=0.5, anchor="center")
        
        # Content
        content_frame = ctk.CTkFrame(inner, fg_color="transparent")
        content_frame.pack(side="left", fill="x", expand=True)
        
        title_lbl = ctk.CTkLabel(
            content_frame,
            text=notif.get("title", ""),
            font=ctk.CTkFont(family="Segoe UI", size=12, weight="bold"),
            text_color="#1e293b",
            anchor="w"
        )
        title_lbl.pack(anchor="w")
        
        content_lbl = ctk.CTkLabel(
            content_frame,
            text=notif.get("content", ""),
            font=ctk.CTkFont(family="Segoe UI", size=11),
            text_color="#64748b",
            anchor="w"
        )
        content_lbl.pack(anchor="w")
    
    def refresh(self):
        """Refresh dashboard data"""
        pass
