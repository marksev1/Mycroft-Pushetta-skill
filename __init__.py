from os.path import dirname
from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

from pushetta import Pushetta

__author__ = 'msev'

LOGGER = getLogger(__name__)

class PushettaSkill(MycroftSkill):
    def __init__(self):
        super(PushettaSkill, self).__init__(name="PushettaSkill")
        self.api_key = self.config.get("pushetta_api_key")
	self.p = Pushetta(self.api_key)
        self.channel_name = self.config.get("pushetta_channel")

    def initialize(self):
        self.load_data_files(dirname(__file__))
        self.register_regex("(push to me|push|push it) (?P<Source>.*)")
        pushetta_intent = IntentBuilder("PushettaIntent").\
            require("PushettaKeyword").require("Source").build()
        self.register_intent(pushetta_intent, self.handle_pushetta_intent)
 

    def handle_pushetta_intent(self, message):
        self.p.pushMessage(self.channel_name, message.data["Source"])
        self.speak_dialog("pushetta")                                              
        
    def stop(self):
        pass


def create_skill():
    return PushettaSkill()
