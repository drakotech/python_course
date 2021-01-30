/*
Using the findOne Method in MongoDB to Query for a 
Single Document


> db.books.find({name: "Blink"}).pretty()

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
{
	"_id" : ObjectId("6014f54a1ff225f159e17ea4"),
	"name" : "Blink",
	"publisheDate" : ISODate("2021-01-30T05:57:30.463Z"),
	"authors" : [
		{
			"name" : "Malcolm Gladwell"
		},
		{
			"name" : "Ghost Writer"
		}
	]
}


> db.books.find({name: "Blink"}).length()
2


> db.books.findOne({name: "Blink"})
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

When you want to find out how many documents there are you
can use the .length() method.

In the above example we have the find method finding two
documents with the name of "Blink" and to find only one
we can use the .findOne() method to only return the first
one that meets the query.

*/