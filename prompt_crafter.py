import re
from typing import Dict, Any, List

class PromptTemplate:
    def __init__(self, template: str, version: str = "1.0.0"):
        self.template = template
        self.version = version
        self.variables: List[str] = re.findall(r'\{\{(\w+)\}\}', template)

    def render(self, **kwargs: Any) -> str:
        missing = [v for v in self.variables if v not in kwargs]
        if missing:
            raise ValueError(f"Missing required prompt variables: {', '.join(missing)}")
        
        result = self.template
        for k, v in kwargs.items():
            result = result.replace(f"{{{{{k}}}}}", str(v))
        return result

    def validate(self, **kwargs: Any) -> bool:
        return all(v in kwargs for v in self.variables)

if __name__ == '__main__':
    tpl = PromptTemplate("You are an expert {{role}}. Help the user with: {{task}}")
    print("Rendered:", tpl.render(role="Database Engineer", task="Optimize PostgreSQL indexing"))
