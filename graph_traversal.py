from arango import ArangoClient

# Initialize the ArangoDB client.
client = ArangoClient()

# Connect to "test" database as root user.
db = client.db('test', username='root', password='naman02')

# Get the API wrapper for graph "school".
school = db.graph('school')

# Get API wrappers for "from" and "to" vertex collections.
teachers = school.vertex_collection('teachers')
lectures = school.vertex_collection('lectures')

# Get the API wrapper for the edge collection.:
teaches = school.edge_collection('teaches')

# Insert vertices into the graph.
teachers.update({'_key': 'jon', 'name': 'Professor jon'})
lectures.update({'_key': 'CSC101', 'name': 'Introduction to CS'})
lectures.insert({'_key': 'MAT223', 'name': 'Linear Algebra'})
lectures.insert({'_key': 'STA201', 'name': 'Statistics'})

# Insert edges into the graph.
teaches.insert({'_from': 'teachers/jon', '_to': 'lectures/CSC101'})
teaches.insert({'_from': 'teachers/jon', '_to': 'lectures/STA201'})
teaches.insert({'_from': 'teachers/jon', '_to': 'lectures/MAT223'})

# Traverse the graph in outbound direction, breath-first.
school.traverse(
    start_vertex='teachers/jon',
    direction='outbound',
    strategy='bfs',
    edge_uniqueness='global',
    vertex_uniqueness='global',
)