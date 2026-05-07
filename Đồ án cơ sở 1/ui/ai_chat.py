"""
SmartStudy AI - AI Chat Page
Trang chatbot AI hỗ trợ học tập
"""

import customtkinter as ctk
from datetime import datetime


class AIChatPage(ctk.CTkFrame):
    """AI Chat assistant page"""
    
    def __init__(self, parent, app):
        super().__init__(parent)
        
        self.app = app
        self.messages = []
        
        # Configure frame
        self.configure(
            fg_color="#f8f9fa",
            corner_radius=0
        )
        
        self.create_widgets()
        self.add_welcome_message()
    
    def create_widgets(self):
        """Create chat page widgets"""
        
        # ==================== MAIN LAYOUT ====================
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        
        # ==================== LEFT SIDEBAR (Quick Actions) ====================
        left_panel = ctk.CTkFrame(
            self,
            width=250,
            fg_color="#ffffff",
            corner_radius=0
        )
        left_panel.grid(row=0, column=0, sticky="nsew")
        left_panel.grid_propagate(False)
        
        # AI Info Header
        ai_header = ctk.CTkFrame(left_panel, fg_color="#667eea", corner_radius=0)
        ai_header.pack(fill="x", pady=(0, 0))
        
        ai_avatar = ctk.CTkLabel(
            ai_header,
            text="🤖",
            font=("Segoe UI Emoji", 40),
            text_color="#ffffff"
        )
        ai_avatar.pack(pady=(25, 10))
        
        ai_title = ctk.CTkLabel(
            ai_header,
            text="SmartStudy AI",
            font=ctk.CTkFont(family="Segoe UI", size=18, weight="bold"),
            text_color="#ffffff"
        )
        ai_title.pack(pady=(0, 5))
        
        ai_subtitle = ctk.CTkLabel(
            ai_header,
            text="Trợ lý học tập 24/7",
            font=ctk.CTkFont(family="Segoe UI", size=12),
            text_color="#e0e0ff"
        )
        ai_subtitle.pack(pady=(0, 20))
        
        # Quick Actions
        actions_title = ctk.CTkLabel(
            left_panel,
            text="✏️ Gợi ý hỏi nhanh",
            font=ctk.CTkFont(family="Segoe UI", size=14, weight="bold"),
            text_color="#333333"
        )
        actions_title.pack(anchor="w", padx=20, pady=(25, 15))
        
        # Suggested questions
        suggestions = [
            {"icon": "📚", "text": "Giải thích bài toán", "color": "#667eea"},
            {"icon": "📝", "text": "Hướng dẫn làm bài", "color": "#11998e"},
            {"icon": "🔍", "text": "Tìm kiếm tài liệu", "color": "#f59e0b"},
            {"icon": "📊", "text": "Thống kê học tập", "color": "#764ba2"},
            {"icon": "💡", "text": "Mẹo học tập", "color": "#10b981"},
            {"icon": "❓", "text": "Hỏi đáp nhanh", "color": "#ef4444"}
        ]
        
        for sugg in suggestions:
            btn = ctk.CTkButton(
                left_panel,
                text=f"{sugg['icon']} {sugg['text']}",
                width=210,
                height=40,
                fg_color="#f8f9fa",
                hover_color="#f0f0f0",
                text_color="#333333",
                corner_radius=10,
                font=("Segoe UI", 12),
                anchor="w",
                command=lambda s=sugg: self.send_quick_message(s["text"])
            )
            btn.pack(pady=4, padx=20)
        
        # New chat button
        new_chat_btn = ctk.CTkButton(
            left_panel,
            text="💬 Trò chuyện mới",
            width=210,
            height=45,
            fg_color="#667eea",
            hover_color="#764ba2",
            text_color="#ffffff",
            corner_radius=12,
            font=("Segoe UI", 13, "bold"),
            command=self.new_chat
        )
        new_chat_btn.pack(side="bottom", pady=20)
        
        # ==================== CHAT AREA ====================
        chat_container = ctk.CTkFrame(self, fg_color="#f8f9fa")
        chat_container.grid(row=0, column=1, sticky="nsew")
        
        # Header
        header = ctk.CTkFrame(
            chat_container,
            fg_color="#ffffff",
            height=70,
            corner_radius=0
        )
        header.pack(fill="x")
        header.pack_propagate(False)
        
        chat_title = ctk.CTkLabel(
            header,
            text="💬 Trò chuyện với AI",
            font=ctk.CTkFont(family="Segoe UI", size=20, weight="bold"),
            text_color="#333333"
        )
        chat_title.pack(side="left", padx=25, pady=15)
        
        # Model selector
        model_combo = ctk.CTkOptionMenu(
            header,
            values=["GPT-4", "GPT-3.5", "Claude", "Local AI"],
            width=120,
            height=35,
            corner_radius=10,
            font=("Segoe UI", 11)
        )
        model_combo.pack(side="right", padx=25, pady=15)
        model_combo.set("GPT-4")
        
        # Messages area
        self.messages_frame = ctk.CTkScrollableFrame(
            chat_container,
            fg_color="transparent",
            scrollbar_button_color="#e0e0e0"
        )
        self.messages_frame.pack(fill="both", expand=True, padx=25, pady=15)
        
        # Input area
        input_frame = ctk.CTkFrame(
            chat_container,
            fg_color="#ffffff",
            height=80,
            corner_radius=0
        )
        input_frame.pack(fill="x", side="bottom")
        input_frame.pack_propagate(False)
        
        # Input container
        input_container = ctk.CTkFrame(input_frame, fg_color="#f0f0f0", corner_radius=15)
        input_container.pack(fill="x", padx=20, pady=15, ipady=5)
        
        # Text input
        self.input_field = ctk.CTkTextbox(
            input_container,
            height=50,
            fg_color="transparent",
            border_width=0,
            font=("Segoe UI", 13),
            wrap="word"
        )
        self.input_field.place(relx=0.02, rely=0.2, relwidth=0.82, relheight=0.6)
        
        # Send button
        send_btn = ctk.CTkButton(
            input_container,
            text="➤",
            width=45,
            height=45,
            fg_color="#667eea",
            hover_color="#764ba2",
            text_color="#ffffff",
            corner_radius=10,
            font=("Segoe UI", 20),
            command=self.send_message
        )
        send_btn.place(relx=0.9, rely=0.5, anchor="center")
        
        # Bind Enter key to send
        self.input_field.bind("<Return>", lambda e: self.send_message())
    
    def add_welcome_message(self):
        """Add welcome message from AI"""
        welcome_msg = {
            "role": "ai",
            "content": "Xin chào! 👋\n\nTôi là SmartStudy AI, trợ lý học tập của bạn. Tôi có thể giúp bạn:\n\n📚 Giải thích các khái niệm học thuật\n📝 Hướng dẫn làm bài tập\n💡 Chia sẻ mẹo học tập hiệu quả\n🔍 Tìm kiếm và tổng hợp tài liệu\n📊 Phân tích dữ liệu học tập\n\nBạn cần tôi hỗ trợ gì hôm nay?"
        }
        self.messages.append(welcome_msg)
        self.render_message(welcome_msg)
    
    def render_message(self, message):
        """Render a single message"""
        role = message.get("role", "user")
        content = message.get("content", "")
        timestamp = message.get("timestamp", datetime.now().strftime("%H:%M"))
        
        if role == "user":
            # User message (right aligned)
            msg_frame = ctk.CTkFrame(
                self.messages_frame,
                fg_color="#667eea",
                corner_radius=16
            )
            msg_frame.pack(anchor="e", pady=5, padx=(100, 10))
            
            content_label = ctk.CTkLabel(
                msg_frame,
                text=content,
                font=("Segoe UI", 12),
                text_color="#ffffff",
                wraplength=450,
                justify="right"
            )
            content_label.pack(padx=15, pady=10)
            
            time_label = ctk.CTkLabel(
                msg_frame,
                text=timestamp,
                font=("Segoe UI", 9),
                text_color="#e0e0ff"
            )
            time_label.pack(anchor="e", padx=15, pady=(0, 5))
        
        else:
            # AI message (left aligned)
            msg_frame = ctk.CTkFrame(
                self.messages_frame,
                fg_color="#ffffff",
                corner_radius=16,
                border_width=1,
                border_color="#e8e8e8"
            )
            msg_frame.pack(anchor="w", pady=5, padx=(10, 100))
            
            # Avatar
            avatar = ctk.CTkLabel(
                msg_frame,
                text="🤖",
                font=("Segoe UI Emoji", 16)
            )
            avatar.pack(anchor="w", padx=12, pady=(10, 0))
            
            content_label = ctk.CTkLabel(
                msg_frame,
                text=content,
                font=("Segoe UI", 12),
                text_color="#333333",
                wraplength=450,
                justify="left"
            )
            content_label.pack(anchor="w", padx=40, pady=(5, 0))
            
            time_label = ctk.CTkLabel(
                msg_frame,
                text=f"AI • {timestamp}",
                font=("Segoe UI", 9),
                text_color="#aaaaaa"
            )
            time_label.pack(anchor="w", padx=40, pady=(0, 8))
        
        # Scroll to bottom
        self.messages_frame._parent_canvas.yview_moveto(1.0)
    
    def send_message(self):
        """Send user message"""
        content = self.input_field.get("1.0", "end-1c").strip()
        
        if not content:
            return
        
        # Add user message
        user_msg = {
            "role": "user",
            "content": content,
            "timestamp": datetime.now().strftime("%H:%M")
        }
        self.messages.append(user_msg)
        self.render_message(user_msg)
        
        # Clear input
        self.input_field.delete("1.0", "end")
        
        # Simulate AI response (in real app, this would call the AI API)
        self.after(1000, lambda: self.add_ai_response(content))
    
    def add_ai_response(self, user_message):
        """Add AI response (mock)"""
        # Mock AI responses
        responses = [
            "Cảm ơn bạn đã hỏi! Để tôi giúp bạn về vấn đề này.\n\nDựa trên những gì bạn mô tả, tôi nghĩ bạn có thể tham khảo các bước sau:\n\n1. Tìm hiểu kỹ đề bài\n2. Phân tích yêu cầu cụ thể\n3. Lên kế hoạch giải quyết\n4. Thực hiện và kiểm tra lại\n\nBạn có muốn tôi giải thích chi tiết hơn không?",
            
            "Đây là một câu hỏi rất hay! Để tôi giúp bạn.\n\nTheo nghiên cứu, có một số phương pháp học tập hiệu quả bao gồm:\n\n📖 Học chủ động (Active Learning)\n⏰ Học phân tán (Spaced Repetition)\n🧠 Ôn tập bằng cách giảng lại\n✍️ Ghi chú bằng tay\n\nBạn muốn tìm hiểu thêm về phương pháp nào?",
            
            "Tôi hiểu bạn đang gặp khó khăn. Đừng lo lắng!\n\n💡 Mẹo: Hãy thử chia nhỏ vấn đề thành các phần nhỏ hơn và giải quyết từng phần một.\n\nNếu bạn cần hỗ trợ thêm, đừng ngại hỏi nhé!"
        ]
        
        import random
        ai_msg = {
            "role": "ai",
            "content": random.choice(responses),
            "timestamp": datetime.now().strftime("%H:%M")
        }
        self.messages.append(ai_msg)
        self.render_message(ai_msg)
    
    def send_quick_message(self, text):
        """Send a quick suggestion message"""
        self.input_field.insert("1.0", text)
        self.send_message()
    
    def new_chat(self):
        """Start a new chat"""
        # Clear messages
        self.messages.clear()
        
        # Clear display
        for widget in self.messages_frame.winfo_children():
            widget.destroy()
        
        # Add welcome message
        self.add_welcome_message()
    
    def refresh(self):
        """Refresh chat page"""
        pass
