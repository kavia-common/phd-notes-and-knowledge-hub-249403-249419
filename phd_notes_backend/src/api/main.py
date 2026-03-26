from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="PhD Notes Backend (Placeholder)",
    description="Minimal FastAPI placeholder for the PhD Notes & Knowledge Hub backend container.",
    version="0.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# PUBLIC_INTERFACE
@app.get(
    "/",
    summary="Health check",
    description="Minimal health check endpoint to verify the backend container is running.",
    tags=["System"],
    operation_id="health_check",
)
def health_check() -> dict:
    """Return a minimal health payload.

    Returns:
        dict: A small JSON payload indicating the service is up.
    """
    return {"message": "Healthy"}
