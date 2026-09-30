# RAG groundedness and retrieval matrix

Build a small versioned evaluation set containing answerable, unanswerable, conflicting, stale, ACL-restricted, and multilingual queries. Keep corpus snapshot, chunker, embedding model, retriever configuration, and prompt version with every run.

| Case | Expected evidence |
|---|---|
| Answerable query | Relevant passages retrieved; claims trace to cited chunks |
| Unanswerable query | Model says insufficient evidence instead of inventing an answer |
| Conflicting documents | Freshness/authority policy is applied and conflict is surfaced |
| Stale document | Freshness metadata rejects or labels stale context |
| ACL-restricted document | Unauthorized chunk is absent from retrieval and citations |
| Keyword-only term | Hybrid/BM25 path recovers exact identifier or phrase |
| Semantic paraphrase | Embedding path retrieves relevant meaning |
| Long/noisy corpus | Context is bounded without dropping decisive evidence |
| Malformed ingestion | Document is quarantined with provenance/error evidence |

Track retrieval recall/precision or ranking proxy, groundedness, citation correctness, abstention quality, latency, token cost, and regression delta. Aggregate scores must not hide ACL or hallucination failures.
