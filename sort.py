from roboflow import Roboflow
rf = Roboflow(api_key="uJc1DR4FwucyYkplgW6Q")
project = rf.workspace("new-workspace-xslri").project("person-b9j2g")
dataset = project.version(1).download("yolov5")