"""
SmartStudy AI - Tasks Page
Trang quản lý công việc, bài tập
"""

import customtkinter as ctk
from datetime import datetime, timedelta


class TasksPage(ctk.CTkFrame):
    """Tasks management page"""
    
    def __init__(self, parent, app):
        super().__init__(parent)
        
        self.app = app
        self.filter = "all"  # "all", "today", "week", "completed"
        
        # Configure frame
        self.configure(
            fg_color="#f8f9fa",
            corner_radius=0
        )
        
        # Load data first
        self.load_tasks()
        
        self.create_widgets()
    
    def create_widgets(self):
        """Create tasks page widgets"""
        
        # ==================== HEADER ====================
        header = ctk.CTkFrame(
            self,
            fg_color="#ffffff",
            height=70,
            corner_radius=0
        )
        header.pack(fill="x")
        header.pack_propagate(False)
        
        # Page title
        title_label = ctk.CTkLabel(
            header,
            text="📝 Công việc",
            font=ctk.CTkFont(family="Segoe UI", size=24, weight="bold"),
            text_color="#333333"
        )
        title_label.pack(side="left", padx=25, pady=15)
        
        # Add task button
        add_btn = ctk.CTkButton(
            header,
            text="➕ Thêm công việc",
            width=160,
            height=40,
            fg_color="#667eea",
            hover_color="#764ba2",
            text_color="#ffffff",
            corner_radius=12,
            font=("Segoe UI", 13, "bold"),
            command=self.show_add_task_dialog
        )
        add_btn.pack(side="right", padx=25, pady=15)
        
        # ==================== FILTER SECTION ====================
        filter_frame = ctk.CTkFrame(self, fg_color="#f8f9fa")
        filter_frame.pack(fill="x", padx=25, pady=(20, 10))
        
        # Filter buttons
        self.filter_buttons = {}
        filters = [
            {"id": "all", "label": "Tất cả", "icon": "📋"},
            {"id": "today", "label": "Hôm nay", "icon": "📅"},
            {"id": "week", "label": "Tuần này", "icon": "📆"},
            {"id": "completed", "label": "Đã hoàn thành", "icon": "✅"}
        ]
        
        for i, f in enumerate(filters):
            btn = ctk.CTkButton(
                filter_frame,
                text=f"{f['icon']} {f['label']}",
                width=130,
                height=38,
                fg_color="#ffffff" if i > 0 else "#667eea",
                hover_color=("#667eea" if i > 0 else "#764ba2"),
                text_color=("#333333" if i > 0 else "#ffffff"),
                corner_radius=10,
                font=("Segoe UI", 12, "bold" if i == 0 else "normal"),
                command=lambda fid=f["id"]: self.set_filter(fid)
            )
            btn.pack(side="left", padx=(0, 10) if i < len(filters) - 1 else (0, 0))
            self.filter_buttons[f["id"]] = btn
        
        # Task count
        self.task_count_label = ctk.CTkLabel(
            filter_frame,
            text="",
            font=ctk.CTkFont(family="Segoe UI", size=12),
            text_color="#888888"
        )
        self.task_count_label.pack(side="right")
        
        # ==================== TASKS LIST ====================
        # Main content area
        content_frame = ctk.CTkFrame(self, fg_color="#f8f9fa")
        content_frame.pack(fill="both", expand=True, padx=25, pady=(10, 20))
        
        # Left column - Tasks list
        self.tasks_container = ctk.CTkScrollableFrame(
            content_frame,
            fg_color="transparent",
            scrollbar_button_color="#e0e0e0"
        )
        self.tasks_container.pack(side="left", fill="both", expand=True)
        
        # Right column - Stats panel
        stats_panel = ctk.CTkFrame(
            content_frame,
            fg_color="#ffffff",
            width=280,
            corner_radius=16
        )
        stats_panel.pack(side="right", fill="y", padx=(15, 0))
        stats_panel.pack_propagate(False)
        
        # Stats title
        stats_title = ctk.CTkLabel(
            stats_panel,
            text="📊 Thống kê",
            font=ctk.CTkFont(family="Segoe UI", size=16, weight="bold"),
            text_color="#333333"
        )
        stats_title.pack(anchor="w", padx=20, pady=(15, 15))
        
        # Stats content
        stats_content = ctk.CTkFrame(stats_panel, fg_color="transparent")
        stats_content.pack(fill="x", padx=20)
        
        # Total tasks
        self.total_label = self.create_stat_item(
            stats_content, "Tổng công việc", "📋", "#667eea", 0
        )
        
        # Completed tasks
        self.completed_label = self.create_stat_item(
            stats_content, "Đã hoàn thành", "✅", "#10b981", 1
        )
        
        # Pending tasks
        self.pending_label = self.create_stat_item(
            stats_content, "Đang chờ", "⏳", "#f59e0b", 2
        )
        
        # Overdue tasks
        self.overdue_label = self.create_stat_item(
            stats_content, "Quá hạn", "⚠️", "#ef4444", 3
        )
        
        # Progress section
        progress_frame = ctk.CTkFrame(stats_panel, fg_color="#f8f9fa", corner_radius=12)
        progress_frame.pack(fill="x", padx=20, pady=(20, 0))
        
        progress_title = ctk.CTkLabel(
            progress_frame,
            text="Tiến độ hoàn thành",
            font=ctk.CTkFont(family="Segoe UI", size=12, weight="bold"),
            text_color="#333333"
        )
        progress_title.pack(anchor="w", padx=15, pady=(12, 5))
        
        self.progress_bar = ctk.CTkProgressBar(
            progress_frame,
            width=220,
            height=10,
            progress_color="#667eea",
            fg_color="#e8e8e8",
            corner_radius=5
        )
        self.progress_bar.pack(padx=15, pady=(0, 10))
        self.progress_bar.set(0)
        
        self.progress_label = ctk.CTkLabel(
            progress_frame,
            text="0% hoàn thành",
            font=ctk.CTkFont(family="Segoe UI", size=11),
            text_color="#888888"
        )
        self.progress_label.pack(anchor="w", padx=15, pady=(0, 12))
    
    def create_stat_item(self, parent, label, icon, color, row):
        """Create a stat item"""
        frame = ctk.CTkFrame(parent, fg_color="transparent")
        frame.grid(row=row, column=0, pady=8, sticky="w")
        
        # Icon
        icon_lbl = ctk.CTkLabel(
            frame,
            text=icon,
            font=("Segoe UI Emoji", 20),
            width=35
        )
        icon_lbl.grid(row=0, column=0)
        
        # Label
        label_lbl = ctk.CTkLabel(
            frame,
            text=label,
            font=ctk.CTkFont(family="Segoe UI", size=12),
            text_color="#666666"
        )
        label_lbl.grid(row=0, column=1, padx=(10, 0))
        
        # Value
        value_lbl = ctk.CTkLabel(
            frame,
            text="0",
            font=ctk.CTkFont(family="Segoe UI", size=18, weight="bold"),
            text_color=color
        )
        value_lbl.grid(row=0, column=2, padx=(50, 0))
        
        return value_lbl
    
    def load_tasks(self):
        """Load tasks from app"""
        self.tasks = self.app.get_tasks().copy()
        # Only render if widgets are already created
        if hasattr(self, 'tasks_container'):
            self.render_tasks()
            self.update_stats()
    
    def render_tasks(self):
        """Render tasks list"""
        # Clear existing tasks
        for widget in self.tasks_container.winfo_children():
            widget.destroy()
        
        # Filter tasks
        filtered_tasks = self.filter_tasks()
        
        # Update count label
        self.task_count_label.configure(text=f"{len(filtered_tasks)} công việc")
        
        # Render tasks
        if not filtered_tasks:
            empty_label = ctk.CTkLabel(
                self.tasks_container,
                text="📭 Không có công việc nào",
                font=ctk.CTkFont(family="Segoe UI", size=14),
                text_color="#888888"
            )
            empty_label.pack(pady=50)
            return
        
        for task in filtered_tasks:
            self.add_task_item(task)
    
    def filter_tasks(self):
        """Filter tasks based on current filter"""
        if self.filter == "all":
            return self.tasks
        elif self.filter == "today":
            return [t for t in self.tasks if not t.get("completed")]
        elif self.filter == "week":
            return [t for t in self.tasks if not t.get("completed")]
        elif self.filter == "completed":
            return [t for t in self.tasks if t.get("completed")]
        return self.tasks
    
    def add_task_item(self, task):
        """Add a single task item to the list"""
        item = ctk.CTkFrame(
            self.tasks_container,
            fg_color="#ffffff",
            corner_radius=12,
            height=90
        )
        item.pack(fill="x", pady=8)
        item.pack_propagate(False)
        
        # Priority indicator
        priority_colors = {
            "high": "#ef4444",
            "medium": "#f59e0b",
            "low": "#10b981"
        }
        priority_color = priority_colors.get(task.get("priority", "medium"), "#888888")
        
        indicator = ctk.CTkFrame(
            item,
            width=5,
            fg_color=priority_color,
            corner_radius=3
        )
        indicator.place(x=0, y=15, relheight=0.7)
        
        # Checkbox
        var = ctk.BooleanVar(value=task.get("completed", False))
        checkbox = ctk.CTkCheckBox(
            item,
            variable=var,
            text="",
            width=30,
            fg_color="#667eea",
            hover_color="#764ba2",
            command=lambda t=task, v=var: self.toggle_task(t, v)
        )
        checkbox.place(x=20, y=35)
        
        # Task info
        info_frame = ctk.CTkFrame(item, fg_color="transparent")
        info_frame.place(x=60, y=12, relwidth=0.55, relheight=1)
        
        # Title
        title_color = "#aaaaaa" if task.get("completed") else "#333333"
        title_decoration = "✓ " if task.get("completed") else ""
        title = ctk.CTkLabel(
            info_frame,
            text=f"{title_decoration}{task.get('title', '')}",
            font=ctk.CTkFont(
                family="Segoe UI", 
                size=14, 
                weight="bold",
                overstrike=task.get("completed", False)
            ),
            text_color=title_color,
            anchor="w"
        )
        title.pack(anchor="w")
        
        # Subject and deadline
        details = f"📚 {task.get('subject', '')}  •  ⏰ {task.get('due_time', '')}"
        details_lbl = ctk.CTkLabel(
            info_frame,
            text=details,
            font=ctk.CTkFont(family="Segoe UI", size=11),
            text_color="#888888",
            anchor="w"
        )
        details_lbl.pack(anchor="w", pady=(5, 0))
        
        # Action buttons
        actions_frame = ctk.CTkFrame(item, fg_color="transparent")
        actions_frame.place(x=550, y=30)
        
        # Edit button
        edit_btn = ctk.CTkButton(
            actions_frame,
            text="✏️",
            width=35,
            height=35,
            fg_color="#f0f0f0",
            hover_color="#e8e8e8",
            text_color="#333333",
            corner_radius=8,
            font=("Segoe UI Emoji", 12),
            command=lambda t=task: self.edit_task(t)
        )
        edit_btn.pack(side="left", padx=3)
        
        # Delete button
        delete_btn = ctk.CTkButton(
            actions_frame,
            text="🗑️",
            width=35,
            height=35,
            fg_color="#fef2f2",
            hover_color="#fee2e2",
            text_color="#ef4444",
            corner_radius=8,
            font=("Segoe UI Emoji", 12),
            command=lambda t=task: self.delete_task(t)
        )
        delete_btn.pack(side="left", padx=3)
    
    def set_filter(self, filter_id):
        """Set task filter"""
        self.filter = filter_id
        
        # Update button styles
        for fid, btn in self.filter_buttons.items():
            if fid == filter_id:
                btn.configure(
                    fg_color="#667eea",
                    text_color="#ffffff",
                    font=("Segoe UI", 12, "bold")
                )
            else:
                btn.configure(
                    fg_color="#ffffff",
                    text_color="#333333",
                    font=("Segoe UI", 12)
                )
        
        self.render_tasks()
    
    def toggle_task(self, task, var):
        """Toggle task completion"""
        task["completed"] = var.get()
        self.render_tasks()
        self.update_stats()
    
    def delete_task(self, task):
        """Delete a task"""
        self.tasks = [t for t in self.tasks if t.get("id") != task.get("id")]
        self.render_tasks()
        self.update_stats()
    
    def edit_task(self, task):
        """Edit a task - show simple edit dialog"""
        dialog = ctk.CTkToplevel(self)
        dialog.title("Chỉnh sửa công việc")
        dialog.geometry("400x350")
        dialog.transient(self)
        dialog.grab_set()
        
        # Center dialog
        dialog.update_idletasks()
        x = (dialog.winfo_screenwidth() // 2) - (400 // 2)
        y = (dialog.winfo_screenheight() // 2) - (350 // 2)
        dialog.geometry(f"+{x}+{y}")
        
        # Title input
        title_label = ctk.CTkLabel(dialog, text="Tên công việc:", font=("Segoe UI", 12))
        title_label.pack(anchor="w", padx=30, pady=(20, 5))
        
        title_entry = ctk.CTkEntry(dialog, width=340, height=40, corner_radius=10)
        title_entry.insert(0, task.get("title", ""))
        title_entry.pack(padx=30, pady=(0, 15))
        
        # Subject input
        subject_label = ctk.CTkLabel(dialog, text="Môn học:", font=("Segoe UI", 12))
        subject_label.pack(anchor="w", padx=30, pady=(0, 5))
        
        subject_entry = ctk.CTkEntry(dialog, width=340, height=40, corner_radius=10)
        subject_entry.insert(0, task.get("subject", ""))
        subject_entry.pack(padx=30, pady=(0, 15))
        
        # Due time input
        time_label = ctk.CTkLabel(dialog, text="Giờ hạn:", font=("Segoe UI", 12))
        time_label.pack(anchor="w", padx=30, pady=(0, 5))
        
        time_entry = ctk.CTkEntry(dialog, width=340, height=40, corner_radius=10)
        time_entry.insert(0, task.get("due_time", ""))
        time_entry.pack(padx=30, pady=(0, 15))
        
        # Priority dropdown
        priority_label = ctk.CTkLabel(dialog, text="Mức độ ưu tiên:", font=("Segoe UI", 12))
        priority_label.pack(anchor="w", padx=30, pady=(0, 5))
        
        priority_combo = ctk.CTkOptionMenu(
            dialog,
            values=["Cao", "Trung bình", "Thấp"],
            width=340,
            height=40,
            corner_radius=10
        )
        priorities = {"high": "Cao", "medium": "Trung bình", "low": "Thấp"}
        current_priority = priorities.get(task.get("priority", "medium"), "Trung bình")
        priority_combo.set(current_priority)
        priority_combo.pack(padx=30, pady=(0, 20))
        
        # Buttons
        btn_frame = ctk.CTkFrame(dialog, fg_color="transparent")
        btn_frame.pack(pady=(0, 15))
        
        cancel_btn = ctk.CTkButton(
            btn_frame,
            text="Hủy",
            width=150,
            height=40,
            fg_color="#f0f0f0",
            text_color="#333333",
            corner_radius=10,
            command=dialog.destroy
        )
        cancel_btn.pack(side="left", padx=10)
        
        save_btn = ctk.CTkButton(
            btn_frame,
            text="Lưu",
            width=150,
            height=40,
            fg_color="#667eea",
            hover_color="#764ba2",
            text_color="#ffffff",
            corner_radius=10,
            command=lambda: self.save_task_edit(
                dialog, task, title_entry.get(), subject_entry.get(),
                time_entry.get(), priority_combo.get()
            )
        )
        save_btn.pack(side="left", padx=10)
    
    def save_task_edit(self, dialog, task, title, subject, time, priority):
        """Save task edit"""
        priorities = {"Cao": "high", "Trung bình": "medium", "Thấp": "low"}
        
        task["title"] = title
        task["subject"] = subject
        task["due_time"] = time
        task["priority"] = priorities.get(priority, "medium")
        
        dialog.destroy()
        self.render_tasks()
        self.update_stats()
    
    def show_add_task_dialog(self):
        """Show add task dialog"""
        dialog = ctk.CTkToplevel(self)
        dialog.title("Thêm công việc mới")
        dialog.geometry("400x400")
        dialog.transient(self)
        dialog.grab_set()
        
        # Center dialog
        dialog.update_idletasks()
        x = (dialog.winfo_screenwidth() // 2) - (400 // 2)
        y = (dialog.winfo_screenheight() // 2) - (400 // 2)
        dialog.geometry(f"+{x}+{y}")
        
        # Title input
        title_label = ctk.CTkLabel(dialog, text="Tên công việc:", font=("Segoe UI", 12))
        title_label.pack(anchor="w", padx=30, pady=(20, 5))
        
        title_entry = ctk.CTkEntry(dialog, width=340, height=40, corner_radius=10)
        title_entry.pack(padx=30, pady=(0, 15))
        
        # Subject input
        subject_label = ctk.CTkLabel(dialog, text="Môn học:", font=("Segoe UI", 12))
        subject_label.pack(anchor="w", padx=30, pady=(0, 5))
        
        subject_entry = ctk.CTkEntry(dialog, width=340, height=40, corner_radius=10)
        subject_entry.pack(padx=30, pady=(0, 15))
        
        # Due time input
        time_label = ctk.CTkLabel(dialog, text="Giờ hạn:", font=("Segoe UI", 12))
        time_label.pack(anchor="w", padx=30, pady=(0, 5))
        
        time_entry = ctk.CTkEntry(dialog, width=340, height=40, corner_radius=10)
        time_entry.insert(0, "23:59")
        time_entry.pack(padx=30, pady=(0, 15))
        
        # Priority dropdown
        priority_label = ctk.CTkLabel(dialog, text="Mức độ ưu tiên:", font=("Segoe UI", 12))
        priority_label.pack(anchor="w", padx=30, pady=(0, 5))
        
        priority_combo = ctk.CTkOptionMenu(
            dialog,
            values=["Cao", "Trung bình", "Thấp"],
            width=340,
            height=40,
            corner_radius=10
        )
        priority_combo.set("Trung bình")
        priority_combo.pack(padx=30, pady=(0, 20))
        
        # Buttons
        btn_frame = ctk.CTkFrame(dialog, fg_color="transparent")
        btn_frame.pack(pady=(0, 15))
        
        cancel_btn = ctk.CTkButton(
            btn_frame,
            text="Hủy",
            width=150,
            height=40,
            fg_color="#f0f0f0",
            text_color="#333333",
            corner_radius=10,
            command=dialog.destroy
        )
        cancel_btn.pack(side="left", padx=10)
        
        add_btn = ctk.CTkButton(
            btn_frame,
            text="Thêm",
            width=150,
            height=40,
            fg_color="#667eea",
            hover_color="#764ba2",
            text_color="#ffffff",
            corner_radius=10,
            command=lambda: self.add_task(
                dialog, title_entry.get(), subject_entry.get(),
                time_entry.get(), priority_combo.get()
            )
        )
        add_btn.pack(side="left", padx=10)
    
    def add_task(self, dialog, title, subject, time, priority):
        """Add a new task"""
        if not title:
            return
        
        priorities = {"Cao": "high", "Trung bình": "medium", "Thấp": "low"}
        
        new_task = {
            "id": max([t.get("id", 0) for t in self.tasks], default=0) + 1,
            "title": title,
            "subject": subject,
            "due_time": time,
            "priority": priorities.get(priority, "medium"),
            "completed": False
        }
        
        self.tasks.append(new_task)
        dialog.destroy()
        self.render_tasks()
        self.update_stats()
    
    def update_stats(self):
        """Update statistics panel"""
        total = len(self.tasks)
        completed = len([t for t in self.tasks if t.get("completed")])
        pending = total - completed
        overdue = 0  # Mock - can be calculated based on due dates
        
        self.total_label.configure(text=str(total))
        self.completed_label.configure(text=str(completed))
        self.pending_label.configure(text=str(pending))
        self.overdue_label.configure(text=str(overdue))
        
        # Update progress bar
        if total > 0:
            progress = completed / total
            self.progress_bar.set(progress)
            self.progress_label.configure(text=f"{int(progress * 100)}% hoàn thành")
    
    def refresh(self):
        """Refresh tasks"""
        self.load_tasks()
