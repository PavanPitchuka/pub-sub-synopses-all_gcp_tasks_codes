from google.cloud import firestore

# Connect to Firestore
db = firestore.Client(database="pavandb1")

# ---------------- CREATE ----------------
doc_ref = db.collection("students").add({
    "class": 5,
    "number": 4,
    "student": "naveen"
})

doc_id = doc_ref[1].id
print(f"Created student with ID: {doc_id}")

# ---------------- READ ----------------
print("\nStudents with class >= 5:")
docs = db.collection("students").where("class", ">=", 5).stream()

for doc in docs:
    print(f"{doc.id} => {doc.to_dict()}")

# ---------------- UPDATE ----------------
db.collection("students").document(doc_id).update({
    "number": 5
})
print(f"\nUpdated student {doc_id} number to 5")

# ---------------- DELETE ----------------
query = db.collection("students").where("student", "==", "naveen")

for doc in query.stream():
    db.collection("students").document(doc.id).delete()
    print(f"Deleted student with ID: {doc.id}")

