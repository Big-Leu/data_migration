import json
from jinja2 import Environment, FileSystemLoader
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

def create_model(class_name, fields):
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)
    template = env.get_template('model_template.j2')

    output = template.render(class_name=class_name, fields=fields)
    return output

def main():
    with open('config.json', 'r') as f:
        json_data = json.load(f)

    fields = json_data.get("fields", {})
    class_name = json_data.get("class_name", "MyModel")

    model_definition = create_model(class_name, fields)

    with open('generated_model.py', 'w') as f:
        f.write(model_definition)

if __name__ == "__main__":
    main()
