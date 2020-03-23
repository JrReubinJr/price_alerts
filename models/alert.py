__author__ = 'sinclairSolutions'

from typing import Dict
from models.item import Item
from models.model import Model
from models.user import User
from dataclasses import dataclass, field
from libs.mailgun import Mailgun
import uuid


@dataclass(eq=False)
class Alert(Model):
    collection: str = field(init=False, default='alerts')
    name: str
    item_id: str
    price_limit: float
    user_email: str
    _id: str = field(default_factory=lambda : uuid.uuid4().hex)

    def __post_init__(self):
        self.item = Item.get_by_id(self.item_id)
        self.user = User.find_by_email(self.user_email)

    def json(self) -> Dict:
        return {
            '_id': self._id,
            'name': self.name,
            'item_id': self.item_id,
            'price_limit': self.price_limit,
            'user_email': self.user_email
        }

    def load_item_price(self) -> float:
        self.item.load_price()
        return self.item.price

    def notify_if_price_reached(self):
        if self.item.price < self.price_limit:
            print(f"Item {self.item} is now {self.item.price} and is in your budget")
            Mailgun.send_mail(
                ['wolsk011@umn.edu'],
                f'Notification for {self.name}',
                f'Your alert {self.name} has reached a price under {self.price_limit}. The latest price is {self.item.price}.  Go to {self.item.url} for more information',
                f'<p>Your alert {self.name} has reached a price under {self.price_limit}.</p><p> The latest price is {self.item.price}.</p><p>Go to <a href="{self.item.url}">here</a> for more information</p>'
            )


