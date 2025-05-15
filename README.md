
![spark_github_banner](https://github.com/user-attachments/assets/4af391c3-b79a-4a56-9f10-bfc25909a05d)


# Spark Tracker

Wallet tracking and sentiment analysis tool to detect multi-buy and multi-sell events, analyze tweets and track wallets in real time.


## Features

- Track multiple Solana wallets
- Detect multi-buy patterns (3+ wallets buying the same token in 6 hours)
- Detect multi-sell patterns (3+ wallets selling the same token in 6 hours)
- Persistent storage of wallet data, and consistent improvements & bug fixes being released with each new update
- Track specific tokens across all wallets
- Toggle alerts on/off
- Real-time collection and processing of crypto-related tweets and social media sentiment


## Core Technologies

- Python 3.11.9
- Moralis API for API endpoints
- Docker & Kubernetes
- OAuth2 for authentication 
- Swagger/OpenAPI for documentation
- Apache Airflow for processing and handling the data


## Moralis API Integration

The bot uses the Moralis API to fetch transaction data:

- Endpoint: `https://solana-gateway.moralis.io/account/mainnet/{wallet_address}/swaps`
- Checks transactions every minute
- Filters transactions from the last 6 hours
- Processes transaction types:
  - `newPosition` for buys
  - `sellAll` for sells

## Error Handling

The bot includes error handling for:

- API rate limits
- Network issues
- Invalid wallet addresses
- Transaction parsing errors
- Notification sending failures


## Development Plan

- Phase 1: Initial Setup and Basic Structure (Completed) ✓ 
- Phase 2: Database Implementation (Completed) ✓
- Phase 3: Basic Security Implementation (Completed) ✓
- Phase 4: X API Integration (Completed) ✓
- Phase 5: Blockchain Network Management System (Completed) ✓
- Phase 6: Bug fixes and advanced security testing (ongoing)

## Marketing & token implementation

- Phase 1: Artwork and basic UI/UX features (Completed) ✓ 
- Phase 2: Social media banners, icons, marketing supplies (Completed) ✓
- Phase 3: Marketing budget allocation for trendings, boosts and marketing campaigns (Completed) ✓
- Phase 4: KOL focused marketing campaigns (planned after token launch)
- Phase 5: Community contests and airdrops (planned after token launch)
- Phase 6: Token implementation & rewards (ongoing)(planned after token launch)
