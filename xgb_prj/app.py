from xgb_prj import xgb_func

def handler(event, context):   
    ret = xgb_func(test_size=event['test_size'])
    print(ret)
    return ret