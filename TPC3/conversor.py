import re

def markdown_to_html(markdown: str) -> str:
    lines = markdown.split("\n")
    html_lines = []
    
    in_ol = False  # Para controlar listas numeradas
    
    for line in lines:
        # Cabeçalhos
        if re.match(r"^# (.+)", line):
            html_lines.append(f"<h1>{line[2:]}</h1>")
        elif re.match(r"^## (.+)", line):
            html_lines.append(f"<h2>{line[3:]}</h2>")
        elif re.match(r"^### (.+)", line):
            html_lines.append(f"<h3>{line[4:]}</h3>")
        
        # Listas numeradas
        elif re.match(r"^\d+\. (.+)", line):
            if not in_ol:
                html_lines.append("<ol>")
                in_ol = True
            item_text = re.sub(r"^\d+\. ", "", line)
            html_lines.append(f"<li>{item_text}</li>")
        else:
            if in_ol:
                html_lines.append("</ol>")
                in_ol = False
            
            # Negrito e Itálico
            line = re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", line)
            line = re.sub(r"\*(.*?)\*", r"<i>\1</i>", line)
            
            # Links
            line = re.sub(r"\[(.*?)\]\((.*?)\)", r"<a href='\2'>\1</a>", line)
            
            html_lines.append(line)
    
    if in_ol:
        html_lines.append("</ol>")
    
    return "\n".join(html_lines)

# Teste de exemplo
md_text = """
# Exemplo
Este é um **exemplo** e um *teste*.
1. Primeiro item
2. Segundo item
3. Terceiro item
Como pode ser consultado em [página da UC](http://www.uc.pt)
"""

print(markdown_to_html(md_text))
