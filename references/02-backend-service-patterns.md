# 02 — Backend Service Architecture Patterns

## 1. Module Overview

The backend is structured as a **Modular Monolith**, containing multiple isolated business modules alongside a shared foundation layer.

### 1.1. Sub-project Layout per Module
Each domain module consists of standardized sub-projects to enforce separation of concerns:
- **Business/Domain**: Contains core business logic, entities, and repository interfaces.
- **Contract**: Contains public interfaces and DTOs. This acts as an anti-corruption layer.
- **Infrastructure**: Contains concrete implementations of repositories, database contexts, and dependency injection configurations.
- **Tests**: Co-located unit and integration tests for the specific module.

## 2. Core Architectural Rules

### 2.1. Cross-Module Communication
- Modules are strictly prohibited from directly importing or referencing the internal business logic or entities of other modules.
- If Module A needs data or services from Module B, it must communicate exclusively through Module B's **Contract** project. 

### 2.2. Shared Kernel
A foundation layer (Shared Infrastructure & Shared Module) provides cross-cutting concerns that all modules rely on:
- **Base Database Context**: Enforces tenant filters, audit logging, and master/replica routing.
- **Utilities**: Distributed caching wrappers, object storage helpers, and HTTP resilience policies (retry/circuit breaker).
- **Global Error Handling**: Middleware that intercepts unhandled exceptions and formats them into a standardized JSON envelope.

## 3. Request Pipeline & Middlewares

The API pipeline is structured to execute cross-cutting concerns predictably:
1. **Logging Middleware**: Initiates a structured log context for the incoming request, capturing timing and path.
2. **Tenant Isolation Middleware**: Resolves the tenant context from the JWT or URL and scopes the dependency injection container.
3. **Exception Middleware**: A global try-catch block that translates domain exceptions or system crashes into uniform HTTP responses.
4. **Validation Filters**: Automatically validates incoming request DTOs against predefined rules before hitting the controller logic.

## 4. Data Access Pattern

### 4.1. Unit of Work & Repositories
- Each module defines its own `IUnitOfWork` interface to manage transaction boundaries specific to its domain.
- The **Repository Pattern** is used to abstract database queries. Interfaces reside in the Domain layer, while implementations reside in the Infrastructure layer.

### 4.2. Database Routing
- The system supports read/write splitting. By default, write operations are routed to the Primary (Master) database node, while read-only queries (`AsNoTracking`) can be routed to Replica (Slave) nodes to distribute load.

## 5. Background Jobs

The architecture decouples long-running operations from the main HTTP request thread:
- **Async Workers**: Handled via message queues or webhooks to process heavy tasks (e.g., report generation, bulk data processing) in the background.
- **Scheduled Jobs**: Handled via a CRON scheduler for periodic maintenance tasks (e.g., data cleanup, nightly aggregations).
