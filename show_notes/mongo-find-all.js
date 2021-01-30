/*
How to Query All Documents in a MongoDB Collection with
the find() Method.

> db.books.find()
{ "_id" : ObjectId("60149e20451bd27e8326a3dc"), "name" : "OOP Programming", "publishedDate" : ISODate("2021-01-29T23:45:36.583Z"), "authors" : [ { "name" : "Jon Snow" }, { "name" : "Ned Stark" } ] }
{ "_id" : ObjectId("60149f2b451bd27e8326a3dd"), "name" : "OOP Programming", "publishedDate" : ISODate("2021-01-29T23:50:03.798Z"), "authors" : [ { "name" : "Jon Snow Jr" } ] }
{ "_id" : ObjectId("60149fba451bd27e8326a3de"), "name" : "OOP Programming", "startDate" : ISODate("2021-01-29T23:52:26.345Z"), "authors" : [ { "name" : "Jon Snow Jr" } ] }
{ "_id" : ObjectId("6014ceb8451bd27e8326a3df"), "name" : "Confident Ruby", "publishedDate" : ISODate("2021-01-30T03:12:56.992Z"), "authors" : [ { "name" : "Avdi Grimm" } ] }
{ "_id" : ObjectId("6014ceb8451bd27e8326a3e0"), "name" : "The War of Art", "publishedDate" : ISODate("2021-01-30T03:12:56.992Z"), "authors" : [ { "name" : "Steven Pressfield" } ] }
{ "_id" : ObjectId("6014ceb8451bd27e8326a3e1"), "name" : "Blink", "publishedDate" : ISODate("2021-01-30T03:12:56.992Z"), "authors" : [ { "name" : "Malcom Gladwell" } ] }

> db.books.find().pretty()
{
	"_id" : ObjectId("60149e20451bd27e8326a3dc"),
	"name" : "OOP Programming",
	"publishedDate" : ISODate("2021-01-29T23:45:36.583Z"),
	"authors" : [
		{
			"name" : "Jon Snow"
		},
		{
			"name" : "Ned Stark"
		}
	]
}
{
	"_id" : ObjectId("60149f2b451bd27e8326a3dd"),
	"name" : "OOP Programming",
	"publishedDate" : ISODate("2021-01-29T23:50:03.798Z"),
	"authors" : [
		{
			"name" : "Jon Snow Jr"
		}
	]
}
{
	"_id" : ObjectId("60149fba451bd27e8326a3de"),
	"name" : "OOP Programming",
	"startDate" : ISODate("2021-01-29T23:52:26.345Z"),
	"authors" : [
		{
			"name" : "Jon Snow Jr"
		}
	]
}
{
	"_id" : ObjectId("6014ceb8451bd27e8326a3df"),
	"name" : "Confident Ruby",
	"publishedDate" : ISODate("2021-01-30T03:12:56.992Z"),
	"authors" : [
		{
			"name" : "Avdi Grimm"
		}
	]
}
{
	"_id" : ObjectId("6014ceb8451bd27e8326a3e0"),
	"name" : "The War of Art",
	"publishedDate" : ISODate("2021-01-30T03:12:56.992Z"),
	"authors" : [
		{
			"name" : "Steven Pressfield"
		}
	]
}
{
	"_id" : ObjectId("6014ceb8451bd27e8326a3e1"),
	"name" : "Blink",
	"publishedDate" : ISODate("2021-01-30T03:12:56.992Z"),
	"authors" : [
		{
			"name" : "Malcom Gladwell"
		}
	]
}


Notes: 

To return all documents in a given collection you can use
db.collection.find()
This will return all the documents as objects.

To make them more readable you can add the pretty() 
command to return them in a more readable format.

*/