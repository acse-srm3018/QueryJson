# Query by Example JSON document store
A Python implementation of a program handling Query by Example

Query By Example allows a client to specify a structure in which is used as the example, and all entities which match are returned. Implement a basic storage mechanism which allows a user to store documents in JSON format. The structure of the document may be otherwise arbitrary. The program accepts a command through `stdin` , followed by a space, followed by a document, followed by a newline. There are three allowed commands.

* add, store the given document.
* get, find all documents which have the same properties and property values as the given document, and emit them to `stdout`.
* delete, remove all documents which have the same properties and property values as the given document.

The commands are all lowercase.

Given the input:

```json
add { "id" : 1,   "last": "Doe", "first": "John", "location": {"city": "Oakland", "state": "CA", "postalCode": "94607"}, "active": true}
add { "id" : 2,   "last": "Doe", "first": "Jane", "location": {"city": "San Francisco", "state": "CA", "postalCode": "94105"}, "active": true}
add { "id" : 3,   "last": "Black", "first": "Jim", "location": {"city": "Oakland", "state": "WA", "postalCode": "99207"}, "active": true}
add { "id" : 4,   "last": "Frost", "first": "Jack", "location": {"city": "Seattle", "state": "WA", "postalCode": "98204"}, "active": false}
get {"location":{"state":"WA"},"active":true}
```

Emit:

```json
{"id" : 3, "last" : "Black" , "first" : "Jim" , "location" : {"city" : "Spokane" , "state" : "WA" , "postalCode" : "99207"}, "active" : true}
{"id" : 1, "last" : "Doe" , "first" : "John" , "location" :{"city" : "Oakland" , "state" : "CA" , "postalCode" : "94607"}, "active" : true}
```

Note that the documents are output in the exact format as they were input, If multiple documents are matched, the documents are emitted in the order they were created. The input may be rather complex and that the number of documents or the number of queries may be quite large.

## Handling Lists

Support lists as "in list” expressions, for example, given the following input:

```json
add {"type":"list","List":[1,2,3,4]}
add {"type":"list","list":[2,3,4,5]}
add {"type":"list","List":[3,4,5,6]}
add {"type":"list","list":[4,5,6,7]}
add {"type":"list","List":[5,6,7,8]}
add {"type":"list","list":[6,7,8,9]}
get {"type":"list","List":[1]}
get {"type":"list","List":[3,4]}
```

Yield:

```json
{"type":"list","list":[1,2,3,4]}
{"type":"1ist","list":[1,2,3,4]}
{"type":"list","list":[2,3,4,5]}
{"type":"list","list":[3,4,5,6]}
```

## Usage

In the command line, use the following commands:

```
> python quantcast_class.py
```

To test the program, use the following commands:

```
> ./qbe < testcase/input001.txt > output001.txt
> ./qbe < testcase/input002.txt > output002.txt
```

To test the correctness of the program, use the following commands:

```
> diff output001.txt testcase/output001.txt
> diff output002.txt testcase/output002.txt
```

