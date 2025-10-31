from fastapi import APIRouter, Request

router = APIRouter(prefix="/integrations/slack", tags=["integrations:slack"])

@router.post("/events")
async def slack_events(req: Request):
    body = await req.json()
    # URL verification challenge
    if body.get("type") == "url_verification":
        return {"challenge": body.get("challenge")}
    # TODO: handle events
    return {"ok": True}