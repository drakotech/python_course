/*
How to Include Nested Fields in a find Query


db.books.insert({
    "name": "Blink",
    "publishedDate": new Date(),
    "authors": [
        { "name": "Malcolm Gladwell", "active": "true" },
        { "name": "Ghost Writer", "active": "true" }
    ]
});

db.books.find(
  {
    name: "Blink"
  },
  {
    name: 1,
    publishedDate: 1,
    "authors.name": 1
  }
).pretty()

{
	"_id" : ObjectId("6014ebe31ff225f159e17ea3"),
	"name" : "Blink",
	"publishedDate" : ISODate("2021-01-30T05:17:23.990Z"),
	"authors" : [
		{
			"name" : "Malcolm Gladwell"
		},
		{
			"name" : "Ghost Writer"
		}
	]
}

db.books.find(
  {
    name: "Blink"
  },
  {
    name: 1,
    publishedDate: 1,
    authors: 1
  }
).pretty()

{
	"_id" : ObjectId("6014ebe31ff225f159e17ea3"),
	"name" : "Blink",
	"publishedDate" : ISODate("2021-01-30T05:17:23.990Z"),
	"authors" : [
		{
			"name" : "Malcolm Gladwell",
			"active" : "true"
		},
		{
			"name" : "Ghost Writer",
			"active" : "true"
		}
	]
}


Notes:

Using the "authors.name": 1 will return the first element 
inside the authors objects. The name element. Notice the
active status is omitted. This is how you can select what
nested objects you wish to pull from the document.

*/