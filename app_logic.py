from PySide6.QtCore import QTimer, Qt, QTime
from system_monitor import get_sys_info
from db_manager import insert_sys_data, db_records_list


class AppLogic:
    def __init__(self, main_window):
        self.main_window = main_window
        self.is_recording = False  # Recording status
        self.timer = QTimer()  # timer object
        self.timer_interval = 1000 # Default interval = 1 sec
        self.timer.timeout.connect(self.update_system_info)  # connect timer to update_system_info
        
        self.time_timer = QTimer()
        self.time_timer_interval = 1000 # Default time timer interval 1 sec
        self.time_timer.timeout.connect(self.update_time)
        self.time_timer.start(self.time_timer_interval) # Start time_timer with default interval
        self.update_time()

        self.recording_timer = QTimer()
        self.recording_seconds = 0
        self.recording_timer.timeout.connect(self.update_recording_time)
        self.update_system_info() # Переместили вызов после определения recording_seconds


    def switch_recording_text(self):
        if self.main_window.record_button.text() == "Start Rec":
            self.main_window.record_button.setText("Stop Rec")
            self.is_recording = True
            self.timer.start(self.timer_interval)  # start timer
            self.recording_timer.start(1000)
        else:
            self.main_window.record_button.setText("Start Rec")
            self.is_recording = False
            self.timer.stop()  # stop timer
            self.recording_timer.stop()
            self.recording_seconds = 0
            self.update_recording_time()

    def open_history_window(self):
        records = db_records_list()
        self.main_window.history_window.set_data(records)
        self.main_window.history_window.show()

    def update_system_info(self):
        sys_info = get_sys_info()
        self.main_window.cpu_progress.setValue(int(sys_info['cpu_percent']))
        self.main_window.cpu_percent_label.setText(f"{sys_info['cpu_percent']:.1f} %")
        self.main_window.ram_progress.setValue(int(sys_info['ram_percent']))
        self.main_window.ram_usage_label.setText(f"{sys_info['ram_used']:.1f} / {sys_info['ram_total']:.1f} GB")
        self.main_window.disk_progress.setValue(int(sys_info['disk_percent']))
        self.main_window.disk_usage_label.setText(f"{sys_info['disk_used']:.1f} / {sys_info['disk_total']:.1f} GB")
        
        minutes = self.recording_seconds // 60
        seconds = self.recording_seconds % 60
        hours = minutes // 60
        minutes = minutes % 60
        time_text = f"{hours:02}:{minutes:02}:{seconds:02}"
        sys_info['recording_time'] = time_text

        if self.is_recording:
            insert_sys_data(sys_info)

    def set_timer_interval(self, interval):
        self.timer_interval = interval
        if self.timer.isActive():
            self.timer.stop()
            self.timer.start(self.timer_interval)

            self.time_timer_interval = interval #Set interval for time timer
            if self.time_timer.isActive(): #restart timer with new interval
                self.time_timer.stop()
                self.time_timer.start(self.time_timer_interval)

    def update_time(self):
        current_time = QTime.currentTime()
        time_text = current_time.toString("hh:mm:ss")
        self.main_window.time_label.setText(time_text)

    def update_recording_time(self):
        if self.is_recording:
            self.recording_seconds += 1

        minutes = self.recording_seconds // 60
        seconds = self.recording_seconds % 60
        hours = minutes // 60
        minutes = minutes % 60
        time_text = f"Recording time: {hours:02}:{minutes:02}:{seconds:02}"
        self.main_window.recording_time_label.setText(time_text)