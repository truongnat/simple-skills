# 01 — System Architecture Patterns

## 1. Executive Summary

The system is designed as a **Multi-tenant SaaS** application using a **Modular Monolith** architecture. This approach is highly suitable for complex enterprise systems (like ERPs) where business domains are tightly coupled and ACID transactional integrity is prioritized over horizontal microservice scaling. 

The architecture relies on a central Identity Provider (SSO/OIDC) for authentication, a robust relational database for the primary data store, and an in-memory datastore (e.g., Redis) for caching and distributed locks.

## 2. Core Architecture

### 2.1. Modular Monolith Approach
- **Structure**: The backend is organized into distinct business modules (e.g., Sales, Manufacturing, Purchasing) hosted within a single API process.
- **Rationale**: Avoids network latency and complex distributed transactions while maintaining clean code boundaries. Modules are separated logically rather than physically.

### 2.2. Multi-Tenancy & Data Isolation
- **Tenant Resolution**: Multi-tenancy is enforced at the middleware layer. Each incoming request carries a JWT containing a tenant claim (or tenant slug in the URL).
- **Isolation Strategy**: A shared-database, shared-schema approach is used. The middleware extracts the tenant context, and the ORM applies global query filters automatically to ensure tenants cannot access each other's data.

## 3. Database Architecture

### 3.1. Entity & Table Naming Conventions
Tables are prefixed to denote their data lifecycle, making the schema self-documenting:
- **Master Data (`m_`)**: Reference data that changes infrequently (e.g., configurations, product catalogs).
- **Transaction Data (`t_`)**: Permanent business records generated during daily operations (e.g., orders, invoices).
- **Work/Staging Data (`w_`)**: Temporary data buffers for in-progress operations or batch processing.

### 3.2. Internationalization (I18n) via JSON
- Instead of complex EAV (Entity-Attribute-Value) models or separate translation tables, multi-language support is achieved using native JSON columns. 
- Example: `name_column: {"en": "Product", "ja": "製品"}`. This simplifies schema design and improves read performance.

### 3.3. Automated Audit Trails
Every business table includes mandatory audit columns (Created At, Created By, Updated At, Updated By). To ensure data integrity, these fields are populated automatically by the ORM's interceptor layer before saving, completely abstracting this responsibility from business logic.

## 4. Authentication & Authorization

### 4.1. Authentication Flow
- **Identity Provider**: The system integrates with a centralized OIDC/SSO provider.
- **Mechanism**: The client authenticates via standard OAuth2/OIDC flows, receiving a JWT Access Token and Refresh Token. All API endpoints validate the JWT signature.

### 4.2. Granular Authorization
- Authorization is decoupled from standard role-based access control (RBAC). 
- A custom **Permission Handler** evaluates policies based on the user's claims, their active organizational role, and the specific screen (UI context) making the request.

## 5. Deployment & Observability

- **Containerization**: The system is packaged into discrete container images (e.g., one for the Web API, one for asynchronous background jobs).
- **Observability**: Structured logging is enforced across all requests. Logs are enriched with application-level context (Tenant ID, User ID, Trace ID) and forwarded to a centralized telemetry and monitoring platform.
