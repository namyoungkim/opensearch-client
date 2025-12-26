# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Build & Test Commands

```bash
# Install dependencies (all extras including openai and local embeddings)
uv sync --all-extras

# Run unit tests
uv run pytest tests/unit -v

# Run a single test file
uv run pytest tests/unit/test_query_builder.py -v

# Run a specific test
uv run pytest tests/unit/test_query_builder.py::test_function_name -v

# Run integration tests (requires OpenSearch running on port 9201)
docker compose -f docker-compose.test.yml up -d
uv run pytest tests/integration -v

# Run all tests with coverage
uv run pytest --cov=opensearch_client --cov-report=html
```

## Architecture

This is a Python client library for OpenSearch with hybrid search support (text + vector) designed for Korean text via Nori analyzer.

### Module Structure

- **`client.py`**: Main `OpenSearchClient` class wrapping opensearch-py. Provides index/document CRUD, search, and hybrid search pipeline management.

- **`index.py`**: `IndexManager` with static methods for creating index configurations (text, vector, hybrid) with Korean analyzer settings.

- **`text_search/`**: Text query building (`TextQueryBuilder`, `AnalyzerConfig`) with multi-match support.

- **`semantic_search/`**:
  - `knn_search.py`: k-NN vector search queries
  - `embeddings/`: Pluggable embedding providers (`BaseEmbedding`, `FastEmbedEmbedding`, `OpenAIEmbedding`). Optional deps loaded conditionally.

- **`hybrid_search/`**: Combines text + vector search using OpenSearch Search Pipelines (2.10+)
  - `pipeline.py`: `SearchPipelineManager` for normalization/scoring config
  - `hybrid_query.py`: `HybridQueryBuilder` for building combined queries

- **`vectorstore.py`**: High-level `VectorStore` wrapper for simple add/search interface with automatic embedding

### Key Patterns

- Embeddings are optional: `opensearch-client[openai]` or `opensearch-client[local]` for FastEmbed
- Hybrid search requires a Search Pipeline set up via `client.setup_hybrid_pipeline()`
- Integration tests use port 9201 to avoid conflicts (configured via `OPENSEARCH_TEST_PORT` env var)
- Test markers: `@pytest.mark.integration` for tests requiring OpenSearch
