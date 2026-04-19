from datetime import datetime

from pydantic import BaseModel, Field


class NoteCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=200, description="笔记标题，1-200个字符")
    content: str = Field(..., min_length=1, description="笔记内容，不能为空")


class NoteRead(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class NotePatch(BaseModel):
    title: str | None = Field(None, min_length=1, max_length=200, description="笔记标题，1-200个字符")
    content: str | None = Field(None, min_length=1, description="笔记内容，不能为空")


class ActionItemCreate(BaseModel):
    description: str = Field(..., min_length=1, max_length=500, description="行动项描述，1-500个字符")


class ActionItemRead(BaseModel):
    id: int
    description: str
    completed: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class ActionItemPatch(BaseModel):
    description: str | None = Field(None, min_length=1, max_length=500, description="行动项描述，1-500个字符")
    completed: bool | None = None