#coding:utf-8

def check_params(self,*args):
    params = [self.get_argument(i,None) for i in args]
    if not all(params):
        data = {'success': -1, 'code': 400, 'msg': '缺少必要参数'}
        self.write(data)
        return
    return params