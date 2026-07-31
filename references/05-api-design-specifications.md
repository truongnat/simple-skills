# 05 — API Design Specifications

## 1. Executive Summary

This document outlines the standard RESTful API conventions utilized across the enterprise system. It enforces a unified route structure, standardized HTTP verbs, consistent error envelopes, and mechanisms for multi-tenancy and data concurrency.

## 2. Global Conventions

### 2.1. Route Structure
All endpoints follow a strict hierarchical pattern to ensure consistency and predictability:
`GET/POST /api/{module}/{feature-slug}/{screen-id}/{action}`

- **module**: The overarching business domain.
- **feature-slug**: A readable, kebab-case grouping of related functionality.
- **screen-id**: The traceability code linking the API to a specific UI screen.
- **action**: The specific operation being performed (e.g., `search`, `save`, `init`).

### 2.2. HTTP Verb Usage
- **GET**: Used for fetching simple data, initializing screens, or retrieving master records by ID.
- **POST**: Used for creating resources, executing complex calculations, AND performing advanced searches.
  - *Note on Search*: Enterprise searches often involve complex, nested criteria that exceed URL length limits and are difficult to encode in query strings. Therefore, POST is designated as the standard verb for complex filtering.
- **PUT**: Full replacement of an aggregate resource.
- **DELETE**: Soft or hard deletion of records.

## 3. Response Formatting & Error Handling

### 3.1. Standardized Error Envelope
All unhandled exceptions and validation failures are intercepted by a global middleware and transformed into a unified JSON format:

| HTTP Status | Trigger Condition | Standardized Body Content |
|---|---|---|
| **400 Bad Request** | Request payload fails schema validation | Array of validation errors with field paths and message IDs |
| **401 Unauthorized** | Missing, expired, or invalid JWT | Generic unauthorized message |
| **403 Forbidden** | User lacks required permissions for the action | Indication of permission denied |
| **404 Not Found** | The requested resource ID does not exist | Generic not found message |
| **409 Conflict** | Optimistic lock (Row-Version) mismatch | Conflict indicator, prompting UI to refresh |
| **500 Internal Error** | System crash or unhandled exception | Trace ID for log correlation (no stack traces leaked) |

## 4. Cross-Cutting Headers

The API expects specific contextual metadata attached as HTTP headers by the client:
- **Authorization**: `Bearer <token>` for identity verification.
- **Language/Locale**: Indicates the preferred language for formatting localized data or error message IDs.
- **Screen Context**: Explicit headers declaring which UI screen and UI form originated the request, used primarily for comprehensive audit logging.
- **Organizational Role**: If a user belongs to multiple groups, a header explicitly declares the context under which they are currently operating.

## 5. Optimistic Concurrency Control

To safely handle simultaneous data edits in a distributed environment:
1. Every GET request fetching a modifiable aggregate includes a `Row-Version` (RV) token.
2. The client must include this exact `RV` token in the body of any subsequent POST/PUT/PATCH request.
3. If the backend detects that the database's current `RV` does not match the client's `RV`, the operation is aborted and a `409 Conflict` is returned.
4. For complex payloads containing arrays of nested items, the `RV` logic is applied recursively to each nested entity to ensure fine-grained concurrency control.
