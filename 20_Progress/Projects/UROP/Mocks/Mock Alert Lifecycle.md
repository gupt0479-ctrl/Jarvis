---
type: evergreen
status: sprout
created: 2026-04-23
tags:
  - evergreen
notes:
  - "[[Alerts and Data Flow]]"
  - "[[Kafka Redis and Workers]]"
  - "[[MongoDB Data Model and Filters]]"
---
# Mock Alert Lifecycle

This is a simplified, teaching-oriented walkthrough of one alert moving through BOOM.

Related notes:

- [[Alerts and Data Flow]]
- [[Kafka Redis and Workers]]
- [[MongoDB Data Model and Filters]]

## Scenario

Imagine ZTF observes a patch of sky and detects a brightness change.

The survey emits an alert packet containing:

- object ID
- candidate ID
- RA/Dec
- photometric measurements
- cutout images

## Step 1: Kafka input

The survey alert enters a Kafka topic.

Meaning:

- the alert is now part of a stream
- BOOM can subscribe to and consume it

## Step 2: Kafka consumer

BOOM's Kafka consumer reads the packet and pushes it into Redis or Valkey.

Meaning:

- BOOM has accepted the alert into its internal processing system

## Step 3: Alert worker

The alert worker:

- parses and normalizes the packet
- writes initial alert/object/image records to MongoDB
- pushes the candidate ID into the enrichment queue

Meaning:

- the alert now exists as structured BOOM data, not just an external packet

## Step 4: Enrichment worker

The enrichment worker:

- loads the relevant alert data
- cross-matches against catalogs
- computes or stores model scores
- writes new fields back to MongoDB
- pushes the candidate ID into the filter queue

Meaning:

- the alert has more scientific and operational context than the raw packet had

## Step 5: Filter worker

The filter worker:

- loads the enriched record
- runs user-defined filter logic
- if the alert passes, emits it to an output stream

Meaning:

- BOOM has now decided whether the alert is interesting for downstream consumers

## Step 6: API and downstream access

At this point, users or systems can:

- query BOOM through the API
- consume filtered alerts from output topics
- inspect the processed record in MongoDB

## What This Walkthrough Teaches

- one alert turns into multiple internal records and processing stages
- Kafka is not the whole story
- MongoDB is not just storage; it supports downstream enrichment and filtering
- BOOM's value comes from transforming raw signals into usable scientific candidates

## Command Recipes

### Open the files behind this walkthrough

```bash
cd ~/projects/boom
sed -n '1,220p' src/bin/kafka_consumer.rs
sed -n '1,260p' src/enrichment/base.rs
sed -n '1,260p' src/filter/base.rs
```

## Screenshot Placeholders

- [ ] one hand-drawn pipeline sketch
- [ ] one trace of a worker processing path
- [ ] one API or database view showing processed alert data

## Data view
### Notes that reference this walkthrough
```dataview
TABLE type, status, file.folder
FROM "20_Progress/UROP"
WHERE file.path != this.file.path
AND contains(file.outlinks, this.file.link)
SORT file.folder ASC, file.name ASC
```
