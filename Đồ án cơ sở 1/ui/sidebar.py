"""
SmartStudy AI - Sidebar Component
Thanh menu điều hướng bên trái
"""

import customtkinter as ctk


class Sidebar(ctk.CTkFrame):
    """Sidebar navigation component"""
    
    def __init__(self, parent, app, **kwargs):
        super().__init__(parent, **kwargs)
        
        self.app = app
        self.current_active = "dashboard"
        
        # Sidebar background color
        self.sidebar_bg = "#1a1a2e"
        self.active_color = "#667eea"
        self.hover_color = "#764ba2"
        
        # Configure sidebar
        self.configure(
            width=250,
            height=850,
            fg_color=self.sidebar_bg,
            corner_radius=0
        )
        self.grid(row=0, column=0, sticky="nsew")
        
        # Configure grid
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=0)
        
        # Create widgets
        self.create_header()
        self.create_navigation()
    
    def create_header(self):
        """Create sidebar header with logo and user info"""
        # Header frame
        header_frame = ctk.CTkFrame(self, fg_color="transparent")
        header_frame.grid(row=0, column=0, padx=20, pady=(20, 15), sticky="ew")
        
        # Top section - Logo with emoji
        logo_frame = ctk.CTkFrame(header_frame, fg_color="transparent")
        logo_frame.pack(fill="x", pady=(0, 15))
        
        # App Icon
        icon_label = ctk.CTkLabel(
            logo_frame,
            text="📚",
            font=("Segoe UI Emoji", 32),
            width=60,
            height=60,
            fg_color="#667eea",
            corner_radius=15
        )
        icon_label.pack(side="left", padx=(0, 12))
        
        # App name and tagline
        name_frame = ctk.CTkFrame(logo_frame, fg_color="transparent")
        name_frame.pack(side="left", fill="both", expand=True)
        
        logo_label = ctk.CTkLabel(
            name_frame,
            text="✨ SmartStudy",
            font=ctk.CTkFont(family="Segoe UI", size=22, weight="bold"),
            text_color="#667eea",
            anchor="w"
        )
        logo_label.pack(anchor="w")
        
        tagline = ctk.CTkLabel(
            name_frame,
            text="📖 Học tập thông minh",
            font=ctk.CTkFont(family="Segoe UI", size=11),
            text_color="#888888",
            anchor="w"
        )
        tagline.pack(anchor="w")
        
        # Divider
        divider = ctk.CTkFrame(header_frame, height=2, fg_color="#333355")
        divider.pack(fill="x", pady=(0, 15))
        
        # User info section
        user_info_frame = ctk.CTkFrame(header_frame, fg_color="#252540", corner_radius=12)
        user_info_frame.pack(fill="x", pady=(0, 5))
        
        # Avatar
        avatar_label = ctk.CTkLabel(
            user_info_frame,
            text="👨‍🎓",
            font=("Segoe UI Emoji", 18),
            width=40,
            height=40,
            fg_color="#764ba2",
            corner_radius=20
        )
        avatar_label.pack(side="left", padx=10, pady=10)
        
        # User name
        name_label = ctk.CTkLabel(
            user_info_frame,
            text="👤 Nguyễn Văn Minh",
            font=ctk.CTkFont(family="Segoe UI", size=13, weight="bold"),
            text_color="#ffffff",
            anchor="w"
        )
        name_label.pack(anchor="w", padx=(0, 10), pady=(10, 0))
        
        # Student ID
        student_id_label = ctk.CTkLabel(
            user_info_frame,
            text="B21DCCN001",
            font=ctk.CTkFont(family="Segoe UI", size=11),
            text_color="#888888",
            anchor="w"
        )
        student_id_label.pack(anchor="w", padx=(50, 10), pady=(0, 10))
        
        # Status indicator
        status_frame = ctk.CTkFrame(user_info_frame, fg_color="transparent")
        status_frame.pack(anchor="e", padx=10, pady=(0, 8))
        
        status_dot = ctk.CTkLabel(
            status_frame,
            text="●",
            font=("Segoe UI", 10),
            text_color="#4ade80",
            width=10
        )
        status_dot.pack(side="left")
        
        status_text = ctk.CTkLabel(
            status_frame,
            text="Online",
            font=ctk.CTkFont(family="Segoe UI", size=10),
            text_color="#4ade80"
        )
        status_text.pack(side="left")
    
    def create_navigation(self):
        """Create navigation menu items"""
        # Navigation frame
        nav_frame = ctk.CTkFrame(self, fg_color="transparent")
        nav_frame.grid(row=1, column=0, padx=15, pady=20, sticky="nsew")
        
        # Menu items configuration - no emoji
        self.menu_items = [
            {"id": "dashboard", "icon": "🏠", "label": "Trang chủ", "page": "dashboard"},
            {"id": "schedule", "icon": "📅", "label": "Lịch học", "page": "schedule"},
            {"id": "tasks", "icon": "📝", "label": "Công việc", "page": "tasks"},
            {"id": "ai_chat", "icon": "🤖", "label": "AI Hỗ trợ", "page": "ai_chat"},
            {"id": "profile", "icon": "👤", "label": "Hồ sơ", "page": "profile"},
        ]
        
        # Create menu buttons
        self.menu_buttons = {}
        for i, item in enumerate(self.menu_items):
            btn = self.create_menu_button(nav_frame, item)
            self.menu_buttons[item["id"]] = btn
        
        # Set dashboard as default active
        self.menu_buttons["dashboard"].configure(
            fg_color=self.active_color
        )
    
    def create_menu_button(self, parent, item):
        """Create a single menu button"""
        btn = ctk.CTkButton(
            parent,
            text=f"  {item['icon']}  {item['label']}",
            command=lambda: self.app.show_page(item["page"]),
            fg_color="transparent",
            hover_color=self.active_color,
            text_color="#ffffff",
            font=ctk.CTkFont(family="Segoe UI Emoji", size=14, weight="normal"),
            height=48,
            corner_radius=12,
            anchor="w"
        )
        btn.pack(fill="x", pady=4, padx=5)
        return btn
    
    def set_active(self, page_id):
        """Set the active menu item"""
        # Reset all buttons
        for btn_id, btn in self.menu_buttons.items():
            if btn_id == page_id:
                btn.configure(
                    fg_color=self.active_color,
                    text_color="#ffffff"
                )
            else:
                btn.configure(
                    fg_color="transparent",
                    text_color="#cccccc"
                )
        
        self.current_active = page_id
