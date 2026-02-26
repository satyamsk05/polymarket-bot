```mermaid
flowchart TD
    A[User] -->|Initiates bet| B[Polymarket Bot]
    B -->|Fetches market data| C[Polymarket API]
    C --> D[Market Data]
    B -->|Updates bets| E[Database]
    E --> F[User Confirmation]
    F -->|Notifies user| A
```