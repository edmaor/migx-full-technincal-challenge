from pymongo import MongoClient
from pymongo.collection import Collection
from typing import Any, Dict, List, Optional

class MongoDAO:
    def __init__(self, connection_string: str, database_name: str, collection_name: str):
        """
        Initialize MongoDAO with database connection, database, and collection.
        """
        self.client = MongoClient(connection_string)
        self.database = self.client[database_name]
        self.collection: Collection = self.database[collection_name]

    def create(self, document: Dict[str, Any]) -> str:
        """
        Insert a document into the collection.
        :param document: The document to insert.
        :return: The ID of the inserted document.
        """
        result = self.collection.insert_one(document)
        return str(result.inserted_id)

    def read(self, query: Dict[str, Any] = {}) -> List[Dict[str, Any]]:
        """
        Retrieve documents matching a query.
        :param query: Query to filter documents (default: empty query to return all).
        :return: List of matching documents.
        """
        return list(self.collection.find(query))

    def update(self, query: Dict[str, Any], new_values: Dict[str, Any]) -> int:
        """
        Update documents matching a query.
        :param query: Query to identify documents to update.
        :param new_values: New values to update in matching documents.
        :return: Count of updated documents.
        """
        result = self.collection.update_many(query, {"$set": new_values})
        return result.modified_count

    def delete(self, query: Dict[str, Any]) -> int:
        """
        Delete documents matching a query.
        :param query: Query to identify documents to delete.
        :return: Count of deleted documents.
        """
        result = self.collection.delete_many(query)
        return result.deleted_count

    def find_one(self, query: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """
        Retrieve a single document matching a query.
        :param query: Query to find a single document.
        :return: A matching document, or None if not found.
        """
        return self.collection.find_one(query)

    def close_connection(self):
        """
        Close the MongoDB connection.
        """
        self.client.close()