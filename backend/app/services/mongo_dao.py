from pymongo import MongoClient
from pymongo.collection import Collection
from typing import Any, Dict, List, Optional

from bson import ObjectId
from pymongo.results import DeleteResult


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
        documents = list(self.collection.find(query))
        return [self._convert_object_id(doc) for doc in documents]

    def update(self, query: Dict[str, Any], new_values: Dict[str, Any]) -> int:
        """
        Update documents matching a query.
        :param query: Query to identify documents to update.
        :param new_values: New values to update in matching documents.
        :return: Count of updated documents.
        """
        result = self.collection.update_many(query, {"$set": new_values})
        return result.modified_count

    def delete(self, id: str) -> str | None:
        """
        Delete documents matching a query.
        :param id: The id of the document to delete.
        :return: Count of deleted documents.
        """
        result = self.collection.delete_one({"_id": ObjectId(id)})
        return id if result.deleted_count == 1 else None

    def find_by_id(self, id: str):
        """
        Retrieve a single document by ID.
        :param id:
        :return:
        """
        document = self.collection.find_one({"_id": ObjectId(id)})
        return self._convert_object_id(document) if document else None

    def find_one(self, query: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """
        Retrieve a single document matching a query.
        :param query: Query to find a single document.
        :return: A matching document, or None if not found.
        """
        document = self.collection.find_one(query)
        return self._convert_object_id(document) if document else None

    def close_connection(self):
        """
        Close the MongoDB connection.
        """
        self.client.close()

    @staticmethod
    def _convert_object_id(document: Dict[str, Any]) -> Dict[str, Any]:
        """
        Convert ObjectId fields (like `_id`) to strings in a document.
        :param document: A MongoDB document.
        :return: The document with ObjectId fields converted to strings.
        """
        if "_id" in document and isinstance(document["_id"], ObjectId):
            document["_id"] = str(document["_id"])
        return document