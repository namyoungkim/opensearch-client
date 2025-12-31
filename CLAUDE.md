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

- **`async_client.py`**: `AsyncOpenSearchClient` for async/await operations. Requires `[async]` extra.

- **`exceptions.py`**: Custom exceptions (`OpenSearchClientError`, `BulkIndexError`)

### Key Patterns

- Embeddings are optional: `opensearch-client[openai]` or `opensearch-client[local]` for FastEmbed
- Async support is optional: `opensearch-client[async]` for `AsyncOpenSearchClient`
- Hybrid search requires a Search Pipeline set up via `client.setup_hybrid_pipeline()`
- Integration tests use port 9201 to avoid conflicts (configured via `OPENSEARCH_TEST_PORT` env var)
- Test markers: `@pytest.mark.integration` for tests requiring OpenSearch

## Development Workflow

### Branch Strategy (Git Flow)

| 브랜치 | 용도 | 병합 대상 |
|--------|------|-----------|
| `main` | 프로덕션 릴리스 | - |
| `develop` | 개발 통합 (향후 도입) | `main` |
| `feature/*` | 새 기능 개발 | `develop` 또는 `main` |
| `fix/*` | 버그 수정 | `develop` 또는 `main` |
| `chore/*` | 설정, 문서, 리팩토링 | `develop` 또는 `main` |

### Code Quality Commands

```bash
# Lint check
uv run ruff check .

# Auto-fix lint issues
uv run ruff check --fix .

# Format code
uv run ruff format .

# Type check
uv run ty check
```

### Before Commit Checklist

1. `uv run ruff check --fix .`
2. `uv run ruff format .`
3. `uv run ty check`
4. `uv run pytest`
