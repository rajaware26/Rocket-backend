import mysql.connector
from datetime import date
import card
import user

config = {
    'user': 'rocket',
    'password': 'r0ck3t',
    'host': 'nickarli.com',
    'database': 'rocket'
}
db = mysql.connector.connect(**config)
cursor=db.cursor()

#query = "the query"
#cursor.execute(query)

def addUserCard(user, card):
    now = date.today()
    statement = "INSERT INTO usercards (USERCARDS_USERID, USERCARDS_CARDID, USERCARDS_DATEADDED) VALUES "+card.id+", "+user.id+", "+now.strftime("%Y/%m/%d")+";"
    cursor.execute(statement)
    db.commit()

def addCard(card: card.CardClass):
    statement = "INSERT INTO cards (CARDID, CARDMULTIVERSEID, CARDNAME, CARDLAYOUT, CARDCMC, CARDTYPE, CARDRARITY, CARDSET, CARDSETNAME, CARDTEXT, CARDNUMBER, CARDIMAGEURL) VALUES (%(id)s, %(multiverseid)s, %(name)s, %(layout)s, %(cmc)s, %(type)s, %(rarity)s, %(set)s, %(setname)s, %(text)s, %(number)s, %(imageurl)s);"
    card_info = {
        'id': card.id,
        'multiverseid': card.multiverseId,
        'name': card.name,
        'layout': card.layout,
        'cmc': card.cmc,
        'type': card.type,
        'rarity': card.rarity,
        'set': card.set,
        'setname': card.setName,
        'text': card.text,
        'number': card.number,
        'imageurl': card.imageUrl
    }
    cursor.execute(statement, card_info)
    db.commit()


cursor.close()
db.close()


print()