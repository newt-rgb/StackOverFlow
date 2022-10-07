from PyQt5.QtWidgets import QCalendarWidget
from PyQt5.QtCore import QPoint, QDate, Qt
from PyQt5 import QtWidgets
import sqlite3

class newCalendar(QCalendarWidget):
    def __init__(self,_tab):
        super().__init__(_tab)
    
    #给日历加上小红点如果这天有日程
    def paintCell(self, painter, rect, date):
        super().paintCell(painter, rect, date)
        db = sqlite3.connect("database.db")
        cursor = db.cursor()
        query = "SELECT date FROM Data"
        results = cursor.execute(query).fetchall()
        list_of_events = []
        for _date in results:
            list_of_events.append(QDate.fromString(_date[0], 'yyyy-MM-dd'))
        if date in list_of_events:
            painter.setBrush(Qt.red)
            painter.drawEllipse(rect.topLeft() + QPoint(12, 7), 6, 6)
            