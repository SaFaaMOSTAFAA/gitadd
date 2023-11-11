import logging
attendance=logging.getLogger('company_branch_model')
company_branch_model={
    "version": 1,   
    "disable_existing_loggers": False,
    "handlers" :{
        "file":{
            "class" : "company_branch_model.filehandlers",
            "filename" :"company_branch_model.log",
            "level" :"debug",
             "formatter": "file",
        },
    "company_branch_log":{
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

