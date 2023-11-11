import logging
attendance=logging.getLogger('attendance')
logging={
    "version": 1,   
    "disable_existing_loggers": False,
    "handlers" :{
        "file":{
            "class" : "logging.filehandlers",
            "filename" :"attendance.log",
            "level" :"debug",
             "formatter": "file",
        },
    "logger":{
        "" :{
            "level" :"debug",
            "handlers" :["file"],
        },
    "formatters" :{
        "file":{
            "format":{"{name} {levelname} {module} {massage} {asctime}"}
        }
    }    
    }    
    },
}