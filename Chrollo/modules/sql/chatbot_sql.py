import threading

from sqlalchemy import Column, String

from Chrollo.modules.sql import BASE, SESSION


class ChrolloChats(BASE):
    __tablename__ = "chrollo_chats"
    chat_id = Column(String(14), primary_key=True)

    def __init__(self, chat_id):
        self.chat_id = chat_id


ChrolloChats.__table__.create(checkfirst=True)
INSERTION_LOCK = threading.RLock()


def is_chrollo(chat_id):
    try:
        chat = SESSION.query(ChrolloChats).get(str(chat_id))
        return bool(chat)
    finally:
        SESSION.close()


def set_fallen(chat_id):
    with INSERTION_LOCK:
        chrollochat = SESSION.query(ChrolloChats).get(str(chat_id))
        if not chrollochat:
            chrollochat = ChrolloChats(str(chat_id))
        SESSION.add(chrollochat)
        SESSION.commit()


def rem_chrollo(chat_id):
    with INSERTION_LOCK:
        chrollochat = SESSION.query(ChrolloChats).get(str(chat_id))
        if chrollochat:
            SESSION.delete(chrollochat)
        SESSION.commit()
