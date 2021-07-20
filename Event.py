import json


class Event:
    def __init__(self, idEvent, target, effect):
        self.id = idEvent
        self.target = target
        self.effect = effect

    def event(self, n):
        with open("ressources/events.json") as file:
            data = json.load(file)
            events = data["events"]

            for event in events:
                if event["id"] == n:
                    self.idEvent = event["id"]
                    self.target = event["target"]
                    self.effect = event["effect"]