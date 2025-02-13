from pydantic import BaseModel, Field
class Template(BaseModel):
    id: str = Field(description="ID du mème")
    champs:list[str] = Field(description="Liste des champs du mème")
    link: str = Field(description="Lien vers l'image du mème")