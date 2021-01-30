/*
Guide to Inserting Documents into a MongoDB Collection


When in a mongo terminal:


db.books.insert({
    "name": "OOP Programming",
    "publishedDate": new Date(),
    "authors": [
        { "name": "Jon Snow" },
        { "name": "Ned Stark" },
    ]
})
#WriteResult({ "nInserted" : 1 })

db.books.insert({
    "name": "OOP Programming",
    "startDate": new Date(),
    "authors": [
        { "name": "Jon Snow Jr" },
    ]
})
#WriteResult({ "nInserted" : 1 })


Notes:

Create a document in a collection by utilizing:
db.collection.insert({})

You can create a database with whatever structure you'd
like. Meaning use different key value structure but without
a customized schema your code will be messy and you won't
be able to make queries if everything is named without
following a structure.


*/