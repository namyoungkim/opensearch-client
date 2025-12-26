"""
OpenSearch Client - Hybrid Search Support for Korean Text

A Python client for OpenSearch with built-in support for:
- Text search with Korean (Nori) analyzer
- Semantic search with vector embeddings
- Hybrid search combining both approaches
"""

from opensearch_client.client import OpenSearchClient
from opensearch_client.index import IndexManager
from opensearch_client.text_search import TextQueryBuilder, AnalyzerConfig
from opensearch_client.semantic_search.knn_search import KNNSearch
from opensearch_client.hybrid_search import SearchPipelineManager, HybridQueryBuilder
from opensearch_client.vectorstore import VectorStore, SearchResult

__version__ = "0.1.0"
__all__ = [
    "OpenSearchClient",
    "IndexManager",
    "TextQueryBuilder",
    "AnalyzerConfig",
    "KNNSearch",
    "SearchPipelineManager",
    "HybridQueryBuilder",
    "VectorStore",
    "SearchResult",
]
