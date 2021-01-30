/*
How to Insert Many Documents into a MongoDB Collection

db.books.insertMany([
    {
        "name": "Confident Ruby",
        "publishedDate": new Date(),
        "authors": [
            {"name": "Avdi Grimm"}
        ]
    },
    {
        "name": "The War of Art",
        "publishedDate": new Date(),
        "authors": [
            {"name": "Steven Pressfield"}
        ]
    },
    {
        "name": "Blink",
        "publishedDate": new Date(),
        "authors": [
            {"name": "Malcom Gladwell"}
        ]
    }
])

Returned:
{
	"acknowledged" : true,
	"insertedIds" : [
		ObjectId("6014ceb8451bd27e8326a3df"),
		ObjectId("6014ceb8451bd27e8326a3e0"),
		ObjectId("6014ceb8451bd27e8326a3e1")
	]
}


Notes:

Using the insertMany command you can insert multiple
documents into a collection and mongo will return an
object containing the IDs for all the documents added.

*/
