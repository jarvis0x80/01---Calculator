from PySide6.QtWidgets import QWidget,QLineEdit,QVBoxLayout,QHBoxLayout, QPushButton, QSizePolicy
from PySide6.QtGui import QFont
# from playsound import playsound


class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")

        self.setGeometry(300,300,400,400)
        self.layout = QVBoxLayout()
        
        font = QFont()
        font.setPointSize(20)

        self.display_exp = QLineEdit()
        self.display_exp.setFont(font)
        self.display_res = QLineEdit()
        self.display_exp.setMinimumWidth(390)
        self.display_exp.setMinimumHeight(80)

        self.display_res.setMinimumWidth(390)
        self.display_res.setMinimumHeight(40)

        
        self.layout.addWidget(self.display_exp)
        self.layout.addWidget(self.display_res)
        self.setLayout(self.layout)

        button_grid = [

            ["Clear" , "Back" , "Ans" , "*" ],
            ['7'     ,  '8'   , '9' , '/' ],
            ['4'     ,  '5'   , '6' , '+' ],
            ['1'     ,  '2'   , '3' , '-' ],
            ['%'     ,  '0'   , '.' , '=']
        ]

        for row in button_grid:
            row_layout = QHBoxLayout()

            for button_text in row:

                button = QPushButton(button_text)
                button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                button.clicked.connect(self.button_clicked)

                if button_text in ["*","/","-","+", "="]:
                    button.setStyleSheet("""
                            QPushButton {
                                background-color: #fc980c;
                                color: white;
                                border: 2px solid #afafaf;
                                padding: 10px 20px;
                                font-size: 16px;
                            }
                            QPushButton:hover{
                                background-color: #cc7906;
                            }
                            """)
                else:
                    button.setStyleSheet("""
                            QPushButton {
                                background-color: #f0f0f0;
                                color: rgb(17, 17, 17);
                                border: 2px solid #afafaf;
                                padding: 10px 20px;
                                font-size: 16px;
                                        }
                            QPushButton:hover{
                                background-color: #afafaf;
                                        }
                            """)
                row_layout.addWidget(button)
                
            self.layout.addLayout(row_layout)

        self.setLayout(self.layout)

        self.current_exp = ''
        self.last_result = ''


        self.setStyleSheet("""
        QWidget {
            background-color: #f0f0f0;
        }
       
        QLineEdit {
            background-color: #ffffff;
            border: 2px solid #ccc;
            padding: 5px;
        }
        """)


    def button_clicked(self):
        button = self.sender()
        button_text = button.text()
        # playsound("click.wav")

        if button_text == 'Clear':
            self.current_exp = ''
            self.display_exp.setText(self.current_exp)
            self.display_res.setText('')

        elif button_text == "Back":
            self.current_exp = self.current_exp[:-1] 
            self.display_exp.setText(self.current_exp)

        elif button_text == "Ans":
            self.current_exp += self.last_result
            self.display_exp.setText(self.current_exp)

        elif button_text == "%":
            try:
                result = str(eval(self.current_exp) / 100)
                self.display_exp.setText(self.current_exp)
                self.display_res.setText('= ' + result)
                self.current_exp = result
            except Exception as e:
                self.display_res.setText("Error")
                self.current_exp = ""

        elif button_text == '=':
            try:
                result = str(eval(self.current_exp))
                self.display_res.setText("= "+ result)
                self.last_result = result

            except Exception as e:
                self.display_res.setText('Error')

        else:
            self.current_exp += button_text
            self.display_exp.setText(self.current_exp)
