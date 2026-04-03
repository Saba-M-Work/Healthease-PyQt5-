import sys
import random
from PyQt5.QtGui import QFont, QColor, QIcon
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QFrame,
QLabel, QPushButton, QLineEdit, QStackedWidget, QScrollArea,
    QCalendarWidget, QTimeEdit, QMessageBox, QDialog, QGraphicsDropShadowEffect,
    QButtonGroup, QCheckBox, QGridLayout
)
from PyQt5.QtCore import Qt, QDate, QTime
from PyQt5.QtGui import QFont, QColor

class HealtheaseApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Healthease - Doctor Booking Platform")
        self.setWindowIcon(QIcon('HEALTHEASE-LOGO.png'))
        self.resize(1280, 720)
        self.appointments_tracker = {}
        self.selected_doctor = ""
        self.doctors = [
            ("Dr. Sarah Ali", "Cardiology", "Mon-Fri: 9AM - 5PM", "Heart specialist"),
            ("Dr. Ahmed Ali", "Pediatrics", "Mon-Sat: 10AM - 6PM", "Child care expert"),
            ("Dr. Shaan Saif", "Dermatology", "Tue-Sat: 11AM - 7PM", "Skin specialist"),
            ("Dr. Kamran Zaffar", "Neurology", "Mon-Fri: 8AM - 4PM", "Brain & nerve specialist"),
            ("Dr. Fatima Khan", "Cardiology", "Mon-Thu: 9AM - 3PM", "Senior heart consultant"),
            ("Dr. Bilal Ahmed", "Pediatrics", "Mon-Sat: 2PM - 8PM", "Neonatal specialist"),
            ("Dr. Ayesha Malik", "Dermatology", "Wed-Sun: 10AM - 5PM", "Cosmetic dermatology"),
            ("Dr. Omar Farooq", "Neurology", "Mon-Fri: 1PM - 8PM", "Stroke & migraine expert"),
            ("Dr. Zainab Hussain", "Orthopedics", "Mon-Fri: 10AM - 6PM", "Joint specialist"),
            ("Dr. Ali Raza", "General", "Mon-Sun: 8AM - 8PM", "Family physician"),
        ]

        self.stacked = QStackedWidget()
        self.setCentralWidget(self.stacked)

        self.login_page = self.create_login_page()
        self.home_page = self.create_home_page()
        self.standard_page = self.create_standard_booking_page()
        self.emergency_page = self.create_emergency_page()  # Now properly defined

        self.stacked.addWidget(self.login_page)
        self.stacked.addWidget(self.home_page)
        self.stacked.addWidget(self.standard_page)
        self.stacked.addWidget(self.emergency_page)

        self.stacked.setCurrentIndex(0)

    # ==================== LOGIN / SIGN UP PAGE ====================
    def create_login_page(self):
     
        widget = QWidget()
        main_layout = QHBoxLayout(widget)
        main_layout.setContentsMargins(0, 0, 0, 0)

        auth_stack = QStackedWidget()

        # Login Screen
        login_widget = QWidget()
        login_layout = QHBoxLayout(login_widget)

        left = QWidget()
        left.setStyleSheet("background-color: white;")
        left_layout = QVBoxLayout(left)
        left_layout.setAlignment(Qt.AlignCenter)
        left_layout.setSpacing(20)
        left_layout.setContentsMargins(120, 120, 120, 120)

        title = QLabel("Login To Your Account")
        title.setFont(QFont("Arial", 22, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        left_layout.addWidget(title)

        email = QLineEdit()
        email.setPlaceholderText("Email")
        email.setFixedSize(400, 50)
        email.setStyleSheet("border-radius: 25px; padding-left: 20px; background: #f5f5f5; font-size: 14px;")
        left_layout.addWidget(email)

        password = QLineEdit()
        password.setPlaceholderText("Password")
        password.setEchoMode(QLineEdit.Password)
        password.setFixedSize(400, 50)
        password.setStyleSheet("border-radius: 25px; padding-left: 20px; background: #f5f5f5; font-size: 14px;")
        left_layout.addWidget(password)

        signin = QPushButton("Sign in")
        signin.setFixedSize(400, 50)
        signin.setStyleSheet("background: #007bff; color: white; border-radius: 25px; font-size: 14px; font-weight: bold;")
        signin.clicked.connect(lambda: self.stacked.setCurrentIndex(1))
        left_layout.addWidget(signin)

        right = QWidget()
        right.setStyleSheet("background-color: #007bff;")
        right_layout = QVBoxLayout(right)
        right_layout.setAlignment(Qt.AlignCenter)
        right_layout.setSpacing(25)

        new = QLabel("New Here?")
        new.setFont(QFont("Arial", 26, QFont.Bold))
        new.setStyleSheet("color: white;")
        right_layout.addWidget(new)

        desc = QLabel("Sign up and discover a great healthcare experience")
        desc.setFont(QFont("Arial", 12))
        desc.setStyleSheet("color: white;")
        desc.setAlignment(Qt.AlignCenter)
        right_layout.addWidget(desc)

        signup = QPushButton("Sign up")
        signup.setFixedSize(200, 50)
        signup.setStyleSheet("background: white; color: #007bff; border-radius: 25px; font-size: 14px;")
        signup.clicked.connect(lambda: auth_stack.setCurrentIndex(1))
        right_layout.addWidget(signup)

        login_layout.addWidget(left, 1)
        login_layout.addWidget(right, 1)

        # Register Screen
        register_widget = QWidget()
        reg_layout = QHBoxLayout(register_widget)

        reg_left = QWidget()
        reg_left.setStyleSheet("background-color: #007bff;")
        reg_left_layout = QVBoxLayout(reg_left)
        reg_left_layout.setAlignment(Qt.AlignCenter)
        reg_left_layout.setSpacing(25)

        welcome = QLabel("Welcome Back!")
        welcome.setFont(QFont("Arial", 26, QFont.Bold))
        welcome.setStyleSheet("color: white;")
        reg_left_layout.addWidget(welcome)

        reg_desc = QLabel("To keep connected with us please\nlogin with your personal info")
        reg_desc.setFont(QFont("Arial", 12))
        reg_desc.setStyleSheet("color: white;")
        reg_desc.setAlignment(Qt.AlignLeft)
        reg_left_layout.addWidget(reg_desc)

        signin_back = QPushButton("Sign In")
        signin_back.setFixedSize(200, 50)
        signin_back.setStyleSheet("background: white; color: #007bff; border-radius: 25px; font-size: 14px;")
        signin_back.clicked.connect(lambda: auth_stack.setCurrentIndex(0))
        reg_left_layout.addWidget(signin_back)

        reg_right = QWidget()
        reg_right.setStyleSheet("background-color: white;")
        reg_right_layout = QVBoxLayout(reg_right)
        reg_right_layout.setAlignment(Qt.AlignCenter)
        reg_right_layout.setSpacing(20)
        reg_right_layout.setContentsMargins(120, 120, 120, 120)

        reg_title = QLabel("Create Account")
        reg_title.setFont(QFont("Arial", 22, QFont.Bold))
        reg_right_layout.addWidget(reg_title)

        first_name = QLineEdit()
        first_name.setPlaceholderText("First Name")
        first_name.setFixedSize(400, 50)
        first_name.setStyleSheet("border-radius: 25px; padding-left: 20px; background: #f5f5f5; font-size: 14px;")
        reg_right_layout.addWidget(first_name)

        last_name = QLineEdit()
        last_name.setPlaceholderText("Last Name")
        last_name.setFixedSize(400, 50)
        last_name.setStyleSheet("border-radius: 25px; padding-left: 20px; background: #f5f5f5; font-size: 14px;")
        reg_right_layout.addWidget(last_name)

        email_reg = QLineEdit()
        email_reg.setPlaceholderText("Email")
        email_reg.setFixedSize(400, 50)
        email_reg.setStyleSheet("border-radius: 25px; padding-left: 20px; background: #f5f5f5; font-size: 14px;")
        reg_right_layout.addWidget(email_reg)

        password_reg = QLineEdit()
        password_reg.setPlaceholderText("Password")
        password_reg.setEchoMode(QLineEdit.Password)
        password_reg.setFixedSize(400, 50)
        password_reg.setStyleSheet("border-radius: 25px; padding-left: 20px; background: #f5f5f5; font-size: 14px;")
        reg_right_layout.addWidget(password_reg)

        retype_password = QLineEdit()
        retype_password.setPlaceholderText("Retype Password")
        retype_password.setEchoMode(QLineEdit.Password)
        retype_password.setFixedSize(400, 50)
        retype_password.setStyleSheet("border-radius: 25px; padding-left: 20px; background: #f5f5f5; font-size: 14px;")
        reg_right_layout.addWidget(retype_password)

        instructions = QLabel(
            "Password must be at least 8 characters long\n"
            "and include uppercase, lowercase, number, and special character."
        )
        instructions.setFont(QFont("Arial", 10))
        instructions.setStyleSheet("color: #666;")
        instructions.setAlignment(Qt.AlignLeft)
        reg_right_layout.addWidget(instructions)

        final_signup = QPushButton("Sign up")
        final_signup.setFixedSize(400, 50)
        final_signup.setStyleSheet("background: #007bff; color: white; border-radius: 25px; font-size: 14px; font-weight: bold;")
        final_signup.clicked.connect(lambda: self.stacked.setCurrentIndex(1))
        reg_right_layout.addWidget(final_signup)

        reg_layout.addWidget(reg_left, 1)
        reg_layout.addWidget(reg_right, 1)

        auth_stack.addWidget(login_widget)
        auth_stack.addWidget(register_widget)

        main_layout.addWidget(auth_stack)
        return widget

    # ====================HOME PAGE====================
    def create_home_page(self):
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("border: none;")
        content = QWidget()
        content_layout = QVBoxLayout(content)

        header = QWidget()
        header.setStyleSheet("background-color: #007bff;")
        header.setFixedHeight(70)
        h_layout = QHBoxLayout(header)
        h_layout.setContentsMargins(60, 0, 60, 0)

        logo = QLabel("Healthease")
        logo.setFont(QFont("Arial", 22, QFont.Bold))
        logo.setStyleSheet("color: white;")
        h_layout.addWidget(logo)
        h_layout.addStretch()

        logout = QPushButton("Log out")
        logout.setFixedSize(110, 40)
        logout.setStyleSheet("background: white; color: #007bff; border-radius: 20px; font-weight: bold; font-size: 12px;")
        logout.clicked.connect(lambda: self.stacked.setCurrentIndex(0))
        h_layout.addWidget(logout)

        content_layout.addWidget(header)

        hero = QWidget()
        hero.setStyleSheet("background-color: #007bff;")
        hero.setFixedHeight(300)
        hero_layout = QVBoxLayout(hero)
        hero_layout.setAlignment(Qt.AlignCenter)
        hero_layout.setSpacing(15)

        welcome = QLabel("Welcome to Healthease")
        welcome.setFont(QFont("Arial", 34, QFont.Bold))
        welcome.setStyleSheet("color: white;")
        hero_layout.addWidget(welcome)

        tagline = QLabel("Your trusted hospital doctor booking platform")
        tagline.setFont(QFont("Arial", 14))
        tagline.setStyleSheet("color: white;")
        hero_layout.addWidget(tagline)

        desc = QLabel("Book appointments with experienced doctors anytime, anywhere.\nFast, secure, and hassle-free healthcare at your fingertips.")
        desc.setFont(QFont("Arial", 10))
        desc.setStyleSheet("color: white;")
        desc.setAlignment(Qt.AlignCenter)
        hero_layout.addWidget(desc)

        content_layout.addWidget(hero)

        white = QWidget()
        white.setStyleSheet("background-color: #f8f9fa; border-top-left-radius: 50px; border-top-right-radius: 50px;")
        white_layout = QVBoxLayout(white)
        white_layout.setContentsMargins(100, 60, 100, 100)
        white_layout.setSpacing(40)

        why = QLabel("Why Choose Healthease?")
        why.setFont(QFont("Arial", 26, QFont.Bold))
        why.setAlignment(Qt.AlignCenter)
        white_layout.addWidget(why)

        sub = QLabel("Smart Healthcare. Simplified Booking.")
        sub.setFont(QFont("Arial", 14))
        sub.setAlignment(Qt.AlignCenter)
        white_layout.addWidget(sub)

        cards_container = QHBoxLayout()
        cards_container.addStretch()
        cards = QHBoxLayout()
        cards.setSpacing(50)

        std_card = QWidget()
        std_card.setFixedSize(400, 300)
        std_card.setStyleSheet("background-color: #e3f2fd; border-radius: 25px;")
        std_v = QVBoxLayout(std_card)
        std_v.setContentsMargins(25, 25, 25, 25)
        std_v.setSpacing(15)

        std_title = QLabel("Standard Booking")
        std_title.setFont(QFont("Arial", 18, QFont.Bold))
        std_title.setAlignment(Qt.AlignCenter)
        std_v.addWidget(std_title)

        std_desc = QLabel("For routine checkups and consultations.\nSchedule with qualified doctors at your convenience.")
        std_desc.setWordWrap(True)
        std_desc.setFont(QFont("Arial", 11))
        std_desc.setAlignment(Qt.AlignCenter)
        std_v.addWidget(std_desc)

        book_std = QPushButton("Book now")
        book_std.setFixedSize(200, 45)
        book_std.setStyleSheet("background-color: #007bff; color: white; border-radius: 22px; font-size: 14px; font-weight: bold;")
        book_std.clicked.connect(lambda: self.stacked.setCurrentIndex(2))
        std_v.addStretch()
        std_v.addWidget(book_std, alignment=Qt.AlignCenter)
        cards.addWidget(std_card)

        em_card = QWidget()
        em_card.setFixedSize(400, 300)
        em_card.setStyleSheet("background-color: #ffebee; border-radius: 25px;")
        em_v = QVBoxLayout(em_card)
        em_v.setContentsMargins(25, 25, 25, 25)
        em_v.setSpacing(15)

        em_title = QLabel("Emergency")
        em_title.setFont(QFont("Arial", 18, QFont.Bold))
        em_title.setAlignment(Qt.AlignCenter)
        em_v.addWidget(em_title)

        em_desc = QLabel("For urgent medical needs requiring immediate attention.\nGet priority access to doctors during emergencies.")
        em_desc.setWordWrap(True)
        em_desc.setFont(QFont("Arial", 11))
        em_desc.setAlignment(Qt.AlignCenter)
        em_v.addWidget(em_desc)

        book_em = QPushButton("Book now")
        book_em.setFixedSize(200, 45)
        book_em.setStyleSheet("background-color: #007bff; color: white; border-radius: 22px; font-size: 14px; font-weight: bold;")
        book_em.clicked.connect(lambda: self.stacked.setCurrentIndex(3))
        em_v.addStretch()
        em_v.addWidget(book_em, alignment=Qt.AlignCenter)
        cards.addWidget(em_card)

        cards_container.addLayout(cards)
        cards_container.addStretch()
        white_layout.addLayout(cards_container)
        content_layout.addWidget(white)
        scroll.setWidget(content)
        layout.addWidget(scroll)
        return widget

    # ==================== STANDARD BOOKING PAGE ====================
    def create_standard_booking_page(self):
        

        main_widget = QWidget()
        main_widget.setStyleSheet("background-color: #FDFDFD;")
        layout = QVBoxLayout(main_widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # Navbar
        navbar = QFrame()
        navbar.setFixedHeight(60)
        navbar.setStyleSheet("background-color: white; border-bottom: 1px solid #EDEDED;")
        nav_layout = QHBoxLayout(navbar)
        nav_layout.setContentsMargins(30, 0, 30, 0)

        back_btn = QPushButton("← Go Back")
        back_btn.setFixedSize(120, 35)
        back_btn.setStyleSheet("""
            QPushButton {
                border: 1px solid #DDD; border-radius: 6px; font-size: 13px; font-weight: 600; color: #444;
            }
            QPushButton:hover { background-color: #F0F0F0; }
        """)
        back_btn.clicked.connect(lambda: self.stacked.setCurrentIndex(1))
        nav_layout.addWidget(back_btn)
        nav_layout.addStretch()
        layout.addWidget(navbar)

        content_scroll = QScrollArea()
        content_scroll.setWidgetResizable(True)
        content_scroll.setStyleSheet("border: none;")

        container = QWidget()
        c_layout = QVBoxLayout(container)
        c_layout.setContentsMargins(50, 30, 50, 40)
        c_layout.setSpacing(30)

        search_box = QLineEdit()
        search_box.setPlaceholderText("Search doctor by name...")
        search_box.setFixedSize(700, 60)
        search_box.setStyleSheet("""
            QLineEdit {
                background: white; 
                border: 2px solid #CCC; 
                border-radius: 30px;
                padding-left: 25px; 
                padding-right: 25px;
                font-size: 18px;
            }
            QLineEdit:focus {
                border-color: #007bff;
                background: #f8fdff;
            }
        """)
        search_box.textChanged.connect(self.filter_doctors_by_name)
        c_layout.addWidget(search_box, alignment=Qt.AlignCenter)

        cat_header = QLabel("BROWSE BY DEPARTMENT")
        cat_header.setStyleSheet("color: #666; font-size: 13px; font-weight: 800; letter-spacing: 2px;")
        c_layout.addWidget(cat_header, alignment=Qt.AlignCenter)

        spec_scroll = QScrollArea()
        spec_scroll.setFixedHeight(220)
        spec_scroll.setWidgetResizable(True)
        spec_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        spec_scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        spec_scroll.setStyleSheet("background: transparent; border: none;")

        spec_content = QWidget()
        spec_h_layout = QHBoxLayout(spec_content)
        spec_h_layout.setAlignment(Qt.AlignCenter)
        spec_h_layout.setContentsMargins(20, 20, 20, 20)
        spec_h_layout.setSpacing(20)

        specialties = [
            ("Cardiology", "#EBF5FF", "#2563EB"),
            ("Pediatrics", "#F0FDF4", "#16A34A"),
            ("Dermatology", "#FFF7ED", "#EA580C"),
            ("Neurology", "#FAF5FF", "#9333EA"),
            ("Orthopedics", "#FEF2F2", "#DC2626"),
            ("General", "#F8FAFC", "#475569")
        ]

        for name, bg_color, text_color in specialties:
            btn = QPushButton(name)
            btn.setFixedSize(280, 160)
            btn.setCursor(Qt.PointingHandCursor)
            btn.setStyleSheet(f"""
                QPushButton {{
                    background-color: {bg_color};
                    color: {text_color};
                    border: 4px solid {text_color};
                    border-radius: 24px;
                    font-weight: 900;
                    font-size: 22px;
                }}
                QPushButton:hover {{
                    background-color: {text_color};
                    color: white;
                }}
            """)
            btn.clicked.connect(lambda checked, n=name: self.filter_doctors_by_specialty(n))
            spec_h_layout.addWidget(btn)

        spec_scroll.setWidget(spec_content)
        c_layout.addWidget(spec_scroll)

        res_header = QLabel("Available Physicians")
        res_header.setStyleSheet("color: #1E293B; font-size: 24px; font-weight: 800;")
        c_layout.addWidget(res_header, alignment=Qt.AlignCenter)

        self.results_layout = QVBoxLayout()
        self.results_layout.setSpacing(18)
        self.results_layout.setContentsMargins(30, 20, 30, 30)
        c_layout.addLayout(self.results_layout)

        self.display_all_doctors()

        c_layout.addStretch()
        content_scroll.setWidget(container)
        layout.addWidget(content_scroll)

        return main_widget

    # ==================== DOCTOR CARD & FILTERING ====================
    def display_all_doctors(self):
        self.clear_doctor_cards()
        self.add_doctor_cards(self.doctors)

    def filter_doctors_by_specialty(self, specialty):
        self.clear_doctor_cards()
        filtered = [d for d in self.doctors if d[1] == specialty]
        self.add_doctor_cards(filtered)

    def filter_doctors_by_name(self, text):
        self.clear_doctor_cards()
        query = text.strip().lower()
        if not query:
            self.display_all_doctors()
            return
        filtered = [d for d in self.doctors if query in d[0].lower()]
        self.add_doctor_cards(filtered)

    def clear_doctor_cards(self):
        while self.results_layout.count():
            child = self.results_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def add_doctor_cards(self, doctor_list):
        for n, s, avail, _ in doctor_list:
            card = QFrame()
            card.setFixedHeight(120)
            card.setCursor(Qt.PointingHandCursor)
            card.setStyleSheet("""
                QFrame {
                    background: white;
                    border: 1px solid #E2E8F0;
                    border-radius: 15px;
                }
                QFrame:hover {
                    border: 2px solid #2563EB;
                    background: #F8FAFC;
                }
            """)

            shadow = QGraphicsDropShadowEffect()
            shadow.setBlurRadius(15)
            shadow.setXOffset(0)
            shadow.setYOffset(4)
            shadow.setColor(QColor(0, 0, 0, 25))
            card.setGraphicsEffect(shadow)

            cl = QHBoxLayout(card)
            cl.setContentsMargins(20, 10, 20, 10)
            cl.setSpacing(15)

            # Avatar
            name_parts = n.replace("Dr. ", "").split()
            initials = "".join([p[0] for p in name_parts])[:2].upper()

            avatar = QLabel(initials)
            avatar.setFixedSize(55, 55)
            avatar.setAlignment(Qt.AlignCenter)
            avatar.setStyleSheet("""
                QLabel {
                    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #2563EB, stop:1 #1D4ED8);
                    color: white;
                    border-radius: 27px;
                    font-size: 16px;
                    font-weight: 800;
                    border: none;
                }
            """)
            cl.addWidget(avatar)

            # Info Section
            info_layout = QVBoxLayout()
            info_layout.setSpacing(2)

            # Specialty Tag (no border)
            specialty_tag = QLabel(s.upper())
            specialty_tag.setStyleSheet("""
                QLabel {
                    color: #2563EB;
                    background: #EFF6FF;
                    padding: 4px 12px;
                    border-radius: 6px;
                    font-size: 10px; 
                    font-weight: 800;
                    letter-spacing: 1px;
                    border: none;   /* Explicitly no border */
                }
            """)
            info_layout.addWidget(specialty_tag, alignment=Qt.AlignLeft)

            # Doctor Name (no border)
            name_label = QLabel(n)
            name_label.setFont(QFont("Segoe UI", 13, QFont.Bold))
            name_label.setStyleSheet("""
                color: #1E293B;
                border: none;
                background: transparent;
            """)
            info_layout.addWidget(name_label)

            # Availability (no border)
            avail_layout = QHBoxLayout()
            avail_layout.setSpacing(5)
            dot = QLabel("●")
            dot.setStyleSheet("color: #22C55E; font-size: 10px; border: none;")
            
            avail_label = QLabel(avail)
            avail_label.setFont(QFont("Segoe UI", 9))
            avail_label.setStyleSheet("""
                color: #64748B;
                border: none;
                background: transparent;
            """)
            
            avail_layout.addWidget(dot)
            avail_layout.addWidget(avail_label)
            avail_layout.addStretch()
            info_layout.addLayout(avail_layout)

            cl.addLayout(info_layout)
            cl.addStretch()

            # Book Button
            book_btn = QPushButton("Book Visit")
            book_btn.setFixedSize(130, 40)
            book_btn.setCursor(Qt.PointingHandCursor)
            book_btn.setStyleSheet("""
                QPushButton {
                    background: #2563EB;
                    color: white;
                    border-radius: 10px;
                    font-size: 12px;
                    font-weight: 700;
                    border: none;
                }
                QPushButton:hover { background: #1D4ED8; }
            """)
            book_btn.clicked.connect(lambda checked=False, doc=n: self.show_appointment_dialog(doc))
            cl.addWidget(book_btn, alignment=Qt.AlignVCenter)

            self.results_layout.addWidget(card)

    # ==================== APPOINTMENT DIALOG ====================
        # ==================== "WHICH TIME WORKS BEST?" STYLE UI ====================
    def show_appointment_dialog(self, doctor_name):
        self.selected_doctor = doctor_name

        dialog = QDialog(self)
        dialog.setWindowTitle(f"Book Appointment - {doctor_name}")
        dialog.resize(620, 800)
        dialog.setStyleSheet("background: #f9fafb;")

        main_layout = QVBoxLayout(dialog)
        main_layout.setContentsMargins(40, 40, 40, 40)
        main_layout.setSpacing(25)

        # Title
        title = QLabel("Which time works best?")
        title.setFont(QFont("Segoe UI", 20, QFont.Bold))
        title.setStyleSheet("color: #1e293b;")
        main_layout.addWidget(title)

        # Week Selector Card
        week_card = QFrame()
        week_card.setStyleSheet("""
            QFrame {
                background: white;
                border-radius: 20px;
                border: 1px solid #e2e8f0;
            }
        """)
        week_layout = QVBoxLayout(week_card)
        week_layout.setContentsMargins(25, 20, 25, 20)
        week_layout.setSpacing(15)

        # Top bar with "Today" button
        top_bar = QHBoxLayout()
        top_bar.addStretch()

        today_btn = QPushButton("Today")
        today_btn.setFixedSize(90, 36)
        today_btn.setStyleSheet("""
            QPushButton {
                background: #f1f5f9;
                color: #475569;
                border-radius: 18px;
                font-size: 13px;
                font-weight: 600;
                border: none;
            }
            QPushButton:hover {
                background: #e2e8f0;
            }
        """)
        top_bar.addWidget(today_btn)
        week_layout.addLayout(top_bar)

        # Horizontal days grid
        days_layout = QHBoxLayout()
        days_layout.setSpacing(15)

        today = QDate.currentDate()
        # Start from Monday of this week
        start_date = today.addDays(1 - today.dayOfWeek())  # Monday = 1

        self.day_buttons = []
        self.selected_date = today  # Default selected

        for i in range(7):
            date = start_date.addDays(i)
            day_name = date.toString("ddd").upper()
            day_num = date.toString("d")

            day_btn = QPushButton(f"{day_name}\n{day_num}")
            day_btn.setFixedSize(80, 80)
            day_btn.setCheckable(True)
            day_btn.setStyleSheet("""
                QPushButton {
                    background: transparent;
                    color: #64748b;
                    border: none;
                    border-radius: 40px;
                    font-size: 12px;
                    text-align: center;
                }
                QPushButton:checked {
                    background: #2563eb;
                    color: white;
                    font-weight: bold;
                }
                QPushButton:hover:!checked {
                    background: #f1f5f9;
                }
            """)

            if date == today:
                day_btn.setChecked(True)

            day_btn.clicked.connect(lambda checked, d=date, btn=day_btn: self.select_day(d, btn, self.day_buttons, today_btn))
            days_layout.addWidget(day_btn)
            self.day_buttons.append(day_btn)

        # Connect "Today" button
        today_btn.clicked.connect(lambda: self.select_day(today, self.day_buttons[today.dayOfWeek() - 1], self.day_buttons, today_btn))

        week_layout.addLayout(days_layout)
        main_layout.addWidget(week_card)

        # Time Slots Header
        time_header = QLabel("Available time slots")
        time_header.setFont(QFont("Segoe UI", 14))
        time_header.setStyleSheet("color: #475569;")
        main_layout.addWidget(time_header)

        # Time Slots Scroll Area
        self.time_scroll = QScrollArea()
        self.time_scroll.setWidgetResizable(True)
        self.time_scroll.setFixedHeight(320)
        self.time_scroll.setStyleSheet("border: none; background: transparent;")

        self.time_container = QWidget()
        self.time_grid = QGridLayout(self.time_container)
        self.time_grid.setSpacing(12)
        self.time_grid.setContentsMargins(0, 0, 0, 20)

        self.time_group = QButtonGroup(dialog)
        self.time_group.setExclusive(True)

        self.time_scroll.setWidget(self.time_container)
        main_layout.addWidget(self.time_scroll)

        # Load initial time slots
        self.update_time_slots(today)

        # Bottom Buttons
        btn_layout = QHBoxLayout()
        cancel_btn = QPushButton("Cancel")
        cancel_btn.setFixedHeight(50)
        cancel_btn.setStyleSheet("""
            background: white;
            border: 1px solid #cbd5e1;
            border-radius: 12px;
            color: #475569;
            font-weight: 600;
            font-size: 14px;
        """)
        cancel_btn.clicked.connect(dialog.reject)

        confirm_btn = QPushButton("Confirm Booking")
        confirm_btn.setFixedHeight(50)
        confirm_btn.setStyleSheet("""
            background: #2563eb;
            color: white;
            border-radius: 12px;
            font-weight: bold;
            font-size: 14px;
        """)
        confirm_btn.clicked.connect(lambda: self.confirm_selected_time(dialog))

        btn_layout.addWidget(cancel_btn)
        btn_layout.addWidget(confirm_btn)
        main_layout.addLayout(btn_layout)

        dialog.exec_()

    def select_day(self, date, clicked_btn, all_buttons, today_btn):
        self.selected_date = date
        for btn in all_buttons:
            btn.setChecked(btn == clicked_btn)
        self.update_time_slots(date)

    def update_time_slots(self, date):
        # Clear previous slots
        for i in reversed(range(self.time_grid.count())):
            widget = self.time_grid.itemAt(i).widget()
            if widget:
                widget.setParent(None)

        self.time_group = QButtonGroup(self)
        self.time_group.setExclusive(True)

        start_time = QTime(9, 0)
        row, col = 0, 0
        for i in range(18):
            slot_time = start_time.addSecs(i * 1800)  # 30 min intervals
            time_str = slot_time.toString("h:mm AP")

            key = (self.selected_doctor, date.toString("yyyy-MM-dd"), time_str)
            booked = self.appointments_tracker.get(key, 0)
            is_full = booked >= 3

            btn = QPushButton(time_str)
            btn.setFixedSize(150, 50)
            btn.setCheckable(True)
            btn.setCursor(Qt.PointingHandCursor)

            if is_full:
                btn.setEnabled(False)
                btn.setText("Unavailable")
                btn.setStyleSheet("""
                    QPushButton {
                        background: #fee2e2;
                        color: #991b1b;
                        border-radius: 25px;
                        font-size: 13px;
                        font-weight: 600;
                    }
                """)
            else:
                btn.setStyleSheet("""
                    QPushButton {
                        background: #f1f5f9;
                        color: #475569;
                        border-radius: 25px;
                        font-size: 14px;
                        font-weight: 600;
                        border: none;
                    }
                    QPushButton:hover {
                        background: #e2e8f0;
                    }
                    QPushButton:checked {
                        background: #2563eb;
                        color: white;
                    }
                """)

            self.time_grid.addWidget(btn, row, col)
            self.time_group.addButton(btn)
            col += 1
            if col == 3:
                col = 0
                row += 1

    def confirm_selected_time(self, dialog):
        checked = self.time_group.checkedButton()
        if not checked or not checked.isEnabled():
            QMessageBox.warning(dialog, "Selection Required", "Please select an available time slot.")
            return

        time_str = checked.text()
        self.confirm_booking(dialog, self.selected_date, time_str)

    def confirm_booking(self, dialog, date, time_str):
        dialog.accept()
        token = random.randint(1, 110)
        key = (self.selected_doctor, date.toString(), time_str)
        self.appointments_tracker[key] = self.appointments_tracker.get(key, 0) + 1

        msg = QMessageBox(self)
        msg.setWindowTitle("Booking Confirmed")
        msg.setText(
            f"<b>Success!</b><br><br>"
            f"<b>Doctor:</b> {self.selected_doctor}<br>"
            f"<b>Date:</b> {date.toString('dddd, MMM d')}<br>"
            f"<b>Time:</b> {time_str}<br><br>"
            f"<span style='font-size: 18px; color: #d32f2f;'><b>Token: {token}</b></span>"
        )
        
        msg.exec_()

    # ==================== EMERGENCY PAGE (FIXED) ====================
    def create_emergency_page(self):
        widget = QWidget()
        widget.setStyleSheet("background-color: #FCFAFA;") # Soft off-white
        layout = QVBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # 1. Clean Navbar
        sub_header = QFrame()
        sub_header.setFixedHeight(80)
        sub_header.setStyleSheet("background-color: white; border-bottom: 1px solid #E2E8F0;")
        sh_layout = QHBoxLayout(sub_header)
        sh_layout.setContentsMargins(40, 0, 40, 0)

        back = QPushButton(" ← Back to Home")
        back.setFixedSize(140, 45)
        back.setCursor(Qt.PointingHandCursor)
        back.setStyleSheet("""
            QPushButton {
                background-color: transparent; border: 1px solid #E2E8F0; 
                border-radius: 12px; font-weight: 600; color: #64748B;
            }
            QPushButton:hover { background-color: #F8FAFC; color: #1E293B; }
        """)
        back.clicked.connect(lambda: self.stacked.setCurrentIndex(1))

        title = QLabel("EMERGENCY RESPONSE")
        title.setStyleSheet("color: #941111; font-weight: 800; letter-spacing: 2px; font-size: 14px;")

        sh_layout.addWidget(back)
        sh_layout.addStretch()
        sh_layout.addWidget(title)
        layout.addWidget(sub_header)

        # 2. Main Content
        container = QWidget()
        container_layout = QVBoxLayout(container)
        container_layout.setAlignment(Qt.AlignCenter)
        container_layout.setContentsMargins(0, 50, 0, 50)

        # Emergency Card
        card = QFrame()
        card.setFixedSize(750, 450)
      
        card.setStyleSheet("""
            QFrame {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #FFFFFF, stop:1 #FFF5F5);
                border-radius: 40px;
                border: 2px solid #FEE2E2;
            }
        """)
        
       
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(50)
        shadow.setColor(QColor(211, 47, 47, 60)) # Reddish glow
        shadow.setOffset(0, 10)
        card.setGraphicsEffect(shadow)

        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(50, 50, 50, 50)
        card_layout.setSpacing(10)

        icon_label = QLabel("🚨")
        icon_label.setFont(QFont("Arial", 30))
        icon_label.setAlignment(Qt.AlignCenter)
        card_layout.addWidget(icon_label)

        etitle = QLabel("Critical Emergency Care")
        etitle.setFont(QFont("Segoe UI", 22, QFont.Bold))
        etitle.setStyleSheet("color: #B91C1C; border: none;")
        etitle.setAlignment(Qt.AlignCenter)
        card_layout.addWidget(etitle)

        phone = QLabel("Dial: 108")
        phone.setFont(QFont("Segoe UI", 20, QFont.Black))
        phone.setStyleSheet("color: #DC2626; border: none; letter-spacing: -2px;")
        phone.setAlignment(Qt.AlignCenter)
        card_layout.addWidget(phone)

        avail = QLabel("Our dedicated trauma team is standing by.\nAverage response time: 8-12 minutes.")
        avail.setFont(QFont("Segoe UI", 12))
        avail.setStyleSheet("color: #64748B; border: none;")
        avail.setAlignment(Qt.AlignCenter)
        card_layout.addWidget(avail)

        card_layout.addStretch()

        # Action Button
        request_btn = QPushButton("REQUEST IMMEDIATE AMBULANCE")
        request_btn.setFixedSize(400, 60)
        request_btn.setCursor(Qt.PointingHandCursor)
        request_btn.setStyleSheet("""
            QPushButton {
                background-color: #DC2626; color: white; border-radius: 15px;
                font-size:22px; font-weight: 600; border: none;
            }
            QPushButton:hover { background-color: #B91C1C; }
            QPushButton:pressed { background-color: #991B1B; }
        """)
        # Mock action
        request_btn.clicked.connect(lambda: QMessageBox.critical(self, "SOS Sent", "Emergency services have been notified of your location."))
        card_layout.addWidget(request_btn, alignment=Qt.AlignCenter)

        container_layout.addWidget(card)
        layout.addWidget(container)
        layout.addStretch()

        return widget


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HealtheaseApp()
    window.show()
    sys.exit(app.exec_())