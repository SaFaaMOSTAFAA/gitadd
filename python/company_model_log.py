import logging
company_model=logging.getLogger('company_model')

company_model_logging={
    "version" :1,
    "disable_existing_loggers": False,
    "handlers":{
        "file":{
           "class": "logging.filehandler",
            "filename":"company_model_log",
            "level" :"debug",
            "formatter":"file"

        },
    
    "company_model":{
        "":{
            "level" :"debug",
            "handlers" :["file"],
        },
    
    "formatters":{
        "file":{
            "format":{"{name} {levelname} {module} {massege} {asctime}"}
        },
    },
    },
    }
}