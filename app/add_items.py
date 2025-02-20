from db import SessionLocal, Item

db = SessionLocal()

existing_ids = {item.id for item in db.query(Item.id).all()}
items = [
    Item(id=1, name="Foo"),
    Item(id=2, name="Bar"),
    Item(id=3, name="Baz"),
]
items = [item for item in items if item.id not in existing_ids]

db.add_all(items)
db.commit()
db.close()