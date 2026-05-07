"""
SmartStudy AI - Profile Page
Trang hồ sơ cá nhân và cài đặt - Nâng cấp đồ họa
"""

import customtkinter as ctk
from datetime import datetime


class ProfilePage(ctk.CTkFrame):
    """User profile and settings page - Enhanced UI"""
    
    # Modern color palette
    colors = {
        "primary": "#667eea",
        "secondary": "#764ba2",
        "accent_green": "#10b981",
        "accent_orange": "#f59e0b",
        "accent_pink": "#ec4899",
        "accent_blue": "#3b82f6",
        "bg_light": "#f8fafc",
        "bg_card": "#ffffff",
        "text_dark": "#1e293b",
        "text_gray": "#64748b",
        "text_light": "#94a3b8",
        "border": "#e2e8f0",
        "success": "#22c55e",
        "warning": "#eab308",
        "danger": "#ef4444",
        "gradient_start": "#667eea",
        "gradient_end": "#764ba2",
    }
    
    def __init__(self, parent, app):
        super().__init__(parent)
        
        self.app = app
        self.user_info = app.get_user_info()
        
        # Configure frame
        self.configure(fg_color=self.colors["bg_light"], corner_radius=0)
        
        self.create_widgets()
    
    def create_widgets(self):
        """Create profile page widgets with enhanced graphics"""
        
        # ==================== HEADER ====================
        self.create_header()
        
        # ==================== SCROLLABLE CONTENT ====================
        scroll_frame = ctk.CTkScrollableFrame(
            self,
            fg_color="transparent",
            scrollbar_button_color=self.colors["border"],
            scrollbar_fg_color="transparent"
        )
        scroll_frame.pack(fill="both", expand=True, padx=25, pady=20)
        
        # Configure grid
        scroll_frame.grid_columnconfigure(0, weight=1)
        scroll_frame.grid_columnconfigure(1, weight=1)
        
        # ==================== PROFILE HERO SECTION ====================
        self.create_hero_card(scroll_frame)
        
        # ==================== STATS CARDS ROW ====================
        self.create_stats_row(scroll_frame)
        
        # ==================== ACADEMIC PROGRESS ====================
        self.create_academic_card(scroll_frame)
        
        # ==================== SETTINGS SECTION ====================
        self.create_settings_card(scroll_frame)
        
        # ==================== QUICK ACTIONS ====================
        self.create_quick_actions_card(scroll_frame)
        
        # ==================== ABOUT SECTION ====================
        self.create_about_card(scroll_frame)
    
    def create_header(self):
        """Create header with gradient background"""
        header = ctk.CTkFrame(self, fg_color="transparent", height=80)
        header.pack(fill="x")
        header.pack_propagate(False)
        
        # Gradient background bar
        gradient_bar = ctk.CTkFrame(header, fg_color=self.colors["primary"], height=4)
        gradient_bar.pack(fill="x")
        
        # Title
        title_frame = ctk.CTkFrame(header, fg_color="transparent")
        title_frame.pack(fill="x", padx=5, pady=15)
        
        # Last updated
        ctk.CTkLabel(
            title_frame,
            text=f"Cập nhật: {datetime.now().strftime('%d/%m/%Y %H:%M')}",
            font=ctk.CTkFont(family="Segoe UI", size=12),
            text_color=self.colors["text_light"]
        ).pack(side="right")
    
    def create_hero_card(self, parent):
        """Create hero profile card with avatar and basic info"""
        hero_card = ctk.CTkFrame(parent, fg_color="transparent")
        hero_card.grid(row=0, column=0, columnspan=2, pady=(0, 20), sticky="ew")
        
        # Main card with gradient header
        card = ctk.CTkFrame(hero_card, fg_color=self.colors["bg_card"], corner_radius=20)
        card.pack(fill="x")
        
        # Gradient header
        header_gradient = ctk.CTkFrame(
            card,
            fg_color=self.colors["primary"],
            corner_radius=20,
            height=140
        )
        header_gradient.pack(fill="x")
        header_gradient.pack_propagate(False)
        
        # Wave decoration
        wave = ctk.CTkCanvas(header_gradient, width=800, height=40, bg=self.colors["primary"], highlightthickness=0)
        wave.pack(fill="x", side="bottom")
        wave.create_arc(0, 0, 100, 60, start=0, extent=180, fill="#ffffff", outline="")
        wave.create_arc(80, 0, 180, 60, start=0, extent=180, fill="#ffffff", outline="")
        wave.create_arc(160, 0, 260, 60, start=0, extent=180, fill="#ffffff", outline="")
        wave.create_arc(240, 0, 340, 60, start=0, extent=180, fill="#ffffff", outline="")
        
        # Avatar container (overlapping the gradient)
        avatar_container = ctk.CTkFrame(header_gradient, fg_color="transparent")
        avatar_container.place(relx=0.5, rely=0.6, anchor="center")
        
        # Avatar circle with border
        avatar_border = ctk.CTkFrame(
            avatar_container,
            fg_color="#ffffff",
            corner_radius=60,
            width=120,
            height=120
        )
        avatar_border.pack()
        avatar_border.pack_propagate(False)
        
        avatar = ctk.CTkFrame(avatar_border, fg_color=self.colors["primary"], corner_radius=55)
        avatar.pack(padx=5, pady=5)
        
        ctk.CTkLabel(
            avatar,
            text="👤",
            font=("Segoe UI Emoji", 50),
            text_color="#ffffff"
        ).place(relx=0.5, rely=0.5, anchor="center")
        
        # User info section
        info_section = ctk.CTkFrame(card, fg_color="transparent")
        info_section.pack(fill="x", pady=(80, 25), padx=25)
        
        # Name with verification badge
        name_frame = ctk.CTkFrame(info_section, fg_color="transparent")
        name_frame.pack()
        
        ctk.CTkLabel(
            name_frame,
            text=self.user_info.get("name", "Nguyễn Văn Minh"),
            font=ctk.CTkFont(family="Segoe UI", size=26, weight="bold"),
            text_color=self.colors["text_dark"]
        ).pack(side="left")
        
        # Verified badge
        verified = ctk.CTkFrame(name_frame, fg_color="#dcfce7", corner_radius=12)
        verified.pack(side="left", padx=(10, 0))
        ctk.CTkLabel(
            verified,
            text="✓ Đã xác thực",
            font=ctk.CTkFont(family="Segoe UI", size=11, weight="bold"),
            text_color="#16a34a"
        ).pack(padx=10, pady=4)
        
        # Student ID and Email
        ctk.CTkLabel(
            info_section,
            text=f"MSSV: {self.user_info.get('student_id', 'B21DCCN001')} • Khoa Công nghệ thông tin",
            font=ctk.CTkFont(family="Segoe UI", size=13),
            text_color=self.colors["text_gray"]
        ).pack(pady=(8, 0))
        
        ctk.CTkLabel(
            info_section,
            text=f"📧 {self.user_info.get('email', 'minh.nv@example.com')}",
            font=ctk.CTkFont(family="Segoe UI", size=13),
            text_color=self.colors["text_gray"]
        ).pack(pady=(5, 0))
        
        # Action buttons
        action_frame = ctk.CTkFrame(card, fg_color="transparent")
        action_frame.pack(fill="x", padx=25, pady=(0, 25))
        
        edit_btn = ctk.CTkButton(
            action_frame,
            text="✏️ Chỉnh sửa hồ sơ",
            width=160,
            height=42,
            fg_color=self.colors["primary"],
            hover_color=self.colors["secondary"],
            text_color="#ffffff",
            corner_radius=12,
            font=ctk.CTkFont(family="Segoe UI", size=13, weight="bold")
        )
        edit_btn.pack(side="left", padx=(0, 10))
        
        share_btn = ctk.CTkButton(
            action_frame,
            text="🔗 Chia sẻ",
            width=120,
            height=42,
            fg_color="#f1f5f9",
            hover_color="#e2e8f0",
            text_color=self.colors["text_dark"],
            corner_radius=12,
            font=ctk.CTkFont(family="Segoe UI", size=13)
        )
        share_btn.pack(side="left")
    
    def create_stats_row(self, parent):
        """Create statistics cards row"""
        stats_frame = ctk.CTkFrame(parent, fg_color="transparent")
        stats_frame.grid(row=1, column=0, columnspan=2, pady=(0, 20), sticky="ew")
        
        # Configure columns
        stats_frame.grid_columnconfigure(0, weight=1)
        stats_frame.grid_columnconfigure(1, weight=1)
        stats_frame.grid_columnconfigure(2, weight=1)
        stats_frame.grid_columnconfigure(3, weight=1)
        
        # GPA Card
        self.create_stat_card(
            stats_frame, 0, 0,
            "📊", "GPA",
            f"{self.user_info.get('gpa', 3.5)}/4.0",
            self.colors["accent_green"],
            "Xuất sắc"
        )
        
        # Credits Card
        self.create_stat_card(
            stats_frame, 0, 1,
            "📚", "Tín chỉ",
            f"{self.user_info.get('credits_completed', 85)}/{self.user_info.get('total_credits', 140)}",
            self.colors["accent_blue"],
            "Đã tích lũy"
        )
        
        # Attendance Card
        self.create_stat_card(
            stats_frame, 0, 2,
            "✅", "Điểm danh",
            "96%",
            self.colors["primary"],
            "Tỷ lệ"
        )
        
        # Rank Card
        self.create_stat_card(
            stats_frame, 0, 3,
            "🏆", "Xếp hạng",
            "Top 15%",
            self.colors["accent_orange"],
            "Toàn trường"
        )
    
    def create_stat_card(self, parent, row, col, icon, label, value, color, subtitle):
        """Create a single stat card"""
        card = ctk.CTkFrame(parent, fg_color=self.colors["bg_card"], corner_radius=16)
        card.grid(row=row, column=col, padx=6, sticky="ew")
        
        # Color accent bar
        accent = ctk.CTkFrame(card, fg_color=color, height=4, corner_radius=2)
        accent.pack(fill="x", padx=12, pady=(12, 0))
        
        # Icon
        ctk.CTkLabel(
            card,
            text=icon,
            font=("Segoe UI Emoji", 28)
        ).pack(pady=(12, 0))
        
        # Value
        ctk.CTkLabel(
            card,
            text=value,
            font=ctk.CTkFont(family="Segoe UI", size=20, weight="bold"),
            text_color=color
        ).pack()
        
        # Label
        ctk.CTkLabel(
            card,
            text=label,
            font=ctk.CTkFont(family="Segoe UI", size=12, weight="bold"),
            text_color=self.colors["text_dark"]
        ).pack()
        
        # Subtitle
        ctk.CTkLabel(
            card,
            text=subtitle,
            font=ctk.CTkFont(family="Segoe UI", size=10),
            text_color=self.colors["text_light"]
        ).pack(pady=(0, 12))
    
    def create_academic_card(self, parent):
        """Create academic progress card"""
        card = ctk.CTkFrame(parent, fg_color=self.colors["bg_card"], corner_radius=16)
        card.grid(row=2, column=0, padx=(0, 10), sticky="nsew")
        
        # Header
        header = ctk.CTkFrame(card, fg_color="transparent")
        header.pack(fill="x", padx=20, pady=18)
        
        ctk.CTkLabel(
            header,
            text="📈 Tiến độ học tập",
            font=ctk.CTkFont(family="Segoe UI", size=16, weight="bold"),
            text_color=self.colors["text_dark"]
        ).pack(side="left")
        
        ctk.CTkLabel(
            header,
            text="Học kỳ 2024.2",
            font=ctk.CTkFont(family="Segoe UI", size=12),
            text_color=self.colors["text_light"]
        ).pack(side="right")
        
        # Progress bars
        progress_items = [
            ("Môn hoàn thành", 24, 32, self.colors["accent_green"]),
            ("Điểm trung bình", 3.5, 4.0, self.colors["accent_blue"]),
            ("Giờ học/tuần", 18, 25, self.colors["accent_orange"]),
            ("Bài tập đã nộp", 45, 50, self.colors["primary"]),
        ]
        
        for label, value, max_val, color in progress_items:
            self.create_progress_item(card, label, value, max_val, color)
        
        ctk.CTkLabel(
            card,
            text="",
            font=ctk.CTkFont(family="Segoe UI", size=8)
        ).pack(pady=5)
    
    def create_progress_item(self, parent, label, value, max_val, color):
        """Create a progress bar item"""
        frame = ctk.CTkFrame(parent, fg_color="transparent")
        frame.pack(fill="x", padx=20, pady=6)
        
        # Label and value
        ctk.CTkLabel(
            frame,
            text=label,
            font=ctk.CTkFont(family="Segoe UI", size=12),
            text_color=self.colors["text_gray"]
        ).pack(side="left")
        
        val_text = f"{value}/{max_val}"
        if isinstance(value, float):
            val_text = f"{value:.1f}/{max_val}"
        ctk.CTkLabel(
            frame,
            text=val_text,
            font=ctk.CTkFont(family="Segoe UI", size=12, weight="bold"),
            text_color=color
        ).pack(side="right")
        
        # Progress bar background
        bar_bg = ctk.CTkFrame(parent, fg_color="#f1f5f9", height=8, corner_radius=4)
        bar_bg.pack(fill="x", padx=20, pady=(0, 12))
        bar_bg.pack_propagate(False)
        
        # Progress bar fill
        fill_width = value / max_val
        bar_fill = ctk.CTkFrame(bar_bg, fg_color=color, corner_radius=4)
        bar_fill.place(relx=0, rely=0, relwidth=min(fill_width, 1.0), relheight=1)
    
    def create_settings_card(self, parent):
        """Create settings card"""
        card = ctk.CTkFrame(parent, fg_color=self.colors["bg_card"], corner_radius=16)
        card.grid(row=2, column=1, sticky="nsew")
        
        # Header
        ctk.CTkLabel(
            card,
            text="⚙️ Cài đặt",
            font=ctk.CTkFont(family="Segoe UI", size=16, weight="bold"),
            text_color=self.colors["text_dark"]
        ).pack(anchor="w", padx=20, pady=18)
        
        # Settings items
        settings_items = [
            ("🌙", "Chế độ tối", True, self.toggle_theme),
            ("🔔", "Thông báo", True, None),
            ("🔊", "Âm thanh", True, None),
            ("💾", "Tự động lưu", False, None),
            ("🌐", "Ngôn ngữ", False, None),
        ]
        
        for icon, label, default, cmd in settings_items:
            self.create_setting_item(card, icon, label, default, cmd)
        
        ctk.CTkLabel(
            card,
            text="",
            font=ctk.CTkFont(family="Segoe UI", size=8)
        ).pack(pady=10)
    
    def create_setting_item(self, parent, icon, label, default, command):
        """Create a setting toggle item"""
        frame = ctk.CTkFrame(parent, fg_color="#f8fafc", corner_radius=12)
        frame.pack(fill="x", padx=20, pady=4)
        
        # Icon
        ctk.CTkLabel(
            frame,
            text=icon,
            font=("Segoe UI Emoji", 16)
        ).pack(side="left", padx=(12, 8), pady=10)
        
        # Label
        ctk.CTkLabel(
            frame,
            text=label,
            font=ctk.CTkFont(family="Segoe UI", size=13),
            text_color=self.colors["text_dark"]
        ).pack(side="left", pady=10)
        
        # Switch
        switch = ctk.CTkSwitch(
            frame,
            text="",
            width=44,
            switch_width=44,
            switch_height=24,
            command=command
        )
        switch.pack(side="right", padx=10)
        if default:
            switch.select()
    
    def create_quick_actions_card(self, parent):
        """Create quick actions card"""
        card = ctk.CTkFrame(parent, fg_color=self.colors["bg_card"], corner_radius=16)
        card.grid(row=3, column=0, columnspan=2, pady=20, sticky="ew")
        
        # Header
        ctk.CTkLabel(
            card,
            text="🚀 Thao tác nhanh",
            font=ctk.CTkFont(family="Segoe UI", size=16, weight="bold"),
            text_color=self.colors["text_dark"]
        ).pack(anchor="w", padx=20, pady=(18, 15))
        
        # Action buttons
        actions_frame = ctk.CTkFrame(card, fg_color="transparent")
        actions_frame.pack(fill="x", padx=20, pady=(0, 18))
        
        actions_frame.grid_columnconfigure(0, weight=1)
        actions_frame.grid_columnconfigure(1, weight=1)
        actions_frame.grid_columnconfigure(2, weight=1)
        
        self.create_action_button(actions_frame, 0, "📤", "Xuất dữ liệu", self.colors["accent_blue"])
        self.create_action_button(actions_frame, 1, "🔑", "Đổi mật khẩu", self.colors["accent_orange"])
        self.create_action_button(actions_frame, 2, "🚪", "Đăng xuất", self.colors["danger"])
    
    def create_action_button(self, parent, col, icon, label, color):
        """Create an action button"""
        btn = ctk.CTkButton(
            parent,
            text=f"{icon}\n{label}",
            height=70,
            fg_color=color,
            hover_color=self.adjust_color(color, -10),
            text_color="#ffffff",
            corner_radius=12,
            font=ctk.CTkFont(family="Segoe UI", size=12, weight="bold"),
            compound="top"
        )
        btn.grid(row=0, column=col, padx=5, sticky="ew")
    
    def create_about_card(self, parent):
        """Create about section"""
        card = ctk.CTkFrame(parent, fg_color=self.colors["bg_card"], corner_radius=16)
        card.grid(row=4, column=0, columnspan=2, sticky="ew")
        
        # Header with gradient
        header = ctk.CTkFrame(card, fg_color=self.colors["primary"], corner_radius=16)
        header.pack(fill="x", ipady=50)
        
        ctk.CTkLabel(
            header,
            text="📱 SmartStudy AI",
            font=ctk.CTkFont(family="Segoe UI", size=20, weight="bold"),
            text_color="#ffffff"
        ).pack(pady=(15, 5))
        
        ctk.CTkLabel(
            header,
            text="Ứng dụng quản lý học tập thông minh",
            font=ctk.CTkFont(family="Segoe UI", size=12),
            text_color="#ffffff"
        ).pack()
        
        # Info
        info_frame = ctk.CTkFrame(card, fg_color="transparent")
        info_frame.pack(fill="x", padx=20, pady=20)
        
        info_items = [
            ("Phiên bản", "1.0.0"),
            ("Nhà phát triển", "SmartStudy Team"),
            ("Bản quyền", f"© 2024 - {datetime.now().year}"),
            ("Liên hệ", "support@smartstudy.edu.vn"),
        ]
        
        for label, value in info_items:
            row = ctk.CTkFrame(info_frame, fg_color="transparent")
            row.pack(fill="x", pady=4)
            
            ctk.CTkLabel(
                row,
                text=label,
                font=ctk.CTkFont(family="Segoe UI", size=12),
                text_color=self.colors["text_light"],
                width=120,
                anchor="w"
            ).pack(side="left")
            
            ctk.CTkLabel(
                row,
                text=value,
                font=ctk.CTkFont(family="Segoe UI", size=12, weight="bold"),
                text_color=self.colors["text_dark"],
                anchor="w"
            ).pack(side="left")
    
    def toggle_theme(self):
        """Toggle dark/light mode"""
        if self.theme_switch.get() if hasattr(self, 'theme_switch') else False:
            ctk.set_appearance_mode("dark")
        else:
            ctk.set_appearance_mode("light")
    
    def adjust_color(self, hex_color, amount):
        """Adjust hex color brightness"""
        hex_color = hex_color.lstrip('#')
        r = max(0, min(255, int(hex_color[0:2], 16) + amount))
        g = max(0, min(255, int(hex_color[2:4], 16) + amount))
        b = max(0, min(255, int(hex_color[4:6], 16) + amount))
        return f"#{r:02x}{g:02x}{b:02x}"
    
    def refresh(self):
        """Refresh profile data"""
        self.user_info = self.app.get_user_info()
