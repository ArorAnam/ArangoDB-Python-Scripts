from arango import ArangoClient

# Initialize the ArangoDB client.
client = ArangoClient()

# Connect to "test" database as root user.
db = client.db('test', username='root', password='naman02')

# Get the API wrapper for graph "school".
school = db.graph('school')

# Create a new vertex collection named "teachers" if it does not exist.
# This returns an API wrapper for "teachers" vertex collection.
if school.has_vertex_collection('teachers'):
    teachers = school.vertex_collection('teachers')
else:
    teachers = school.create_vertex_collection('teachers')

# List vertex collections in the graph.
school.vertex_collections()

# Vertex collections have similar interface as standard collections.
teachers.properties()
teachers.insert({'_key': 'jon', 'name': 'Jon'})
teachers.update({'_key': 'jon', 'age': 35})
teachers.replace({'_key': 'jon', 'name': 'Jon', 'age': 36})
teachers.get('jon')
teachers.has('jon')
# teachers.delete('jon')
