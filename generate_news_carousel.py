import os
import re

def generate_news_carousel(md_file, html_file, delimiter):
    # Check if markdown file exists
    if not os.path.exists(md_file):
        raise FileNotFoundError(f"The file '{md_file}' does not exist.")

    # Read content from the markdown file
    with open(md_file, 'r', encoding='utf-8') as md:
        content = md.read()

    # Extract news items after the delimiter
    if delimiter in content:
        content = content.split(delimiter, 1)[1]
    else:
        raise ValueError(f"The delimiter '{delimiter}' was not found in the file.")

    # Split news items
    news_items = content.split(delimiter)

    # Generate carousel items HTML
    carousel_items_html = ""
    for index, news in enumerate(news_items):
        if news.strip():  # Skip empty items
            # Clean markdown syntax (e.g., remove **)
            cleaned_news = re.sub(r"\*\*", "", news.strip())

            # Extract headline and summary/body
            lines = cleaned_news.split("\n")
            headline = lines[0].strip() if len(lines) > 0 else ""
            
            # Process body content, excluding parenthetical counts and formatting
            body = "\n".join(line.strip() for line in lines[1:]) if len(lines) > 1 else ""
            body = re.sub(r"\([^)]*\)", "", body).strip()  # Remove parentheses content
            body = body.replace("Summary:", "<br>")  # Move content after "Summary:" to the next line

            active_class = "active" if index == 0 else ""
            carousel_items_html += f"""
                <div class="carousel-item {active_class}">
                    <div class="d-block w-100 p-4">
                        <div style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; padding: 30px; border: 1px solid #ddd; border-radius: 8px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); text-align: center; width: 90%; font-size: 1.4em; line-height: 1.6; margin: 0 auto;">
                            <h3 style="margin-bottom: 20px; font-size: 1.3em; line-height: 1.5;">{headline}</h3>
                            <p style="margin-top: 0; font-size: 1.1em; line-height: 1.4;">{body}</p>
                        </div>
                    </div>
                </div>
            """

    # Check if HTML file exists
    if not os.path.exists(html_file):
        raise FileNotFoundError(f"The file '{html_file}' does not exist.")

    # Read the HTML template
    with open(html_file, 'r', encoding='utf-8') as html:
        base_html = html.read()

    # Replace the placeholder in the HTML template
    if '<div id="carouselItems" class="carousel-inner">' not in base_html:
        raise ValueError("Placeholder '<div id=\"carouselItems\" class=\"carousel-inner\">' not found in the HTML file.")
    
    updated_html = base_html.replace(
        '<div id="carouselItems" class="carousel-inner">', 
        f'<div id="carouselItems" class="carousel-inner">{carousel_items_html}'
    )

    # Write the updated HTML content back to the file
    with open(html_file, 'w', encoding='utf-8') as updated_html_file:
        updated_html_file.write(updated_html)

    print(f"HTML file '{html_file}' updated successfully.")

# Example usage
md_file = 'output.md'  # Path to your .md file
html_file = 'index.html'  # Path to your existing HTML file
delimiter = '- ***'  # Delimiter to split the news

generate_news_carousel(md_file, html_file, delimiter)
