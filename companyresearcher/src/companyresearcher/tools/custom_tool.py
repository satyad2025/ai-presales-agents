from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from crewai_tools import SerperDevTool

class LinkedInSearchtoolInput(BaseModel):
    """Input schema for MyCustomTool."""
    #company_founder: str = Field(..., description="Name of the company founder")
    company_name: str = Field(..., description="Name of the company")

class LinkedInSearchTool(BaseTool):
    name: str = "LinkedIn Profile Search Tool"
    description: str = (
        "Search the founder linkedin profile and return the best suitable profile."
    )
    args_schema: Type[BaseModel] = LinkedInSearchtoolInput
    
    def _run(self, company_name: str) -> str:
        serper_tool=SerperDevTool()
        search_results =  serper_tool.run(query=f"Search LinkedIn profile of the founders who is from company {company_name} and provide the most suitable profiles")
        linkedin_links = [
            result['link']
            for result in search_results.get('results', [])
            if 'linkedin.com' in result.get('link', '')
        ]
        return linkedin_links[0] if linkedin_links else "No LinkedIn profile found."