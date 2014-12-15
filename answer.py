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


from collections import OrderedDict


# -------------------------------
# ----- List of answers for users
# -------------------------------

# ----- Valid Placeholders for Chat Message:
#       bot                 Bot name

# ----- Valid Placeholders for Answer:
#       username            Who write a message in chat for the bot
#       insult              Random Insult from insults list


ANSWERS = OrderedDict([
    ('.*privmsg {bot}', 'Aiutatemi vi prego! {username} ci prova con me nei messaggi privati'),
    ('.*ha abbandonato.*', 'Finalmente {username} va via. Più spazio per chi rimane.'),
    ('.*ciao|buonasera|buongiorno|salve.*', 'Ciao {username}!'),
    ('.*(manual[ei]|guid[ae]|documentazione|doc|materiale|tutorial).*(odoo|openerp).*', '{username}, forse questo link può aiutarti: https://www.odoo.com/documentation/8.0/'),
    ('.*{bot}.*grazie', 'Prego {username}! È stato un piacere per me! Cosa ne dici di una donazione per aiutarmi?'),
    ('.*grazie.*{bot}', 'Prego {username}! È stato un piacere per me! Cosa ne dici di una donazione per aiutarmi?'),
    ('.*{bot}.*(insulta|offendi) OpenCode', 'Voglio troppo bene a mio padre! Grazie per avermi creato papà <3!'),
    ('.*{bot}.*(insulta|offendi) {bot}', '{username} stai cercando di fregare un BOT. Sei molto furbo, eh?'),
    ('.*{bot}.*(insulta|offendi).*', '{insult}'),
    ('.*{bot}.*(developers|ballmer).*remix.*', 'LOL https://www.youtube.com/watch?v=KMU0tzLwhbE'),
    ('.*{bot}.*(developers|ballmer).*', 'Buon gustaio: https://www.youtube.com/watch?v=Vhh_GeBPOhs'),
    ('.*{bot}.*', '{username} smettila di menzionarmi. Sono solo un BOT. Pensa a lavorare!'),
    ])
