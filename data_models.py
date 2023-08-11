

class Author(db.Model):
    __tablename__ = 'Authors'

    Author_id = Column(Integer, primary_key=True)
    Author_name = Column(String)
    restaurant_city = Column(String)
    famous_dish = Column(String)

    def __repr__(self) -> str:
        return f"Restaurant(restaurant_id = {self.restaurant_id}, name = {self.restaurant_name})"