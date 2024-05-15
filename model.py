import json
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

def create_model(class_name, fields):
    class_definition = f"class {class_name}(Base):\n"
    class_definition += f"    __tablename__ = '{class_name.lower()}'\n\n"
    class_definition += f"    id = Column(Integer, primary_key=True, autoincrement=True)\n"

    for field, data_type in fields.items():
        class_definition += f"    {field} = Column({data_type.capitalize()})\n"

    return class_definition

def main():
    with open('tableformat.json', 'r') as f:
        json_data = json.load(f)

    fields = json_data.get("fields", {})
    
    class_name = json_data.get("class_name", "MyModel")

    model_definition = create_model(class_name, fields)

    with open('generated_model.py', 'w') as f:
        f.write("from sqlalchemy import Column, Integer, String\n")
        f.write("from sqlalchemy.ext.declarative import declarative_base\n\n")
        f.write("Base = declarative_base()\n\n")
        f.write(model_definition)

if __name__ == "__main__":
    main()
