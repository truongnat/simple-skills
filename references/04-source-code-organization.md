# 04 — Source Code Organization & Traceability

## 1. Executive Summary

In a massive enterprise codebase, discoverability is critical. This architecture enforces strict naming conventions and a **Screen-ID Driven** organizational model. The goal is to allow any developer to seamlessly trace a feature across the entire stack (Frontend to Database) simply by searching a unique identifier.

## 2. Naming Conventions

### 2.1. Feature Codes & Screen-IDs
- **Feature Code**: A short, alphanumeric code representing a distinct business domain and sub-domain (e.g., `SA` for Sales -> Ordering).
- **Screen-ID**: A unique string combining the Feature Code and a sequence number (e.g., `SA03001`). 
- **Usage**: The Screen-ID is ubiquitous. It is used as the base name for Route files, Page components, Query hooks, Service Interfaces, Backend Controllers, and DTOs.

### 2.2. Entity & Table Prefixes
Database entities are prefixed to immediately communicate their lifecycle:
- **Master Data (`M_` / `m_`)**: Static or slow-changing reference dictionaries.
- **Transaction Data (`T_` / `t_`)**: Permanent records of business operations.
- **Work Buffer (`W_` / `w_`)**: Temporary or staging data representing uncommitted work.

## 3. Cross-Stack Traceability

By strictly adhering to the Screen-ID convention, the system achieves perfect 1:1 mapping across layers. For a given Screen-ID (e.g., `SA03001`):

| Layer | Artifact Description | Naming Pattern |
|---|---|---|
| **Frontend Route** | The URL path definition | `sa03001.tsx` |
| **Frontend Page** | The root UI component | `pages/ordering/sa03001/` |
| **Frontend Queries** | Data fetching hooks | `sa03001.queries.ts` |
| **Frontend Service** | The API communication layer | `sa03001.service.ts` |
| **Backend API** | The HTTP endpoint handler | `SA03001Controller.cs` |
| **Backend Service** | The business logic implementation | `ISA03001Service.cs` |
| **Backend DTOs** | The request/response payloads | `SA03001SaveRequest.cs` |

## 4. Code Organization Rules

### 4.1. Clean Architecture Enforcement
- **Dependency Rule**: The API layer depends on the Application (Business) layer. The Application layer depends on the Domain layer. The Domain layer has zero external dependencies.
- **Cross-Module Limits**: As outlined in the Backend patterns, modules interact strictly via designated Contract interfaces. Direct namespace importing across module boundaries is forbidden.

### 4.2. File and Folder Practices
- **One Class per File**: Backend files must contain exactly one top-level type, and the file name must perfectly match the type name.
- **Co-located Tests**: In the frontend, unit tests and component stories are placed immediately adjacent to the source file they test (e.g., `Button.tsx`, `Button.test.tsx`, `Button.stories.tsx`), ensuring tests are discovered easily.
- **Constants Isolation**: Magic strings and numbers are strictly prohibited. Constants are scoped appropriately (Global, Module-scoped, or Screen-scoped) and extracted into dedicated configuration files.
