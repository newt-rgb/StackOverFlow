from PyQt5.QtWidgets import QCalendarWidget
from PyQt5.QtCore import QPoint, QDate, Qt
from PyQt5 import QtWidgets
import sqlite3
import frozen_dir
from datetime import date, datetime, time


class newCalendar(QCalendarWidget):
    def __init__(self,_tab):
        super().__init__(_tab)

    base = frozen_dir.app_path()
    #给日历加上小红点如果这天有日程
    def paintCell(self, painter, rect, date):
        super().paintCell(painter, rect, date)
        db = sqlite3.connect('{}\database.db'.format(self.base))
        cursor = db.cursor()
        query = "SELECT date,completed,frequency FROM Data"
        results = cursor.execute(query).fetchall()
        list_of_date = []
        list_of_freq = []
        list_of_comp =  []
        for _date in results:
            list_of_date.append(QDate.fromString(_date[0], 'yyyy-MM-dd'))
            list_of_comp.append(_date[1])
            _list_freq = []
            datestr = _date[2].split(',')
            if datestr[0] == '':
                _list_freq = []
            else:
                for dt in datestr:
                    _list_freq.append(QDate.fromString(dt.split(' ')[0], 'yyyy-MM-dd'))
            list_of_freq.append(_list_freq)
        
        for i, _date in enumerate(list_of_date):
            if list_of_comp[i] == '1' and _date == date:
                painter.setBrush(Qt.green)
                painter.drawEllipse(rect.topLeft() + QPoint(12, 7), 6, 6)
            elif list_of_comp[i] == '0' and _date == date:
                painter.setBrush(Qt.red)
                painter.drawEllipse(rect.topLeft() + QPoint(12, 7), 6, 6)
            
            