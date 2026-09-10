from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.domain.grant_proposal_writer.schemas import AgenticGrantProposalWriterSessionCreate, AgenticGrantProposalWriterSessionResponse
from app.domain.grant_proposal_writer.service import AgenticGrantProposalWriterService

router = APIRouter(prefix="/api/v1/grant_proposal_writer", tags=["Agentic Grant Proposal Writer Domain"])

@router.post("/sessions", response_model=AgenticGrantProposalWriterSessionResponse, status_code=status.HTTP_201_CREATED)
def create_domain_session(data: AgenticGrantProposalWriterSessionCreate, db: Session = Depends(get_db)):
    """
    Creates a new FastAPI domain session for Agentic Grant Proposal Writer.
    """
    return AgenticGrantProposalWriterService.create_session(db, data)

@router.get("/sessions/{session_id}", response_model=AgenticGrantProposalWriterSessionResponse)
def get_domain_session(session_id: str, db: Session = Depends(get_db)):
    obj = AgenticGrantProposalWriterService.get_session(db, session_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Domain session not found")
    return obj
