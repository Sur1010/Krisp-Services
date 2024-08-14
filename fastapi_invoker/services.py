import httpx
import asyncio

GENERATOR_SERVICE_URL = "http://flask_generator:5000/recommend"


async def runcascade():
    models = ["ModelA", "ModelB", "ModelC", "ModelD", "ModelE"]
    tasks = [fetch_recommendation(model) for model in models]
    results = await asyncio.gather(*tasks)

    # Merge results (you might need a more complex merge logic depending on requirements)
    merged_result = {"results": results}
    return merged_result


async def fetch_recommendation(model_name: str):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            GENERATOR_SERVICE_URL,
            json={"model_name": model_name, "viewer_id": "dummy_viewer_id"}
        )
        response.raise_for_status()
        return response.json()
