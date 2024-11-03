from flask import Flask, render_template, request, jsonify, redirect
from sqlalchemy import create_engine, text, func, inspect, String, Integer
from sqlalchemy.orm import DeclarativeBase, Session, Mapped, mapped_column
from helper import parse_report, sort_machine_parts

app = Flask(__name__)

engine = create_engine('sqlite:///app.db')
with engine.connect() as connection:
    inspector = inspect(engine)
    if "logs" not in inspector.get_table_names():
        connection.execute(text("CREATE TABLE logs (id INTEGER PRIMARY KEY AUTOINCREMENT, name varchar(200) NULL, description varchar(200) NULL, severity varchar(200) NULL, log_group varchar(200) NULL);"))

class Base(DeclarativeBase):
    pass

class Logs(Base):
    __tablename__ = 'logs'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    name: Mapped[str] = mapped_column(String(200), nullable=True)
    description: Mapped[str] = mapped_column(String(200), nullable=True)
    severity: Mapped[str] = mapped_column(String(200), nullable=True)
    log_group: Mapped[str] = mapped_column(String(200), nullable=True)


@app.route('/')
def home():
    with Session(engine) as session:
        logs = session.query(Logs).all()
        counts = session.query(Logs.severity, func.count(Logs.id).label('count')).group_by(Logs.severity).all()
        counts = [{"severity": count[0], "count": count[1]} for count in counts]
        logs = [{"name": log.name, "description": log.description, "severity": log.severity, "group": log.log_group} for log in logs]
    return render_template("home.html", data=logs, counts=counts)

@app.route('/parse', methods=['POST'])
def parse():
    log = request.form.get('log')
    if not (data := parse_report(log)):
        print(data)
        return jsonify({"error": "Invalid data"})
    data = sort_machine_parts(data)
    logs = []
    for dat in data['machine']['parts']:
        name = dat['name']
        for issue in dat['issues']:
            log = Logs(name=name, 
                    description=issue['description'], 
                    severity=issue['severity'], 
                    log_group=issue['group'])
            logs.append(log)
    with Session(engine) as session:
        session.add_all(logs)
        session.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)