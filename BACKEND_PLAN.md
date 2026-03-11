# validator.com - Backend Structure

## Current Status

### Public Site
- Live at: https://validator.com (or the domain it's deployed to)
- Static HTML: /home/openclaw/public/validator.html
- Tracker: /home/openclaw/public/validator-tracker.html

### Docs (Quill)
- Location: /home/openclaw/vault/Dev/validator-com/docs/
- Status: index.md exists (needs to be integrated)

## What's Needed

### 1. Dynamic Data Integration
The current site is static. To make it dynamic:
- Fetch live validator stats (already done: fetch-validators.py)
- Store in /public/data/validators.json
- Frontend fetches from API

### 2. API Endpoints Needed
| Endpoint | Data | Status |
|----------|------|--------|
| /api/validators | Live validator list | Need to build |
| /api/roi-calculator | ROI projections | Need to build |
| /api/docs | Quill's docs | Need to integrate |

### 3. Docs Integration
Quill wrote docs but they're not connected to the site. Need:
- Convert docs/index.md to HTML
- Add to site navigation

## Implementation Plan

### Phase 1: Data Pipeline (Today)
- [x] fetch-validators.py - Working ✅
- [ ] Add cron to fetch hourly
- [ ] Serve at /api/validators

### Phase 2: Frontend Updates (Today)
- [ ] Connect validator-tracker.html to API
- [ ] Add real-time updates

### Phase 3: Docs (Tomorrow)
- [ ] Convert Quill's docs to HTML
- [ ] Add to navigation

## Current Files
- /vault/Dev/validator-com/fetch-validators.py - Data fetcher
- /vault/Dev/validator-com/validators.json - Cached data
- /vault/Dev/validator-com/docs/index.md - Quill's content

## Next Steps
1. Deploy current site to production domain
2. Set up cron for validator data
3. Integrate Quill's docs
