from arango import ArangoClient

# Initialize the ArangoDB client.
client = ArangoClient()

# Connect to "test" database as root user.
db = client.db('test', username='root', password='naman02')

# Get the API wrapper for graph "school".
school = db.graph('school')

# Create a new vertex collection named "lectures" if it does not exist.
# This returns an API wrapper for "lectures" vertex collection.
if school.has_vertex_collection('lectures'):
    school.vertex_collection('lectures')
else:
    school.create_vertex_collection('lectures')

# The "_id" field is required instead of "_key" field (except for insert).
school.insert_vertex('lectures', {'_key': 'CSC101'})
school.update_vertex({'_id': 'lectures/CSC101', 'difficulty': 'easy'})
school.replace_vertex({'_id': 'lectures/CSC101', 'difficulty': 'hard'})
school.has_vertex('lectures/CSC101')
school.vertex('lectures/CSC101')
# school.delete_vertex('lectures/CSC101')
