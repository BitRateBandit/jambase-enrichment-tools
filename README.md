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

### Usage

export JAMBASE_API_KEY=your_key_here

make run-jambase-enrich INPUT=data/events.xlsx OUTPUT=data/events_enriched.xlsx
