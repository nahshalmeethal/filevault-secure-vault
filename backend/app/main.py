from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import files

app = FastAPI(
    title="FileVault API",
    description="Secure file vault backend with AES-256-GCM encryption",
    version="1.0.0"
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(files.router, prefix="/api/files", tags=["files"])

@app.get("/")
def root():
    return {"message": "FileVault backend online", "version": "1.0.0"}
