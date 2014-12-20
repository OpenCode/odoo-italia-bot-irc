#!/usr/bin/python
# -*- coding: utf-8 -*-
# -*- encoding: utf-8 -*-
# ######################################################################
#
#  odoo-italia-bot: #odoo-it IRC BOT
#
#  Copyright 2014 Francesco OpenCode Apruzzese <cescoap@gmail.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
# ######################################################################

# -------
# IMPORTS
# -------
from os import path
import re
from random import randint
from datetime import datetime

import lib.botlib as botlib
from sentence.insult import INSULTS
from sentence.answer import ANSWERS


# ---------
# CONSTANTS
# ---------
BOT_NAME = 'Ticelli'
PROJECT_PATH = path.dirname(path.realpath(__file__))


# ----- Create a new class for our bot extending the Bot class from botlib
class OdooItaliaBotIRC(botlib.Bot):

    def __init__(self, server, channel, nick, password=None):
        botlib.Bot.__init__(self, server, 6667, channel, nick)

    def __actions__(self):
        botlib.Bot.__actions__(self)
        # ----- Update log file
        with open('%s/logs/%s' % (PROJECT_PATH,
                                  datetime.today().strftime('%Y_%m_%d')),
                  'ab') as log_file:
            log_file.write(self.data)
        # ----- Get the senders username
        username = self.get_username()
        # ----- With this if we eclude standard channel messages
        if self.nick.lower() != username.lower() and not '\n' in username and \
                not ' ' in username:
            message_yet = False
            chat_message = self.data.lower()
            # ----- Check if there is some valid answer
            for regex_answer in ANSWERS:
                if message_yet:
                    break
                formatted_regex_answer = regex_answer.format(bot=BOT_NAME)
                formatted_regex_answer = formatted_regex_answer.lower()
                #print '[MSG]', chat_message
                #print '[RGX]', formatted_regex_answer
                # ----- If valid answer exists, use it
                if re.search(formatted_regex_answer, chat_message):
                    self.protocol.privmsg(
                        self.channel,
                        ANSWERS[regex_answer].format(
                            username=username,
                            bot=BOT_NAME,
                            insult=self.get_random_insult(chat_message),))
                    message_yet = True

    def get_random_insult(self, chat_message):
        insulted = chat_message.split()[-1]
        random_index = randint(0, len(INSULTS)-1)
        return INSULTS[random_index].format(insulted=insulted)


if __name__ == "__main__":
    # ----- New instance of our bot and run it
    OdooItaliaBotIRC("irc.freenode.net", "#odoo-it", BOT_NAME).run()
