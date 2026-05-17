import asyncio
import random
import httpx

class AdaptiveHTTPClient:

    def __init__(self, concurrency=10, timeout=10):

        self.semaphore = asyncio.Semaphore(concurrency)
        self.timeout = timeout
        self.delay = 0

    async def get(self, url):

        async with self.semaphore:

            if self.delay:
                await asyncio.sleep(self.delay)

            try:
                async with httpx.AsyncClient(timeout=self.timeout) as client:

                    response = await client.get(url)

                    if response.status_code == 429:
                        self.delay += 1

                    return response

            except Exception:
                return None

    async def jitter(self):
        await asyncio.sleep(random.uniform(0.1, 1.5))
