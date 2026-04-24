---
type: input
status: seed
created: 2026-04-24
tags:
  - input
  - api
  - openrouter
notes:
  - "[[API Documentation]]"
  - "[[OpenRouter]]"
---

# Rate Limits and Credits Remaining

To check your rate limit or credits remaining on your OpenRouter API key, make a GET request to:

```
https://openrouter.ai/api/v1/key
```

## How to Check Your Rate Limits

### Using curl
```bash
curl -H "Authorization: Bearer YOUR_API_KEY" https://openrouter.ai/api/v1/key
```

Replace `YOUR_API_KEY` with your actual OpenRouter API key.

### Using TypeScript SDK
```typescript
import { OpenRouter } from '@openrouter/sdk';

const openRouter = new OpenRouter({
  apiKey: '<OPENROUTER_API_KEY>',
});

const keyInfo = await openRouter.apiKeys.getCurrent();
console.log(keyInfo);
```

### Using Python
```python
import requests

response = requests.get(
    "https://openrouter.ai/api/v1/key",
    headers={"Authorization": "Bearer YOUR_API_KEY"}
)
print(response.json())
```

## Response Format

If your API key is valid, you'll get a response like:

```json
{
  "data": {
    "label": "string",
    "limit": number | null,        // Credit limit, or null if unlimited
    "limit_reset": string | null,  // When the limit resets
    "limit_remaining": number | null,  // Remaining credits for the key
    "include_byok_in_limit": boolean,
    "usage": number,              // Total credits used (all time)
    "usage_daily": number,        // Credits used today (UTC)
    "usage_weekly": number,       // Credits used this week
    "usage_monthly": number,      // Credits used this month
    "byok_usage": number,         // External BYOK usage
    "byok_usage_daily": number,
    "byok_usage_weekly": number,
    "byok_usage_monthly": number,
    "is_free_tier": boolean       // Whether you've paid for credits before
  }
}
```

## Rate Limits

### Free Usage Limits
- **Free model variants** (ID ending in `:free`):
  - Up to 20 requests per minute
- **Daily limits**:
  - If you've purchased less than 10 credits: 50 free model requests/day
  - If you've purchased at least 10 credits: 1000 free model requests/day

### DDoS Protection
- Cloudflare's DDoS protection will block requests that dramatically exceed reasonable usage
- If your account has a negative credit balance, you may see 402 errors (even for free models)
- Adding credits to make your balance positive allows you to use the models again

## Key Fields to Watch

- `limit_remaining`: How many requests you have left
- `usage_daily`: How much you've used today
- `is_free_tier`: Whether you're on the free tier
- `limit_reset`: When your limit resets (if applicable)