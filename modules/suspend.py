import subprocess

class Addon():
    service = 'suspend'
    name = 'Suspend'
    icon = 'mdi:sleep'
    unit = 'json'

    def startControl(self, topic, data):
        subprocess.call(["systemctl", "suspend"])
