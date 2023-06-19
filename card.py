from mtgsdk import Card

class CardClass():
    # for cards we know everything about
    def __init__(self, id: int, multiverseId: int, name: str, 
                 layout: str, cmc: int, type: str, rarity: str,
                 set: str, setName: str, text: str, number: str,
                 imageUrl: str):
        self.id = id
        self.multiverseId = multiverseId
        self.name = name
        self.layout = layout
        self.cmc = cmc
        self.type = type
        self.rarity = rarity
        self.set = set
        self.setName = setName
        self.text = text
        self.number = number
        self.imageUrl = imageUrl

    # for cards we only know a few details about
    def __init__(self, name: str, set: str):
        cards = Card.where(name=name) \
                    .where(set=set) \
                    .all()
        self.id = cards[0].id
        self.multiverseId = cards[0].multiverse_id
        self.name = cards[0].name
        self.layout = cards[0].layout
        self.cmc = cards[0].cmc
        self.type = cards[0].type
        self.rarity = cards[0].rarity
        self.set = cards[0].set
        self.setName = cards[0].set_name
        self.text = cards[0].text
        self.number = cards[0].number
        self.imageUrl = cards[0].image_url

#card = CardClass("Narset, Enlightened Master", "KTK")
#print(card.rarity)

        
    
    

    

