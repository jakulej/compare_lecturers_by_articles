from lpmn_client2.lpmn_client_biz import Connection, IOType, Task, download, upload

#API exaple:
LPMN_BASE = ["any2txt",
             "morphodita",
             {
                 "liner2": {
                     "model": "n82"
                 }
             }]
INPUT_BASE = "Tomasz Bombaliński pojechał do Wrocławia"
_Connection = Connection(config_file='config.yml')

task = Task(LPMN_BASE, connection=_Connection)

output_file_id = task.run(INPUT_BASE, IOType.TEXT)

downloaded = download(_Connection, output_file_id, IOType.FILE)

