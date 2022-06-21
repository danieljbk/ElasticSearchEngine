import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
from typing import List
from constants import DOC_TYPE, INDEX_NAME


HEADERS = {"content-type": "application/json"}


class SearchResult:
    """Represents a product returned from elasticsearch."""

    def __init__(
        self, id_, number, name, type_one, type_two, max_cp, max_hp, image_url
    ):
        self.id = id_
        self.number = number
        self.name = name
        self.type_one = type_one
        self.type_two = type_two
        self.max_cp = max_cp
        self.max_hp = max_hp
        self.image_url = image_url

    def from_doc(doc) -> "SearchResult":
        return SearchResult(
            id_=doc.meta.id,
            number=doc.number,
            name=doc.name,
            type_one=doc.type_one,
            type_two=doc.type_two,
            max_cp=doc.max_cp,
            max_hp=doc.max_hp,
            image_url=doc.image_url,
        )


def search(term: str, count: int) -> List[SearchResult]:
    client = Elasticsearch(
        hosts=["http://localhost:9200"], http_auth=("elastic", "BOUGSd4No0SuDBjLe77I")
    )

    # Elasticsearch 6 requires the content-type header to be set, and this is
    # not included by default in the current version of elasticsearch-py
    client.transport.connection_pool.connection.headers.update(HEADERS)

    s = Search(using=client, index=INDEX_NAME, doc_type=DOC_TYPE)
    name_query = {
        "match": {
            "name": {
                "query": term,
            }
        }
    }
    type_one_query = {
        "match": {
            "type_one": {
                "query": term,
            }
        }
    }
    type_two_query = {
        "match": {
            "type_two": {
                "query": term,
            }
        }
    }
    dis_max_query = {  # disjunction max query
        "dis_max": {
            "queries": [name_query, type_one_query, type_two_query],
        },
    }
    docs = s.query(dis_max_query)[:count].execute()

    return [SearchResult.from_doc(d) for d in docs]
