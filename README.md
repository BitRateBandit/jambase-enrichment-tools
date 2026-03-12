## JamBase Enrichment Tool

scripts/jambase_spotify_enricher.py

This utility enriches JamBase event IDs with external identifiers.

Retrieved fields include:

• Event name  
• Artist name  
• Spotify Artist ID  
• MusicBrainz ID  
• Ticketmaster ID  
• Other external identifiers when available

The script uses the JamBase API with:

expandExternalIdentifiers=true

## Setup

Clone the repository

git clone https://github.com/BitRateBandit/jambase-enrichment-tools.git
cd jambase-enrichment-tools

Install dependencies

pip install -r requirements.txt
