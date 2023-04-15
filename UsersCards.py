
from flask import url_for
class UsersCards():

    def get_idCard(self):
        return str(self.__user_cards['id'])


    def getNameCard(self):
        return self.__user_cards['name'] if self.__user_cards else "Без имени"


    def getEmailCard(self):
        return self.__user_cards['email'] if self.__user_cards else "Без email"


    def getNumberCard(self):
        return self.__user_cards['numbers'] if self.__user_cards else "Без number"
    def getAvatarCard(self, app):
        img = None
        if not self.__user_cards['avatar']:
            try:
                with app.open_resource(app.root_path + url_for('static', filename='images/default.png'), "rb") as f:
                    img = f.read()
            except FileNotFoundError as e:
                print("Не найден аватар по умолчанию: "+str(e))
        else:
            img = self.__user_cards['avatar']

        return img
    def getQR(self, app):
        img = None
        if not self.__user_cards['QR']:
            try:
                with app.open_resource(app.root_path + url_for('static', filename='images/default.png'), "rb") as f:
                    img = f.read()
            except FileNotFoundError as e:
                print("Не найден аватар по умолчанию: "+str(e))
        else:
            img = self.__user_cards['QR']

        return img