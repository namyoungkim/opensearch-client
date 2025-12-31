"""
OpenSearch Client - Hybrid Search Support for Korean Text

A Python client for OpenSearch with built-in support for:
- Text search with Korean (Nori) analyzer
- Semantic search with vector embeddings
- Hybrid search combining both approaches
"""

from opensearch_client.client import OpenSearchClient
from opensearch_client.exceptions import BulkIndexError, OpenSearchClientError
from opensearch_client.hybrid_search import HybridQueryBuilder, SearchPipelineManager
from opensearch_client.index import IndexManager
from opensearch_client.semantic_search.knn_search import KNNSearch
from opensearch_client.text_search import AnalyzerConfig, TextQueryBuilder
from opensearch_client.vectorstore import SearchResult, VectorStore

__version__ = "0.1.0"
__all__ = [
    "AnalyzerConfig",
    "BulkIndexError",
    "HybridQueryBuilder",
    "IndexManager",
    "KNNSearch",
    "OpenSearchClient",
    "OpenSearchClientError",
    "SearchPipelineManager",
    "SearchResult",
    "TextQueryBuilder",
    "VectorStore",
]
