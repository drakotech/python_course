/*
How to Check if a Field Exists in a MongoDB Document


db.books.insert( 
  {
    "name": "Deep Work: Rules for Focused Success in a Distracted World",
    "publishedDate": new Date(),
    "reviews": 100,
    "authors": [
      {"name": "Cal Newport"}
    ]
  }
)

db.books.find({ reviews: { $exists: true } })
Returns only the above insert that has a review key.

db.books.find({ reviews: { $exists: false } })
Returns all the others that don't have a review key.

Notes:

Using the %exists method you can find and clean up your
datase to add in features later on to the older documents.


*/