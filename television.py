class Television:
    # Class variables
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.__status = False  # TV is off by default
        self.__muted = False  # TV is not muted by default
        self.__volume = self.MIN_VOLUME  # Default volume is the minimum
        self.__channel = self.MIN_CHANNEL  # Default channel is the minimum

    def power(self):
        self.__status = not self.__status

    def mute(self):
        if self.__status:  # Only if the TV is on
            self.__muted = not self.__muted

    def channel_up(self):
        if self.__status:  # Only if the TV is on
            self.__channel += 1
            if self.__channel > self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL

    def channel_down(self):
        if self.__status:  # Only if the TV is on
            self.__channel -= 1
            if self.__channel < self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL

    def volume_up(self):
        if self.__status:  # Only if the TV is on
            if self.__muted:  # Unmute if muted
                self.__muted = False
            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        if self.__status:  # Only if the TV is on
            if self.__muted:  # Unmute if muted
                self.__muted = False
            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self):
        power_status = "On" if self.__status else "Off"
        return f"Power: {power_status}, Channel: {self.__channel}, Volume: {self.__volume}"
