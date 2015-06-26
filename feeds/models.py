from mongoengine.document import Document, EmbeddedDocument
from mongoengine.fields import IntField, StringField, \
    GenericEmbeddedDocumentField, URLField, EmbeddedDocumentField, \
    BooleanField, ListField


class Story(Document):
    tile_size = IntField()
    tile_type = StringField()
    values = GenericEmbeddedDocumentField()


class Action(EmbeddedDocument):
    type = StringField()
    url = URLField()


class ProductThumbnails(EmbeddedDocument):
    product_image = StringField()
    action = EmbeddedDocumentField(Action)


class Brand(EmbeddedDocument):
    banner_url = URLField()
    banner_title = StringField()
    brand_logo = URLField()
    nearest_store = StringField()
    is_following = BooleanField()
    product_count = IntField()
    followers_count = IntField()
    products = ListField(GenericEmbeddedDocumentField(ProductThumbnails))


class Collection(EmbeddedDocument):
    banner_url = URLField()
    banner_title = StringField()
    collection_logo = URLField()
    last_updated = StringField()
    is_following = BooleanField()
    product_count = IntField()
    followers_count = IntField()
    products = ListField(GenericEmbeddedDocumentField(ProductThumbnails))


class Product(EmbeddedDocument):
    product_name = StringField
    product_image = URLField
    is_bookmarked = BooleanField
    price_marked = IntField()
    price_effective = IntField()
    brand_name = StringField()
    badge_url = URLField()
    action = EmbeddedDocumentField(Action)
