# 03 — Frontend Architecture Patterns

## 1. Executive Summary

The frontend architecture is designed for a large-scale Single Page Application (SPA). It utilizes a feature-module pattern, strict dependency injection, and a robust state management strategy to handle complex business logic and forms independently of the backend.

## 2. Solution Layout

The application is structured to cleanly separate cross-cutting concerns from feature-specific logic:
- **`app/` (Composition Root)**: Contains global providers (Theme, State, Error Boundaries) and bootstrap logic.
- **`commons/` (Shared Kernel)**: Contains cross-cutting UI components (Atomic Design), shared utilities, HTTP clients, and global state stores.
- **`modules/` (Feature Modules)**: Contains domain-specific features. Each module encapsulates its own pages, components, queries, and services.
- **`routes/`**: Handles file-based routing and navigation guards.

## 3. Dependency Injection (DI) & Mocking

To decouple the UI from network requests and enable parallel development:
- **Service Interfaces**: Data-fetching logic is defined via abstract interfaces.
- **DI Container**: At runtime, a DI container resolves these interfaces to either Real Implementations (calling the backend API) or Mock Implementations (returning fake data).
- **Benefit**: Frontend teams can build, test, and render complete UI flows before backend APIs are ready.

## 4. State Management Strategy

### 4.1. Server State vs. Client State
- **Global Client State**: Manages user sessions, selected themes, and layout preferences (persisted to cookies or local storage).
- **Server State**: Managed via a query-caching library to handle data fetching, caching, synchronization, and background updates.

### 4.2. Intentional Deviation in Complex Forms
- **Pattern**: While data is typically fetched declaratively via queries, highly complex business forms often require imperative data fetching (using mutations instead of queries).
- **Rationale**: This allows developers to trigger data fetching manually upon specific user actions (e.g., pressing Enter) and pipe the result directly into a complex form state manager, avoiding infinite render loops and cache invalidation headaches.

## 5. Networking & HTTP Context

### 5.1. Auto-Injection of Context Headers
To simplify backend processing, the frontend HTTP client automatically injects contextual metadata into every request via interceptors:
- **Screen ID / Form ID**: Identifies exactly which UI screen initiated the request (crucial for audit logs and granular permissions).
- **Language Code**: Informs the backend to return localized error messages or data.
- **Role/Tenant Context**: Explicitly declares the active organizational role.

### 5.2. Row-Version Optimistic Locking
- To prevent "Lost Updates" in collaborative environments, the HTTP client automatically detects and injects a `Row-Version` (RV) token into the payload of all write requests (POST/PUT/PATCH/DELETE). 
- If the backend detects a version mismatch, it returns a `409 Conflict`, and the frontend globally intercepts this to prompt the user to refresh the stale data.

## 6. Internationalization (I18n)

- Language detection prioritizes the URL segment first, followed by user cookies, and finally browser defaults.
- The UI binds to translation files split by domain to prevent a monolithic translation dictionary.
- Backend error codes (Message IDs) are translated at the frontend layer to ensure the UI remains fully localized without forcing the backend to format user-facing strings.
